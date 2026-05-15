"""
screening.py — Bước 8.1.2 WorkPlan v5.6
Pha A — Python pre-screen với 13 priority rules (regex IC/EC).

Nguyên tắc toàn vẹn dữ liệu (§0.3):
  - KHÔNG truncate title/abstract trong bất kỳ bước matching nào
  - Match trên TOÀN BỘ chuỗi: title + abstract + author_keywords sau lowercase + strip
  - Mỗi record giữ nguyên doi gốc; PRE_LABEL ghi vào field N1

Pipeline:
  1. tf_journal_exclusion.py → gán TF_PRE_LABEL cho records nguồn T&F
  2. Áp 13 rules (top-down, rule đầu wins) lên text = title+abstract+keywords
  3. Records T&F whitelist → bypass rules 4–12 (chỉ áp rules 1–3 + 13)
  4. Records T&F blacklist → LIKELY_EXCLUDE ngay (không áp rules 1–3)

Đầu ra:
  screening_pre.csv            — audit trail đầy đủ (mỗi record 1 dòng)
  screening_pre.ris            — full RIS + N1: PRE_LABEL: <label> | EC: <ec>
  screening_distribution.txt   — thống kê phân bố

Sử dụng:
  python screening.py --input dedup_unique.ris
  python screening.py --input test/sample_pool.ris --out test/   # test
  python screening.py --input dedup_unique.ris --out 03_screening/
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

# Import module T&F exclusion
try:
    from tf_journal_exclusion import (
        classify_tf_journal, is_tf_whitelisted, is_tf_blacklisted,
        TF_LABEL_WHITELIST
    )
    HAS_TF_MODULE = True
except ImportError:
    HAS_TF_MODULE = False
    print("[WARN] tf_journal_exclusion.py không tìm thấy — T&F whitelist/blacklist bị bỏ qua.",
          file=sys.stderr)

# ─── Import parser từ dedup.py ───
try:
    from dedup import parse_ris_records, Record
    HAS_DEDUP = True
except ImportError:
    HAS_DEDUP = False
    print("[ERROR] dedup.py không tìm thấy. Cần dedup.py trong cùng thư mục.", file=sys.stderr)
    sys.exit(1)

# ─── Labels ───
LABEL_INCLUDE = "LIKELY_INCLUDE"
LABEL_REVIEW = "REVIEW_NEEDED"
LABEL_EXCLUDE = "LIKELY_EXCLUDE"

# ─── 13 Priority Rules ───
# Format: (rule_number, pattern_str, label, ec_code, description)
# Regex flags: IGNORECASE
# Áp dụng theo thứ tự; rule đầu tiên match wins.
# Rules 1–3: LIKELY_INCLUDE (OR-merge: match ≥ 1)
# Rules 4–12: LIKELY_EXCLUDE (OR-merge: match ≥ 1)
# Rule 13: default → REVIEW_NEEDED

# Rule 1: DT/Digital Shadow + container terminal/port (cả 2 chiều)
_RULE1_DT = r"\b(digital twin|digital shadow|cyber-physical)\b"
_RULE1_PORT = (r"\b(container terminal|container port|seaport"
               r"|port terminal|port operation|maritime terminal"
               r"|smart port|port logistics|port system"
               r"|port facility|port area|port infrastructure)\b")

# Rule 2: Operations × DT/sim/IoT (5 lĩnh vực × tech)
_RULE2_OPS = r"\b(berth|quay crane|yard|agv|automated guided vehicle|gate)\b"
_RULE2_ACT = r"\b(scheduling|allocation|optim|routing|monitor|dispatching)\b"
_RULE2_TECH = r"\b(digital twin|digital shadow|simulation|iot|sensor|cyber-physical)\b"

# Rule 3: Simulation V&V at container terminal
_RULE3_SIM = r"\b(simulation|des|discrete event simulation|agent-based|hardware.in.the.loop|hardware in the loop)\b"
_RULE3_PORT = r"\b(container|terminal|port|seaport)\b"
_RULE3_VV = r"\b(validat|verif|calibrat|emulat)\b"

# Rule 4: port-Hamiltonian (EC-NOSCOPE — control theory, not container port)
_RULE4 = r"\bport.hamiltonian\b"

# Rule 5: USB/serial/network/COM port (EC-NOSCOPE — IT/electronics)
_RULE5 = r"\b(usb|serial|i/o|network|com|ethernet|transport layer|port number)\s*port\b"

# Rule 6: Docker/Kubernetes/side-channel (EC-IT/EC-NOSCOPE — software containers/CPU)
_RULE6 = r"\b(docker|kubernetes|side.channel|smt execution port)\b"

# Rule 7: Airport/heliport (EC-NOSCOPE — aviation)
_RULE7 = r"\b(airport|heliport|air terminal)\b"

# Rule 8: City names containing "port" (EC-NOSCOPE — geographic false positive)
_RULE8 = (r"\b(port vila|port moresby|port said|port harcourt"
           r"|port.au.prince|portsmouth|newport news|port elizabeth|port louis)\b")

# Rule 9: Non-container terminals (EC2 — bulk/RoRo/cruise/ferry)
_RULE9 = (r"\b(bulk terminal|tanker terminal|oil terminal|lng terminal"
           r"|coal terminal|grain terminal|ore terminal|cruise terminal"
           r"|ferry terminal|passenger terminal|roll.on roll.off|ro.ro|roro terminal"
           r"|solid bulk|bulk port terminal|bulk cargo terminal|multipurpose terminal"
           r"|dry bulk|wet bulk|liquid cargo terminal)\b")

# Rule 10: Healthcare / medical (EC7-health)
# Loại bỏ "cell", "protein", "tissue" vì quá chung chung (fuel cell, solar cell...)
_RULE10 = (r"\b(patient|clinical|cancer|tumor|tumour|surgery|medical"
            r"|pharmaceutical|chemotherapy|biospecimen"
            r"|cardiovascular|diabetes|oncology|genomic|patholog)\b")

# Rule 10b: Hệ thống năng lượng (EC-ENERGY) — microgrid, cold ironing, hydrogen, PV tại cảng
# Chỉ fire khi KHÔNG có từ khóa operations trong 5 lĩnh vực (berth/crane/yard/AGV/gate)
_RULE10B_ENERGY = (r"\b(microgrid|shore power|cold ironing|hydrogen fuel cell"
                   r"|photovoltaic panel|wind turbine|energy storage system"
                   r"|power grid|electricity grid|demand response|load balancing.*energy)\b")
_RULE10B_OPS_NEG = r"\b(berth|quay crane|yard management|agv dispatching|gate scheduling|crane scheduling)\b"

# Rule 11: Ship hull/marine engine/offshore (EC1) + Structural SHM civil (EC-STRUCT)
# Chỉ loại trừ nếu KHÔNG có "container terminal/container port" trong context
# — tránh false negative với review papers bao quát cả maritime + container
_RULE11A = r"\b(ship hull|marine engine|offshore platform|vessel routing|vessel design)\b"
_RULE11B = (r"\b(structural health monitoring|shm|bridge monitoring|seismic monitoring)\b"
             r".*\b(bridge|wharf|civil|concrete|seismic)\b")
_RULE11_CONTAINER_NEG = r"\b(container terminal|container port)\b"

# Rule 12: BIM + construction (EC7-bim) — only if NO port keyword nearby
_RULE12_BIM = r"\b(bim|building information model)\b"
_RULE12_CIVIL = r"\b(construction|civil engineering|architecture|building)\b"
_RULE12_PORT_NEG = r"\b(port|terminal|container|seaport|maritime)\b"

# Rule 13: default → REVIEW_NEEDED

RULES_COMPILED: list[dict] = []

def _compile_rules() -> None:
    """Compile all regex patterns once at import time."""
    flags = re.IGNORECASE | re.DOTALL

    RULES_COMPILED.append({
        "num": 1, "label": LABEL_INCLUDE, "ec": "IC1",
        "desc": "DT/CPS + container terminal (strong signal)",
        "type": "and_or",   # (_DT AND _PORT) OR (_PORT AND _DT)
        "_r1": re.compile(_RULE1_DT, flags),
        "_r2": re.compile(_RULE1_PORT, flags),
    })
    RULES_COMPILED.append({
        "num": 2, "label": LABEL_INCLUDE, "ec": "IC2/IC3",
        "desc": "Operations × DT/sim/IoT (5 lĩnh vực)",
        "type": "and3",
        "_r1": re.compile(_RULE2_OPS, flags),
        "_r2": re.compile(_RULE2_ACT, flags),
        "_r3": re.compile(_RULE2_TECH, flags),
    })
    RULES_COMPILED.append({
        "num": 3, "label": LABEL_INCLUDE, "ec": "IC3",
        "desc": "Simulation V&V at container terminal",
        "type": "and3",
        "_r1": re.compile(_RULE3_SIM, flags),
        "_r2": re.compile(_RULE3_PORT, flags),
        "_r3": re.compile(_RULE3_VV, flags),
    })
    RULES_COMPILED.append({
        "num": 4, "label": LABEL_EXCLUDE, "ec": "EC-NOSCOPE",
        "desc": "port-Hamiltonian control theory",
        "type": "simple",
        "_r1": re.compile(_RULE4, flags),
    })
    RULES_COMPILED.append({
        "num": 5, "label": LABEL_EXCLUDE, "ec": "EC-NOSCOPE",
        "desc": "USB/serial/network port — IT electronics",
        "type": "simple",
        "_r1": re.compile(_RULE5, flags),
    })
    RULES_COMPILED.append({
        "num": 6, "label": LABEL_EXCLUDE, "ec": "EC-IT",
        "desc": "Docker/Kubernetes — IT container",
        "type": "simple",
        "_r1": re.compile(_RULE6, flags),
    })
    RULES_COMPILED.append({
        "num": 7, "label": LABEL_EXCLUDE, "ec": "EC-NOSCOPE",
        "desc": "Airport/heliport — aviation",
        "type": "simple",
        "_r1": re.compile(_RULE7, flags),
    })
    RULES_COMPILED.append({
        "num": 8, "label": LABEL_EXCLUDE, "ec": "EC-NOSCOPE",
        "desc": "City names: Port Vila, Port Moresby, etc.",
        "type": "simple",
        "_r1": re.compile(_RULE8, flags),
    })
    RULES_COMPILED.append({
        "num": 9, "label": LABEL_EXCLUDE, "ec": "EC2",
        "desc": "Non-container terminal (bulk/RoRo/cruise/ferry)",
        "type": "simple",
        "_r1": re.compile(_RULE9, flags),
    })
    RULES_COMPILED.append({
        "num": 10, "label": LABEL_EXCLUDE, "ec": "EC7-health",
        "desc": "Healthcare / medical",
        "type": "simple",
        "_r1": re.compile(_RULE10, flags),
    })
    RULES_COMPILED.append({
        "num": 10.5, "label": LABEL_EXCLUDE, "ec": "EC-ENERGY",
        "desc": "Hệ thống năng lượng (microgrid/shore power/hydrogen) không phải ops port",
        "type": "energy_special",
        "_r1": re.compile(_RULE10B_ENERGY, flags),
        "_r2": re.compile(_RULE10B_OPS_NEG, flags),
    })
    RULES_COMPILED.append({
        "num": 11, "label": LABEL_EXCLUDE, "ec": "EC1/EC-STRUCT",
        "desc": "Ship hull/offshore + structural SHM civil (only if no container context)",
        "type": "vessel_special",
        "_r1": re.compile(_RULE11A, flags),
        "_r2": re.compile(_RULE11B, flags),
        "_r3": re.compile(_RULE11_CONTAINER_NEG, flags),
    })
    RULES_COMPILED.append({
        "num": 12, "label": LABEL_EXCLUDE, "ec": "EC7-bim",
        "desc": "BIM + construction (without port context)",
        "type": "bim_special",
        "_r1": re.compile(_RULE12_BIM, flags),
        "_r2": re.compile(_RULE12_CIVIL, flags),
        "_r3": re.compile(_RULE12_PORT_NEG, flags),
    })
    # Rule 13: default — no compile needed


_compile_rules()


def _apply_rules(text: str, whitelist_bypass: bool = False) -> tuple[str, str, list[int]]:
    """
    Áp 13 rules theo thứ tự. Trả về (label, ec_code, matched_rules_list).

    whitelist_bypass=True: chỉ áp rules 1–3 + 13 (bỏ qua 4–12).
    """
    matched_rules: list[int] = []
    include_matches: list[tuple[str, str]] = []  # (ec, rule_num)

    for rule in RULES_COMPILED:
        num = rule["num"]
        rtype = rule["type"]
        label = rule["label"]
        ec = rule["ec"]

        # Skip exclusion rules 4–12 (kể cả 10.5) nếu whitelist
        if whitelist_bypass and 4 <= num <= 12.5:
            continue

        hit = False
        if rtype == "simple":
            hit = bool(rule["_r1"].search(text))
        elif rtype == "and_or":
            hit = bool(rule["_r1"].search(text) and rule["_r2"].search(text))
        elif rtype == "and3":
            hit = bool(rule["_r1"].search(text) and
                       rule["_r2"].search(text) and
                       rule["_r3"].search(text))
        elif rtype == "or2":
            hit = bool(rule["_r1"].search(text) or rule["_r2"].search(text))
        elif rtype == "energy_special":
            # Energy system terms (microgrid/shore power) + KHÔNG có ops port scheduling → EXCLUDE
            has_energy = bool(rule["_r1"].search(text))
            has_ops = bool(rule["_r2"].search(text))
            hit = has_energy and not has_ops
        elif rtype == "vessel_special":
            # Ship hull/offshore/vessel terms, nhưng KHÔNG loại nếu có "container terminal/port"
            # — tránh false negative với review papers bao quát cả maritime + container
            has_vessel = bool(rule["_r1"].search(text))
            has_shm = bool(rule["_r2"].search(text))
            has_container = bool(rule["_r3"].search(text))
            hit = (has_vessel or has_shm) and not has_container
        elif rtype == "bim_special":
            # BIM + construction BUT no port keyword → EXCLUDE
            # Nếu có từ "port" trong văn bản → không loại (có thể borderline)
            has_bim = bool(rule["_r1"].search(text))
            has_civil = bool(rule["_r2"].search(text))
            has_port_kw = bool(rule["_r3"].search(text))
            hit = has_bim and has_civil and not has_port_kw

        if hit:
            matched_rules.append(num)
            if label == LABEL_INCLUDE:
                include_matches.append((ec, num))
            elif label == LABEL_EXCLUDE:
                # Exclusion rule wins — return immediately
                return LABEL_EXCLUDE, ec, matched_rules

    # Nếu có ít nhất 1 include match → LIKELY_INCLUDE
    if include_matches:
        ec_combined = "/".join(ec for ec, _ in include_matches)
        return LABEL_INCLUDE, ec_combined, matched_rules

    # Default Rule 13
    matched_rules.append(13)
    return LABEL_REVIEW, "", matched_rules


@dataclass
class ScreeningResult:
    study_id: str
    doi: str
    title: str
    abstract: str
    source: str
    source_file: str
    journal: str
    year: str
    pre_label: str
    ec_candidate: str
    matched_rules: str
    tf_pre_label: str = ""

    @property
    def has_abstract(self) -> bool:
        return bool(self.abstract.strip())


def screen_record(rec: "Record") -> ScreeningResult:
    """Áp screening pipeline cho một record."""
    # Lấy text match (title + abstract + keywords) — KHÔNG truncate (§0.3)
    title = rec.title_raw or ""
    abstract = rec.get("AB") or ""
    keywords = " ".join(rec.fields.get("KW", []))
    text = f"{title} {abstract} {keywords}"

    journal = rec.get("T2") or rec.get("JF") or rec.get("T1") or ""

    # Bước 1: T&F journal filter
    tf_pre_label = ""
    whitelist_bypass = False
    immediate_exclude = False
    immediate_ec = ""

    if HAS_TF_MODULE and rec.source in ("tf",):
        tf_pre_label = classify_tf_journal(journal, rec.source) or ""
        if is_tf_whitelisted(tf_pre_label):
            whitelist_bypass = True
        else:
            is_bl, bl_ec = is_tf_blacklisted(tf_pre_label)
            if is_bl:
                immediate_exclude = True
                immediate_ec = bl_ec

    # Bước 2: Áp 13 rules
    if immediate_exclude:
        pre_label = LABEL_EXCLUDE
        ec_candidate = immediate_ec
        matched_rules_str = "TF_BLACKLIST"
    else:
        pre_label, ec_candidate, matched_rules_list = _apply_rules(text, whitelist_bypass)
        matched_rules_str = ",".join("10b" if r == 10.5 else str(int(r) if isinstance(r, float) else r) for r in matched_rules_list)

    study_id = getattr(rec, "study_id", "") or ""

    return ScreeningResult(
        study_id=study_id,
        doi=rec.doi_raw,
        title=title,              # Giữ nguyên (§0.3 không truncate)
        abstract=abstract,        # Giữ nguyên
        source=rec.source,
        source_file=rec.source_file,
        journal=journal,
        year=rec.year,
        pre_label=pre_label,
        ec_candidate=ec_candidate,
        matched_rules=matched_rules_str,
        tf_pre_label=tf_pre_label,
    )


def write_screening_csv(results: list[ScreeningResult], out_path: str) -> None:
    """Ghi screening_pre.csv — audit trail đầy đủ."""
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "study_id", "doi", "title", "abstract", "source", "journal", "year",
            "pre_label", "ec_candidate", "matched_rules", "tf_pre_label", "has_abstract"
        ])
        for r in results:
            w.writerow([
                r.study_id, r.doi,
                r.title,        # Không truncate (§0.3)
                r.abstract,     # Không truncate
                r.source, r.journal, r.year,
                r.pre_label, r.ec_candidate, r.matched_rules,
                r.tf_pre_label, str(r.has_abstract)
            ])


def write_screening_ris(records: list["Record"], results: list[ScreeningResult],
                        out_path: str) -> None:
    """
    Ghi screening_pre.ris — full RIS metadata + thêm N1: PRE_LABEL.
    Rayyan đọc N1 vào Notes panel.
    """
    result_map: dict[str, ScreeningResult] = {r.study_id: r for r in results if r.study_id}

    with open(out_path, "w", encoding="utf-8") as f:
        for rec in records:
            sid = getattr(rec, "study_id", "")
            result = result_map.get(sid)
            if not result:
                f.write(rec.raw_ris)
                continue

            # Ghi raw RIS với thêm N1 line trước ER
            ris_lines = rec.raw_ris.rstrip().splitlines()
            n1_line = (f"N1  - PRE_LABEL: {result.pre_label}"
                       f" | EC: {result.ec_candidate}"
                       f" | RULES: {result.matched_rules}")
            # Chèn N1 trước ER
            output_lines = []
            for line in ris_lines:
                if line.startswith("ER  -"):
                    output_lines.append(n1_line)
                output_lines.append(line)
            f.write("\n".join(output_lines) + "\nER  - \n\n")


def write_distribution(results: list[ScreeningResult], out_path: str) -> None:
    """Ghi screening_distribution.txt — thống kê phân bố."""
    total = len(results)
    n_inc = sum(1 for r in results if r.pre_label == LABEL_INCLUDE)
    n_rev = sum(1 for r in results if r.pre_label == LABEL_REVIEW)
    n_exc = sum(1 for r in results if r.pre_label == LABEL_EXCLUDE)
    n_no_abs = sum(1 for r in results if not r.has_abstract)

    def pct(n: int) -> str:
        return f"{n}/{total} ({100*n/max(total,1):.1f}%)"

    # EC code counts (for EXCLUDE)
    ec_counts: dict[str, int] = {}
    for r in results:
        if r.pre_label == LABEL_EXCLUDE and r.ec_candidate:
            for ec in r.ec_candidate.split("/"):
                ec = ec.strip()
                ec_counts[ec] = ec_counts.get(ec, 0) + 1

    # Source counts
    src_counts_total: dict[str, int] = {}
    src_counts_inc: dict[str, int] = {}
    src_counts_rev: dict[str, int] = {}
    src_counts_exc: dict[str, int] = {}
    for r in results:
        src_counts_total[r.source] = src_counts_total.get(r.source, 0) + 1
        if r.pre_label == LABEL_INCLUDE:
            src_counts_inc[r.source] = src_counts_inc.get(r.source, 0) + 1
        elif r.pre_label == LABEL_REVIEW:
            src_counts_rev[r.source] = src_counts_rev.get(r.source, 0) + 1
        elif r.pre_label == LABEL_EXCLUDE:
            src_counts_exc[r.source] = src_counts_exc.get(r.source, 0) + 1

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("SCREENING DISTRIBUTION — Bước 8.1.3 WorkPlan v5.6\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total records:     {total}\n")
        f.write(f"LIKELY_INCLUDE  :  {pct(n_inc)}   [kỳ vọng 15–25%]\n")
        f.write(f"REVIEW_NEEDED   :  {pct(n_rev)}   [kỳ vọng 40–60%]\n")
        f.write(f"LIKELY_EXCLUDE  :  {pct(n_exc)}   [kỳ vọng 20–40%]\n")
        f.write(f"Missing abstract :  {n_no_abs}\n\n")

        # Kiểm tra ngưỡng
        inc_pct = n_inc / max(total, 1) * 100
        if inc_pct < 5:
            f.write("[WARN] LIKELY_INCLUDE < 5% — rules 1–3 quá strict? Kiểm tra regex.\n")
        elif inc_pct > 40:
            f.write("[WARN] LIKELY_INCLUDE > 40% — rules 1–3 quá broad? Kiểm tra false positives.\n")
        else:
            f.write("[OK] Phân bố LIKELY_INCLUDE trong range hợp lý.\n")

        f.write("\nBy source:\n")
        for src in sorted(src_counts_total.keys()):
            n = src_counts_total[src]
            ni = src_counts_inc.get(src, 0)
            nr = src_counts_rev.get(src, 0)
            ne = src_counts_exc.get(src, 0)
            f.write(f"  {src:10s}: total={n:5d} | INC={ni:4d} | REV={nr:4d} | EXC={ne:4d}\n")

        f.write("\nTop EC codes (LIKELY_EXCLUDE):\n")
        for ec, count in sorted(ec_counts.items(), key=lambda x: -x[1])[:15]:
            f.write(f"  {ec:20s}: {count}\n")

        f.write("\nRule match distribution (LIKELY_INCLUDE):\n")
        rule_counts: dict[str, int] = {}
        for r in results:
            if r.pre_label == LABEL_INCLUDE:
                for rn in r.matched_rules.split(","):
                    rn = rn.strip()
                    rule_counts[rn] = rule_counts.get(rn, 0) + 1
        for rn, cnt in sorted(rule_counts.items(), key=lambda x: -x[1]):
            f.write(f"  Rule {rn:5s}: {cnt}\n")

        f.write("\nRule match distribution (LIKELY_EXCLUDE):\n")
        exc_rule_counts: dict[str, int] = {}
        for r in results:
            if r.pre_label == LABEL_EXCLUDE:
                for rn in r.matched_rules.split(","):
                    rn = rn.strip()
                    exc_rule_counts[rn] = exc_rule_counts.get(rn, 0) + 1
        for rn, cnt in sorted(exc_rule_counts.items(), key=lambda x: -x[1]):
            f.write(f"  Rule {rn:10s}: {cnt}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bước 8.1.2 — Pha A Python pre-screen (13 priority rules)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--input", required=True,
                        help="File RIS đầu vào (thường là dedup_unique.ris)")
    parser.add_argument("--out", default=".",
                        help="Thư mục đầu ra (mặc định: .)")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"[ERROR] File không tồn tại: {args.input}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.out, exist_ok=True)

    print(f"[+] Đọc {args.input}...")
    records = parse_ris_records(args.input)
    print(f"    {len(records)} records")

    print("[+] Áp 13 priority rules (Pha A pre-screen)...")
    results: list[ScreeningResult] = []
    for rec in records:
        result = screen_record(rec)
        results.append(result)

    # Xuất
    csv_out = os.path.join(args.out, "screening_pre.csv")
    ris_out = os.path.join(args.out, "screening_pre.ris")
    dist_out = os.path.join(args.out, "screening_distribution.txt")

    write_screening_csv(results, csv_out)
    write_screening_ris(records, results, ris_out)
    write_distribution(results, dist_out)

    # Tóm tắt nhanh
    total = len(results)
    n_inc = sum(1 for r in results if r.pre_label == LABEL_INCLUDE)
    n_rev = sum(1 for r in results if r.pre_label == LABEL_REVIEW)
    n_exc = sum(1 for r in results if r.pre_label == LABEL_EXCLUDE)

    print(f"\n[+] Kết quả:")
    print(f"    LIKELY_INCLUDE : {n_inc:5d} ({100*n_inc/max(total,1):.1f}%)")
    print(f"    REVIEW_NEEDED  : {n_rev:5d} ({100*n_rev/max(total,1):.1f}%)")
    print(f"    LIKELY_EXCLUDE : {n_exc:5d} ({100*n_exc/max(total,1):.1f}%)")
    print(f"\n[+] Đầu ra:")
    print(f"    {csv_out}")
    print(f"    {ris_out}")
    print(f"    {dist_out}")

    # Calibration reminder
    print("\n[NEXT] Bước 8.1.4 — Calibration pilot 30 records:")
    print("  1. Chọn 10 LIKELY_INCLUDE + 10 LIKELY_EXCLUDE + 10 REVIEW_NEEDED")
    print("  2. NCS chấm thủ công (mù với pre_label)")
    print("  3. Tính Cohen's κ — mục tiêu ≥ 0.75")
    print("  4. Nếu κ < 0.75 → refine rules + re-run screening.py")


if __name__ == "__main__":
    main()
