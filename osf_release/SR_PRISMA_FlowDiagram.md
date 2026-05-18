# PRISMA 2020 FLOW DIAGRAM — DỮ LIỆU
# Digital Twin cho Vận hành Cảng Container

**File:** SR_PRISMA_FlowDiagram.md
**Phiên bản:** v1.1 — 2026-05-15
**NCS:** HoaTX
**OSF Project:** https://osf.io/dxjw9/ (DOI: 10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 Figure 1 + Item 16a (Records identified) + Item 16b (Included)
**Anchor:** `SR_Search_Results_Summary.md` v1.1 (nguồn số liệu)

> File này chứa dữ liệu điền vào PRISMA 2020 Flow Diagram (4 ô chính: Identification → Screening → Eligibility → Included). Hình vẽ cuối cùng tạo bằng PRISMA2020 R package hoặc tool online tại https://www.prisma-statement.org/prisma-2020-flow-diagram sau khi Pha B + Bước 9 hoàn tất.

---

# §1. SƠ ĐỒ CẤU TRÚC

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           IDENTIFICATION                                    │
│                                                                             │
│  Records identified from databases (n = 7.847):                            │
│    Scopus:           3.422                                                  │
│    IEEE Xplore:      1.943                                                  │
│    Springer Link:      904                                                  │
│    Taylor & Francis:   928                                                  │
│    Google Scholar:     650                                                  │
│                                                                             │
│  [Q10 Vintage đã chạy 2026-05-15 — DEV-004 Resolved]                       │
│                                                                             │
│  Records from other methods (n = 0):                                        │
│    Snowball: 0 (chưa thực hiện — sau Bước 9)                               │
│    Hand search: 0 (chưa thực hiện — trước Submit)                          │
└────────────────────────────┬────────────────────────────────────────────────┘
                             │ n = 7.847
                             ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Duplicates removed                                      │
│                                                                             │
│  Automated dedup (dedup.py 3 lớp):       2.025                             │
│    L1 — DOI exact:                        1.675                             │
│    L2 — Fuzzy title (RapidFuzz ≥ 90):      347                             │
│    L3 — Author+Year+Title hash:               3                             │
│                                                                             │
│  Rayyan auto-dedup (DOI-only):           TBD (chờ Bước 1.10)              │
└────────────────────────────┬────────────────────────────────────────────────┘
                             │ n = 5.822 unique
                             ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SCREENING                                         │
│                                                                             │
│  Records screened (T/A):                  5.822                            │
│                                                                             │
│  Pha A — Regex pre-screen (screening.py):                                  │
│    LIKELY_EXCLUDE:                          477 → loại trực tiếp           │
│    LIKELY_INCLUDE + REVIEW_NEEDED:        5.345 → chuyển sang Pha B        │
│                                                                             │
│  Pha B — Rayyan manual (NCS):             TBD  (chờ Bước 1.10–8.2)        │
│    Excluded T/A Pha B:                    TBD                               │
│    Reason distribution:                   TBD                               │
└────────────────────────────┬────────────────────────────────────────────────┘
                             │ n = TBD (sau Pha B)
                             ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ELIGIBILITY                                         │
│                                                                             │
│  Full-text assessed:                      TBD (Bước 9)                    │
│  Full-text not retrieved (EC6):           TBD                               │
│  Full-text excluded + reasons:            TBD                               │
│    EC-ENV:                                TBD                               │
│    EC-VESSEL:                             TBD                               │
│    EC-POLICY:                             TBD                               │
│    EC-SECUR:                              TBD                               │
│    EC-BLOCK:                              TBD                               │
│    EC-TELECOM:                            TBD                               │
│    EC-CUSTOMS:                            TBD                               │
│    EC-AGRI:                               TBD                               │
│    Other Lớp 2 EC:                        TBD                               │
└────────────────────────────┬────────────────────────────────────────────────┘
                             │ n = TBD (sau Bước 9)
                             ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INCLUDED                                          │
│                                                                             │
│  Studies included in synthesis:           TBD (Bước 11–12)                │
│  Studies in quantitative synthesis:       N/A (qualitative SR)             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# §2. BẢNG SỐ LIỆU ĐIỀN VÀO FLOW DIAGRAM

## 2.1 Identification box

| Trường PRISMA | Giá trị | Trạng thái |
|---------------|---------|------------|
| Records from Scopus | 3.422 | ✅ Confirmed (dedup_report.txt authoritative) |
| Records from IEEE Xplore | 1.943 | ✅ Confirmed |
| Records from Springer Link | 904 | ✅ Confirmed |
| Records from Taylor & Francis | 928 | ✅ Confirmed |
| Records from Google Scholar | 650 | ✅ Confirmed |
| Records from other sources | 0 | ✅ (snowball + hand search chưa thực hiện) |
| **Tổng raw** | **7.847** | **✅ Confirmed** |

*Ghi chú PRISMA Item 16a:* Q10 Vintage (Scopus + IEEE) chạy ngày 2026-05-15 — `T8_Scopus.ris` (9 records) + `T8_IEEE.ris` (13 records). DEV-004 Resolved. Tất cả 12 truy vấn chính đã thực hiện.

## 2.2 Deduplication box

| Trường PRISMA | Giá trị | Trạng thái |
|---------------|---------|------------|
| Duplicates — L1 DOI exact | 1.675 | ✅ Confirmed |
| Duplicates — L2 Fuzzy title | 347 | ✅ Confirmed |
| Duplicates — L3 Hash | 3 | ✅ Confirmed |
| **Tổng duplicates (automated — dedup.py)** | **2.025** | ✅ Confirmed |
| Duplicates (Rayyan auto-dedup) | TBD | ⬜ Chờ Bước 1.10 |
| Records after dedup | 5.822 | ✅ Confirmed |

## 2.3 Screening box (T/A)

| Trường PRISMA | Giá trị | Trạng thái |
|---------------|---------|------------|
| Records screened | 5.822 | ✅ |
| Records excluded — Pha A regex | 477 | ✅ |
| — EC-ENERGY | 154 | ✅ |
| — EC-STRUCT | 113 | ✅ |
| — EC7-mfg | 72 | ✅ |
| — EC-NOSCOPE | 50 | ✅ |
| — EC7-health | 33 | ✅ |
| — EC1 (vessel/offshore) | 27 | ✅ |
| — EC7-bim | 20 | ✅ |
| — EC2 (bulk/non-container) | 18 | ✅ |
| — Khác | 10 | ✅ |
| Records sent to Pha B (Rayyan) | 5.345 | ✅ |
| — LIKELY_INCLUDE | 284 | ✅ |
| — REVIEW_NEEDED | 5.061 | ✅ |
| Records excluded — Pha B Rayyan | TBD | ⬜ |
| Reasons (top EC codes) | TBD | ⬜ |

## 2.4 Eligibility box (Fulltext — Bước 9)

| Trường PRISMA | Giá trị | Trạng thái |
|---------------|---------|------------|
| Full-text assessed | TBD | ⬜ |
| Full-text not retrieved (EC6) | TBD | ⬜ |
| Full-text excluded | TBD | ⬜ |
| Reasons (EC Lớp 2) | TBD | ⬜ |

## 2.5 Included box

| Trường PRISMA | Giá trị | Trạng thái |
|---------------|---------|------------|
| Studies included in synthesis | TBD | ⬜ |
| Studies in quantitative synthesis | N/A | N/A — qualitative SR |

---

# §3. GHI CHÚ PHƯƠNG PHÁP (cho Methods §3.3 manuscript)

## 3.1 Identification

Tìm kiếm thực hiện ngày 2026-05-10 (Q1–Q9, Q11–Q12, GS) và 2026-05-15 (Q10 Vintage) trên 5 cơ sở dữ liệu: Scopus, IEEE Xplore, Springer Link, Taylor & Francis Online, và Google Scholar. Tổng 23 file RIS thu thập được 7.847 records. Chiến lược tìm kiếm bao gồm 12 truy vấn chính (Q1–Q12) + 10 sub-queries GS (Q13–Q22), phủ 5 chiều phân tích theo 5 RQ.

## 3.2 Deduplication

Khử trùng lặp thực hiện bằng pipeline 3 lớp tự động (`dedup.py`): (1) DOI exact matching sau chuẩn hoá, (2) Fuzzy title matching với RapidFuzz `token_sort_ratio ≥ 90` kết hợp năm xuất bản ±1, (3) MD5 hash của Author + Year + Title. Tổng 2.025 records bị loại (25,8%). Borderline pairs (score 85–89): 19 cặp lưu trong `dedup_borderline_pairs.csv`. Cross-validation với Rayyan auto-dedup sẽ thực hiện sau khi upload (dự kiến AGREE ≥ 99%).

## 3.3 Screening Pha A (automated)

Pre-screening tự động bằng `screening.py` (13 priority rules — IC1/IC2 inclusion rules + EC1–EC-STRUCT exclusion rules) trên toàn bộ pool 5.822 records. Kết quả: 477 LIKELY_EXCLUDE (loại trực tiếp), 5.345 records (284 LIKELY_INCLUDE + 5.061 REVIEW_NEEDED) chuyển sang Pha B Rayyan.

## 3.4 Screening Pha B (Rayyan — chờ NCS)

NCS sẽ review thủ công 5.345 records trên Rayyan Essentials, áp dụng đầy đủ 28 mã EC/IC từ `SR_Eligibility_Criteria.md`. Intra-rater reliability: 50 records chấm lần 2 sau ≥ 14 ngày → Cohen's κ mục tiêu ≥ 0.75 (Bước 14).

---

# §4. CÔNG CỤ TẠO HÌNH VẼ CUỐI

Sau khi có đủ số liệu (Bước 9 hoàn tất), tạo hình PRISMA 2020 chính thức bằng một trong:

1. **PRISMA2020 R package** (Haddaway et al. 2022):
   ```r
   install.packages("PRISMA2020")
   library(PRISMA2020)
   # Điền data từ §2 vào PRISMA_data template
   PRISMA_flowdiagram(data, interactive = FALSE, prior_studies = FALSE)
   ```

2. **Online tool** tại https://www.prisma-statement.org/prisma-2020-flow-diagram — điền tay từ §2.

3. **Shiny app** tại https://estech.shinyapps.io/prisma_flowdiagram/ — cho phép export SVG/PNG chất lượng cao.

Output: `figures/PRISMA_flowdiagram_v1.0.pdf` (500 dpi, embed font).

---

# §5. VERSIONING

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-05-14 | Tạo ban đầu — Identification (7.825, Q10 chưa chạy) + Dedup (2.014) + Screening Pha A (476/5.335) |
| **v1.1** | **2026-05-15** | **Q10 Vintage chạy xong. Cập nhật: 7.847 raw, 2.025 dedup, 5.822 unique, Pha A 477/5.345. Scopus 3.422, IEEE 1.943. DEV-004 Resolved.** |

---

# §6. LIÊN KẾT

| File | Quan hệ |
|------|---------|
| `SR_Search_Results_Summary.md` | Nguồn số liệu §2.1–2.3 |
| `SR_Eligibility_Criteria.md` | 28 mã EC/IC dùng trong §2.3–2.4 |
| `SR_Deviation_Log.md` | DEV-004 (Q10 Resolved) — không còn ảnh hưởng §2.1 |
| `dedup_report.txt` | Chi tiết Lớp 1/2/3 cho §2.2 |
| `03_screening/screening_distribution.txt` | Chi tiết EC codes cho §2.3 |
| `SR_PRISMA_Checklist.md` | Item 16a/16b cross-reference |

---

*SR_PRISMA_FlowDiagram.md — v1.1 — 2026-05-15 — NCS HoaTX*
