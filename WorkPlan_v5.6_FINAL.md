# KẾ HOẠCH TỔNG THỂ TỔNG QUAN HỆ THỐNG
# Digital Twin cho Vận hành Cảng Container

**Phiên bản:** v1.0 — 2026-05-08
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**OSF DOI:** [10.17605/OSF.IO/DXJW9](https://doi.org/10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 (Page et al. 2021) — 27 items / 42 sub-items + PRISMA-S (Rethlefsen et al. 2021) 16 items + Kitchenham & Charters (2007) SE SR Guidelines + PRESS (McGowan et al. 2016)
**Loại tổng quan:** Systematic Review định tính — typology synthesis với bibliometric layer (Donthu et al. 2021); KHÔNG meta-analysis
**Mục tiêu xuất bản:** Tạp chí Q1 — ưu tiên *International Journal of Production Research* (IF ≈ 9.2), *Maritime Policy & Management* (IF ≈ 6.0); dự phòng *Computers in Industry*, *Annual Reviews in Control*, *Journal of Marine Science and Engineering*

---

# §0. NGUYÊN TẮC LÀM VIỆC — BẮT BUỘC ĐỌC TRƯỚC

## 0.1 Vai trò Claude và NCS

1. Claude đóng vai trợ lý nghiên cứu — hỗ trợ phân tích, viết tài liệu, code khi được phép.
2. **Mặc định: Claude KHÔNG code.** Mọi yêu cầu mặc định là phân tích/viết — code cần NCS xác nhận trước.
3. NCS là người quyết định cuối cùng về mọi vấn đề khoa học và là **người chấm duy nhất** (single reviewer).

## 0.2 Ngôn ngữ và Tài liệu nội bộ vs Công khai

- Toàn bộ tài liệu SR nội bộ viết bằng **tiếng Việt**; thuật ngữ tiếng Anh giữ trong ngoặc.
- **Nhãn nội bộ "v5.6"** chỉ dùng trong workspace cá nhân — KHÔNG xuất hiện trong: (i) bản thảo manuscript, (ii) tài liệu OSF, (iii) supplementary nộp tạp chí.
- Khi viết text cho OSF / manuscript / supplementary → strip "v5.6" và dùng `osf_release/` làm thư mục bản công khai.

## 0.3 Toàn vẹn dữ liệu gốc (tuyệt đối)

- **NGHIÊM CẤM truncate** title hoặc abstract trong bất kỳ bước so khớp / dedup / sàng lọc.
- Mọi matching dùng TOÀN BỘ chuỗi sau khi chuẩn hoá (lowercase, strip whitespace).
- Dedup DOI: chuẩn hoá để so sánh, giữ nguyên DOI gốc trong output.
- Đánh giá tóm tắt: đọc toàn bộ abstract, không chỉ câu đầu.

## 0.4 Đồ thị tri thức (Graph Network)

- File trung tâm: `D:\NCS_BaiBao_1\baibao1.bk_a_congviec\graph_net.md`.
- Mọi tri thức / kết quả / quyết định thiết kế PHẢI cập nhật vào graph_net.md sau mỗi bước.
- Node phải liên kết logic, không chỉ liệt kê.

## 0.5 Backup Policy

| Đối tượng | Tần suất | Đích |
|------------|-----------|-------|
| `#checklist/sr_works_v5.6/` (trừ `osf_release/`, `bak/`) | Hàng tuần Chủ nhật 22:00 | Google Drive / GitHub private |
| RIS files trong `search_results_v5.6/` | 1 lần sau Bước 7 | OSF Files |
| Rayyan project state | Weekly snapshot CSV | `03_screening/Rayyan_weekly_snapshots/` |
| OSF Project state | Sau mỗi mốc Bước | `SR_OSF_Registration_v5.6.md` |
| Archive `bak/` | Sau Bước 22 + 30 ngày sau publication | External storage |

## 0.6 Mô hình một người chấm + Rayyan Essentials

- **NCS chấm duy nhất.** Rayyan Essentials = audit trail + custom reasons.
- **Không giả định Essentials có:** PDF attachment, AI ranking, blinded mode. Thiếu features → phương án dự phòng (Recovery R2).
- **Thay Inter-rater Reliability (IRR) bằng Intra-rater Reliability:** chấm 50 bài lần 1 → đợi ≥ 14 ngày → chấm lại không xem lần 1 → tính Cohen's κ giữa 2 lần (mục tiêu κ ≥ 0.75).
- **Bù trừ:** ghi rõ trong Limitations (single reviewer + non-blinded) + bổ sung Expert Validation (Bước 21) đóng vai "ý kiến thứ hai" về phân loại Maturity Level và Research Agenda.

## 0.7 Câu hỏi nghiên cứu — Single Source of Truth

> **Bộ 5 RQ chính thức** lưu trong file riêng `SR_Research_Questions_v5.6.md` v1.0. WorkPlan KHÔNG duplicate RQ — chỉ tham chiếu. Mọi sửa đổi RQ phải bắt đầu từ file SoT đó, sau đó propagate xuống WorkPlan + Strategy + Extraction Form.

### Tóm tắt RQ (chi tiết xem RQ doc)

| RQ | Tên | Sub | Bước giải quyết | Output |
|----|-----|------|------------------|---------|
| **RQ1** | Bức tranh tổng thể (WHAT) | 1a–1e | 16 (Bibliometric) | `SR_Bibliometric_v5.6.md` + 5 PNG |
| **RQ2** | Mức độ trưởng thành (HOW MATURE) — L1–L5 × 5 lĩnh vực × Quy mô | 2a–2c | 11 + 12 + 17.2 | Heat-map L × Lĩnh vực + L × Quy mô |
| **RQ3** | Phương pháp + Nguồn lực (HOW METHOD) | 3a–3c | 11 + 17.4 | Bảng method × tầng × resource |
| **RQ4** | Khoảng trống (WHERE GAPS) — 5 chiều | 4a–4e | 17.2, 17.3, 17.4, 17.5 | Heat-map 3D + bảng vintage + open problems |
| **RQ5** | Chương trình NC + Lộ trình (WHAT NEXT) — conditional roadmap | 5a–5d | 17.5, 17.6 | `SR_Research_Agenda_v5.6.md` |

**Đặc điểm thiết kế RQ:**

1. RQ4 phủ 5 chiều (combinatorial, method, geographic, vintage, open problems) — không bỏ sót dimension thực tiễn quan trọng.
2. RQ5a derive priorities từ RQ4 với *gap_size × demand × feasibility* — KHÔNG pre-empt direction.
3. RQ5b dùng "Trần thực tế (Realistic Ceiling)" — không giả định mọi cảng cần lên L5.

**Chất lượng nghiên cứu** (8 tiêu chí Q1–Q8 Kitchenham) là PRISMA Item 11 — đặt ở Methods §3.5 manuscript, KHÔNG phải RQ độc lập.

## 0.8 Tuân thủ PRISMA 2020 nghiêm khắc

- Mỗi Bước có **mapping tường minh tới PRISMA item(s)** — ghi trong header.
- Items không áp dụng (12, 13e, 14, 15, 19, 20c, 21, 22) phải có **justification tường minh** trong `SR_PRISMA_Checklist_v5.6.md` và mục Limitations.
- 4 lý do mặc định cho N/A: (i) qualitative typology SR, không meta-analysis; (ii) không có effect estimates; (iii) heterogeneity statistic không áp dụng; (iv) GRADE / funnel plot dành cho intervention outcomes.

## 0.9 Quản trị Rủi ro và Sai lệch

- **`SR_Deviation_Log_v5.6.md`** — log mọi sai lệch so với WorkPlan/Protocol (8 trường). Source duy nhất cho Bước 20.3 OSF Amendments.
- **`SR_Risk_Register_v5.6.md`** — 15 rủi ro với likelihood × impact × mitigation × Recovery trigger.
- **Recovery Procedures R1–R7** — xem §V cuối file.

---

# §I. CẤU TRÚC 6 PHA × 22 BƯỚC

| Pha | Bước | Mục tiêu | PRISMA Items |
|-----|-------|----------|---------------|
| **Pha 1 — Thiết kế** | 1–3 | Pre-registration + Eligibility + Search design + Pilot | 1, 2, 5, 6, 7, 24a, 24b |
| **Pha 2 — Tìm kiếm** | 4–7 | Database + Supplementary + Integrity + Dedup | 6, 7, 8, 16a + PRISMA-S 1–16 |
| **Pha 3 — Sàng lọc** | 8–10 | T/A → Fulltext → Flow Diagram | 8, 16a, 16b |
| **Pha 4 — Trích xuất + Chất lượng** | 11–13 | Data extraction + Maturity classification + Quality appraisal | 9, 10a, 10b, 11, 17 |
| **Pha 5 — Tổng hợp + Phân tích** | 14–17 | Intra-rater + Sensitivity + Bibliometric + Synthesis | 8, 13c, 13d, 13f, 17, 18, 20a, 20b, 23c, 23d |
| **Pha 6 — Viết + Nộp** | 18–22 | Manuscript + Supplementary + Expert Validation + Submit | 1, 2, 3, 4, 14, 15, 21, 22, 23a–d, 25, 26, 27 |

## Tổng quan trạng thái

| Pha | Bước | Trạng thái |
|-----|-------|-------------|
| Pha 1 — Thiết kế | 1–3 | 🔄 Bước 1: 1.1/1.3/1.6/1.7/1.8/1.9 ✅; 1.10–1.13 ⬜ (NCS Rayyan); Bước 2: SR_Eligibility_Criteria ✅; Bước 3: pilot PRIMARY_Scopus 130 records ✅ |
| Pha 2 — Tìm kiếm | 4–7 | ✅ Dữ liệu 21 files / 7.825 records (search_results_v5.6/); dedup 7.825→5.811 (25.7%) |
| Pha 3 — Sàng lọc | 8–10 | 🔄 Bước 8 Pha A ✅ (284/5.051/476); Pha B ⬜ chờ Rayyan; Bước 9–10 ⬜ |
| Pha 4 — Trích xuất + Chất lượng | 11–13 | ⬜ Chưa (chờ Pha B xong) |
| Pha 5 — Tổng hợp + Phân tích | 14–17 | ⬜ Chưa |
| Pha 6 — Viết + Nộp | 18–22 | ⬜ Chưa |

**Cập nhật 2026-05-14:**
- Pha 2 hoàn tất: 21 RIS files (7.825 records), dedup pipeline chạy OK, 5.811 unique records.
- Pha A screening hoàn tất: `03_screening/screening_pre.ris` sẵn sàng upload Rayyan.
- Bước 2 sub-tasks 2.1–2.5 xác nhận ✅ (SR_Eligibility_Criteria v1.0 đầy đủ).
- Bước 4.12, 5.4, 6.4 ✅: Strategy §9 cập nhật với số records thực tế.
- DEV-004 thêm: Q10 Vintage (Scopus+IEEE) chưa chạy — NCS cần chạy trước Pha B.
- Tạo mới 4 files: SR_Search_Results_Summary_v5.6.md, SR_PRISMA_FlowDiagram_v5.6.md, SR_Classification_Rubric_v5.6.md, SR_Quality_Appraisal_v5.6.md.
- SR_PRISMA_Checklist_v5.6.md skeleton 27/27 items (section/page TBD sau Bước 18).
- Xem `SR_Deviation_Log_v5.6.md` DEV-001/002/003/004 cho các lệch kế hoạch đã ghi nhận.

## Đường găng (Critical Path)

```text
[⬜] Bước 1  Pre-registration OSF + Rayyan setup            [PRISMA 24a, 24b]
[⬜] Bước 2  Eligibility Criteria độc lập (28 EC/IC)        [PRISMA 5]
[⬜] Bước 3  Pilot search + Calibration                     [PRISMA 6]
    ↓
[⬜] Bước 4  Database search Q1–Q10 (Scopus + IEEE)         [PRISMA 6, 7]
[⬜] Bước 5  GS supplementary Q13–Q22                       [PRISMA 6, 7]
[⬜] Bước 6  Springer + T&F bổ trợ Q11–Q12                  [PRISMA 6, 7]
[⬜] Bước 7  Khử trùng lặp 3 lớp                            [PRISMA 8, 16a + PRISMA-S 16]
    ↓
[⬜] Bước 8  Title/Abstract Screening (Pha A + Pha B)       [PRISMA 8, 16a, 16b]
[⬜] Bước 9  Fulltext + Snowball + Hand search              [PRISMA 6, 8, 16a, 16b]
[⬜] Bước 10 PRISMA Flow Diagram                            [PRISMA 16a]
    ↓
[⬜] Bước 11 Data Extraction Form (6 nhóm trường)           [PRISMA 9, 10a, 10b]
[⬜] Bước 12 Maturity + Operational Area classification     [PRISMA 10a, 17]
[⬜] Bước 13 Quality Appraisal + Borderline Protocol        [PRISMA 11, 18]
    ↓
[⬜] Bước 14 Intra-rater reliability (Cohen's κ)            [PRISMA 8, 23c]
[⬜] Bước 15 Sensitivity Analysis (recall validation)       [PRISMA 13f, 20d]
[⬜] Bước 16 Bibliometric Analysis (RQ1)                    [PRISMA 17, 20a, 23d]
[⬜] Bước 17 Thematic Synthesis + Heat-map 3D + RA          [PRISMA 13c, 13d, 17, 20a, 20b]
    ↓
[⬜] Bước 18 Manuscript drafting (IMRaD + Q1 style)         [PRISMA 1, 2, 3, 4, 23a–d]
[⬜] Bước 19 PRISMA Checklist + Limitations + N/A           [PRISMA 14, 15, 21, 22, 23b, 23c, 27]
[⬜] Bước 20 Supplementary Package + OSF Amendments         [PRISMA 24c, 27 + PRISMA-S 8]
[⬜] Bước 21 Expert Validation (Delphi-lite, 3–5 chuyên gia)[bổ trợ PRISMA 23]
[⬜] Bước 22 Final review + Cover letter + Submit           [PRISMA 1, 2, 25, 26]
```

---

# §II. CHI TIẾT TỪNG BƯỚC

## === PHA 1: THIẾT KẾ ===

---

### BƯỚC 1 — Pre-registration OSF + Rayyan setup

**Pre-conditions:** Tài khoản OSF + Rayyan active.
**Exit criteria:** OSF Project + Registration DOI + Rayyan project sẵn sàng; verify Essentials features done; cập nhật OSF DOI vào header WorkPlan + Strategy + RQ doc.
**PRISMA items:** 24a (Registration), 24b (Protocol accessibility), 8 (Selection process — setup).
**Người thực hiện:** NCS (chính) + Claude (hỗ trợ).

#### 1.1 OSF Project chain

| Việc | Người | Trạng thái |
|------|-------|-------------|
| 1.1 Tạo OSF Project (public) cho bài SR | NCS | ✅ 2026-05-10 — Project `dxjw9` ([osf.io/dxjw9](https://osf.io/dxjw9/)) |
| 1.2 Cấu hình metadata (Title, Description, Tags, Contributors, License CC-BY 4.0) | NCS | ⬜ |
| 1.3 Soạn Registration submission text (PRISMA-P style 20 mục) | Claude | ✅ 2026-05-10 — [SR_OSF_Registration_Submission_v5.6.md](#checklist/sr_dt_port/SR_OSF_Registration_Submission_v5.6.md) v1.0 |
| 1.4 NCS review + chỉnh sửa Registration text (4 trường ⚠️) | NCS | ⬜ NCS hoãn để sau (Funding/CoI/Authors/Support) |
| 1.5 Submit Registration → nhận DOI 10.17605/OSF.IO/* | NCS | 🔄 DOI có sẵn `10.17605/OSF.IO/DXJW9` — ⚠️ cần verify Project DOI vs Registration DOI |
| 1.6 Cập nhật OSF Project ID vào header 5 file v1.0 (RQ + Strategy + WorkPlan + Eligibility + Extraction Form) | Claude | ✅ 2026-05-10 |
| 1.7 Tạo `osf_release/` với 5 file đã strip nhãn nội bộ (RQ + Strategy + WorkPlan + Eligibility + Extraction Form) | Claude | ✅ 2026-05-11 |
| 1.8 Cập nhật OSF DOI vào header 5 file v1.0 + 5 file `osf_release/` | Claude | ✅ 2026-05-11 |
| 1.9 NCS upload `osf_release/` lên OSF Files | NCS | ✅ 2026-05-11 — folder `01_protocol/` |

#### 1.2 Rayyan chain

| Việc | Người | Trạng thái |
|------|-------|-------------|
| 1.10 Tạo Rayyan project SR_DT_Port | NCS | ⬜ |
| 1.11 Verify Essentials features (custom reasons, PDF, AI ranking, blinded mode) — ghi nhận features có/không | NCS | ⬜ |
| 1.12 Nạp 28 mã EC/IC làm Reasons taxonomy (nếu Essentials hỗ trợ) | NCS | ⬜ |
| 1.13 Cập nhật Rayyan project ID vào `SR_OSF_Registration_v5.6.md` | NCS | ⬜ |

> **CẢNH BÁO trình tự (Recovery R1):** KHÔNG upload pool RIS lên Rayyan trước Bước 7 dedup. Bước 1 chỉ tạo project trống — pool sẽ upload sau Bước 7.

---

### BƯỚC 2 — Eligibility Criteria độc lập

**Pre-conditions:** Bước 1 done; định hướng RQ rõ.
**Exit criteria:** `SR_Eligibility_Criteria_v5.6.md` v1.0 phê duyệt; PICOC khung; 28 mã EC/IC đầy đủ; 6 borderline rules.
**PRISMA items:** 5 (Eligibility criteria).

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 2.1 Khung PICOC | Population, Intervention, Comparison, Outcome, Context | ✅ 2026-05-08 — §I file |
| 2.2 Tiêu chí bao gồm IC1–IC5 | Align với 5 lĩnh vực vận hành (RQ2) | ✅ 2026-05-08 — §II file |
| 2.3 Tiêu chí loại trừ Lớp 1 (T/A) | EC1–EC9 + EC7-{mfg/bim/health/noctx/other} + EC-CYBER/ENERGY/GENERIC/IT/NOSCOPE/PAX/STRUCT | ✅ 2026-05-08 — §III file |
| 2.4 Tiêu chí loại trừ Lớp 2 (Fulltext) | EC-ENV / VESSEL / POLICY / SECUR / BLOCK / TELECOM / CUSTOMS / AGRI + EC6 | ✅ 2026-05-08 — §IV file |
| 2.5 Borderline rules (6) | DT-driven, Smart port, Mfg-transferable, Bulk/RoRo, Review paper, Vintage greenfield/brownfield | ✅ 2026-05-08 — §VI file |
| 2.6 PRESS peer review của Strategy | NCS self-review 8 tiêu chí (xem Strategy §8) | ⬜ NCS task |

**Output cuối:** `SR_Eligibility_Criteria_v5.6.md` v1.0 phê duyệt.

---

### BƯỚC 3 — Pilot search + Calibration

**Pre-conditions:** Bước 2 done.
**Exit criteria:** Pilot 100 records → calibration regex EC/IC; điều chỉnh threshold borderline.
**PRISMA items:** 6 (Information sources — pilot).

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 3.1 Chạy thử Q1 CORE NARROW trên Scopus → ≈ 130 records | NCS | ⬜ |
| 3.2 Đọc 50 abstract đầu tiên → calibrate IC1 (DT-driven vs DT-mention) | NCS | ⬜ |
| 3.3 Verify SUBJAREA filter không loại bỏ bài DT-port hợp lệ | NCS | ⬜ |
| 3.4 Refine query Q2 EXTENDED dựa trên gap nhận diện | Claude | ⬜ |
| 3.5 Quyết định: chạy đầy đủ 32 lượt query hay điều chỉnh trước | NCS | ⬜ |

---

## === PHA 2: TÌM KIẾM ===

---

### BƯỚC 4 — Database search Scopus + IEEE (Q1–Q10)

**Pre-conditions:** Bước 3 done.
**Exit criteria:** 20 lượt query (10 Scopus + 10 IEEE) chạy đủ; RIS files lưu trong `search_results_v5.6/`; số records mỗi query ghi vào Strategy §9.
**PRISMA items:** 6, 7 + PRISMA-S 1–8.

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 4.1 Chạy Q1 CORE NARROW trên Scopus → `Q1_Scopus.ris` | NCS | ✅ `PRIMARY_Scopus.ris` — 130 records |
| 4.2 Chạy Q1 CORE NARROW trên IEEE Xplore → `Q1_IEEE.ris` | NCS | ✅ `PRIMARY_IEEE.ris` — 50 records |
| 4.3 Chạy Q2 CORE EXTENDED trên Scopus + IEEE | NCS | ✅ `EXTENDED_Scopus.ris` (1518) + `EXTENDED_IEEE.ris` (1118) |
| 4.4 Chạy Q3 T-L1 trên Scopus + IEEE | NCS | ✅ `T1_Scopus.ris` (180) + `T1_IEEE.ris` (53) |
| 4.5 Chạy Q4 T-L2 trên Scopus + IEEE | NCS | ✅ `T2_Scopus.ris` (246) + `T2_IEEE.ris` (154) |
| 4.6 Chạy Q5 T-L3 trên Scopus + IEEE | NCS | ✅ `T3_Scopus.ris` (422) + `T3_IEEE.ris` (135) |
| 4.7 Chạy Q6 T-L4 trên Scopus + IEEE | NCS | ✅ `T4_Scopus.ris` (54) + `T4_IEEE.ris` (10) |
| 4.8 Chạy Q7 T-L5 trên Scopus + IEEE | NCS | ✅ `T5_Scopus.ris` (34) + `T5_IEEE.ris` (54) — xem DEV-003 |
| 4.9 Chạy Q8 Gate trên Scopus + IEEE | NCS | ✅ `T6_Scopus.ris` (345) + `T6_IEEE.ris` (110) |
| 4.10 Chạy Q9 Quy mô + tên cảng VN/ĐNÁ trên Scopus + IEEE | NCS | ✅ `T7_Scopus.ris` (483) + `T7_IEEE.ris` (246) |
| 4.11 Chạy Q10 Vintage trên Scopus + IEEE | NCS | ✅ 2026-05-15 — `T8_Scopus.ris` (9) + `T8_IEEE.ris` (13) — DEV-004 Resolved |
| 4.12 Cập nhật Strategy §9 status table với số records thực tế | Claude | ✅ 2026-05-14 — Strategy §9 cập nhật đầy đủ |

---

### BƯỚC 5 — Google Scholar supplementary (Q13–Q22)

**Pre-conditions:** Bước 4 done.
**Exit criteria:** 10 truy vấn con × 50–100 records; export RIS gs01.ris … gs10.ris; gộp `GS.ris`.
**PRISMA items:** 6, 7 + PRISMA-S 4 (Online resources / browsing).

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 5.1 Chạy Q13–Q22 trên Google Scholar (10 sub-queries) | NCS | ✅ 10 sub-queries thực hiện |
| 5.2 Lưu kết quả vào RIS (dùng Publish or Perish hoặc Zotero connector) | NCS | ✅ |
| 5.3 Gộp 10 RIS thành `GS.ris` | NCS | ✅ `GS.ris` — 650 records |
| 5.4 Cập nhật Strategy §9 | Claude | ✅ 2026-05-14 |

---

### BƯỚC 6 — Springer Link + Taylor & Francis bổ trợ (Q11–Q12)

**Pre-conditions:** Bước 5 done.
**Exit criteria:** SPRINGER.ris + TF.ris đầy đủ; T&F-specific exclusion list lưu trong Strategy §4.12.
**PRISMA items:** 6, 7 + PRISMA-S 4.

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 6.1 Chạy Q11 trên Springer Link (12 tháng) | NCS | ✅ `SPRINGER.ris` — 905 records |
| 6.2 Chạy Q12 trên Taylor & Francis (6 tháng) | NCS | ✅ `TF.ris` — 928 records |
| 6.3 Verify pool T&F whitelist (5 tạp chí target) | NCS | ✅ `tf_journal_exclusion.py` — whitelist embedded |
| 6.4 Cập nhật Strategy §9 | Claude | ✅ 2026-05-14 |

**Tổng cuối Pha 2 (kỳ vọng):** ≈ 6.000–9.000 records raw.

---

### BƯỚC 7 — Khử trùng lặp 3 lớp

**Pre-conditions:** Bước 4–6 done.
**Exit criteria:** unique pool nằm trong [5.000, 7.000] (kỳ vọng); cross-validate với Rayyan DOI-only; output `dedup_unique.ris` + `dedup_report.txt`.
**PRISMA items:** 8 (Selection process), 16a (Records identified) + PRISMA-S 16 (Deduplication).

#### 7.1 Pipeline 3 lớp

| Lớp | Tiêu chí | Công cụ |
|------|----------|----------|
| **1 — DOI exact** | Chuẩn hoá DOI (lowercase, strip prefix `https://doi.org/`) → so sánh chuỗi | Python stdlib |
| **2 — Fuzzy title** | RapidFuzz `token_sort_ratio ≥ 90` trên title đã chuẩn hoá; ưu tiên giữ source theo Scopus > IEEE > GS > SP > TF | RapidFuzz |
| **3 — Author + Year + Title hash** | Hash MD5 (lowercase author1 + year + first 30 char title) | Python stdlib |

#### 7.2 Quy trình

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 7.1 Liệt kê toàn bộ RIS files trong `search_results_v5.6/` | Claude | ✅ 21 files confirmed |
| 7.2 Viết `check_ris_integrity.py` → output `ris_integrity_report.csv` | Claude | ✅ Script viết + chạy OK |
| 7.3 NCS review + chạy script | NCS | ✅ Chạy OK — báo cáo lưu `ris_integrity_report.csv` |
| 7.4 Viết `dedup.py` 3 lớp + inject N1 source annotation | Claude | ✅ Script viết + N1 injection hoàn tất |
| 7.5 Chạy dedup → `dedup_unique.ris` (5.811 records) + `dedup_report.txt` | NCS | ✅ 7.825→5.811 (25,7%) |
| 7.6 Cross-validate với Rayyan auto-dedup DOI-only | NCS | ⬜ Chờ Rayyan setup (Bước 1.10) |
| 7.7 NCS upload `03_screening/screening_pre.ris` vào Rayyan | NCS | ⬜ Chờ Bước 1.10 + Q10 Vintage |
| 7.8 Export Rayyan pool → `rayyan_export_after_dedup.csv` (audit trail) | NCS | ⬜ |

**Output Bước 7:**

- `dedup_unique_records.csv` — danh sách unique với key fields
- `dedup_unique.ris` — full RIS metadata
- `dedup_report.txt` — chi tiết Lớp 1/2/3
- `dedup_strict_report.txt` — Python vs Rayyan AGREE evidence
- `dedup_borderline_pairs.csv` — Layer 2 score 85–89 (chưa đủ 90 nhưng đáng review)

---

## === PHA 3: SÀNG LỌC ===

---

### BƯỚC 8 — Title/Abstract Screening (Pha A Python + Pha B Rayyan)

**Pre-conditions:** Bước 7 done.
**Exit criteria:** mỗi record có 1 trong 3 nhãn cuối {INCLUDE, EXCLUDE, MAYBE} + EC code (cho EXCLUDE); pilot 30 bài calibration κ ≥ 0.75 trên Pha A.
**PRISMA items:** 8 (Selection process), 16a, 16b.

#### 8.1 Pha A — Python pre-screen

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 8.1.1 Viết `tf_journal_exclusion.py` (T&F whitelist + journal/publisher exclusion) | Claude | ⬜ |
| 8.1.2 Viết `screening.py` với 13 priority rules (regex IC/EC) | Claude | ⬜ |
| 8.1.3 Chạy `screening.py` trên `dedup_unique.ris` → output `screening_pre_v5.6.csv` + `.ris` (PRE_LABEL trong N1) + `screening_distribution.txt` | NCS + Claude | ⬜ |
| 8.1.4 NCS review distribution — kỳ vọng LIKELY_INCLUDE 15–25%, REVIEW_NEEDED 40–60%, LIKELY_EXCLUDE 20–40% | NCS | ⬜ |

#### 8.2 Pha B — Rayyan formal screening

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 8.2.1 NCS upload `screening_pre_v5.6.ris` vào Rayyan project | NCS | ⬜ |
| 8.2.2 Pilot 30 records (10 INCLUDE + 10 EXCLUDE + 10 REVIEW theo PRE_LABEL) → NCS đọc tóm tắt → tính κ Pha A vs NCS trên 30 bài | NCS | ⬜ |
| 8.2.3 Nếu κ < 0.75 → hiệu chỉnh regex `screening.py` v1.1 → re-run Pha A | conditional | ⬜ |
| 8.2.4 NCS chấm tuần tự pool: LIKELY_EXCLUDE (xác nhận nhanh) → REVIEW_NEEDED (kỹ) → LIKELY_INCLUDE (xác nhận) | NCS | ⬜ |
| 8.2.5 Custom reasons trong Rayyan = 28 mã EC/IC (verify Essentials hỗ trợ; nếu không → fallback Excel) | NCS | ⬜ |
| 8.2.6 Snapshot weekly CSV (Bước 0.5 backup) | NCS | ⬜ |

**Output Bước 8:** `ta_screening_v5.6.csv` (n × 4 cột: doi, title, ta_decision, ta_ec_code).

---

### BƯỚC 9 — Fulltext Screening + Snowball + Hand search

**Pre-conditions:** Bước 8 done.
**Exit criteria:** mỗi included record có quyết định fulltext + EC code Lớp 2 (nếu excluded); snowball + hand search hoàn thành.
**PRISMA items:** 6, 8, 16a, 16b + PRISMA-S 5, 6, 7.

#### 9.1 Retrieval gating

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 9.1.1 Lấy fulltext PDF: VNU institutional → email tác giả | NCS | ⬜ |
| 9.1.2 Records không có fulltext sau 14 ngày → EC6 | NCS | ⬜ |
| 9.1.3 Lưu PDF trong `04_fulltext/<authoryear>.pdf` | NCS | ⬜ |

#### 9.2 Fulltext screen

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 9.2.1 Đọc PDF → quyết định INCLUDE / EXCLUDE với 1 mã EC Lớp 2 | NCS | ⬜ |
| 9.2.2 Borderline → ghi vào `borderline_decisions_log.md` | NCS | ⬜ |
| 9.2.3 Output `fulltext_decisions.csv` | NCS | ⬜ |

#### 9.3 Snowball — 6 hạt giống (xem Strategy §5.1)

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 9.3.1 Backward — rà references của S1–S6, dedup với pool | Claude script + NCS | ⬜ |
| 9.3.2 Forward — Cited by GS cho S1, S2, S4, S5 | NCS + Claude | ⬜ |
| 9.3.3 Áp IC/EC trên kết quả → bổ sung pool included nếu pass | NCS | ⬜ |

#### 9.4 Hand search — 10 tạp chí (Strategy §5.2)

Rà mục lục 2024–2026 → ghi vào `hand_search_v5.6.csv`.

**Output Bước 9:** `included_studies_v5.6.csv` (kỳ vọng 80–150 studies).

---

### BƯỚC 10 — PRISMA 2020 Flow Diagram

**Pre-conditions:** Bước 7, 8, 9 done.
**Exit criteria:** Flow diagram đầy đủ 4 cấp + PNG export.
**PRISMA items:** 16a.

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 10.1 Soạn diagram theo template Strategy §7 | Claude | ⬜ |
| 10.2 Điền số liệu thực tế từ Bước 7–9 | Claude | ⬜ |
| 10.3 Render PNG bằng [PRISMA2020 Shiny](https://prisma.shinyapps.io/prisma2020/) | NCS | ⬜ |
| 10.4 Lưu `prisma_flow_v5.6.png` + source | NCS | ⬜ |

---

## === PHA 4: TRÍCH XUẤT + ĐÁNH GIÁ CHẤT LƯỢNG ===

---

### BƯỚC 11 — Data Extraction Form

**Pre-conditions:** Bước 10 done; included pool ≈ 80–150 studies.
**Exit criteria:** Mỗi study có đủ 6 nhóm trường; pilot 5 studies + κ ≥ 0.75 intra-rater.
**PRISMA items:** 9, 10a, 10b.

#### 11.1 Form structure (xem `SR_Data_Extraction_Form_v5.6.md` v1.0 — 6 nhóm × 40 trường)

| Nhóm | Tên | Số trường | RQ |
|------|-----|-----------|-----|
| **A** | Bibliographic | 8 | RQ1 |
| **B** | Methodology | 7 | RQ3a |
| **C** | Maturity Level | 5 | RQ2, RQ3 |
| **D** | Operational Area | 5 | RQ2, RQ4a |
| **D'** | Port Size + Vintage + Resource | 11 | RQ2c, RQ3, RQ4d, RQ5 |
| **E** | Geographic + Gap + Future | 4 | RQ4, RQ5 |

#### 11.2 Pilot extraction

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 11.2.1 NCS chọn 5 included studies đa dạng (1 L1 + 1 L2 + 1 L3 + 1 L4 + 1 cảng-ĐNÁ) | NCS | ⬜ |
| 11.2.2 Trích xuất lần 1 → CSV | NCS | ⬜ |
| 11.2.3 Đợi ≥ 14 ngày → trích xuất lần 2 mù | NCS | ⬜ |
| 11.2.4 Tính κ — mục tiêu κ ≥ 0.75 | Claude | ⬜ |
| 11.2.5 Nếu κ < 0.75 → refine form v1.x → Recovery R6 | conditional | ⬜ |

#### 11.3 Full extraction

NCS chấm tuần tự included pool, ưu tiên cảng VN/ĐNÁ + cảng nguồn lực hạn chế. Output: `extraction_v5.6.csv`.

---

### BƯỚC 12 — Maturity + Operational Area classification

**Pre-conditions:** Bước 11 done.
**Exit criteria:** Mỗi study có (L1–L5 primary, secondary) + 5 boolean lĩnh vực + port_size + port_vintage; ma trận đầy đủ.
**PRISMA items:** 10a, 17.

#### 12.1 Maturity rubric (`SR_Classification_Rubric_v5.6.md`)

| Cấp | Bằng chứng yêu cầu |
|------|----------------------|
| **L1 Khả kiến** | IoT/sensor/dashboard/monitoring + real-time data flow |
| **L2 Trạng thái** | Data integration + ontology/process model + computed state |
| **L3 Hỗ trợ QĐ** | Optimization/RL/MILP/heuristic dùng dữ liệu DT |
| **L4 Sim+V&V** | DES/agent-based + validation/calibration; what-if; 3D/4D |
| **L5 Vòng kín** | Closed-loop autonomy: data → decision → verify → feedback |

#### 12.2 Port size classification

| Mức | Throughput TEU/năm | Ví dụ |
|-----|---------------------|--------|
| Megaport | ≥ 10M | Shanghai, Singapore, Ningbo |
| Lớn | 3M–10M | Rotterdam, Hamburg, Tanger Med |
| Vừa | 0.5M–3M | Hai Phong, Cai Mep, Manila |
| Nhỏ | < 0.5M | Da Nang, Quy Nhon, regional |
| Unspecified | Không nêu | Theoretical |

#### 12.3 Port vintage classification

Theo Eligibility Borderline 6 — greenfield / brownfield / mixed / unspecified.

---

### BƯỚC 13 — Quality Appraisal + Borderline Protocol

**Pre-conditions:** Bước 12 done.
**Exit criteria:** Mỗi study có điểm Q1–Q8 (0/0.5/1) + tổng (max 8); borderline log đầy đủ.
**PRISMA items:** 11, 18.

#### 13.1 Bộ 8 tiêu chí Kitchenham & Charters (2007)

| # | Tiêu chí | Hỏi |
|---|----------|------|
| Q1 | Aims clearly stated? | Mục tiêu rõ ràng? |
| Q2 | Context described? | Bối cảnh cảng / DT mô tả đủ? |
| Q3 | Research design appropriate? | Thiết kế phù hợp? |
| Q4 | Sampling/selection clear? | Chọn case rõ ràng? |
| Q5 | Data collection rigorous? | Thu thập dữ liệu chặt chẽ? |
| Q6 | Data analysis appropriate? | Phân tích phù hợp? |
| Q7 | Findings stated clearly? | Phát hiện rõ ràng? |
| Q8 | Value of research established? | Đóng góp rõ? |

Điểm: 0 (no), 0.5 (partial), 1 (yes). Tổng max 8.

#### 13.2 Áp dụng + Borderline log

NCS chấm từng study; output `quality_appraisal_v5.6.csv` + `borderline_decisions_log.md`.

---

## === PHA 5: TỔNG HỢP + PHÂN TÍCH ===

---

### BƯỚC 14 — Intra-rater Reliability

**Pre-conditions:** Bước 8.2.2 + 11.2 + 12 done.
**Exit criteria:** κ ≥ 0.75 cho 3 vòng; báo cáo IRR trong manuscript Methods §3.6.
**PRISMA items:** 8, 23c.

| Vòng | Đối tượng | Số bài | κ mục tiêu |
|-------|-----------|--------|-------------|
| 14.1 Pha A regex vs NCS T/A pilot | 30 | ≥ 0.75 | ⬜ |
| 14.2 NCS lần 1 vs lần 2 (data extraction pilot, gap 14 ngày) | 5 | ≥ 0.75 | ⬜ |
| 14.3 NCS lần 1 vs lần 2 (Maturity classification, 10 random) | 10 | ≥ 0.75 | ⬜ |

> Recovery R6 nếu κ < 0.75 ở bất kỳ vòng nào.

---

### BƯỚC 15 — Sensitivity Analysis

**Pre-conditions:** Bước 14 done.
**Exit criteria:** Recall validation report; SA-1/2/3 chỉ chạy nếu cần.
**PRISMA items:** 13f, 20d, 23c.

#### 15.1 Recall validation 78 hạt giống

| Việc | Mô tả | Trạng thái |
|------|--------|-------------|
| 15.1.1 Lập 78 seed list (lưu trong `graph_net.md`) | Claude | ⬜ |
| 15.1.2 Map từng seed → DOI/title | Claude | ⬜ |
| 15.1.3 So với pool đã chạy → tính recall | Claude | ⬜ |
| 15.1.4 Báo cáo recall + danh sách seeds bị bỏ sót | Claude | ⬜ |

**Ngưỡng:**

| Recall | Hành động |
|---------|------------|
| ≥ 95% | Giữ nguyên thiết kế |
| 80–95% | Chạy SA-1, SA-2, SA-3 (Strategy §6) → bổ sung pool |
| < 80% | Recovery R5 — tái thiết kế truy vấn |

---

### BƯỚC 16 — Bibliometric Analysis (RQ1)

**Pre-conditions:** Bước 11 done.
**Exit criteria:** `SR_Bibliometric_v5.6.md` + 5 hình VOSviewer (PNG).
**PRISMA items:** 17, 20a, 23d.

#### 16.1 Phân tích mô tả

- Xu hướng năm: line chart 2015–2026
- Phân bố quốc gia: choropleth map
- Top 10 tạp chí + IF + Quartile
- Top 10 tác giả + h-index
- Phân bố loại tài liệu

#### 16.2 Phân tích mạng (VOSviewer 1.6.20)

| Bản đồ | Output |
|---------|---------|
| Co-authorship | `vos_coauth.png` |
| Co-occurrence keywords | `vos_keyword.png` |
| Co-citation | `vos_cocit.png` |
| Bibliographic coupling | `vos_coupling.png` |
| Country collaboration | `vos_country.png` |

Threshold: min cluster size = 5; resolution = 1.0.

---

### BƯỚC 17 — Thematic Synthesis + Heat-map 3D + Research Agenda

**Pre-conditions:** Bước 13, 16 done.
**Exit criteria:** Heat-map 3D + RA1–RA6 ranked + Lộ trình điều kiện hoá.
**PRISMA items:** 13c, 13d, 17, 20a, 20b, 23d.

#### 17.1 Thematic synthesis (Braun & Clarke 2006)

6 sub-steps: Familiarisation → Initial coding → Theme search → Theme review → Define themes → Output `thematic_synthesis_v5.6.md`.

#### 17.2 Heat-map 3D — Tầng × Lĩnh vực × Quy mô (RQ2 + RQ4a)

3 lát cắt 2D bằng `seaborn.heatmap`. Gap = #studies ≤ 3 hoặc = 0 → Priority list.

#### 17.3 Geographic + Vintage gap (RQ4c + RQ4d)

- Bảng top 5 leader vs VN/ĐNÁ
- Bảng so sánh greenfield ↔ brownfield (Tầng đạt được, method dùng, thách thức)

#### 17.4 Method × Maturity × Resource (RQ3 + RQ4b)

Ma trận: hàng = method (DES/RL/MILP/IoT/hybrid…); cột = L1–L5; ô = (#studies, mean resource_intensity).
Light DT components (RQ3c): liệt kê components có resource_intensity = Low đã được dùng cho L1–L3.

#### 17.5 Research Agenda RA1–RA6 (RQ5a)

Sáu hướng ưu tiên derived từ RQ4 với *Priority_score = w1 × gap_size + w2 × demand + w3 × feasibility* (xem RQ doc §IV RQ5):

| Mã | Tên gợi ý (sẽ refine sau RQ4) | Nội dung |
|----|---------------------------------|------------|
| RA1 | DT-Edge Lightweight Architecture | Kiến trúc DT edge cho cảng nhỏ |
| RA2 | Multi-source Data Integration Ontology | Ontology cảng container chuẩn hoá |
| RA3 | Hybrid MILP-RL with Resource Constraints | Tối ưu lai cho giới hạn nguồn lực |
| RA4 | Open-source Simulation Framework for Mid-size Ports | DES + AGV + crane mã nguồn mở |
| RA5 | Federated DT for Regional Port Cluster | DT chia sẻ tài nguyên cụm cảng |
| RA6 | Validation Protocol for Low-data Environment | V&V khi dữ liệu ít |

> RA1-RA6 trên là **gợi ý ban đầu** — sẽ refine sau khi có evidence từ RQ4.

#### 17.6 Lộ trình thực tế cho cảng nguồn lực hạn chế (RQ5b)

Bảng điều kiện hoá (Tầng hiện tại × Quy mô × Vintage) → Tầng kế tiếp khả thi:

| Cảng đang ở | Trần khuyến nghị | Bước kế tiếp khả thi | Open-source toolkit | Cost estimate |
|--------------|---------------------|------------------------|------------------------|----------------|
| L1, nhỏ, brownfield | L2 | Tích hợp dữ liệu cơ bản | InfluxDB + Kafka + Grafana | $50k–150k |
| L1, vừa, greenfield | L3 | IoT + Decision Support đơn giản | Node-RED + Streamlit | $100k–250k |
| L2, vừa, brownfield | L3 | Optimization với data có sẵn | Python pandas + scikit-learn | $80k–200k |
| L2, lớn, greenfield | L4 | DES + V&V + 4D | SimPy + AnyLogic Personal | $150k–400k |
| L3, lớn, brownfield | L4 | Sim + calibration với data legacy | JaamSim + custom adapters | $200k–500k |
| L3, megaport | L5 | Closed-loop autonomy | Commercial DT platform | $1M+ |

Output: `SR_Research_Agenda_v5.6.md`.

---

## === PHA 6: VIẾT + NỘP ===

---

### BƯỚC 18 — Manuscript drafting

**Pre-conditions:** Bước 16, 17 done.
**Exit criteria:** Bản thảo IMRaD đầy đủ + figures + tables + đáp ứng word limit của tạp chí target.
**PRISMA items:** 1, 2, 3, 4, 23a–d.

#### 18.1 Cấu trúc bản thảo (target IJPR — 8.000–12.000 words)

| Section | Word target | PRISMA Items |
|---------|-------------|---------------|
| **Abstract** (PRISMA-S structured 250 words) | 250 | 2 |
| **1. Introduction** | 1.000–1.500 | 3, 4 |
| **2. Background — Theoretical Framework (DT 3-property + L1-L5 maturity + Realistic Ceiling)** | 1.000 | 3 |
| **3. Methodology** | 2.000–3.000 | 5–11, 13, 17 |
| **3.1 Protocol and registration** | – | 24a, 24b |
| **3.2 Eligibility criteria** | – | 5 |
| **3.3 Information sources + search strategy** | – | 6, 7 |
| **3.4 Selection process + dedup** | – | 8 |
| **3.5 Quality appraisal (Kitchenham 8 criteria)** | – | 11 |
| **3.6 Intra-rater reliability** | – | 8, 23c |
| **3.7 Synthesis methods (typology + bibliometric + thematic)** | – | 13, 17 |
| **4. Results** | 2.500–3.500 | 16a, 16b, 17, 20a, 20b |
| **4.1 Selection (Flow Diagram)** | – | 16a, 16b |
| **4.2 RQ1 Bibliometric landscape** | – | 17 |
| **4.3 RQ2 Maturity × Operational area × Port size** | – | 17, 20a |
| **4.4 RQ3 Method × Maturity × Resource** | – | 17, 20a |
| **4.5 RQ4 Gap analysis (3D + geographic + vintage)** | – | 20b |
| **5. Discussion** | 1.500–2.000 | 23a–d |
| **5.1 Summary of evidence** | – | 23a |
| **5.2 Limitations of the review** | – | 23b |
| **5.3 Implications for research and practice** | – | 23d |
| **5.4 RQ5 Research Agenda + roadmap for low-resource ports** | – | 23d |
| **6. Conclusion** | 300 | – |
| **References (≥ 100)** | – | – |
| **Supplementary** | – | 24c, 27 |

#### 18.2 Iteration plan

| Vòng | Reviewer | Focus |
|-------|-----------|--------|
| Draft 1 | NCS | Cấu trúc + nội dung + figures |
| Draft 2 | Supervisor | Logic + scientific rigor |
| Draft 3 | Co-author / Expert | Domain-specific + figures clarity |
| Draft 4 | Native English editor | Language polish |
| Submission ready | NCS + Supervisor | Final check + cover letter |

---

### BƯỚC 19 — PRISMA Checklist + Limitations + N/A justification

**Pre-conditions:** Bước 18 Draft 2 done.
**Exit criteria:** PRISMA Checklist 27/27 hoàn thành + 8 N/A justified; Limitations 5 nhóm.
**PRISMA items:** 14, 15, 21, 22, 23b, 23c, 27.

#### 19.1 PRISMA Checklist 27 items

Đối chiếu mỗi item ↔ section bản thảo + page number. 8 N/A items với justification:

| Item | Lý do N/A |
|------|-----------|
| 12 | No effect measures — qualitative typology |
| 13e | No certainty per outcome — không có outcome statistic |
| 14 | No risk of bias domain — replaced by Kitchenham 8 criteria (Item 11) |
| 15 | No statistical synthesis — typology |
| 19 | No certainty (GRADE) — không phù hợp typology |
| 20c | No reporting bias — không có funnel plot |
| 21 | No risk of bias results — replaced by Kitchenham scores (Item 18) |
| 22 | No synthesis statistics — typology |

#### 19.2 Limitations 5 nhóm

1. **Single reviewer** — bù bằng intra-rater κ + Expert Validation
2. **Không có WoS/ACM** — bù bằng recall validation 78 seeds
3. **2 cơ sở dữ liệu bổ trợ giới hạn thời gian** (SP 12 tháng, TF 6 tháng)
4. **Không có meta-analysis** — bản chất typology định tính
5. **Single language (English)** — bài tiếng Trung/TBN/Đức không xét

---

### BƯỚC 20 — Supplementary Package + OSF Amendments

**Pre-conditions:** Bước 19 done.
**Exit criteria:** Supplementary đầy đủ trên OSF Files; OSF Amendments tổng hợp (nếu có).
**PRISMA items:** 24c, 27 + PRISMA-S 8.

#### 20.1 Supplementary Package (uploaded OSF)

| File | Mô tả |
|------|--------|
| `osf_release/SR_Search_Strategy.md` | Strategy đã strip nhãn nội bộ |
| `osf_release/SR_Eligibility_Criteria.md` | EC/IC đã strip |
| `osf_release/SR_Research_Questions.md` | RQ doc đã strip |
| `osf_release/SR_PRISMA_Checklist.md` | 27/27 items |
| `osf_release/SR_Quality_Appraisal.md` | 8 tiêu chí Kitchenham |
| `osf_release/SR_Data_Extraction_Form.md` | Form v1.x với 6 nhóm |
| `prisma_flow_v5.6.png` + source | Flow diagram |
| `dedup.py` + `dedup_unique.ris` | Reproducibility code + data |
| `screening.py` + `tf_journal_exclusion.py` | Pha A pre-screen |
| `included_studies_v5.6.csv` | Final pool |
| `extraction_v5.6.csv` | Trích xuất |
| `quality_appraisal_v5.6.csv` | Q1–Q8 scores |
| `vos_*.png` | 5 bản đồ VOSviewer |
| `borderline_decisions_log.md` | Audit trail borderline |

#### 20.2 OSF Amendments (nếu có sai lệch ghi trong DEV log)

Tổng hợp từ `SR_Deviation_Log_v5.6.md` → submit từng Amendment trên OSF Project.

---

### BƯỚC 21 — Expert Validation (Delphi-lite)

**Pre-conditions:** Bước 17 done; Heat-map + RA1–RA6 sẵn.
**Exit criteria:** 3–5 chuyên gia confirm Maturity classification + RA priority; consensus ≥ 70%.
**PRISMA items:** Bổ trợ 23.

#### 21.1 Panel chuyên gia

| # | Vai trò | Số người |
|---|---------|----------|
| 1 | Chuyên gia DT (academic) | 1–2 |
| 2 | Chuyên gia vận hành cảng (industry: SNP, VICT, VIP) | 1–2 |
| 3 | Chuyên gia phương pháp SR (Supervisor / Library) | 1 |

#### 21.2 Quy trình Delphi-lite (2 vòng)

| Vòng | Việc |
|-------|------|
| 1 | Gửi heat-map + RA list + 5 maturity samples → mỗi chuyên gia đánh giá độc lập (Likert 1–5 + comment) |
| 2 | Tổng hợp anonymous → gửi lại + cho chuyên gia điều chỉnh → consensus |

Output: `expert_validation_v5.6.md` + 3–5 expert confirmation letters.

---

### BƯỚC 22 — Final review + Cover letter + Submit

**Pre-conditions:** Bước 18–21 done.
**Exit criteria:** Manuscript submitted to target Q1 journal + acknowledgement received.
**PRISMA items:** 1, 2, 25, 26.

#### 22.1 Cover letter (3 đoạn)

1. Topic + significance
2. Novelty (heat-map 3D × Vintage analysis × Roadmap conditional cho cảng nguồn lực hạn chế là contribution chính)
3. Suggested reviewers (3–5)

#### 22.2 Submission checklist

| Mục | Yêu cầu |
|-------|---------|
| Manuscript | Word/LaTeX theo target journal template |
| Figures | TIFF/PNG ≥ 300 DPI |
| Tables | Trong manuscript hoặc separate |
| Supplementary | ZIP đính kèm hoặc DOI link OSF |
| Cover letter | PDF |
| ORCID iDs | NCS + Supervisor |
| Funding statement | (nếu có) |
| Competing interests | None declared |
| Author contributions | NCS chính, Supervisor advisory |
| Data availability | "Data available on OSF: <DOI sau Bước 1.5>" |

#### 22.3 Target journal escalation

Nếu reject ở target 1 (IJPR / MPM):
- Revise → resubmit target 2 (Computers in Industry)
- Reject lần 2 → target 3 (JMSE / Annual Reviews in Control)

---

# §III. ÁNH XẠ PRISMA 2020 27 ITEMS ↔ BƯỚC

| Item | Section | Bước thực hiện |
|------|---------|------------------|
| 1 | Title | 18, 22 |
| 2 | Abstract | 18, 22 |
| 3 | Rationale | 18 (Section 1) |
| 4 | Objectives | 18 (Section 1) |
| 5 | Eligibility criteria | 2 |
| 6 | Information sources | 4, 5, 6, 9 (snowball + hand) |
| 7 | Search strategy | 4, 5, 6 (Strategy §4) |
| 8 | Selection process | 7, 8, 9 |
| 9 | Data collection process | 11 |
| 10a | Data items — outcomes | 11, 12 |
| 10b | Data items — other | 11 |
| 11 | Risk of bias / Quality appraisal | 13 |
| 12 | Effect measures | **N/A** (typology) |
| 13a | Synthesis — eligible criteria | 17 |
| 13b | Synthesis — preparing data | 11, 12 |
| 13c | Synthesis — methods | 16, 17 |
| 13d | Synthesis — software | 16 (VOSviewer), 17 (Python) |
| 13e | Synthesis — heterogeneity | **N/A** |
| 13f | Sensitivity | 15 |
| 14 | Risk of bias domains | **N/A** (use Item 11 Kitchenham) |
| 15 | Synthesis statistics | **N/A** |
| 16a | Selection — Records identified/screened | 7, 8, 9, 10 |
| 16b | Selection — Reasons for exclusion | 8, 9 (28 EC mã) |
| 17 | Synthesis results | 16, 17 |
| 18 | Risk of bias results | 13 |
| 19 | Certainty of evidence | **N/A** (no GRADE) |
| 20a | Synthesis — main results | 16, 17 |
| 20b | Synthesis — heterogeneity (gap) | 17 |
| 20c | Reporting bias | **N/A** |
| 20d | Sensitivity results | 15 |
| 21 | Risk of bias detailed | **N/A** (Item 18) |
| 22 | Certainty of evidence per outcome | **N/A** |
| 23a | Discussion — summary | 18 |
| 23b | Discussion — limitations | 19 |
| 23c | Discussion — confidence | 19 |
| 23d | Discussion — implications | 17 (RA), 18 |
| 24a | Registration | 1 |
| 24b | Protocol accessibility | 1, 20 |
| 24c | Amendments | 20 |
| 25 | Funding | 22 |
| 26 | Competing interests | 22 |
| 27 | Availability of materials | 20 |

---

# §IV. ÁNH XẠ PRISMA-S 16 ITEMS ↔ BƯỚC

| Item | Tên | Bước |
|-------|------|------|
| 1 | Database name | 4–6 (Strategy §1.6) |
| 2 | Multi-database searching | 4–6 |
| 3 | Study registries | N/A |
| 4 | Online resources / browsing | 5 (Google Scholar) |
| 5 | Citation searching | 9 (Snowball) |
| 6 | Contacts | 9 (email tác giả) |
| 7 | Other methods | 9 (Hand search) |
| 8 | Full search strategies | Strategy §4 đầy đủ |
| 9 | Limits and restrictions | Strategy §3 |
| 10 | Search filters | Strategy §3 |
| 11 | Prior work | Strategy §1.1 |
| 12 | Updates | 22 (re-run + dedup nếu submission > 6 tháng) |
| 13 | Dates of searches | 4–6 |
| 14 | Peer review | 2.6 (PRESS) + 21 (Expert) |
| 15 | Total records | 7 |
| 16 | Deduplication | 7 (3-layer Python + Rayyan cross-check) |

---

# §V. RECOVERY PROCEDURES R1–R7

> Mỗi Recovery có 4 phần: Trigger, Diagnostics, Action plan, Documentation.

## R1 — Out-of-order Rayyan upload

- **Trigger:** Pool đã upload Rayyan trước Bước 7 dedup
- **Diagnostics:** so #records Rayyan vs #records sau Python dedup; nếu khác > 5% → Phương án X
- **Action plan (Phương án X):** chạy Python dedup độc lập → re-upload pool Python vào Rayyan project sạch → audit trail = `dedup_strict_report.txt`
- **Documentation:** DEV-NNN trong `SR_Deviation_Log_v5.6.md` + OSF Amendment

## R2 — Rayyan Essentials thiếu features

- **Trigger:** verify Bước 1.11 phát hiện thiếu PDF / AI / blinded mode / custom reasons
- **Action plan:**
  - PDF không attach → lưu local + Excel `fulltext_decisions.csv`
  - AI ranking không có → chấm tuần tự theo PRE_LABEL Pha A
  - Blinded mode không có → ghi rõ Limitations §19.2
  - Custom reasons không có → fallback Excel `ta_decisions.csv`
- **Documentation:** ghi đầy đủ trong Limitations + Methods §3.6

## R3 — Database access loss (institutional VNU)

- **Trigger:** Scopus/IEEE access token hết hạn hoặc institutional license issue
- **Action plan:**
  - Liên hệ thư viện VNU
  - Backup: free Scopus Preview + IEEE Open Access search
  - Email tác giả request preprint
- **Documentation:** DEV log

## R4 — OSF service outage hoặc Registration cần sửa

- **Trigger:** OSF service down > 24h hoặc Registration metadata sai
- **Action plan:**
  - Outage → đợi resolution; cấp bách → archive vào Zenodo + reference OSF khi resume
  - Metadata sai → thêm Amendment với correction (KHÔNG xoá Registration cũ — DOI immutable)
- **Documentation:** OSF Amendment

## R5 — Recall < 95% trên 78 seeds (Bước 15.1)

- **Trigger:** recall < 95%
- **Action plan:**
  - 80–95% → chạy SA-1, SA-2, SA-3 (Strategy §6); rerun dedup
  - < 80% → tái thiết kế truy vấn — phân tích missed seeds → điều chỉnh keywords; rerun search
- **Documentation:** DEV log + OSF Amendment

## R6 — Cohen's κ < 0.75 ở Bước 14

- **Trigger:** κ < 0.75 ở bất kỳ vòng nào
- **Action plan:**
  - Phân tích disagreement matrix → xác định mã/trường gây ambiguity
  - Refine định nghĩa EC/IC / form / rubric → bump version
  - Re-run vòng đó
  - Lần 2 thất bại → escalate Supervisor (Bước 21 panel)
- **Documentation:** DEV log + version bump

## R7 — Dedup ratio bất thường hoặc Python vs Rayyan disagreement > 5%

- **Trigger:** dedup ratio < 10% hoặc > 50%, hoặc Δ Python-Rayyan > 5%
- **Action plan:**
  - Ratio < 10% → kiểm tra encoding / DOI normalization bug
  - Ratio > 50% → kiểm tra fuzzy threshold (90 quá thấp?)
  - Δ > 5% → so sánh detail; điều chỉnh Layer 2 threshold; thêm `--strict` mode
  - Phương án X: trust Python pool, re-upload vào Rayyan
- **Documentation:** `dedup_reconcile_report.txt` + DEV log

---

# §VI. RỦI RO, EXIT CRITERIA, DEFINITION OF DONE

## VI.1 Risk Register (chi tiết trong `SR_Risk_Register_v5.6.md`)

| Mã | Tên | Likelihood | Impact | Recovery |
|----|-----|--------------|---------|-----------|
| R-01 | Out-of-order Rayyan upload | High | Medium | R1 |
| R-02 | Rayyan Essentials thiếu features | Medium | Medium | R2 |
| R-03 | Database access loss | Low | High | R3 |
| R-04 | OSF outage | Low | Medium | R4 |
| R-05 | Recall < 95% | Medium | High | R5 |
| R-06 | κ < 0.75 (intra-rater) | Medium | High | R6 |
| R-07 | Dedup anomaly | Low | High | R7 |
| R-08 | Time slippage > 30 ngày | Medium | Medium | Re-plan + escalate Supervisor |
| R-09 | Supervisor unavailable | Low | High | Co-supervisor + Expert panel |
| R-10 | Target journal change scope | Medium | Low | Adapt cover letter |
| R-11 | Reviewers reject (round 1) | High | Low | Standard revise + resubmit |
| R-12 | Co-author disagree key decision | Low | Medium | Discussion + Supervisor adjudicate |
| R-13 | Plagiarism flag (Turnitin) | Very Low | Critical | Pre-submit Turnitin check ở Bước 22 |
| R-14 | OSF Amendment missing | Low | Medium | Audit before submit |
| R-15 | Software version drift (Python/RapidFuzz) | Low | Low | requirements.txt + Docker image |

## VI.2 Definition of Done

Một bước được tính ✅ khi:
1. Tất cả Exit criteria pass
2. Output file(s) tồn tại + verified
3. graph_net.md đã có node mới
4. SR_Deviation_Log_v5.6.md cập nhật nếu có sai lệch
5. NCS đánh dấu trạng thái trong file này

---

# §VII. REPRODUCIBILITY CHECKLIST (Q1 Open Science)

| Mục | Trạng thái | Đường dẫn |
|-------|-------------|-------------|
| Pre-registration OSF | ⬜ | DOI _[điền sau Bước 1.5]_ |
| Search strategy reproducible | ⬜ | `SR_Search_Strategy_v5.6_FINAL.md` §4 (12 + 10 query nguyên văn) |
| Dedup pipeline open | ⬜ | `dedup.py` + `requirements.txt` |
| T/A pre-screen open | ⬜ | `screening.py` + `tf_journal_exclusion.py` |
| Eligibility operationalized | ⬜ | `SR_Eligibility_Criteria_v5.6.md` (28 EC/IC + 6 borderline) |
| Quality appraisal protocol | ✅ 2026-05-14 | `SR_Quality_Appraisal_v5.6.md` |
| Data extraction form | ✅ 2026-05-08 | `SR_Data_Extraction_Form_v5.6.md` v1.0 |
| Maturity rubric | ✅ 2026-05-14 | `SR_Classification_Rubric_v5.6.md` |
| Borderline log | ⬜ | `borderline_decisions_log.md` (tạo sau Bước 9) |
| Final pool data | ⬜ | `included_studies_v5.6.csv` |
| Extraction data | ⬜ | `extraction_v5.6.csv` |
| Bibliometric maps | ⬜ | `vos_*.png` + VOSviewer config |
| Synthesis output | ⬜ | `SR_Bibliometric_v5.6.md` + `SR_Research_Agenda_v5.6.md` |
| PRISMA Checklist 27/27 | ✅ 2026-05-14 (skeleton — section/page TBD sau Bước 18) | `SR_PRISMA_Checklist_v5.6.md` |
| OSF Amendments | ⬜ | (cập nhật khi có) |
| Manuscript + Cover letter | ⬜ | (Bước 22) |

---

# §VIII. VERSIONING

| Version | Ngày | Thay đổi | Phê duyệt |
|---------|------|-----------|-------------|
| **v1.0** | 2026-05-08 | Kế hoạch thiết kế đầu tiên — 22 bước trong 6 Pha; PRISMA 2020 + PRISMA-S + Kitchenham 2007 + PRESS; ánh xạ rõ Q1 journal target IJPR/MPM; 7 Recovery procedures R1–R7; 15 risks; Reproducibility Checklist Open Science | NCS HoaTX (chờ phê duyệt) |

---

# §IX. LIÊN KẾT NỘI BỘ

| File | Vai trò |
|------|---------|
| `SR_Research_Questions_v5.6.md` v1.0 | Single Source of Truth cho RQ — WorkPlan reference §0.7 |
| `SR_Search_Strategy_v5.6_FINAL.md` v1.0 | Bước 4–7, 15 — chiến lược tìm kiếm + PRESS |
| `SR_Eligibility_Criteria_v5.6.md` | Bước 2, 8, 9 — 28 EC/IC + 6 borderline rules |
| `SR_Screening_Protocol_v5.6.md` | Bước 8 — Pha A Python + Pha B Rayyan |
| `SR_Data_Extraction_Form_v5.6.md` v1.0 | Bước 11 — 6 nhóm × 40 trường |
| `SR_Quality_Appraisal_v5.6.md` | Bước 13 — Kitchenham 8 criteria |
| `SR_Classification_Rubric_v5.6.md` | Bước 12 — Maturity rubric L1-L5 |
| `SR_PRISMA_Checklist_v5.6.md` | Bước 19 — 27/27 + 8 N/A |
| `SR_OSF_Registration_v5.6.md` | Bước 1, 20 — OSF tracker + Amendments |
| `SR_Deviation_Log_v5.6.md` | Bước 0.9, 20 — DEV log |
| `SR_Risk_Register_v5.6.md` | Bước 0.9 — 15 rủi ro |
| `osf_release/` | Bước 20 — bản công khai đã strip nhãn nội bộ |
| `graph_net.md` | Đồ thị tri thức trung tâm |

---

*WorkPlan_v5.6_FINAL.md — v1.0 — 2026-05-08 — anchored on RQ_v1.0 (`SR_Research_Questions_v5.6.md`) + PRISMA 2020 + PRISMA-S + Kitchenham 2007 + PRESS + Q1 target IJPR/MPM*
