# CÂU HỎI NGHIÊN CỨU — TỔNG QUAN HỆ THỐNG
# Digital Twin cho Vận hành Cảng Container

**Phiên bản:** v1.0 — 2026-05-08
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**OSF DOI:** [10.17605/OSF.IO/DXJW9](https://doi.org/10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 Item 4 (Objectives) + PRISMA-S Item 11 (Prior work) + Kitchenham & Charters (2007) SE SR Guidelines
**Vai trò:** Tài liệu **Single Source of Truth (SoT)** cho toàn bộ bộ Câu hỏi nghiên cứu (RQ). Mọi file khác (`WorkPlan`, `SR_Search_Strategy`, `SR_Eligibility_Criteria`, `SR_Data_Extraction_Form`, `osf_release/`, manuscript) PHẢI tham chiếu vào file này — không lặp định nghĩa RQ.

---

# §I. NGUYÊN TẮC THIẾT KẾ RQ

## 1.1 Nguyên tắc dependency tường minh

Bộ RQ tuân thủ trình tự logic **WHAT → HOW MATURE → HOW METHOD → WHERE GAPS → WHAT NEXT** (Kitchenham & Charters 2007):

```text
RQ1 (WHAT) ─► RQ2 (HOW MATURE) ─► RQ3 (HOW METHOD)
                                          │
                                          ▼
                                  RQ4 (WHERE GAPS) ─► RQ5 (WHAT NEXT)
```

- **RQ1, RQ2, RQ3** mô tả hiện trạng (descriptive).
- **RQ4** phát hiện gap (analytical) — KHÔNG được áp đặt direction trước.
- **RQ5** đề xuất ưu tiên *được dẫn xuất từ RQ4* (prescriptive) + lộ trình *được điều kiện hoá theo bối cảnh* (conditional roadmap).

## 1.2 Ba quy tắc tránh lỗi logic

**Quy tắc 1 — KHÔNG pre-empt direction.** RQ5a không được giả định trước rằng tầng nào đầy / tầng nào thiếu. Direction phải là *output* của RQ4, không phải *input* của RQ5.

**Quy tắc 2 — Tôn trọng dependency RQ4 → RQ5.** Output(RQ4) = Input(RQ5). Mọi RA (Research Agenda) phải có evidence từ RQ4.

**Quy tắc 3 — Tránh giả định đồng nhất "mọi cảng cần lên L5".** Mỗi cảng có **trần thực tế (Realistic Ceiling)** L\* tối ưu cost-benefit, phụ thuộc quy mô + vintage + nguồn lực. Cảng nhỏ có thể chỉ cần L3 là đủ.

---

# §II. KHUNG LÝ THUYẾT 2 LỚP

## 2.1 Lớp 1 — Định nghĩa Digital Twin (3 thuộc tính tối thiểu)

Theo Grieves (2014) + Tao et al. (2019) "mirror model":

1. **Thực thể vật lý (Physical Entity):** cơ sở vật chất tại cảng — cẩu (quay crane, gantry crane, RTG, RMG), AGV, bãi, bến, cổng, tàu.
2. **Thực thể số (Virtual Entity):** biểu diễn số có cập nhật trạng thái (state-aware).
3. **Liên kết hai chiều (Bidirectional Connection):** đồng bộ thời gian thực qua dữ liệu cảm biến + feedback loop.

**Quy tắc inclusion:** bài được coi là DT nếu có ≥ 2/3 thuộc tính. Chỉ 1/3 → coi là Digital Shadow / Digital Model — vẫn nằm trong phạm vi nếu thoả IC4 (IoT/monitoring) hoặc IC5 (Visualization) như cấu phần của khung DT lớn hơn.

## 2.2 Lớp 2 — Năm cấp Maturity (L1 → L5)

Mở rộng từ IDC DT Maturity Model (2019) + ISA-95 Automation Hierarchy:

| Cấp | Tên | Định nghĩa hoạt động |
|-----|-----|------------------------|
| **L1** | Khả kiến dữ liệu (Data Visibility) | Cảm biến IoT, dashboard, giám sát thời gian thực — *thấy* trạng thái nhưng chưa *hiểu* |
| **L2** | Trạng thái vận hành (Operational State) | Tích hợp dữ liệu đa nguồn, ontology, sự kiện vận hành tính toán được — *hiểu* trạng thái |
| **L3** | Hỗ trợ quyết định (Decision Support) | Tối ưu / RL / MILP / metaheuristic dùng dữ liệu DT — *gợi ý* hành động |
| **L4** | Mô phỏng và Kiểm chứng (Simulation & V&V) | DES, what-if, calibration, verification, 3D/4D — *thử nghiệm* hành động trước khi thực thi |
| **L5** | Vòng kín tự trị (Closed-Loop Autonomy) | Data → Decision → Verify → Feedback tự động, không can thiệp người trong vòng |

## 2.3 Khái niệm Trần thực tế (Realistic Ceiling)

Mỗi cảng có **trần thực tế** L\* phụ thuộc cost-benefit (giả thuyết — sẽ kiểm chứng qua RQ5b):

| Quy mô cảng (TEU/năm) | Trần khuyến nghị | Lý do |
|------------------------|---------------------|--------|
| Megaport (≥ 10M) | L5 | ROI cao, đủ ngân sách |
| Lớn (3M–10M) | L4–L5 | ROI tốt với L4; L5 chỉ khi automation toàn diện |
| Vừa (0.5M–3M) | L3–L4 | L4 nếu có nhu cầu what-if; L3 đủ cho daily ops |
| Nhỏ (< 0.5M) | L2–L3 | L5 không cost-benefit positive; L3 đủ |

---

# §III. NĂM CHIỀU PHÂN TÍCH

| # | Chiều | Giá trị | Ghi nhận |
|---|-------|----------|------------|
| 1 | **Tầng trưởng thành** | L1, L2, L3, L4, L5 | Extraction Group C |
| 2 | **Lĩnh vực vận hành** | berth, yard, quay crane, AGV, gate (5 loại) | Extraction Group D (5 boolean) |
| 3 | **Quy mô cảng** | megaport, lớn, vừa, nhỏ, unspecified | Extraction Group D' |
| 4 | **Vintage (tuổi đời triển khai)** | greenfield (xây mới), brownfield (retrofit cảng cũ), mixed, unspecified | Extraction Group D' |
| 5 | **Vị trí địa lý** | quốc gia, khu vực (toàn cầu / VN / ĐNÁ / phát triển / đang phát triển) | Extraction Group A |

> Heat-map RQ4a vẽ 3 chiều (Tầng × Lĩnh vực × Quy mô) — giữ trực quan 3D. Vintage và Geographic phân tích riêng (RQ4d, RQ4c).

---

# §IV. BỘ 5 CÂU HỎI NGHIÊN CỨU

## RQ1 — Bức tranh tổng thể (WHAT)

> Trong giai đoạn 2015–2026, các nghiên cứu về Bản sao số cho vận hành cảng container đã được công bố ra sao về quy mô, xu hướng thời gian, phân bố địa lý, tạp chí trọng điểm và phương pháp chủ đạo?

| Sub | Câu hỏi |
|------|----------|
| **1a** | Xu hướng công bố theo năm 2015–2026 |
| **1b** | Phân bố địa lý — quốc gia / khu vực dẫn đầu, vị trí Việt Nam và Đông Nam Á |
| **1c** | Tạp chí, hội nghị, nhà xuất bản trọng điểm (top 10) |
| **1d** | Phương pháp chủ đạo (mô phỏng, tối ưu, IoT, AI, kết hợp) — phân bố |
| **1e** | Mạng đồng tác giả + đồng từ khoá + đồng trích dẫn (bibliometric VOSviewer) |

**Phương pháp trả lời:** Bibliometric Analysis — descriptive + VOSviewer 5 maps (co-authorship, co-occurrence keywords, co-citation, bibliographic coupling, country collaboration).
**Output cuối:** `SR_Bibliometric.md` + 5 PNG.

---

## RQ2 — Mức độ trưởng thành (HOW MATURE)

> Mỗi nghiên cứu đạt tầng trưởng thành nào (L1–L5) × 5 lĩnh vực vận hành (bến, bãi, cẩu bờ, AGV, cổng), và phân bố này khác biệt thế nào theo quy mô cảng?

| Sub | Câu hỏi |
|------|----------|
| **2a** | Phân bố tầng × lĩnh vực vận hành (heat-map 2D) |
| **2b** | Tầng cao nhất *đã đạt được* trong literature cho từng lĩnh vực |
| **2c** | Phân bố tầng × quy mô cảng (heat-map 2D bổ sung) |

**Phương pháp trả lời:** Data Extraction → Maturity Classification → ma trận phân bố.
**Output cuối:** Ma trận L × Lĩnh vực + ma trận L × Quy mô + 2 heat-map 2D + bảng tầng cao nhất.

---

## RQ3 — Phương pháp và Yêu cầu nguồn lực (HOW METHOD)

> Những phương pháp và kiến trúc kỹ thuật nào đang được sử dụng để đạt từng tầng trưởng thành, và mỗi tổ hợp phương pháp × tầng đòi hỏi mức nguồn lực ra sao (dữ liệu, hạ tầng IoT, năng lực tính toán, nhân lực)?

| Sub | Câu hỏi |
|------|----------|
| **3a** | Phương pháp chủ đạo ở mỗi tầng (DES, RL, MILP, IoT, ontology, hybrid…) |
| **3b** | Cường độ nguồn lực cần cho mỗi tổ hợp phương pháp × tầng (Low / Medium / High) |
| **3c** | Thành phần Bản sao số *nhẹ* / chi phí thấp khả dĩ cho cảng nguồn lực hạn chế |

**Phương pháp trả lời:** Extraction Group B (method) + Group D' (resource_intensity, lightweight components) → bảng tổng hợp.
**Output cuối:** Bảng phương pháp × tầng × cường độ nguồn lực + danh sách light DT components.

---

## RQ4 — Khoảng trống nghiên cứu (WHERE GAPS) — *5 chiều*

> Tổ hợp nào còn ít được khai thác trong y văn, phân theo các chiều: combinatorial (Tầng × Lĩnh vực × Quy mô), method × tầng, địa lý, vintage (greenfield ↔ brownfield), và open problems?

| Sub | Câu hỏi | Loại gap |
|------|----------|------------|
| **4a** | Ô trống combinatorial trong heat-map 3D (Tầng × Lĩnh vực × Quy mô) — định nghĩa "ô trống" = #studies ≤ 3 hoặc = 0 | Spatial / Combinatorial |
| **4b** | Ô trống method × tầng — phương pháp nào *chưa* được áp dụng cho tầng nào | Methodological |
| **4c** | Khoảng cách địa lý: top 5 quốc gia leader so với Việt Nam và Đông Nam Á (số bài, top L, top method) | Geographic |
| **4d** | Khoảng cách vintage: greenfield vs brownfield — sự khác biệt về Tầng đạt được, method dùng, thách thức triển khai | Temporal / Contextual |
| **4e** | Open problems / vấn đề chưa được giải quyết đầy đủ trong literature | Theoretical |

**Phương pháp trả lời:** Gap analysis trên data đã extraction.
**Output cuối:** Danh sách ô trống ưu tiên + heat-map 3D + bảng so sánh greenfield/brownfield + danh sách open problems.

---

## RQ5 — Chương trình nghiên cứu và Lộ trình (WHAT NEXT)

> Trong các khoảng trống đã phát hiện ở RQ4, tổ hợp nào nên được ưu tiên nghiên cứu, và lộ trình nào khả thi cho cảng nguồn lực hạn chế?

| Sub | Câu hỏi |
|------|----------|
| **5a** | Trong các gap đã phát hiện ở RQ4a–4d, tổ hợp nào nên được **ưu tiên nghiên cứu trong 1–5 năm tới**? Tiêu chí ưu tiên = **gap_size × demand × feasibility**. Output: danh sách RA1–RA6 ranked. |
| **5b** | Đối với một cảng đang ở Tầng X với ràng buộc nguồn lực Y (vintage Z), lộ trình thực tế nào để nâng lên **Tầng X+1** (chứ không nhất thiết tới L5)? Mỗi mức trần phải verified là *cost-benefit positive* cho cảng quy mô đó. |
| **5c** | Thách thức kỹ thuật và tổ chức cần vượt qua cho 5a + 5b (dữ liệu, nhân lực, vốn, hạ tầng, chuẩn hoá) |
| **5d** | Đề xuất **kiến trúc DT nhẹ** cho cảng vừa+nhỏ: thành phần tối thiểu, công cụ mã nguồn mở, mô hình dùng chung tài nguyên giữa cụm cảng (federated DT) |

### Tiêu chí ưu tiên RA — định lượng

```text
Priority_score(RA_i) = w1 × gap_size + w2 × demand_signal + w3 × feasibility

  gap_size       = #studies trong cell tương ứng (đảo ngược: ít → cao)
  demand_signal  = (số cảng cần × throughput tổng × áp lực số hoá)
  feasibility    = (data availability × tool maturity × cost_estimate^-1)

  Trọng số mặc định: w1 = w2 = w3 = 1/3 (sensitivity test ở Bước 17.5)
```

### Lộ trình điều kiện hoá theo (Tầng hiện tại × Quy mô × Vintage)

| Cảng đang ở | Trần khuyến nghị | Bước kế tiếp khả thi (giả thuyết — RQ5b verify) |
|--------------|---------------------|---------------------------------------------------|
| L1, nhỏ, brownfield | L2 | Tích hợp dữ liệu cơ bản (PostgreSQL + Kafka) |
| L1, vừa, greenfield | L3 | IoT + Decision Support đơn giản |
| L2, vừa, brownfield | L3 | Optimization với data có sẵn |
| L2, lớn, greenfield | L4 | DES + V&V + 4D Visualization |
| L3, lớn, brownfield | L4 | Sim layer + calibration với data legacy |
| L3, megaport | L5 | Closed-loop autonomy |

> Bài SR sẽ refine bảng này sau khi tổng hợp evidence (Bước 17.6).

**Phương pháp trả lời:** Synthesis — RA1–RA6 ranked + lộ trình điều kiện hoá + Expert Validation Delphi-lite.
**Output cuối:** `SR_Research_Agenda.md`.

---

> **Đánh giá chất lượng nghiên cứu (Quality Appraisal)** — 8 tiêu chí Q1–Q8 theo Kitchenham & Charters 2007 — là yêu cầu của PRISMA 2020 Item 11 (Risk of bias). KHÔNG phải RQ độc lập; trình bày trong Phương pháp luận §3.5 của bản thảo.

---

# §V. ÁNH XẠ RQ → BƯỚC WORKPLAN

| RQ | Sub | Bước WorkPlan | Output cuối |
|----|------|----------------|----------------|
| RQ1 | 1a–1e | Bước 16 (Bibliometric) | `SR_Bibliometric.md` + 5 PNG |
| RQ2 | 2a | Bước 11 + 12 + 17.2 | Heat-map L × Lĩnh vực |
| RQ2 | 2b | Bước 12 + 17.2 | Bảng tầng cao nhất theo lĩnh vực |
| RQ2 | 2c | Bước 11 + 12 + 17.2 | Heat-map L × Quy mô |
| RQ3 | 3a–3b | Bước 11 + 17.4 | Bảng phương pháp × tầng × resource |
| RQ3 | 3c | Bước 11 + 17.4 | Danh sách light DT components |
| RQ4 | 4a | Bước 17.2 + 17.3 | Heat-map 3D + danh sách ô trống ưu tiên |
| RQ4 | 4b | Bước 17.4 | Ma trận method × tầng gap |
| RQ4 | 4c | Bước 17.3 | Bảng top 5 leader vs VN/ĐNÁ |
| RQ4 | 4d | Bước 17.3 | Bảng so sánh greenfield ↔ brownfield |
| RQ4 | 4e | Bước 17.5 | Danh sách open problems |
| RQ5 | 5a | Bước 17.5 | RA1–RA6 với priority_score |
| RQ5 | 5b | Bước 17.6 | Lộ trình điều kiện hoá (Tầng × Quy mô × Vintage) |
| RQ5 | 5c | Bước 17.6 | Bảng thách thức |
| RQ5 | 5d | Bước 17.6 | Kiến trúc DT nhẹ + open-source toolkit |

---

# §VI. ÁNH XẠ RQ → TRUY VẤN TÌM KIẾM

| RQ | Sub | Truy vấn neo (chi tiết §4 Search Strategy) |
|----|------|-----------------------------------------------|
| RQ1 | 1a–1e | Q1 (Core narrow) + Q2 (Core extended) + tổng pool |
| RQ2 | 2a | Q3 (T-L1) + Q4 (T-L2) + Q5 (T-L3) + Q6 (T-L4) + Q7 (T-L5) + Q8 (Gate) |
| RQ2 | 2b | Như 2a |
| RQ2 | 2c | Q9 (Quy mô + tên cảng VN/ĐNÁ) + tổng pool |
| RQ3 | 3a–c | Q3 + Q4 + Q5 + Q6 + Q7 |
| RQ4 | 4a | Tổng pool |
| RQ4 | 4b | Tổng pool method |
| RQ4 | 4c | Q9 (tên cảng VN/ĐNÁ) |
| RQ4 | 4d | Q10 (Vintage greenfield/brownfield) |
| RQ4 | 4e | Tổng pool + snowball |
| RQ5 | 5a–d | Tổng pool — đặc biệt Q9 + Q10 cho cảng nguồn lực hạn chế |

---

# §VII. VERSIONING

| Version | Ngày | Thay đổi | Phê duyệt |
|---------|------|-----------|-------------|
| **v1.0** | 2026-05-08 | Bộ 5 RQ thiết kế đầu tiên — logic chặt theo Kitchenham 2007 (WHAT → HOW MATURE → HOW METHOD → WHERE GAPS → WHAT NEXT); RQ4 5 chiều bao gồm vintage; RQ5 với Realistic Ceiling concept và conditional roadmap | NCS HoaTX (chờ phê duyệt) |

---

# §VIII. LIÊN KẾT NỘI BỘ

| File | Quan hệ |
|------|----------|
| `WorkPlan.md` §0.7 | Reference tới file này — KHÔNG duplicate RQ |
| `SR_Search_Strategy.md` §1.3, §1.4 | Reference tới file này — Strategy chỉ mô tả how to search |
| `SR_Eligibility_Criteria.md` | IC2-IC5 align với 5 lĩnh vực vận hành (RQ2); Borderline 6 align với RQ4d |
| `SR_Data_Extraction_Form.md` Group D + D' | Field `area_*`, `port_size`, `port_vintage`, `realistic_ceiling`, `l5_evidence` align với RQ2, RQ4d, RQ5b |
| `osf_release/SR_Research_Questions.md` | Bản công khai (đã strip nhãn nội bộ) — sync với file này |

---

*SR_Research_Questions.md — v1.0 — 2026-05-08 — Single Source of Truth*
