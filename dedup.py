"""
dedup.py — Bước 7.4 WorkPlan v5.6
Khử trùng lặp 3 lớp theo thứ tự ưu tiên:

  Lớp 1 — DOI exact:
    Chuẩn hoá DOI (lowercase, strip https://doi.org/, strip doi:) → so sánh chuỗi
    Ưu tiên giữ: scopus > ieee > gs > springer > tf

  Lớp 2 — Fuzzy title:
    RapidFuzz token_sort_ratio ≥ 90 trên title đã chuẩn hoá (lowercase, strip)
    Cùng ngưỡng Lớp 1 về ưu tiên nguồn

  Lớp 3 — Author + Year + Title hash:
    MD5(lowercase(first_author) + year + first_30_chars_title)
    Bắt các trường hợp bỏ sót Lớp 1+2

Nguyên tắc toàn vẹn dữ liệu (§0.3):
  - KHÔNG truncate title/abstract trong bất kỳ bước nào
  - DOI: chuẩn hoá để so sánh, giữ nguyên DOI gốc trong output
  - Matching dùng TOÀN BỘ chuỗi sau lowercase + strip

Ưu tiên nguồn khi giữ record (thấp số = ưu tiên cao):
  scopus=1, ieee=2, gs=3, springer=4, tf=5, unknown=6

Đầu ra:
  dedup_unique.ris          — full RIS metadata của pool unique
  dedup_unique_records.csv  — danh sách unique với key fields
  dedup_report.txt          — chi tiết Lớp 1/2/3 + thống kê
  dedup_borderline_pairs.csv— Layer 2 score 85–89 (chưa đủ 90)
  dedup_strict_report.txt   — (chỉ khi --strict) Python vs Rayyan cross-validate

Sử dụng:
  pip install rapidfuzz
  python dedup.py --input-dir search_results_v5.6/
  python dedup.py --files a.ris b.ris c.ris
  python dedup.py --input-dir search_results_v5.6/ --strict    # mode kiểm tra
  python dedup.py --files test/sample_pool.ris --out test/      # test trên sample
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import re
import sys
from dataclasses import dataclass, field
from typing import Optional

# Bảo đảm stdout/stderr UTF-8 trên Windows (chỉ wrap nếu chưa phải UTF-8)
def _ensure_utf8(stream):
    if hasattr(stream, "buffer") and getattr(stream, "encoding", "").lower().replace("-", "") not in ("utf8",):
        return io.TextIOWrapper(stream.buffer, encoding="utf-8", errors="replace")
    return stream

sys.stdout = _ensure_utf8(sys.stdout)
sys.stderr = _ensure_utf8(sys.stderr)

try:
    from rapidfuzz import fuzz
    HAS_RAPIDFUZZ = True
except ImportError:
    HAS_RAPIDFUZZ = False
    print("[WARN] rapidfuzz chưa cài. Lớp 2 (fuzzy title) sẽ bị bỏ qua.", file=sys.stderr)
    print("       Cài đặt: pip install rapidfuzz", file=sys.stderr)

# ─── Hằng số ───
SOURCE_PRIORITY = {
    "scopus": 1, "ieee": 2, "gs": 3, "springer": 4, "tf": 5, "unknown": 6
}
FUZZY_THRESHOLD = 90      # Lớp 2: giữ nếu score ≥ 90
BORDERLINE_LOW = 85       # Lớp 2: lưu borderline nếu 85 ≤ score < 90
FIELD_PATTERN = re.compile(r"^([A-Z][A-Z0-9])  -\s?(.*)$")
ER_PATTERN = re.compile(r"^ER  -\s*$")


# ─── Data model ───
@dataclass
class Record:
    source_file: str       # tên file gốc (không có đường dẫn)
    source: str            # scopus/ieee/gs/springer/tf/unknown
    raw_ris: str           # full RIS text cho record này (để ghi lại)
    fields: dict = field(default_factory=dict)   # {tag: [values]}

    # Key fields (extracted sau khi parse)
    doi_raw: str = ""      # DOI gốc
    doi_norm: str = ""     # DOI chuẩn hoá để so sánh
    title_raw: str = ""    # Title gốc
    title_norm: str = ""   # Title chuẩn hoá để so sánh
    year: str = ""
    first_author: str = ""
    hash3: str = ""        # MD5 hash Lớp 3

    # Audit
    study_id: str = ""     # UUID gán khi dedup

    def get(self, tag: str, default: str = "") -> str:
        vals = self.fields.get(tag, [])
        return vals[0].strip() if vals else default


# ─── Parsing ───
def normalize_doi(raw: str) -> str:
    """Chuẩn hoá DOI để so sánh; giữ nguyên raw DOI trong output."""
    if not raw:
        return ""
    s = raw.strip()
    s = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", s, flags=re.IGNORECASE)
    s = re.sub(r"^doi:\s*", "", s, flags=re.IGNORECASE)
    return s.lower().strip()


def normalize_title(raw: str) -> str:
    """Chuẩn hoá title để so sánh. KHÔNG truncate (§0.3)."""
    s = raw.lower().strip()
    # Xóa dấu câu dư, chuẩn hoá khoảng trắng
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def detect_source(source_file: str, fields: dict) -> str:
    """Xác định nguồn từ tên file hoặc field DB/DP/N1."""
    name = source_file.lower()
    db_vals = " ".join(fields.get("DB", []) + fields.get("DP", []) + fields.get("N1", [])).lower()

    if "scopus" in name or "scopus" in db_vals:
        return "scopus"
    if "ieee" in name or "ieee" in db_vals:
        return "ieee"
    if name.startswith("gs") or "gs." in name or "google scholar" in db_vals or "source=gs" in db_vals:
        return "gs"
    if "springer" in name or "springer" in db_vals:
        return "springer"
    if name.startswith("tf") or name.startswith("tandf") or "taylor" in db_vals or "source=tf" in db_vals:
        return "tf"
    # Fallback: check N1 notes
    n1_text = " ".join(fields.get("N1", [])).lower()
    if "source=scopus" in n1_text:
        return "scopus"
    if "source=ieee" in n1_text:
        return "ieee"
    if "source=gs" in n1_text:
        return "gs"
    if "source=springer" in n1_text:
        return "springer"
    if "source=tf" in n1_text:
        return "tf"
    return "unknown"


def compute_hash3(first_author: str, year: str, title_norm: str) -> str:
    """MD5(lowercase first_author + year + first 30 chars title_norm) — Lớp 3."""
    key = first_author.lower().strip() + year.strip() + title_norm[:30]
    return hashlib.md5(key.encode("utf-8")).hexdigest()


def parse_ris_records(filepath: str) -> list[Record]:
    """Parse một file RIS, trả về danh sách Record."""
    try:
        with open(filepath, encoding="utf-8", errors="replace") as f:
            raw = f.read()
    except OSError as e:
        print(f"[ERROR] Cannot open {filepath}: {e}", file=sys.stderr)
        return []

    source_file = os.path.splitext(os.path.basename(filepath))[0]
    lines = raw.splitlines()
    records: list[Record] = []
    current_fields: dict = {}
    current_lines: list[str] = []
    current_tag: Optional[str] = None

    def finalize_record() -> None:
        if not current_fields:
            return
        raw_ris_text = "\n".join(current_lines) + "\n"
        source = detect_source(source_file, current_fields)
        rec = Record(
            source_file=source_file,
            source=source,
            raw_ris=raw_ris_text,
            fields=current_fields.copy()
        )
        # Trích key fields
        doi_raw = rec.get("DO")
        title_raw = rec.get("TI")
        # Thêm các field alias cho title
        if not title_raw:
            title_raw = rec.get("T1")

        rec.doi_raw = doi_raw
        rec.doi_norm = normalize_doi(doi_raw)
        rec.title_raw = title_raw
        rec.title_norm = normalize_title(title_raw)

        pys = current_fields.get("PY", [""])
        rec.year = pys[0].strip() if pys else ""
        # Extract year if PY has full date like "2024/01/01"
        if rec.year and "/" in rec.year:
            rec.year = rec.year.split("/")[0].strip()

        authors = current_fields.get("AU", [])
        rec.first_author = authors[0].strip().lower() if authors else ""

        rec.hash3 = compute_hash3(rec.first_author, rec.year, rec.title_norm)
        records.append(rec)

    for line in lines:
        if not line.strip():
            continue
        if ER_PATTERN.match(line):
            current_lines.append(line)
            finalize_record()
            current_fields = {}
            current_lines = []
            current_tag = None
            continue

        m = FIELD_PATTERN.match(line)
        if m:
            tag, value = m.group(1), m.group(2).strip()
            current_fields.setdefault(tag, []).append(value)
            current_lines.append(line)
            current_tag = tag
        else:
            # Continuation line — append to last field
            if current_tag and current_tag in current_fields:
                current_fields[current_tag][-1] += " " + line.strip()
                current_lines.append(line)

    # Xử lý record cuối không có ER
    if current_fields:
        finalize_record()

    return records


# ─── Dedup logic ───
def dedup_records(records: list[Record], strict: bool = False) -> tuple[
    list[Record],
    list[tuple[Record, Record, str, float]],   # removed pairs (kept, removed, layer, score)
    list[tuple[Record, Record, float]],         # borderline pairs layer2
]:
    """
    Khử trùng lặp 3 lớp. Trả về (unique, removed_pairs, borderline_pairs).
    Ưu tiên giữ record có SOURCE_PRIORITY thấp hơn (scopus < ieee < gs < springer < tf).
    """
    kept: list[Record] = []        # pool unique
    removed_pairs: list[tuple[Record, Record, str, float]] = []
    borderline_pairs: list[tuple[Record, Record, float]] = []

    # Gán study_id tạm thời
    for i, r in enumerate(records, start=1):
        r.study_id = f"S{i:06d}"

    # ─ Lớp 1: DOI exact ─
    doi_index: dict[str, Record] = {}
    no_doi_list: list[Record] = []

    for rec in records:
        if not rec.doi_norm:
            no_doi_list.append(rec)
            continue
        if rec.doi_norm in doi_index:
            existing = doi_index[rec.doi_norm]
            # Giữ record ưu tiên cao hơn
            if SOURCE_PRIORITY.get(rec.source, 6) < SOURCE_PRIORITY.get(existing.source, 6):
                removed_pairs.append((rec, existing, "L1_doi_exact", 100.0))
                doi_index[rec.doi_norm] = rec  # thay thế
            else:
                removed_pairs.append((existing, rec, "L1_doi_exact", 100.0))
        else:
            doi_index[rec.doi_norm] = rec

    after_l1 = list(doi_index.values()) + no_doi_list

    # ─ Lớp 2: Fuzzy title ─
    if not HAS_RAPIDFUZZ:
        after_l2 = after_l1
    else:
        after_l2: list[Record] = []
        title_pool: list[Record] = []  # pool đã xác nhận unique

        for rec in after_l1:
            if not rec.title_norm:
                after_l2.append(rec)
                continue

            matched = False
            for existing in title_pool:
                if not existing.title_norm:
                    continue
                score = fuzz.token_sort_ratio(rec.title_norm, existing.title_norm)
                if score >= FUZZY_THRESHOLD:
                    # Duplicate
                    if SOURCE_PRIORITY.get(rec.source, 6) < SOURCE_PRIORITY.get(existing.source, 6):
                        # Rec tốt hơn → giữ rec, remove existing
                        removed_pairs.append((rec, existing, "L2_fuzzy_title", float(score)))
                        title_pool.remove(existing)
                        title_pool.append(rec)
                    else:
                        removed_pairs.append((existing, rec, "L2_fuzzy_title", float(score)))
                    matched = True
                    break
                elif BORDERLINE_LOW <= score < FUZZY_THRESHOLD:
                    borderline_pairs.append((rec, existing, float(score)))

            if not matched:
                title_pool.append(rec)

        after_l2 = title_pool + [r for r in after_l1 if not r.title_norm and r not in after_l2]
        # Clean up: records without title were added to after_l2 directly
        # Rebuild properly
        after_l2_set = {id(r) for r in title_pool}
        after_l2 = [r for r in after_l1 if id(r) in after_l2_set or not r.title_norm]

    # ─ Lớp 3: Author+Year+Title hash ─
    hash_index: dict[str, Record] = {}
    after_l3: list[Record] = []

    for rec in after_l2:
        if not rec.hash3 or (not rec.first_author and not rec.year):
            after_l3.append(rec)  # Không đủ thông tin để hash → giữ lại
            continue
        if rec.hash3 in hash_index:
            existing = hash_index[rec.hash3]
            if SOURCE_PRIORITY.get(rec.source, 6) < SOURCE_PRIORITY.get(existing.source, 6):
                removed_pairs.append((rec, existing, "L3_hash", 100.0))
                hash_index[rec.hash3] = rec
            else:
                removed_pairs.append((existing, rec, "L3_hash", 100.0))
        else:
            hash_index[rec.hash3] = rec

    # Merge after_l3 (no hash) + hash_index results
    hash_set = {id(r) for r in hash_index.values()}
    final_unique = [r for r in after_l2 if id(r) in hash_set]
    final_unique += [r for r in after_l3 if id(r) not in {id(x) for x in final_unique}]

    # Re-assign clean sequential study_ids
    for i, r in enumerate(final_unique, start=1):
        r.study_id = f"SRDT{i:05d}"

    return final_unique, removed_pairs, borderline_pairs


# ─── Output writers ───
def write_ris_output(records: list[Record], out_path: str) -> None:
    """Ghi dedup_unique.ris — giữ nguyên full RIS, chèn N1 source+study_id trước ER."""
    with open(out_path, "w", encoding="utf-8") as f:
        for rec in records:
            # Chèn N1 annotation để screening.py có thể detect source
            lines = rec.raw_ris.rstrip().splitlines()
            n1_tag = (f"N1  - source={rec.source}; study_id={rec.study_id}")
            output_lines: list[str] = []
            injected = False
            for line in lines:
                if not injected and line.strip().startswith("ER  -"):
                    output_lines.append(n1_tag)
                    injected = True
                output_lines.append(line)
            if not injected:
                output_lines.append(n1_tag)
                output_lines.append("ER  - ")
            f.write("\n".join(output_lines) + "\n\n")


def write_csv_output(records: list[Record], out_path: str) -> None:
    """Ghi dedup_unique_records.csv — key fields."""
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["study_id", "source", "source_file", "doi", "title", "year",
                    "first_author", "journal", "doc_type"])
        for r in records:
            w.writerow([
                r.study_id, r.source, r.source_file,
                r.doi_raw, r.title_raw, r.year,
                r.first_author,
                r.get("T2") or r.get("JF") or r.get("T1"),
                r.get("TY"),
            ])


def write_report(records: list[Record],
                 all_records: list[Record],
                 removed_pairs: list[tuple],
                 borderline_pairs: list[tuple],
                 out_path: str) -> None:
    """Ghi dedup_report.txt."""
    total_in = len(all_records)
    total_out = len(records)
    total_removed = total_in - total_out
    dedup_ratio = total_removed / total_in * 100 if total_in else 0

    # Count by layer
    l1 = sum(1 for _, _, layer, _ in removed_pairs if layer == "L1_doi_exact")
    l2 = sum(1 for _, _, layer, _ in removed_pairs if layer == "L2_fuzzy_title")
    l3 = sum(1 for _, _, layer, _ in removed_pairs if layer == "L3_hash")

    # Count by source
    source_counts_in: dict[str, int] = {}
    source_counts_out: dict[str, int] = {}
    for r in all_records:
        source_counts_in[r.source] = source_counts_in.get(r.source, 0) + 1
    for r in records:
        source_counts_out[r.source] = source_counts_out.get(r.source, 0) + 1

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("DEDUP REPORT — Bước 7.4 WorkPlan v5.6\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Tổng records đầu vào:  {total_in:6d}\n")
        f.write(f"Tổng records unique:   {total_out:6d}\n")
        f.write(f"Tổng đã loại bỏ:       {total_removed:6d} ({dedup_ratio:.1f}%)\n\n")
        f.write("Chi tiết theo lớp:\n")
        f.write(f"  Lớp 1 (DOI exact):   {l1:6d} cặp trùng\n")
        f.write(f"  Lớp 2 (Fuzzy title): {l2:6d} cặp trùng\n")
        f.write(f"  Lớp 3 (Hash):        {l3:6d} cặp trùng\n\n")

        f.write("Phân bố theo nguồn (đầu vào → sau dedup):\n")
        all_sources = sorted(set(list(source_counts_in.keys()) + list(source_counts_out.keys())))
        for src in all_sources:
            n_in = source_counts_in.get(src, 0)
            n_out = source_counts_out.get(src, 0)
            f.write(f"  {src:10s}: {n_in:5d} → {n_out:5d} (loại {n_in - n_out:4d})\n")

        f.write(f"\nBorderline pairs (score 85–89): {len(borderline_pairs)}\n")

        # Kiểm tra ngưỡng R07 từ WorkPlan
        if dedup_ratio < 10:
            f.write("\n[WARN R07] Dedup ratio < 10% — kiểm tra encoding / DOI normalization bug.\n")
        elif dedup_ratio > 50:
            f.write("\n[WARN R07] Dedup ratio > 50% — kiểm tra fuzzy threshold (90 quá thấp?).\n")
        else:
            f.write(f"\n[OK] Dedup ratio {dedup_ratio:.1f}% trong range bình thường (10–50%).\n")

        expected_range = (5000, 7000)
        if total_out < expected_range[0]:
            f.write(f"[WARN R03] Pool unique {total_out} < {expected_range[0]} (kỳ vọng WorkPlan). "
                    f"Xem xét chạy SA-1/2/3.\n")
        elif total_out > expected_range[1]:
            f.write(f"[WARN R03] Pool unique {total_out} > {expected_range[1]} (kỳ vọng WorkPlan). "
                    f"Cân nhắc tightening NOT block.\n")
        else:
            f.write(f"[OK] Pool unique {total_out} trong range kỳ vọng [{expected_range[0]:,}, "
                    f"{expected_range[1]:,}].\n")

        f.write("\n" + "-" * 70 + "\n")
        f.write("Chi tiết Lớp 1 — DOI exact duplicates (top 20):\n")
        l1_pairs = [(k, r, s) for k, r, layer, s in removed_pairs if layer == "L1_doi_exact"][:20]
        for kept, removed, score in l1_pairs:
            doi_disp = (removed.doi_raw[:60] + "…") if len(removed.doi_raw) > 60 else removed.doi_raw
            f.write(f"  KEEP [{kept.source}] REMOVE [{removed.source}] DOI: {doi_disp}\n")

        f.write("\n" + "-" * 70 + "\n")
        f.write("Chi tiết Lớp 2 — Fuzzy title duplicates (top 20):\n")
        l2_pairs = [(k, r, s) for k, r, layer, s in removed_pairs if layer == "L2_fuzzy_title"][:20]
        for kept, removed, score in l2_pairs:
            t_disp = (removed.title_raw[:60] + "…") if len(removed.title_raw) > 60 else removed.title_raw
            f.write(f"  score={score:.0f}  KEEP [{kept.source}] REMOVE [{removed.source}]\n")
            f.write(f"    TITLE: {t_disp}\n")

        f.write("\n" + "-" * 70 + "\n")
        f.write("Chi tiết Lớp 3 — Hash duplicates (top 20):\n")
        l3_pairs = [(k, r, s) for k, r, layer, s in removed_pairs if layer == "L3_hash"][:20]
        for kept, removed, score in l3_pairs:
            f.write(f"  KEEP [{kept.source}] {kept.first_author} {kept.year} "
                    f"'{kept.title_norm[:40]}…'\n")
            f.write(f"  REMOVED [{removed.source}] {removed.first_author} {removed.year}\n")


def write_borderline_csv(borderline_pairs: list[tuple], out_path: str) -> None:
    """Ghi dedup_borderline_pairs.csv — pairs score 85–89 để NCS xem xét thủ công."""
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["score", "rec1_source", "rec1_doi", "rec1_title",
                    "rec2_source", "rec2_doi", "rec2_title", "ncs_decision"])
        for r1, r2, score in borderline_pairs:
            w.writerow([
                f"{score:.1f}",
                r1.source, r1.doi_raw,
                r1.title_raw,
                r2.source, r2.doi_raw,
                r2.title_raw,
                ""  # NCS điền: DUPLICATE / NOT_DUPLICATE
            ])


# ─── Main ───
def collect_files(args: argparse.Namespace) -> list[str]:
    if args.files:
        return [f for f in args.files if os.path.isfile(f)]
    ris_dir = args.input_dir
    if not os.path.isdir(ris_dir):
        print(f"[ERROR] Thư mục không tồn tại: {ris_dir}", file=sys.stderr)
        sys.exit(1)
    return sorted([
        os.path.join(ris_dir, f)
        for f in os.listdir(ris_dir)
        if f.lower().endswith(".ris")
    ])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bước 7.4 — Khử trùng lặp 3 lớp (DOI + Fuzzy title + Hash)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--input-dir", default="search_results_v5.6",
                        help="Thư mục chứa .ris (mặc định: search_results_v5.6/)")
    parser.add_argument("--files", nargs="*",
                        help="File .ris cụ thể (ghi đè --input-dir)")
    parser.add_argument("--out", default=".",
                        help="Thư mục đầu ra (mặc định: .)")
    parser.add_argument("--strict", action="store_true",
                        help="Strict mode: ghi dedup_strict_report.txt cho cross-validate Rayyan")
    parser.add_argument("--fuzzy-threshold", type=int, default=FUZZY_THRESHOLD,
                        help=f"Ngưỡng fuzzy title score (mặc định: {FUZZY_THRESHOLD})")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    filepath_list = collect_files(args)

    if not filepath_list:
        print("[WARN] Không tìm thấy file .ris nào.")
        return

    print(f"[+] Đọc {len(filepath_list)} file RIS...")
    all_records: list[Record] = []
    for fp in filepath_list:
        recs = parse_ris_records(fp)
        print(f"    {os.path.basename(fp):35s}: {len(recs):5d} records")
        all_records.extend(recs)

    print(f"\n[+] Tổng records đầu vào: {len(all_records)}")
    print(f"[+] Chạy dedup 3 lớp (threshold Lớp 2 = {args.fuzzy_threshold})...")

    unique, removed_pairs, borderline_pairs = dedup_records(
        all_records, strict=args.strict
    )

    print(f"[+] Kết quả:")
    print(f"    Records unique:    {len(unique)}")
    print(f"    Records đã loại:   {len(all_records) - len(unique)}")
    print(f"    Borderline pairs:  {len(borderline_pairs)}")

    # Xuất file
    ris_out = os.path.join(args.out, "dedup_unique.ris")
    csv_out = os.path.join(args.out, "dedup_unique_records.csv")
    report_out = os.path.join(args.out, "dedup_report.txt")
    borderline_out = os.path.join(args.out, "dedup_borderline_pairs.csv")

    write_ris_output(unique, ris_out)
    write_csv_output(unique, csv_out)
    write_report(unique, all_records, removed_pairs, borderline_pairs, report_out)
    write_borderline_csv(borderline_pairs, borderline_out)

    print(f"\n[+] Đầu ra:")
    print(f"    {ris_out}")
    print(f"    {csv_out}")
    print(f"    {report_out}")
    print(f"    {borderline_out}")

    if args.strict:
        strict_out = os.path.join(args.out, "dedup_strict_report.txt")
        with open(strict_out, "w", encoding="utf-8") as f:
            f.write("STRICT MODE REPORT — Bước 7.6 cross-validate với Rayyan\n")
            f.write("=" * 70 + "\n\n")
            f.write(f"Python dedup unique: {len(unique)}\n")
            f.write("Hướng dẫn:\n")
            f.write("  1. Upload dedup_unique.ris lên Rayyan project\n")
            f.write("  2. Rayyan auto-dedup DOI-only → kỳ vọng AGREE ≥ 99%\n")
            f.write("  3. So sánh số records Rayyan vs Python (delta ≤ 5%)\n")
            f.write("  4. Nếu delta > 5% → trigger Recovery R7\n")
        print(f"    {strict_out}")

    # Đọc report để hiển thị
    with open(report_out, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("[") or "DEDUP" in line:
                print("  " + line.rstrip())

    print("\n[OK] Bước 7.4 hoàn tất. Bước tiếp theo: Bước 7.7 — upload dedup_unique.ris lên Rayyan.")


if __name__ == "__main__":
    main()
