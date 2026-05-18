# TÓM TẮT KẾT QUẢ TÌM KIẾM
# Digital Twin cho Vận hành Cảng Container

**File:** SR_Search_Results_Summary_v5.6.md
**Phiên bản:** v1.2 — 2026-05-19
**NCS:** HoaTX
**OSF Project:** https://osf.io/dxjw9/ (DOI: 10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 Items 7, 8, 16a + PRISMA-S Items 1–16
**Anchor:** `SR_Search_Strategy_v5.6_FINAL.md` v1.0 §9 (trạng thái tìm kiếm)

> Tài liệu này tóm tắt kết quả thực tế của Pha 2 (Bước 4–7). Số liệu lấy từ `dedup_report.txt` và `check_ris_integrity.py`. Dùng làm cơ sở cho PRISMA Flow Diagram (Bước 10) và Supplementary Package (Bước 20).

---

# §1. KẾT QUẢ TỔNG QUAN

| Chỉ số | Giá trị |
|--------|---------|
| Số file RIS thu thập | 23 files |
| Số lượt truy vấn thực hiện | 22 lượt (Q1–Q10 × Scopus+IEEE; Q11 Springer; Q12 T&F; Q13–Q22 GS gộp) |
| Tổng records đầu vào (raw) | **7.847** |
| Records sau dedup (unique pool) | **5.822** |
| Records loại bỏ qua dedup | 2.025 (25,8%) |
| Ngày chạy tìm kiếm | 2026-05-10 (Q1–Q9, Q11–Q12, GS); 2026-05-15 (Q10) |
| Ngày chạy dedup | 2026-05-15 (tái chạy sau Q10) |
| Ngày chạy Pha A pre-screen | 2026-05-15 (tái chạy sau Q10) |
| Truy vấn CHƯA chạy | Không — Q10 Vintage đã chạy 2026-05-15 (DEV-004 Resolved) |

---

# §2. CHI TIẾT THEO FILE

## 2.1 Scopus (10 file)

| File | Truy vấn | Records raw |
|------|----------|------------:|
| `PRIMARY_Scopus.ris` | Q1 CORE NARROW | 130 |
| `EXTENDED_Scopus.ris` | Q2 CORE EXTENDED | 1.518 |
| `T1_Scopus.ris` | Q3 T-L1 (Data Visibility) | 180 |
| `T2_Scopus.ris` | Q4 T-L2 (Operational State) | 246 |
| `T3_Scopus.ris` | Q5 T-L3 (Decision Support) | 422 |
| `T4_Scopus.ris` | Q6 T-L4 (Simulation & V&V) | 54 |
| `T5_Scopus.ris` | Q7 T-L5 (Closed-Loop Autonomy) | 34 |
| `T6_Scopus.ris` | Q8 Gate operations | 345 |
| `T7_Scopus.ris` | Q9 Quy mô + VN/ĐNÁ | 483 |
| `T8_Scopus.ris` | Q10 Vintage (Greenfield/Brownfield) | 9 |
| **Tổng Scopus** | | **3.421*** |

## 2.2 IEEE Xplore (10 file)

| File | Truy vấn | Records raw |
|------|----------|------------:|
| `PRIMARY_IEEE.ris` | Q1 CORE NARROW | 50 |
| `EXTENDED_IEEE.ris` | Q2 CORE EXTENDED | 1.118 |
| `T1_IEEE.ris` | Q3 T-L1 (Data Visibility) | 53 |
| `T2_IEEE.ris` | Q4 T-L2 (Operational State) | 154 |
| `T3_IEEE.ris` | Q5 T-L3 (Decision Support) | 135 |
| `T4_IEEE.ris` | Q6 T-L4 (Simulation & V&V) | 10 |
| `T5_IEEE.ris` | Q7 T-L5 (Closed-Loop Autonomy) | 54 |
| `T6_IEEE.ris` | Q8 Gate operations | 110 |
| `T7_IEEE.ris` | Q9 Quy mô + VN/ĐNÁ | 246 |
| `T8_IEEE.ris` | Q10 Vintage (Greenfield/Brownfield) | 13 |
| **Tổng IEEE** | | **1.943** |

## 2.3 Các nguồn bổ trợ (3 file)

| File | Nguồn | Truy vấn | Records raw |
|------|-------|----------|------------:|
| `GS.ris` | Google Scholar | Q13–Q22 GS sub (10 sub gộp) | 650 |
| `SPRINGER.ris` | Springer Link | Q11 (12 tháng) | 904 |
| `TF.ris` | Taylor & Francis | Q12 (6 tháng) | 928 |
| **Tổng bổ trợ** | | | **2.482** |

---

# §3. TỔNG HỢP THEO NGUỒN

| Nguồn | Raw | Unique (sau dedup) | Loại (dedup) |
|-------|----:|-------------------:|-------------:|
| Scopus | 3.422* | 2.787 | 635 |
| IEEE Xplore | 1.943 | 973 | 970 |
| Google Scholar | 650 | 298 | 352 |
| Springer Link | 904 | 872 | 32 |
| Taylor & Francis | 928 | 892 | 36 |
| **Tổng** | **7.847** | **5.822** | **2.025** |

*Ghi chú về chênh lệch parser:*
- *Scopus raw = 3.422 theo `dedup_report.txt`; per-file sum §2.1 = 3.421 (chênh 1 record do T8_Scopus.ris có ER tag không chuẩn từ Publish or Perish export → `check_ris_integrity.py` đếm 8; `dedup.py` đếm 9).*
- *Springer raw = 904 theo `dedup_report.txt`; `ris_integrity_report.csv` ghi 905 (chênh 1 record do 1 record trong SPRINGER.ris có TY nhưng thiếu ER tag chuẩn → integrity parser đếm thêm 1).*
- *Số liệu `dedup_report.txt` là authoritative trong cả hai trường hợp. Tổng 7.847 và unique 5.822 không bị ảnh hưởng.*

---

# §4. CHI TIẾT DEDUP 3 LỚP

| Lớp | Tiêu chí | Cặp loại |
|-----|----------|---------:|
| Lớp 1 — DOI exact | Chuẩn hoá DOI → so sánh chuỗi | 1.675 |
| Lớp 2 — Fuzzy title | RapidFuzz ≥ 90, cùng năm ±1, author prefix | 347 |
| Lớp 3 — Hash | MD5(Author + Year + Title) | 3 |
| **Tổng** | | **2.025** |

Borderline pairs (score 85–89): **19** — lưu trong `dedup_borderline_pairs.csv` để NCS xem xét.

Tỷ lệ dedup 25,8% nằm trong range bình thường (10–50%). Pool unique 5.822 nằm trong kỳ vọng [5.000, 7.000].

### Ưu tiên giữ khi trùng (source priority)

```
scopus=1 > ieee=2 > gs=3 > springer=4 > tf=5
```

---

# §5. KẾT QUẢ PHA A PRE-SCREEN (Bước 8.1)

Chạy `screening.py` trên `dedup_unique.ris` (5.822 records):

| Phân loại | Records | Tỷ lệ | Kỳ vọng |
|-----------|--------:|------:|---------|
| LIKELY_INCLUDE | 284 | 4,9% | 15–25% |
| REVIEW_NEEDED | 5.061 | 86,9% | 40–60% |
| LIKELY_EXCLUDE | 477 | 8,2% | 20–40% |
| Missing abstract | 1.422 | (trong 5.822) | – |

> **[WARN]** LIKELY_INCLUDE 4,9% < 5% — thấp hơn kỳ vọng. Phân tích: pool rất rộng (Q2 CORE EXTENDED + supplementary) bắt nhiều bài ngoài phạm vi; 86,9% REVIEW_NEEDED cho thấy NCS cần review Pha B Rayyan toàn bộ. Rules regex đủ strict, không nên relax vì false negative ít hơn false positive quan trọng hơn ở giai đoạn này.

### Phân bố LIKELY_EXCLUDE theo EC code (top)

| EC code | Số bài |
|---------|-------:|
| EC-ENERGY | 154 |
| EC-STRUCT | 113 |
| EC7-mfg | 72 |
| EC-NOSCOPE | 50 |
| EC7-health | 33 |
| EC1 | 27 |
| EC7-bim | 20 |
| EC2 | 18 |

---

# §6. TRUY VẤN ĐÃ HOÀN TẤT

Tất cả 12 truy vấn chính (Q1–Q12) + GS đã được thực hiện. DEV-004 (Q10 Vintage) đã Resolved 2026-05-15.

| Truy vấn | Ngày chạy | Files | Records |
|---------|-----------|-------|--------:|
| Q10 Vintage (Scopus) | 2026-05-15 | T8_Scopus.ris | 9 |
| Q10 Vintage (IEEE) | 2026-05-15 | T8_IEEE.ris | 13 |

*Q10 phục vụ RQ4d (vintage gap — greenfield vs brownfield). Dedup tái chạy sau khi merge T8 vào pool.*

---

# §7. PRISMA FLOW DIAGRAM DATA (Bước 10 — sơ bộ)

```
Records identified (raw, 23 files):               7.847
  Scopus:          3.422
  IEEE Xplore:     1.943
  Google Scholar:    650
  Springer Link:     904
  Taylor & Francis:  928

Duplicates removed (dedup.py 3 lớp):              2.025
  DOI exact (L1):                                 1.675
  Fuzzy title (L2):                                 347
  Hash (L3):                                          3

Records after dedup (unique pool):                 5.822

Title/Abstract screening (Pha A — regex):
  LIKELY_EXCLUDE (Pha A):                            477
  LIKELY_INCLUDE (→ Pha B Rayyan):                   284
  REVIEW_NEEDED (→ Pha B Rayyan):                  5.061

Records sent to Rayyan (Pha B):                    5.345
  (284 LIKELY_INCLUDE + 5.061 REVIEW_NEEDED)

[CÒN CHỜ — Pha B Rayyan]
Records excluded after T/A Pha B:                     TBD
Records to full-text retrieval:                       TBD
Full-text not retrieved (EC6):                        TBD
Records excluded after full-text:                     TBD
Studies included in synthesis:                        TBD
```

---

# §8. FILES ĐẦU RA PHA 2–3A

| File | Mô tả | Bước |
|------|-------|------|
| `search_results_v5.6/*.ris` | 23 RIS files gốc | 4–6 |
| `dedup_unique.ris` | Pool unique 5.822 records (có N1 source annotation) | 7 |
| `dedup_report.txt` | Báo cáo dedup chi tiết | 7 |
| `dedup_borderline_pairs.csv` | 19 cặp borderline (score 85–89) để NCS review | 7 |
| `dedup_unique_records.csv` | CSV version của pool unique | 7 |
| `ris_integrity_report.csv` | Kiểm tra toàn vẹn RIS (field completeness) | 7 |
| `03_screening/screening_pre.ris` | Pool Pha A (5.345 records → Rayyan) | 8 |
| `03_screening/screening_pre.csv` | CSV version để phân tích | 8 |
| `03_screening/screening_distribution.txt` | Phân bố INCLUDE/REVIEW/EXCLUDE | 8 |

---

# §9. LIÊN KẾT

| File | Quan hệ |
|------|---------|
| `SR_Search_Strategy_v5.6_FINAL.md` §9 | Status table (đã cập nhật với số liệu thực) |
| `SR_Deviation_Log_v5.6.md` | DEV-002 (filename mapping), DEV-004 (Q10 — Resolved) |
| `WorkPlan_v5.6_FINAL.md` | Bước 4–7 trạng thái |
| `dedup_report.txt` | Nguồn dữ liệu authoritative cho §3–4 |
| `03_screening/screening_distribution.txt` | Nguồn dữ liệu cho §5 |

---

## Lịch sử phiên bản

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-05-14 | Tạo ban đầu (21 files, 7.825 raw, 5.811 unique — Q10 chưa chạy) |
| v1.1 | 2026-05-15 | Q10 Vintage chạy xong (T8_Scopus 9 + T8_IEEE 13). Cập nhật: 23 files, 7.847 raw, 5.822 unique, 2.025 dedup, Pha A 284/5.061/477, Rayyan 5.345. DEV-004 Resolved. |
| **v1.2** | **2026-05-19** | **Kiểm toán: Missing abstract sửa 1.417→1.422 (từ screening_distribution.txt). Mở rộng footnote §3 ghi rõ Springer 905→904 discrepancy (parser edge case). Không ảnh hưởng tổng số liệu.** |

---

*SR_Search_Results_Summary_v5.6.md — v1.2 — 2026-05-19 — NCS HoaTX*
