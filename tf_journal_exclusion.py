"""
tf_journal_exclusion.py — Bước 8.1.1 WorkPlan v5.6
Module riêng cho pool Taylor & Francis.

Vấn đề: T&F Online KHÔNG hỗ trợ Subject Area filter ở tầng truy vấn
→ kết quả Q12 trả về tạp chí từ nhiều lĩnh vực không liên quan
→ cần lọc theo tên tạp chí trước khi áp 13 priority rules.

Module này gán TF_PRE_LABEL:
  WHITELIST → "BYPASS_WHITELIST"     (luôn forward sang screening.py, KHÔNG bị block)
  BLACKLIST → "TF_EXCLUDE:<EC_CODE>" (gán LIKELY_EXCLUDE ngay lập tức)
  Còn lại   → "TF_NEUTRAL"          (forward bình thường)

KHÔNG áp dụng cho records từ nguồn không phải tf.

Sử dụng (import vào screening.py):
  from tf_journal_exclusion import classify_tf_journal, TF_LABEL

Hoặc chạy độc lập để test:
  python tf_journal_exclusion.py --file TF.ris --out test/
"""
from __future__ import annotations

import re
from typing import Optional

# ─── Whitelist 5 tạp chí mục tiêu Q1 ───
# Luôn forward sang screening rules (bypass EC-STRUCT, EC-NOSCOPE, EC7-*)
# Kể cả khi regex pre-screen đề xuất LIKELY_EXCLUDE
TF_WHITELIST: list[str] = [
    "International Journal of Production Research",
    "Digital Twin",
    "International Journal of Logistics Research and Applications",
    "Maritime Policy and Management",
    "Maritime Policy & Management",
    "International Journal of Sustainable Transportation",
]

# ─── Blacklist — journal → EC code mapping ───
# Gán LIKELY_EXCLUDE ngay lập tức khi record từ T&F thuộc journal này
TF_BLACKLIST: list[tuple[str, str]] = [
    # Built Environment / Construction
    ("International Journal of Construction Management",  "EC-STRUCT"),
    ("Journal of Asian Architecture and Building Engineering", "EC-STRUCT"),
    ("Nondestructive Testing and Evaluation",             "EC-STRUCT"),
    ("Structure and Infrastructure Engineering",          "EC-STRUCT"),
    ("Construction Management and Economics",             "EC-STRUCT"),
    ("Building and Environment",                          "EC-STRUCT"),
    # Nuclear
    ("Nuclear Technology",                                "EC-NOSCOPE"),
    # HCI / UI-UX
    ("International Journal of Human-Computer Interaction", "EC-NOSCOPE"),
    ("International Journal of Human–Computer Interaction", "EC-NOSCOPE"),
    ("Behaviour and Information Technology",              "EC-NOSCOPE"),
    # Manufacturing / Engineering Design
    ("International Journal of Computer Integrated Manufacturing", "EC7-mfg"),
    ("Journal of Engineering Design",                     "EC7-mfg"),
    ("Production and Manufacturing Research",             "EC7-mfg"),
    ("Production & Manufacturing Research",               "EC7-mfg"),
    ("Virtual and Physical Prototyping",                  "EC7-mfg"),
    ("International Journal of Advanced Manufacturing Technology", "EC7-mfg"),
    # Medical / Health (publisher-level for OA publishers)
    ("Cogent Engineering",                                "EC7-other"),   # Cogent OA multidisciplinary — review individually
    ("Cogent Social Sciences",                            "EC7-other"),
    ("Cogent Business and Management",                    "EC7-other"),
    # Agricultural
    ("Journal of Plant Diseases and Protection",          "EC-AGRI"),
]

# Label constants
TF_LABEL_WHITELIST = "BYPASS_WHITELIST"
TF_LABEL_NEUTRAL = "TF_NEUTRAL"
TF_LABEL_EXCLUDE_PREFIX = "TF_EXCLUDE:"


def normalize_journal(name: str) -> str:
    """Chuẩn hoá tên tạp chí để so sánh."""
    s = name.lower().strip()
    # Thay "&" → "and", xóa dấu câu dư
    s = s.replace("&", "and")
    s = re.sub(r"[–—-]", "-", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


# Precompute normalized versions
_WL_NORM: list[str] = [normalize_journal(j) for j in TF_WHITELIST]
_BL_NORM: list[tuple[str, str]] = [(normalize_journal(j), ec) for j, ec in TF_BLACKLIST]


def classify_tf_journal(journal_name: str, source: str) -> Optional[str]:
    """
    Xác định TF_PRE_LABEL cho một record dựa trên tên tạp chí.

    Trả về:
      TF_LABEL_WHITELIST          — luôn include (bypass exclusion rules)
      "TF_EXCLUDE:<EC_CODE>"      — loại trừ với mã EC cụ thể
      TF_LABEL_NEUTRAL            — không có quyết định từ journal filter
      None                        — source không phải tf (không áp dụng)

    Không thay đổi logic nếu source không phải 'tf'.
    """
    if source.lower() not in ("tf", "taylor & francis", "taylor and francis"):
        return None  # Không áp dụng

    if not journal_name:
        return TF_LABEL_NEUTRAL

    norm = normalize_journal(journal_name)

    # Kiểm tra whitelist trước
    for wl_norm in _WL_NORM:
        # Dùng substring match: journal có thể có volume/issue thêm vào
        if wl_norm in norm or norm in wl_norm:
            return TF_LABEL_WHITELIST

    # Kiểm tra blacklist
    for bl_norm, ec in _BL_NORM:
        if bl_norm in norm or norm in bl_norm:
            return f"{TF_LABEL_EXCLUDE_PREFIX}{ec}"

    return TF_LABEL_NEUTRAL


def is_tf_whitelisted(tf_pre_label: Optional[str]) -> bool:
    return tf_pre_label == TF_LABEL_WHITELIST


def is_tf_blacklisted(tf_pre_label: Optional[str]) -> tuple[bool, str]:
    """Trả về (is_excluded, ec_code)."""
    if tf_pre_label and tf_pre_label.startswith(TF_LABEL_EXCLUDE_PREFIX):
        ec = tf_pre_label[len(TF_LABEL_EXCLUDE_PREFIX):]
        return True, ec
    return False, ""


# ─── CLI độc lập để test ───
if __name__ == "__main__":
    import argparse
    import csv
    import os
    import sys

    # Import parser từ dedup.py nếu có, nếu không thì inline
    try:
        from dedup import parse_ris_records
    except ImportError:
        print("[ERROR] Cần dedup.py trong cùng thư mục để chạy standalone.", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Bước 8.1.1 — Test T&F journal exclusion module"
    )
    parser.add_argument("--file", required=True, help="File TF.ris cần test")
    parser.add_argument("--out", default=".", help="Thư mục đầu ra")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    records = parse_ris_records(args.file)
    print(f"[+] Đọc {len(records)} records từ {args.file}")

    out_path = os.path.join(args.out, "tf_journal_classification.csv")
    whitelist_count = 0
    blacklist_count = 0
    neutral_count = 0

    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["doi", "journal", "source", "tf_pre_label", "ec_code"])
        for r in records:
            journal = r.get("T2") or r.get("JF") or r.get("T1") or ""
            tf_label = classify_tf_journal(journal, r.source)
            is_bl, ec = is_tf_blacklisted(tf_label)
            if tf_label == TF_LABEL_WHITELIST:
                whitelist_count += 1
            elif is_bl:
                blacklist_count += 1
            else:
                neutral_count += 1
            w.writerow([r.doi_raw, journal, r.source, tf_label or "N/A", ec])

    print(f"[+] Kết quả:")
    print(f"    Whitelist (BYPASS):  {whitelist_count}")
    print(f"    Blacklist (EXCLUDE): {blacklist_count}")
    print(f"    Neutral:             {neutral_count}")
    print(f"[+] Báo cáo: {out_path}")
