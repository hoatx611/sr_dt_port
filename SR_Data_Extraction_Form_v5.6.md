# MẪU TRÍCH XUẤT DỮ LIỆU
# Digital Twin cho Vận hành Cảng Container

**Phiên bản:** v1.0 — 2026-05-08
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**OSF DOI:** [10.17605/OSF.IO/DXJW9](https://doi.org/10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 Items 9 (Data items — outcome), 10a (Data collection process), 10b (Data items — other)
**Anchor:** `SR_Research_Questions_v5.6.md` v1.0 — mỗi nhóm trường align với RQ tương ứng

---

# §I. MỤC ĐÍCH VÀ NGUYÊN TẮC

## 1.1 Mục đích

Mẫu trích xuất chuẩn hoá data từ mỗi included study → file `extraction_v5.6.csv` để phân tích ở Bước 16 (bibliometric) + Bước 17 (synthesis).

## 1.2 Nguyên tắc

1. **Mỗi included study = 1 row** trong CSV.
2. **Bắt buộc** trích đủ các trường ghi `*` (required); các trường khác có thể `unspecified` nếu paper không nêu.
3. **Đọc toàn văn** trước khi trích — không chỉ abstract (PRISMA Item 10a).
4. **Trích nguyên văn quote** cho các field đánh giá chủ quan (vd. `port_size_evidence`, `l5_evidence`).
5. **Pilot 5 studies** + Cohen's κ ≥ 0.75 (intra-rater) trước khi trích full pool.

---

# §II. CẤU TRÚC FORM — 6 NHÓM, 40 TRƯỜNG

| Nhóm | Tên | Số trường | RQ phục vụ |
|------|-----|-----------|--------------|
| **A** | Bibliographic | 8 | RQ1 (1a–1e) |
| **B** | Methodology | 7 | RQ3 (3a) |
| **C** | Maturity Level | 5 | RQ2 (2a–2c), RQ3 (3a) |
| **D** | Operational Area | 5 | RQ2 (2a, 2b), RQ4 (4a) |
| **D'** | Port Size + Vintage + Resource | 11 | RQ2 (2c), RQ3 (3b–3c), RQ4 (4d), RQ5 (5b–5d) |
| **E** | Geographic + Gap + Future | 4 | RQ4 (4c, 4e), RQ5 (5a) |

**Tổng:** 40 trường.

---

# §III. CHI TIẾT TỪNG NHÓM TRƯỜNG

## §III.A — Bibliographic (8 trường) — RQ1

| Field | Type | Required | Mô tả |
|-------|------|----------|--------|
| `study_id` | string | * | UUID từ dedup pool (DOI hoặc hash) |
| `doi` | string | * | DOI chuẩn hoá |
| `title` | string | * | Tiêu đề bài (giữ nguyên gốc) |
| `authors` | string | * | Author1; Author2; … (semicolon-separated) |
| `year` | int | * | Năm xuất bản (PY) |
| `journal_or_venue` | string | * | Tên tạp chí / hội nghị (theo Scopus T2 tag) |
| `doc_type` | enum | * | {article, conference_paper, review, book_chapter} |
| `country_of_first_author` | string | * | Quốc gia first author (theo affiliation) |

## §III.B — Methodology (7 trường) — RQ3a

| Field | Type | Required | Mô tả |
|-------|------|----------|--------|
| `dt_method` | enum (multi) | * | {data_integration, ontology, simulation_DES, agent_based, RL, MILP, metaheuristic, deep_learning, IoT_sensor, visualization_3D_4D, gis, hybrid, other} |
| `simulation_tool` | string | – | AnyLogic / SimPy / Plant Simulation / Witness / etc. |
| `optimization_algorithm` | string | – | CPLEX / Gurobi / DDPG / PPO / Genetic / etc. |
| `data_source` | enum (multi) | * | {iot_sensor, ais, tos_log, simulated, historical_record, expert_interview, public_dataset} |
| `validation_method` | enum | * | {none, sim_only, real_data_calibration, hardware_in_loop, field_test, expert_review} |
| `dataset_url` | string | – | URL nếu tác giả publish dataset |
| `code_availability` | enum | * | {none, on_request, github, zenodo, osf, supplementary} |

## §III.C — Maturity Level (5 trường) — RQ2 + RQ3

| Field | Type | Required | Mô tả |
|-------|------|----------|--------|
| `maturity_primary` | enum | * | {L1, L2, L3, L4, L5} — tầng cao nhất *thực sự đạt được* trong paper |
| `maturity_secondary` | enum | – | {L1..L5, none} — tầng kế tiếp được phủ một phần |
| `maturity_evidence` | string (quote) | * | Nguyên văn câu trong paper chứng minh maturity_primary |
| `maturity_confidence` | enum | * | {high, medium, low} — độ tin cậy của classification |
| `l5_evidence` | string | conditional | Nếu maturity_primary = L5: quote chứng minh closed-loop autonomy (data → decision → verify → feedback tự động). Nếu không L5: để trống. |

## §III.D — Operational Area (5 trường) — RQ2 + RQ4a

5 boolean cho 5 lĩnh vực vận hành (xem Eligibility IC2):

| Field | Type | Required | Mô tả |
|-------|------|----------|--------|
| `area_berth` | bool | * | True nếu paper có cấu phần berth allocation/scheduling |
| `area_yard` | bool | * | True nếu paper có cấu phần yard management/allocation/stack |
| `area_quay_crane` | bool | * | True nếu paper có cấu phần quay crane scheduling/operation |
| `area_agv` | bool | * | True nếu paper có cấu phần AGV dispatching/scheduling/routing |
| `area_gate` | bool | * | True nếu paper có cấu phần gate operation, truck appointment, drayage |

> Một paper có thể có nhiều areas = True (vd. paper berth + quay crane scheduling).

## §III.D' — Port Size + Vintage + Resource (11 trường) — RQ2c + RQ3 + RQ4d + RQ5

| Field | Type | Required | Mô tả |
|-------|------|----------|--------|
| `port_size` | enum | * | {megaport, large, mid_size, small, unspecified} — phân loại theo throughput TEU/năm (xem WorkPlan §II Bước 12.2) |
| `port_size_evidence` | string (quote) | conditional | Quote chứng minh port_size (vd. "the case study port handles 2.3 million TEU/year") |
| `port_vintage` | enum | * | {greenfield, brownfield, mixed, unspecified} — xem Eligibility Borderline 6 |
| `port_vintage_evidence` | string (quote) | conditional | Quote chứng minh vintage |
| `realistic_ceiling` | enum | – | {L1, L2, L3, L4, L5, not_assessed} — tầng cao nhất paper *cho rằng* khả thi cost-benefit cho cảng quy mô này; phục vụ RQ5b |
| `realistic_ceiling_rationale` | string (quote) | conditional | Quote chứng minh realistic_ceiling (nếu paper có thảo luận) |
| `resource_intensity` | enum | * | {Low, Medium, High} — cường độ nguồn lực cần (dữ liệu, IoT, computing, nhân lực) — đánh giá theo bảng dưới |
| `resource_components` | string (multi) | * | comma-separated: {sensor_iot, gps_tracking, video_analytics, edge_compute, cloud_compute, GPU_cluster, dedicated_team, specialized_software, …} |
| `lightweight_dt_used` | bool | * | True nếu paper claim/dùng "lightweight DT" / "low-cost DT" / "edge DT" |
| `lightweight_components` | string | conditional | Liệt kê các components được claim là lightweight (nếu lightweight_dt_used = True) |
| `applicable_to_small_port` | bool | * | Đánh giá NCS: paper có thể áp được cho cảng nhỏ/vừa không (theo cost-benefit + resource_intensity) |

### Bảng định nghĩa Resource Intensity (3 mức)

| Mức | Tiêu chí (NCS đánh giá theo paper) |
|------|--------------------------------------|
| **Low** | Sensor đơn giản (RFID, GPS), edge compute, ≤ 2 developer, free/open-source tools, < $100k initial budget |
| **Medium** | IoT network đa cảm biến + cloud compute moderate, 3–8 developers, mix open-source + commercial tools, $100k–$1M |
| **High** | IoT đa lớp + GPU cluster + dedicated DT team, 10+ developers, commercial DT platform (Siemens MindSphere / GE Predix / PTC ThingWorx), > $1M |

## §III.E — Geographic + Gap + Future (4 trường) — RQ4 + RQ5

| Field | Type | Required | Mô tả |
|-------|------|----------|--------|
| `geographic_context` | enum | * | {global, north_america, europe, east_asia, southeast_asia, vietnam, middle_east, africa, south_america, theoretical_no_case} |
| `gap_identified` | string | – | Quote/note: gap mà paper *tự đề cập* (paper's stated limitation hoặc future work) |
| `future_research_proposed` | string | – | Hướng future work paper đề xuất |
| `relevant_to_resource_constrained_port` | bool | * | NCS đánh giá: paper có insight cho cảng nguồn lực hạn chế (RQ5b/c/d) không |

---

# §IV. QUY TRÌNH ÁP DỤNG

## 4.1 Pilot extraction (Bước 11.2)

| Bước | Mô tả |
|-------|--------|
| 11.2.1 | NCS chọn 5 included studies đa dạng: 1 L1 IoT + 1 L2 ontology + 1 L3 RL + 1 L4 DES + 1 cảng-ĐNÁ |
| 11.2.2 | Trích xuất lần 1 → lưu CSV |
| 11.2.3 | Đợi ≥ 14 ngày → trích xuất lần 2 *mù* (không xem lần 1) |
| 11.2.4 | Tính κ giữa 2 lần — mục tiêu κ ≥ 0.75 (intra-rater) |
| 11.2.5 | Nếu κ < 0.75 → refine định nghĩa trường + form v1.x → re-pilot |

## 4.2 Full extraction (Bước 11.3)

NCS chấm tuần tự included pool theo thứ tự ưu tiên (cảng VN/ĐNÁ → cảng nguồn lực hạn chế → các bài còn lại). Output: `extraction_v5.6.csv` — 40 cột × N rows.

## 4.3 Quality control

- **Audit trail:** mỗi row có timestamp + version form sử dụng
- **Borderline log:** quyết định khó ghi vào `borderline_decisions_log.md` (Bước 13)
- **Cross-check:** sau khi extract 50% pool → spot-check 10 random rows với fulltext

---

# §V. ÁNH XẠ FIELD → BƯỚC PHÂN TÍCH

| Field | Bước phân tích | Output |
|-------|------------------|---------|
| year, country, journal | 16 (Bibliometric) | RQ1a-c |
| dt_method | 16, 17.4 | RQ1d, RQ3a |
| maturity_primary, maturity_secondary | 12, 17.2 | RQ2a-b |
| area_* (5 boolean) | 17.2 | RQ2a, RQ4a |
| port_size | 12, 17.2 | RQ2c |
| port_vintage | 17.3 | RQ4d |
| resource_intensity | 17.4 | RQ3b |
| lightweight_dt_used | 17.4 | RQ3c |
| realistic_ceiling | 17.5, 17.6 | RQ5a, RQ5b |
| geographic_context | 17.3 | RQ4c |
| gap_identified, future_research_proposed | 17.5 | RQ4e, RQ5a |
| relevant_to_resource_constrained_port | 17.6 | RQ5b-d |

---

# §VI. VERSIONING

| Version | Ngày | Thay đổi | Phê duyệt |
|---------|------|-----------|-------------|
| **v1.0** | 2026-05-08 | Form thiết kế đầu tiên — 6 nhóm A/B/C/D/D'/E × 40 trường; align với 5 RQ; bảng định nghĩa Resource Intensity 3 mức Low/Medium/High; field `realistic_ceiling` phục vụ RQ5b conditional roadmap | NCS HoaTX (chờ phê duyệt) |

---

# §VII. LIÊN KẾT THAM CHIẾU

| File | Quan hệ |
|------|---------|
| `SR_Research_Questions_v5.6.md` | RQ doc — mỗi field align với RQ qua bảng §V |
| `WorkPlan_v5.6_FINAL.md` | Bước 11 (áp form), Bước 12 (Maturity classification), Bước 17 (synthesis) |
| `SR_Eligibility_Criteria_v5.6.md` | IC2 ↔ Group D 5 areas; Borderline 6 ↔ port_vintage |
| `SR_Classification_Rubric_v5.6.md` | Rubric chi tiết cho maturity_primary (L1-L5) — sẽ tạo ở Bước 12 |
| `SR_Quality_Appraisal_v5.6.md` | Form Quality Appraisal Q1-Q8 song song — tạo ở Bước 13 |

---

*SR_Data_Extraction_Form_v5.6.md — v1.0 — 2026-05-08 — anchored on RQ_v1.0*
