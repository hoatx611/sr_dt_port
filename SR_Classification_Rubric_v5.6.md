# RUBRIC PHÂN LOẠI MATURITY + LĨNH VỰC + BỐI CẢNH
# Digital Twin cho Vận hành Cảng Container

**File:** SR_Classification_Rubric_v5.6.md
**Phiên bản:** v1.0 — 2026-05-14
**NCS:** HoaTX
**OSF Project:** https://osf.io/dxjw9/ (DOI: 10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 Items 10a (Data extraction), 17 (Synthesis methods)
**Anchor:** `SR_Research_Questions_v5.6.md` v1.0 §II (Khung lý thuyết 2 lớp)
**Dùng tại:** Bước 12 (phân loại mỗi study sau extraction Bước 11)

> Rubric này áp dụng sau khi đọc toàn văn. Mọi quyết định phân loại ghi vào `SR_Data_Extraction_Form_v5.6.md` Group C + D + D'. Bất đồng ↔ borderline ghi vào `borderline_decisions_log.md`.

---

# §1. MATURITY LEVEL — RUBRIC L1–L5

## 1.1 Nguyên tắc phân loại

- Mỗi study được gán **1 primary level** và có thể có **1 secondary level** (nếu study phủ nhiều cấp).
- Primary = cấp **cao nhất** study đã implement và validate (không chỉ đề cập).
- Secondary = cấp cao nhất tiếp theo study có đóng góp đáng kể.
- Chỉ gán cấp nếu có **bằng chứng implement** trong paper — không gán dựa trên tuyên bố.

## 1.2 Bảng rubric chi tiết

| Cấp | Tên | Định nghĩa hoạt động | Bằng chứng YÊU CẦU | Bằng chứng KHÔNG ĐỦ |
|-----|-----|---------------------|---------------------|---------------------|
| **L1** | Khả kiến dữ liệu (Data Visibility) | Sensors/IoT → dashboard/visualization, giám sát thời gian thực; *thấy* trạng thái hiện tại | ≥ 1 trong: (a) IoT sensor network deployment, (b) real-time data pipeline từ thiết bị vật lý, (c) monitoring dashboard với live data, (d) digital shadow (one-way sync) | Báo cáo thống kê post-hoc từ log files (không real-time); data collection offline |
| **L2** | Trạng thái vận hành (Operational State) | Tích hợp đa nguồn dữ liệu, ontology/data model, tính toán KPI/state; *hiểu* bối cảnh vận hành | ≥ 1 trong: (a) ontology hoặc knowledge graph cho cảng, (b) multi-source data fusion (TOS + equipment + sensor), (c) event log semantic model, (d) computed operational state (berth occupancy, crane utilization, dwell time) đồng bộ thực tế | Chỉ database thiết kế; chỉ data collection không có semantic model |
| **L3** | Hỗ trợ quyết định (Decision Support) | Optimization/RL/MILP/heuristic + dữ liệu DT làm input; *gợi ý* hành động tối ưu | ≥ 1 trong: (a) optimization model (MILP/CP/heuristic) với DT state làm input, (b) RL/DRL agent trained/tested trên DT environment, (c) DT-fed scheduling algorithm, (d) prescriptive analytics từ DT | Optimization standalone không kết nối DT; rule-based scheduling thuần |
| **L4** | Mô phỏng và Kiểm chứng (Simulation & V&V) | DES/ABS/HiL + calibration/validation với hệ thống thực; *thử nghiệm* what-if trước khi thực thi | ≥ 1 trong: (a) DES/agent-based model được calibrate với dữ liệu thực, (b) hardware-in-the-loop test, (c) what-if scenario analysis, (d) 3D/4D visualization đồng bộ với vận hành thực (không chỉ static render), (e) V&V formal: model validation report | DES thuần không sync với hệ thống thực; 3D visualization static; simulation academic không có real data |
| **L5** | Vòng kín tự trị (Closed-Loop Autonomy) | Data → Decision → Execute → Verify → Feedback loop tự động không cần người; *thực thi* tự trị | TẤT CẢ: (a) automated decision execution (không chỉ recommendation), (b) feedback loop từ physical entity về virtual entity sau mỗi action, (c) performance verification tự động, (d) self-adaptation hoặc re-optimization khi có deviation | Chỉ recommendation system; human-in-the-loop; closed-loop chỉ trong simulation |

## 1.3 Quy trình phân loại bước-by-bước

```
Bước 1: Đọc Abstract + Introduction → xác định domain + claim cấp
Bước 2: Đọc Methodology → tìm bằng chứng implement (không chỉ tuyên bố)
Bước 3: Áp bảng §1.2 từ L5 xuống L1 — gán cấp cao nhất có bằng chứng đủ
Bước 4: Kiểm tra L5 đặc biệt: có closed-loop không? (Không → tối đa L4)
Bước 5: Xác định secondary level nếu có contribution đáng kể ở cấp khác
Bước 6: Ghi vào Extraction Form Group C (primary_maturity, secondary_maturity)
Bước 7: Nếu borderline → ghi vào borderline_decisions_log.md
```

## 1.4 Quy tắc borderline maturity

| Tình huống borderline | Quy tắc |
|-----------------------|---------|
| Paper claim L5 nhưng chỉ demo trong simulation | → Gán L4, note "L5 claimed but simulation-only" |
| Paper có DES + ML recommendation (không auto-execute) | → Gán L4 primary, L3 secondary |
| Paper có optimization với DT state nhưng không validate model | → Gán L3, NOT L4 (thiếu V&V component) |
| Paper có IoT + analytics nhưng không real-time | → Gán L1 nếu có dashboard; L2 nếu có computed state |
| Paper combine nhiều contributions ở các cấp khác nhau | → Primary = cấp đóng góp chính; secondary = cấp phụ |

---

# §2. LĨNH VỰC VẬN HÀNH — 5 BOOLEAN

Mỗi study được đánh dấu **True/False** cho từng lĩnh vực. Một study có thể True cho nhiều lĩnh vực.

| Field | Keyword gợi ý | Ghi chú |
|-------|---------------|---------|
| **op_berth** | berth allocation, berth scheduling, vessel arrival, berthing plan, quayside | Bao gồm ship-to-shore interface |
| **op_yard** | yard management, stack planning, container storage, yard crane (RTG/RMG), block allocation, yard layout | |
| **op_crane** | quay crane, gantry crane, crane scheduling, crane assignment, dual-cycle, crane productivity | Quay cranes — không phải yard cranes |
| **op_agv** | AGV dispatching, AGV routing, horizontal transport, automated straddle carrier, shuttle carrier | |
| **op_gate** | gate scheduling, truck appointment system (TAS), drayage, landside logistics, gate throughput | External truck interface |

**Ghi chú:** Nếu paper đề cập lĩnh vực nhưng không phải focus chính → vẫn đánh True (boolean, không phải primary).

---

# §3. QUY MÔ CẢNG — PORT SIZE

| Mã | Mức | Throughput TEU/năm | Ví dụ cảng tiêu biểu |
|----|-----|---------------------|----------------------|
| `megaport` | Megaport | ≥ 10M | Shanghai (47M), Singapore (38M), Ningbo (35M), Shenzhen (29M) |
| `large` | Lớn | 3M–10M | Rotterdam (14M), Hamburg (8M), Tanger Med (7M), Busan (22M → mega) |
| `medium` | Vừa | 0.5M–3M | Hai Phong (≈1.5M), Cai Mep (≈0.8M), Manila, Colombo |
| `small` | Nhỏ | < 0.5M | Da Nang (≈0.1M), Quy Nhon, regional feeder ports |
| `unspecified` | Không xác định | Không nêu throughput | Theoretical framework, simulation không gắn case |

**Quy trình xác định:** (1) Tìm throughput nêu trong paper; (2) Nếu không nêu → tra cứu tên cảng → phân loại; (3) Nếu không có case study thực → `unspecified`.

---

# §4. VINTAGE — TUỔI ĐỜI TRIỂN KHAI

Theo Eligibility Criteria Borderline 6 (`SR_Eligibility_Criteria_v5.6.md` §VI Rule 6).

| Mã | Loại | Định nghĩa | Dấu hiệu nhận biết |
|----|------|------------|---------------------|
| `greenfield` | Xây mới | Cảng thiết kế + xây từ đầu với DT/automation ngay từ đầu | "new terminal", "greenfield", "purpose-built", cảng mở cửa sau 2010 với full automation |
| `brownfield` | Retrofit | Cảng đang vận hành, DT/automation được cài vào hệ thống cũ | "existing terminal", "legacy TOS", "retrofit", "upgrade", cảng có lịch sử vận hành trước khi DT |
| `mixed` | Kết hợp | Case study tại cảng có cả greenfield phase và brownfield phase | "phase 2 expansion", "greenfield AGV bay + brownfield crane" |
| `unspecified` | Không xác định | Paper không nêu vintage, hoặc theoretical không có case | Framework paper, simulation không gắn cảng cụ thể |

---

# §5. ĐỊA LÝ — GEOGRAPHIC CONTEXT

| Field | Giá trị | Ghi chú |
|-------|---------|---------|
| `geo_country` | Tên quốc gia (ISO-3166 alpha-3) | VNM, CHN, NLD, KOR, SGP, DEU, … |
| `geo_region` | Tên vùng | East Asia, Southeast Asia, Europe, Middle East, Global (không gắn vùng) |
| `geo_vn_sea` | True/False | True nếu case study tại Việt Nam hoặc ĐNÁ (phục vụ RQ4c) |

---

# §6. DECISION TREE TÓM TẮT

```
Paper đọc xong?
  ├── Có DT/DT-equivalent component (≥ 2/3 Grieves attributes)?
  │     ├── Không → Check IC4/IC5 → nếu có → vẫn extract; nếu không → xem xét loại EC4
  │     └── Có → Tiếp tục
  │
  ├── PRIMARY MATURITY:
  │     Có closed-loop auto-execute? → L5
  │     Có DES/sim + validation/calibration thực? → L4
  │     Có optimization/RL fed by DT state? → L3
  │     Có semantic model / ontology / computed state? → L2
  │     Có IoT/sensor/real-time dashboard? → L1
  │     Không có bằng chứng đủ → ghi "L0 (unclear)" + note
  │
  ├── OPERATIONAL AREA: đánh True/False cho 5 lĩnh vực
  ├── PORT SIZE: megaport / large / medium / small / unspecified
  ├── VINTAGE: greenfield / brownfield / mixed / unspecified
  └── GEOGRAPHY: country + region + geo_vn_sea
```

---

# §7. MAPPING VỚI EXTRACTION FORM

| Trường Rubric | Group trong SR_Data_Extraction_Form | Field name |
|---------------|--------------------------------------|------------|
| Primary maturity | Group C | `primary_maturity` |
| Secondary maturity | Group C | `secondary_maturity` |
| op_berth/yard/crane/agv/gate | Group D | 5 boolean fields |
| port_size | Group D' | `port_size` |
| port_vintage | Group D' | `port_vintage` |
| geo_country, geo_region, geo_vn_sea | Group A | geographic fields |

---

# §8. VERSIONING

| Version | Ngày | Thay đổi |
|---------|------|----------|
| **v1.0** | 2026-05-14 | Tạo ban đầu — L1-L5 rubric đầy đủ; port size; vintage; 5 lĩnh vực; decision tree |

**Quy tắc cập nhật:** Sau Bước 14.3 (intra-rater κ cho Maturity) — nếu κ < 0.75 → version 1.1 với clarification definitions. Mỗi update ghi DEV entry + OSF Amendment.

---

# §9. LIÊN KẾT

| File | Quan hệ |
|------|---------|
| `SR_Research_Questions_v5.6.md` §II | Lý thuyết L1-L5 + Realistic Ceiling |
| `SR_Eligibility_Criteria_v5.6.md` §VI | Borderline 6 (vintage rule) |
| `SR_Data_Extraction_Form_v5.6.md` | Group C/D/D' nhận data từ rubric này |
| `SR_Quality_Appraisal_v5.6.md` | Chạy song song với classification Bước 12–13 |
| `WorkPlan_v5.6_FINAL.md` | Bước 12 |

---

*SR_Classification_Rubric_v5.6.md — v1.0 — 2026-05-14 — NCS HoaTX*
