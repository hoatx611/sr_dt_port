# PRISMA 2020 CHECKLIST — 27 ITEMS
# Digital Twin cho Vận hành Cảng Container

**File:** SR_PRISMA_Checklist.md
**Phiên bản:** v1.1 — 2026-05-15
**NCS:** HoaTX
**OSF Project:** https://osf.io/dxjw9/ (DOI: 10.17605/OSF.IO/DXJW9)
**Tham chiếu:** Page MJ et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ* 372:n71. doi: 10.1136/bmj.n71
**Dùng tại:** Bước 19 (sau Draft 2 bản thảo) — điền vào section + page number của bản thảo cuối

> Cột **Trạng thái** dùng: ✅ Hoàn thành | 🔄 Một phần | ⬜ Chưa (chờ bước sau) | **N/A** + justification
> Cột **Section/Page** điền khi bản thảo hoàn tất (Bước 18–19).

---

# §1. TITLE

| Item | Mô tả PRISMA 2020 | Yêu cầu | Section/Page | Trạng thái |
|------|-------------------|---------|--------------|------------|
| **1** | **Title** — Xác định báo cáo là systematic review | Có từ "systematic review" trong tiêu đề | Title | ⬜ Bước 18 |

---

# §2. ABSTRACT

| Item | Mô tả PRISMA 2020 | Yêu cầu | Section/Page | Trạng thái |
|------|-------------------|---------|--------------|------------|
| **2** | **Abstract** — Structured abstract có: Background, Objectives, Methods (eligibility, sources, assessment, synthesis), Results (included studies, synthesis), Discussion, Registration | Structured abstract với các heading rõ | Abstract | ⬜ Bước 18 |

---

# §3. INTRODUCTION

| Item | Mô tả PRISMA 2020 | Yêu cầu | Section/Page | Trạng thái |
|------|-------------------|---------|--------------|------------|
| **3** | **Rationale** — Mô tả lý do tổng quan hệ thống này cần thiết, liên quan đến bằng chứng hiện có | Trình bày gap (5 chiều RQ4) + tầm quan trọng DT cảng | §1 Background | ⬜ Bước 18 |
| **4** | **Objectives** — Cung cấp câu hỏi nghiên cứu rõ ràng với PICO/PICOC | 5 RQ chính thức + PICOC framework | §1 Background / §2 Methods | ⬜ Bước 18 |

---

# §4. METHODS

| Item | Mô tả PRISMA 2020 | Yêu cầu | Section/Page | Trạng thái |
|------|-------------------|---------|--------------|------------|
| **5** | **Eligibility criteria** — Xác định tiêu chí IC/EC đầy đủ với lý do | 28 mã IC/EC (IC1–IC5, EC1–EC-STRUCT), PICOC, 6 borderline rules | §3.1 Methods | ✅ `SR_Eligibility_Criteria.md` v1.0 — 2026-05-08 |
| **6** | **Information sources** — Liệt kê tất cả nguồn tìm kiếm, ngày chạy | Scopus, IEEE, GS, Springer, T&F + ngày 2026-05-10; Q10 2026-05-15 | §3.2 Methods | ✅ 5 databases, 23 files, dates in Strategy §9 |
| **7** | **Search strategy** — Trình bày ít nhất 1 full search string (đủ để tái lập) | Full query Q1–Q12 nguyên văn + PRESS 8/8 PASS + dedup.py + screening.py | §3.2 Methods + Supplementary | ✅ `SR_Search_Strategy_FINAL.md` + `SR_PRESS_Review.md` |
| **8** | **Selection process** — Mô tả ai/bao nhiêu người sàng lọc, cách giải quyết bất đồng | Single reviewer (NCS) + Pha A regex (✅ 284/5.061/477) + Pha B Rayyan (⬜) + intra-rater κ | §3.3 Methods | 🔄 Pha A ✅; Pha B ⬜ chờ Rayyan |
| **9** | **Data collection process** — Mô tả phương pháp và công cụ trích xuất dữ liệu | SR_Data_Extraction_Form 6 nhóm + Rayyan + Excel; pilot extraction 5 studies | §3.4 Methods | ⬜ Bước 18 |
| **10a** | **Data items** — Liệt kê tất cả biến dữ liệu cần thu thập | 6 nhóm (A–F): Bibliometrics, DT characterization, Maturity, Ops area, Port context, Quality | §3.4 Methods + Supplementary | ⬜ Bước 18 |
| **10b** | **Outcomes & prioritization** — Xác định outcomes chính, cách measure và aggregate | RQ1–RQ5 outcomes (bibliometric distribution, L1–L5 heat-map, gap matrix) | §3.4 Methods | ⬜ Bước 18 |
| **11** | **Study risk of bias assessment** — Mô tả phương pháp đánh giá chất lượng | Kitchenham & Charters (2007) 8 tiêu chí; 0/0.5/1; single reviewer; intra-rater κ | §3.5 Methods | ✅ SR_Quality_Appraisal.md |
| **12** | **Effect measure** — Xác định effect size measures | **N/A** — xem §6 justification | N/A | **N/A** |
| **13a** | **Synthesis methods** — Phương pháp tổng hợp (combining results) | Typology synthesis + bibliometric analysis + thematic coding; không có meta-analysis | §3.6 Methods | ⬜ Bước 18 |
| **13b** | **Exploring heterogeneity** — Phương pháp explore heterogeneity | Heterogeneity được mô tả định tính (domain × maturity × method variation) — không có I² | §3.6 Methods | ⬜ Bước 18 |
| **13c** | **Risk of bias due to missing results** — Đánh giá publication bias | Recall validation 78 seeds (Bước 15) — thay cho funnel plot | §3.6 Methods | ⬜ Bước 15 |
| **13d** | **Sensitivity analyses** — Phương pháp sensitivity analysis | SA-1/2/3 (Strategy §6) chạy nếu recall < 95%; mô tả planned scenarios | §3.6 Methods | ⬜ Bước 15 |
| **13e** | **Certainty per outcome** — Assessment of certainty of body of evidence (GRADE) | **N/A** — xem §6 justification | N/A | **N/A** |

---

# §5. RESULTS

| Item | Mô tả PRISMA 2020 | Yêu cầu | Section/Page | Trạng thái |
|------|-------------------|---------|--------------|------------|
| **14** | **Study selection** — PRISMA flow diagram + số loại trừ theo lý do mỗi tầng | PRISMA 2020 flow diagram với số liệu thực (sau Bước 9) + Table EC reasons | §4.1 Results + Figure 1 | 🔄 Dữ liệu Identification+Dedup+PhaA ✅ (`SR_PRISMA_FlowDiagram.md` v1.1); Pha B + Bước 9 ⬜ |
| **15** | **Study characteristics** — Table tóm tắt đặc điểm mỗi study | Table 1: study_id, author/year, source, primary_maturity, ops area, port size, country | §4.2 Results + Table 1 | ⬜ Bước 11 + 18 |
| **16a** | **Risk of bias in studies — assessment** — Trình bày đánh giá chất lượng từng study | Kitchenham scores (Q1–Q8) cho mỗi study trong Supplementary + summary Figure | §4.3 Results + Supplementary | ⬜ Bước 13 (chờ Pha B + extraction) |
| **16b** | **Risk of bias in studies — presentation** | Distribution of quality levels (High/Medium/Low) | §4.3 Results | ⬜ Bước 13 |
| **17** | **Results of individual studies** — Trình bày kết quả từng study | Extraction data table (condensed) per study — L1–L5, ops, method, key finding | §4.4 Results + Table 2 | ⬜ Bước 11 + 18 |
| **18** | **Results of syntheses** — Kết quả tổng hợp chính | Heat-map L×Ops, bibliometric figures (VOSviewer), thematic narrative | §4.5 Results + Figures 2–6 | ⬜ Bước 16–17 + 18 |
| **19** | **Reporting biases** — Kết quả đánh giá reporting bias | Recall validation kết quả (Bước 15) — seed recall %, SA-1/2/3 nếu cần | §4.6 Results | ⬜ Bước 15 + 18 |
| **20** | **Certainty of evidence (GRADE)** | **N/A** — xem §6 justification | N/A | **N/A** |

---

# §6. DISCUSSION

| Item | Mô tả PRISMA 2020 | Yêu cầu | Section/Page | Trạng thái |
|------|-------------------|---------|--------------|------------|
| **20a** | **Interpretation** — Thảo luận kết quả chính trong bối cảnh prior work | Trả lời 5 RQ; so với các SR DT hiện có; Realistic Ceiling | §5 Discussion | ⬜ Bước 18 |
| **20b** | **Limitations** — Thảo luận hạn chế (search, selection, risk of bias) | 5 nhóm limitations: single reviewer, WoS/ACM thiếu, time limits, no meta-analysis, English-only | §5 Discussion | ⬜ Bước 18 |
| **20c** | **Implications** | Implications cho research (RA1–RA6) + implications cho practice (port operators) | §5 Discussion | ⬜ Bước 18 |
| **21** | **Risk of bias across studies (synthesis-level)** | **N/A** — xem §6 justification | N/A | **N/A** |
| **22** | **Quantitative synthesis summary** | **N/A** — xem §6 justification | N/A | **N/A** |

---

# §7. OTHER INFORMATION

| Item | Mô tả PRISMA 2020 | Yêu cầu | Section/Page | Trạng thái |
|------|-------------------|---------|--------------|------------|
| **23a** | **Registration** — Trình bày OSF Registration DOI | OSF Registration DOI: 10.17605/OSF.IO/DXJW9 | Methods §3 hoặc Title page | ✅ DOI confirmed |
| **23b** | **Protocol** — Trình bày OSF Protocol DOI | Như 23a (pre-registration + protocol là cùng 1 OSF project) | Methods §3 | ✅ |
| **23c** | **Amendments** — Ghi nhận sai lệch so với protocol | DEV-001/002/003/004 (all Resolved) + intra-rater κ results (⬜ Bước 14) | Methods §3 hoặc Supplementary | 🔄 DEV log ✅ all Resolved; κ ⬜ chờ Bước 14 |
| **23d** | **Author experience** — Relevant experience/expertise | NCS PhD candidate + supervisor + Expert Validation Panel | Acknowledgments hoặc Methods | ⬜ Bước 18 |
| **24a** | **Funding sources** | [NCS điền: học bổng / tự túc / đề tài] | Funding statement | ⬜ NCS task |
| **24b** | **Role of funder** | Funder không có vai trò trong SR design/analysis | Funding statement | ⬜ NCS task |
| **24c** | **Conflicts of interest** | Không có conflict of interest | CoI declaration | ⬜ NCS task |
| **25** | **Availability of data/code** | OSF Files: dedup.py, screening.py, dedup_unique.ris, extraction CSV | Data availability | ✅ OSF planned |
| **26** | **Other information** | Expert validation (Bước 21) — Delphi-lite panel 3–5 experts | Acknowledgments | ⬜ Bước 21 |
| **27** | **PRISMA checklist** — Đính kèm PRISMA Checklist như Supplementary | File này là checklist — upload lên OSF + nộp kèm manuscript | Supplementary | 🔄 File này (in progress) |

---

# §8. JUSTIFICATION CHO 8 ITEMS N/A

> Theo PRISMA 2020 guidelines — Items không áp dụng phải có justification tường minh.

| Item | Mô tả | Lý do N/A |
|------|-------|-----------|
| **12** | Effect measure | SR này là **qualitative typology**, không có intervention-outcome structure. Không có effect estimates (OR, RR, SMD, MD) nào được tính. Phù hợp với PRISMA 2020 §4 (non-comparative reviews). |
| **13e** | Certainty per outcome | Không có quantitative outcomes để đánh giá certainty. SR tổng hợp theo typology (maturity level × operational area) — không có effect estimates. |
| **14** | Risk of bias per study (statistical) | Thay bằng Kitchenham 8 criteria (Item 11) phù hợp hơn cho SE/Engineering SR (Kitchenham & Charters 2007). Risk of bias trong context này = quality of evidence (Q1–Q8), không phải RoB trong RCT sense. |
| **15** | Statistical synthesis | Không có meta-analysis. Tổng hợp là **typology synthesis** (narrative + heat-map). Không có pooled effect sizes. |
| **20** | Certainty of evidence (GRADE) | GRADE dành cho reviews với health outcomes (RCT-based). SR định tính về DT operations engineering không có GRADE-applicable outcomes. Thay bằng quality distribution (High/Medium/Low). |
| **20c (reporting bias)** | Funnel plot / Egger's test | Không có quantitative synthesis → không có funnel plot. Reporting bias addressed qualitatively qua recall validation (Bước 15, Item 13c). |
| **21** | Risk of bias synthesis-level | Synthesis-level RoB assessment (small study effects, PEESE) không áp dụng — không có effect estimates. |
| **22** | Quantitative synthesis statistics | Không có I², τ², Cochran's Q. SR là qualitative typology. Heterogeneity được mô tả định tính (§4.5 narrative). |

---

# §9. TRẠNG THÁI TỔNG QUAN

| Nhóm | Items | Hoàn thành | Một phần | Chưa | N/A |
|------|-------|------------|----------|------|-----|
| Title/Abstract | 1–2 | 0 | 0 | 2 | 0 |
| Introduction | 3–4 | 0 | 0 | 2 | 0 |
| Methods | 5–13e | 4 (5,6,7,11) | 1 (8) | 4 | 2 (12,13e) |
| Results | 14–22 | 0 | 1 (14) | 5 | 3 (20,21,22) |
| Other | 23–27 | 3 (23a,23b,25) | 3 (23c,27,Item8) | 3 | 0 |
| **Tổng** | **27 items** | **7** | **5** | **7** | **8** |

*Cập nhật v1.1 2026-05-15: Items 5,6,7 → ✅; Item 8 → 🔄; Item 14 → 🔄; Item 23c → 🔄 (DEV-004 Resolved).*

> Tỷ lệ N/A: 8/27 (29,6%) — nằm trong giới hạn chấp nhận cho qualitative typology SR (thường 20–35%).

---

# §10. DANH SÁCH ITEMS THEO BƯỚC WORKPLAN

| WorkPlan Bước | PRISMA Items được giải quyết |
|---------------|------------------------------|
| Bước 1 (Pre-reg) | 23a, 23b |
| Bước 2 (Eligibility) | 5 |
| Bước 3 (Pilot) | 6, 7 |
| Bước 4–6 (Search) | 6, 7 |
| Bước 7 (Dedup) | 8, 16a |
| Bước 8 (T/A Screen) | 8, 16a, 16b |
| Bước 9 (Fulltext) | 8, 14, 16a, 16b |
| Bước 10 (Flow Diagram) | 14 |
| Bước 11 (Extraction) | 9, 10a, 10b, 17 |
| Bước 12 (Classification) | 10a, 17 |
| Bước 13 (Quality) | 11, 16a, 16b |
| Bước 14 (Intra-rater) | 8, 23c |
| Bước 15 (Sensitivity) | 13c, 13d, 19 |
| Bước 16 (Bibliometric) | 17, 18, 20a, 23c |
| Bước 17 (Synthesis) | 13a, 13b, 18, 20a, 20b |
| Bước 18 (Manuscript) | 1, 2, 3, 4, 15, 20a, 20b, 20c |
| Bước 19 (Checklist) | 14, 21, 22, 23b, 23c, 27 |
| Bước 20 (Supplementary) | 25, 27 |
| Bước 21 (Expert Val) | 23d, 26 |
| Bước 22 (Submit) | 24a, 24b, 24c |

---

# §11. VERSIONING

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-05-14 | Tạo ban đầu — 27 items skeleton; 8 N/A justified |
| **v1.1** | **2026-05-15** | **Items 5,6,7 → ✅; Item 8 → 🔄; Item 14 → 🔄; 23c DEV-004 Resolved; PRESS Review ✅** |

**Quy tắc cập nhật:** Sau Bước 18 Draft 2 → điền section/page numbers → cập nhật trạng thái → version 1.1. Sau submit → version 1.2 với response journal checklist.

---

# §12. LIÊN KẾT

| File | Quan hệ |
|------|---------|
| `SR_PRISMA_FlowDiagram.md` | Item 14 (flow diagram data) |
| `SR_Quality_Appraisal.md` | Item 11 (quality assessment) |
| `SR_Eligibility_Criteria.md` | Item 5 (eligibility criteria) |
| `SR_Search_Strategy_FINAL.md` | Items 6, 7 (search strategy) |
| `SR_Deviation_Log.md` | Item 23c (amendments) |
| `WorkPlan_FINAL.md` | §0.8 (mapping của mọi bước tới PRISMA items) |
| `osf_release/` | Public version (strip "v5.6" labels) |

---

*SR_PRISMA_Checklist.md — v1.0 — 2026-05-14 — NCS HoaTX*
