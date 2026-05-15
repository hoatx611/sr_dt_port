"""
check_ris_integrity.py — Bước 7.2 WorkPlan v5.6
Kiểm tra toàn vẹn dữ liệu RIS trước khi dedup.

Đầu vào:  thư mục chứa .ris (mặc định: search_results_v5.6/)
Đầu ra:
  ris_integrity_report.csv  — tổng hợp mỗi file 1 dòng
  ris_integrity_detail.csv  — từng record có vấn đề

Quy tắc kiểm tra:
  1. Mỗi dòng trong RIS phải khớp pattern "^([A-Z][A-Z0-9])  -\\s?(.*)$" hoặc là dòng trống/ER
  2. Mỗi record phải có TY, TI, ER
  3. Ghi nhận records thiếu AB (abstract), DO (doi), PY (year), AU (author)
  4. Không sửa dữ liệu — chỉ báo cáo (principle: toàn vẹn dữ liệu gốc §0.3)

Sử dụng:
  python check_ris_integrity.py                          # default: search_results_v5.6/
  python check_ris_integrity.py --dir path/to/ris        # thư mục tùy chỉnh
  python check_ris_integrity.py --files a.ris b.ris      # file cụ thể
  python check_ris_integrity.py --out reports/           # thư mục đầu ra
"""
from __future__ import annotations

import argparse
import csv
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

# ─── Pattern kiểm tra từng dòng RIS ───
FIELD_PATTERN = re.compile(r"^([A-Z][A-Z0-9])  -\s?(.*)$")
# Dòng "ER  - " kết thúc record (có thể có hoặc không có dấu cách sau)
ER_PATTERN = re.compile(r"^ER  -\s*$")

# Các field bắt buộc trong mỗi record
REQUIRED_FIELDS = {"TY", "TI", "ER"}
# Các field cần thiết cho pipeline (thiếu thì cảnh báo)
RECOMMENDED_FIELDS = {"AU", "PY", "DO", "AB", "T2"}


@dataclass
class RisRecord:
    source_file: str
    record_index: int     # thứ tự trong file (1-based)
    fields: dict = field(default_factory=dict)  # {tag: [values]}
    raw_lines: list[str] = field(default_factory=list)
    bad_lines: list[tuple[int, str]] = field(default_factory=list)  # (lineno, line)
    missing_required: list[str] = field(default_factory=list)
    missing_recommended: list[str] = field(default_factory=list)

    def get(self, tag: str, default: str = "") -> str:
        vals = self.fields.get(tag, [])
        return vals[0].strip() if vals else default

    def get_all(self, tag: str) -> list[str]:
        return self.fields.get(tag, [])

    @property
    def doi(self) -> str:
        return self.get("DO")

    @property
    def title(self) -> str:
        return self.get("TI")

    @property
    def year(self) -> str:
        return self.get("PY")

    @property
    def abstract(self) -> str:
        return self.get("AB")

    @property
    def has_abstract(self) -> bool:
        return bool(self.abstract.strip())

    @property
    def is_valid(self) -> bool:
        return len(self.missing_required) == 0 and len(self.bad_lines) == 0


def parse_ris_file(filepath: str) -> tuple[list[RisRecord], list[tuple[int, str]]]:
    """
    Đọc và phân tích một file RIS.
    Trả về (records, file_level_errors).
    Không truncate, không sửa — chỉ đọc và báo cáo.
    """
    records: list[RisRecord] = []
    file_errors: list[tuple[int, str]] = []

    try:
        with open(filepath, encoding="utf-8", errors="replace") as f:
            raw = f.read()
    except OSError as e:
        file_errors.append((0, f"Cannot open file: {e}"))
        return records, file_errors

    lines = raw.splitlines()
    current_record: Optional[RisRecord] = None
    current_tag: Optional[str] = None
    record_index = 0

    for lineno, line in enumerate(lines, start=1):
        # Dòng trống: tiếp tục (giữa records)
        if not line.strip():
            continue

        # Kiểm tra dòng kết thúc record
        if ER_PATTERN.match(line):
            if current_record is not None:
                current_record.raw_lines.append(line)
                current_record.fields.setdefault("ER", []).append("")
                # Kiểm tra required fields
                for f_tag in REQUIRED_FIELDS:
                    if f_tag not in current_record.fields:
                        current_record.missing_required.append(f_tag)
                # Kiểm tra recommended fields
                for r_tag in RECOMMENDED_FIELDS:
                    if r_tag not in current_record.fields:
                        current_record.missing_recommended.append(r_tag)
                records.append(current_record)
                current_record = None
                current_tag = None
            else:
                file_errors.append((lineno, f"ER  - without matching TY"))
            continue

        # Kiểm tra dòng field RIS
        m = FIELD_PATTERN.match(line)
        if m:
            tag, value = m.group(1), m.group(2).strip()
            if tag == "TY":
                if current_record is not None:
                    # Record chưa đóng — lỗi
                    current_record.bad_lines.append((lineno, f"New TY before ER: {line}"))
                record_index += 1
                source = os.path.splitext(os.path.basename(filepath))[0]
                current_record = RisRecord(source_file=source, record_index=record_index)
            if current_record is not None:
                current_record.fields.setdefault(tag, []).append(value)
                current_record.raw_lines.append(line)
                current_tag = tag
            else:
                file_errors.append((lineno, f"Field outside record: {line[:80]}"))
        else:
            # Dòng không khớp pattern — có thể là continuation của field trước
            if current_record is not None and current_tag is not None:
                # Continuation của field (multi-line abstract, etc.)
                if current_tag in current_record.fields:
                    current_record.fields[current_tag][-1] += " " + line.strip()
                    current_record.raw_lines.append(line)
                else:
                    current_record.bad_lines.append((lineno, f"Malformed line: {line[:80]}"))
            else:
                file_errors.append((lineno, f"Malformed line: {line[:80]}"))

    # Record không đóng (thiếu ER)
    if current_record is not None:
        current_record.missing_required.append("ER (missing end-of-record)")
        for r_tag in RECOMMENDED_FIELDS:
            if r_tag not in current_record.fields:
                current_record.missing_recommended.append(r_tag)
        records.append(current_record)

    return records, file_errors


def collect_files(args: argparse.Namespace) -> list[str]:
    """Thu thập danh sách file .ris cần kiểm tra."""
    if args.files:
        return [f for f in args.files if os.path.isfile(f)]
    ris_dir = args.dir
    if not os.path.isdir(ris_dir):
        print(f"[ERROR] Thư mục không tồn tại: {ris_dir}", file=sys.stderr)
        sys.exit(1)
    return sorted([
        os.path.join(ris_dir, f)
        for f in os.listdir(ris_dir)
        if f.lower().endswith(".ris")
    ])


def write_summary_report(filepath_list: list[str], all_records: dict[str, list[RisRecord]],
                         all_errors: dict[str, list], out_path: str) -> None:
    """Viết báo cáo tổng hợp (1 dòng / file)."""
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "file", "total_records", "valid_records", "bad_lines",
            "missing_TY", "missing_TI", "missing_ER",
            "missing_AB", "missing_DO", "missing_PY", "missing_AU",
            "file_level_errors", "status"
        ])
        for fp in filepath_list:
            fname = os.path.basename(fp)
            records = all_records.get(fp, [])
            ferrors = all_errors.get(fp, [])
            total = len(records)
            valid = sum(1 for r in records if r.is_valid)
            bad_lines_total = sum(len(r.bad_lines) for r in records)
            miss_TI = sum(1 for r in records if "TI" in r.missing_required)
            miss_TY = sum(1 for r in records if "TY" in r.missing_required)
            miss_ER = sum(1 for r in records if any("ER" in m for m in r.missing_required))
            miss_AB = sum(1 for r in records if "AB" in r.missing_recommended)
            miss_DO = sum(1 for r in records if "DO" in r.missing_recommended)
            miss_PY = sum(1 for r in records if "PY" in r.missing_recommended)
            miss_AU = sum(1 for r in records if "AU" in r.missing_recommended)
            status = "OK" if (valid == total and not ferrors) else "WARN"
            w.writerow([
                fname, total, valid, bad_lines_total,
                miss_TY, miss_TI, miss_ER,
                miss_AB, miss_DO, miss_PY, miss_AU,
                len(ferrors), status
            ])


def write_detail_report(filepath_list: list[str], all_records: dict[str, list[RisRecord]],
                        all_errors: dict[str, list], out_path: str) -> None:
    """Viết báo cáo chi tiết từng record có vấn đề."""
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "file", "record_index", "doi", "title_snippet",
            "issue_type", "issue_detail"
        ])
        for fp in filepath_list:
            fname = os.path.basename(fp)
            records = all_records.get(fp, [])
            ferrors = all_errors.get(fp, [])

            # File-level errors
            for lineno, msg in ferrors:
                w.writerow([fname, "FILE", "", "", "file_error", f"line {lineno}: {msg}"])

            # Record-level issues
            for r in records:
                if r.is_valid and not r.missing_recommended:
                    continue
                doi_short = (r.doi[:60] + "…") if len(r.doi) > 60 else r.doi
                title_short = (r.title[:80] + "…") if len(r.title) > 80 else r.title
                if r.missing_required:
                    w.writerow([fname, r.record_index, doi_short, title_short,
                                "missing_required", "; ".join(r.missing_required)])
                if r.missing_recommended:
                    w.writerow([fname, r.record_index, doi_short, title_short,
                                "missing_recommended", "; ".join(r.missing_recommended)])
                for lineno, msg in r.bad_lines:
                    w.writerow([fname, r.record_index, doi_short, title_short,
                                "bad_line", f"line {lineno}: {msg}"])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bước 7.2 — Kiểm tra toàn vẹn RIS files trước dedup",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--dir", default="search_results_v5.6",
                        help="Thư mục chứa .ris (mặc định: search_results_v5.6/)")
    parser.add_argument("--files", nargs="*",
                        help="File .ris cụ thể (ghi đè --dir)")
    parser.add_argument("--out", default=".",
                        help="Thư mục đầu ra cho báo cáo (mặc định: .)")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    filepath_list = collect_files(args)

    if not filepath_list:
        print("[WARN] Không tìm thấy file .ris nào.")
        return

    print(f"[+] Kiểm tra {len(filepath_list)} file RIS...")

    all_records: dict[str, list[RisRecord]] = {}
    all_errors: dict[str, list] = {}
    grand_total = 0
    grand_valid = 0

    for fp in filepath_list:
        records, ferrors = parse_ris_file(fp)
        all_records[fp] = records
        all_errors[fp] = ferrors

        total = len(records)
        valid = sum(1 for r in records if r.is_valid)
        warn_count = sum(1 for r in records if r.missing_recommended)
        grand_total += total
        grand_valid += valid

        status = "✅ OK" if (valid == total and not ferrors) else "⚠️  WARN"
        fname = os.path.basename(fp)
        print(f"    {fname:35s}: {total:5d} records | {valid:5d} valid | "
              f"{warn_count:4d} missing_recommended | {len(ferrors):2d} file_errors  {status}")

    # Xuất báo cáo
    summary_path = os.path.join(args.out, "ris_integrity_report.csv")
    detail_path = os.path.join(args.out, "ris_integrity_detail.csv")
    write_summary_report(filepath_list, all_records, all_errors, summary_path)
    write_detail_report(filepath_list, all_records, all_errors, detail_path)

    print()
    print(f"[+] Tổng kết:")
    print(f"    Tổng records:  {grand_total}")
    print(f"    Valid records: {grand_valid}")
    print(f"    Issues:        {grand_total - grand_valid}")
    print(f"[+] Báo cáo tổng hợp: {summary_path}")
    print(f"[+] Báo cáo chi tiết: {detail_path}")

    if grand_total != grand_valid:
        print("\n[WARN] Có records không hợp lệ — xem ris_integrity_detail.csv trước khi dedup.")
    else:
        print("\n[OK] Tất cả records hợp lệ — sẵn sàng cho Bước 7.4 dedup.")


if __name__ == "__main__":
    main()
