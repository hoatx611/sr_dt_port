# CHIẾN LƯỢC TÌM KIẾM CHO TỔNG QUAN HỆ THỐNG
# Digital Twin cho Vận hành Cảng Container

**Phiên bản:** v1.0 — 2026-05-08
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**OSF DOI:** [10.17605/OSF.IO/DXJW9](https://doi.org/10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 (Page et al. 2021) Items 6, 7 + PRISMA-S (Rethlefsen et al. 2021) 16 items + PRESS (McGowan et al. 2016)
**Mục tiêu xuất bản:** Tạp chí Q1 — ưu tiên *International Journal of Production Research* (Taylor & Francis, IF ≈ 9.2) hoặc *Maritime Policy & Management* (T&F, IF ≈ 6.0); dự phòng *Computers in Industry*, *Annual Reviews in Control*, *Journal of Marine Science and Engineering*.
**Phạm vi:** 2015–2026 | Tiếng Anh | Peer-reviewed (Article / Conference paper / Review article / Book chapter)
**Anchor:** `SR_Research_Questions_v5.6.md` v1.0 — bộ 5 RQ với RQ4 5 chiều + Realistic Ceiling

---

# §1. BỐI CẢNH VÀ NGUYÊN TẮC THIẾT KẾ

## 1.1 Vị trí bài Tổng quan hệ thống trong chương trình nghiên cứu

Bài Tổng quan hệ thống đóng vai trò **bài cơ sở (anchor paper)** của luận án tiến sĩ "Bản sao số cho vận hành cảng container", đặt nền lý thuyết và phát hiện khoảng trống cho các bài tiếp theo:

| Bài | Chủ đề chính | SR cần phủ |
|-----|--------------|---------------|
| Paper 1 | Ontology + Tích hợp dữ liệu cho Mô hình hoá Trạng thái Vận hành | Tầng L2 — `Q4` |
| Paper 2 | Tối ưu hoá lai MILP–RL cho Lập lịch chéo quy trình | Tầng L3 — `Q5` |
| Paper 3 | DES + V&V Framework + Trực quan hoá 4D | Tầng L4 — `Q6` |
| Backup B | Đánh giá mức độ sẵn sàng DT cho cảng vừa và nhỏ | Bối cảnh quy mô — `Q9` |
| Backup C | Bản đồ vận hành GIS-based | L4 visualization — `Q6` |

## 1.2 Năm nguyên tắc thiết kế chiến lược tìm kiếm

**Nguyên tắc 1 — RQ-driven query design.** Mỗi truy vấn phải có một (hoặc nhiều) sub-RQ được nó phục vụ tường minh. Không truy vấn nào được thiết kế "cho chắc" mà không gắn với RQ cụ thể.

**Nguyên tắc 2 — Phủ đủ 5 chiều phân tích.** Bộ truy vấn phải đảm bảo *evidence base* đủ chặt cho cả 5 chiều: (1) Tầng L1-L5; (2) 5 lĩnh vực vận hành; (3) Quy mô cảng; (4) Vintage; (5) Vị trí địa lý. Lỗ hổng chiều nào → truy vấn riêng cho chiều đó.

**Nguyên tắc 3 — Hai lớp Core + Strata.** Lớp Core (Q1, Q2) bắt landscape tổng thể. Lớp Strata (Q3-Q10) phủ từng tầng / lĩnh vực / bối cảnh đặc trưng — tránh phụ thuộc chỉ vào Core.

**Nguyên tắc 4 — Tinh gọn, không trùng.** Mỗi truy vấn có *unique purpose*. Tránh truy vấn redundant (vd. nhiều truy vấn DT-port chung). Giữ tổng số truy vấn ≤ 25 để dễ quản trị, dễ tái lập.

**Nguyên tắc 5 — Reproducibility tuyệt đối.** Toàn bộ chuỗi truy vấn lưu nguyên văn trong file này; ngày chạy + số records + RIS files được ghi vào §9 status table; OSF Files lưu RIS gốc cho PRISMA-S Item 8.

## 1.3 Câu hỏi nghiên cứu — Single Source of Truth

> **Bộ 5 RQ chính thức** lưu trong `SR_Research_Questions_v5.6.md` v1.0. Strategy chỉ mô tả *how to search* — KHÔNG lặp định nghĩa RQ.

### Tóm tắt headlines (chi tiết xem RQ doc §IV)

| RQ | Tên | Số sub | Bước WorkPlan |
|----|-----|---------|------------------|
| **RQ1** | Bức tranh tổng thể (WHAT) | 5 (1a–1e) | 16 (Bibliometric) |
| **RQ2** | Mức độ trưởng thành (HOW MATURE) — L1–L5 × 5 lĩnh vực × Quy mô | 3 (2a–2c) | 11, 12, 17.2 |
| **RQ3** | Phương pháp + Nguồn lực (HOW METHOD) | 3 (3a–3c) | 11, 17.4 |
| **RQ4** | Khoảng trống (WHERE GAPS) — 5 chiều | 5 (4a–4e) | 17.2, 17.3, 17.4, 17.5 |
| **RQ5** | Chương trình NC + Lộ trình (WHAT NEXT) — conditional roadmap | 4 (5a–5d) | 17.5, 17.6 |

## 1.4 Khung trưởng thành 5 cấp — cơ sở thiết kế truy vấn theo tầng

```text
Level 1 — Data Visibility       → IoT, smart port, dashboard, monitoring   (Q3)
Level 2 — Operational State     → Data integration, ontology, event log    (Q4)
Level 3 — Decision Support      → Optimization, RL, scheduling, MILP       (Q5)
Level 4 — Simulation & V&V      → DES, agent-based, calibration, 3D/4D     (Q6)
Level 5 — Closed-Loop Autonomy  → Closed-loop, feedback control, self-adapt(Q7)
```

## 1.5 Ánh xạ RQ → Truy vấn — bảng tường minh

| RQ | Sub | Truy vấn neo | Truy vấn hỗ trợ |
|----|------|---------------|--------------------|
| RQ1 | 1a–1e | Q1 + Q2 | Tổng pool (12 numbered + GS) |
| RQ2 | 2a (Tầng × Lĩnh vực) | Q3 + Q4 + Q5 + Q6 + Q7 + **Q8 (Gate)** | Q1 + Q2 broad coverage |
| RQ2 | 2b (Tầng cao nhất) | Như 2a | – |
| RQ2 | 2c (Tầng × Quy mô) | **Q9 (Quy mô + tên cảng VN/ĐNÁ)** | Tổng pool |
| RQ3 | 3a–3c | Q3 + Q4 + Q5 + Q6 + Q7 | Q1 + Q2 |
| RQ4 | 4a (combinatorial) | Tổng pool | – |
| RQ4 | 4b (method × tầng) | Q5 + Q6 | Q1 + Q2 |
| RQ4 | 4c (geographic VN/ĐNÁ) | **Q9** | – |
| RQ4 | 4d (vintage) | **Q10 (Vintage)** | – |
| RQ4 | 4e (open problems) | Tổng pool + snowball | – |
| RQ5 | 5a–5d | Tổng pool — đặc biệt Q9 + Q10 | – |

## 1.6 Cơ sở dữ liệu

| # | Cơ sở dữ liệu | Vai trò | Truy vấn |
|---|---------------|---------|------------|
| ① | **Scopus** | Chính (Primary) | Q1–Q10 (10 truy vấn) |
| ② | **IEEE Xplore** | Phụ (Secondary) | Q1–Q10 (10 truy vấn) |
| ③ | **Google Scholar** | Bổ sung (Supplementary) | Q13–Q22 (10 sub-queries) |
| ④ | **Springer Link** | Bổ trợ — giảm độ trễ lập chỉ mục | Q11 (1 truy vấn, 12 tháng) |
| ⑤ | **Taylor & Francis Online** | Bổ trợ — giảm độ trễ lập chỉ mục | Q12 (1 truy vấn, 6 tháng) |

**Cơ sở dữ liệu đã loại trừ:** Web of Science (institutional access constraint; ≈ 90% overlap với Scopus theo Mongeon & Paul-Hus 2016); ScienceDirect (đã indexed trong Scopus); ACM Digital Library (phủ chủ yếu HCI, không phù hợp); DBLP (chỉ meta-data, không có abstract).

**Đối phó rủi ro PRISMA-S Item 5:** chạy **recall validation** trên 78 hạt giống (Bước 15.1) để đo độ thu hồi (recall ≥ 95% là ngưỡng chấp nhận).

---

# §2. KIẾN TRÚC TÌM KIẾM

```
┌────────────────────────────────────────────────────────────────────┐
│  LỚP 1: CORE (Scopus + IEEE Xplore)                                │
│                                                                    │
│  Q1  CORE NARROW   ── DT-driven × 12 cụm cảng đặc trưng           │
│  Q2  CORE EXTENDED ── DT/CPS × cảng × 21 từ vận hành rộng         │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│  LỚP 2: STRATA THEO TẦNG (L1 → L5)                                │
│                                                                    │
│  Q3  T-L1 ── IoT, smart port, monitoring, dashboard                │
│  Q4  T-L2 ── Data integration, ontology, process mining            │
│  Q5  T-L3 ── Operations × Optimization (RL/MILP/heuristic)         │
│  Q6  T-L4 ── DES, agent-based, V&V, 3D/4D, GIS                    │
│  Q7  T-L5 ── Closed-loop, autonomy, feedback control               │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│  LỚP 3: STRATA THEO LĨNH VỰC + BỐI CẢNH                          │
│                                                                    │
│  Q8  Gate operations (lĩnh vực thứ 5 không cover trong Q5)        │
│  Q9  Quy mô cảng + Tên cảng VN/ĐNÁ cụ thể                         │
│  Q10 Vintage (greenfield / brownfield / retrofit)                  │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│  LỚP 4: BỔ TRỢ NHÀ XUẤT BẢN                                      │
│                                                                    │
│  Q11 Springer Link  (1 truy vấn, 12 tháng — giảm indexing lag)    │
│  Q12 Taylor & Francis (1 truy vấn, 6 tháng — bắt 2 Q1 target)    │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│  LỚP 5: BỔ SUNG GOOGLE SCHOLAR                                    │
│                                                                    │
│  Q13–Q22 GS-1 → GS-10 (10 sub-queries)                            │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│  LỚP 6: PHƯƠNG PHÁP BỔ SUNG                                      │
│                                                                    │
│  SNOW   Snowball (6 hạt giống: 4 review + 2 anchor)                │
│  HAND   Rà soát thủ công 10 tạp chí trọng điểm 2024–2026           │
│  RECALL Recall validation 78 seeds (Bước 15)                       │
│  SA-1/2/3 Sensitivity (chỉ chạy nếu recall < 95%)                  │
└────────────────────────────────────────────────────────────────────┘

Tổng: 12 truy vấn chính + 10 GS sub + 4 phương pháp bổ sung = 22 numbered queries
```

---

# §3. KHỐI BỘ LỌC CHUẨN (Standard Filter Block)

> Khối bộ lọc chuẩn áp đồng nhất cho mọi truy vấn trong cùng cơ sở dữ liệu — đảm bảo tính tái lập (PRISMA-S Item 8) + giảm nhiễu hệ thống.

## 3.1 Khối bộ lọc Scopus (áp cho Q1–Q10)

```
AND PUBYEAR > 2014 AND PUBYEAR < 2027
AND LANGUAGE ( english )
AND DOCTYPE ( ar OR cp OR re )

AND NOT TITLE-ABS-KEY (
  "airport*" OR "heliport" OR "serial port" OR "I/O port" OR "USB port"
  OR "network port" OR "ethernet" OR "transport layer" OR "COM port"
  OR "port number" OR "wine port" OR "docker" OR "kubernetes"
  OR "port-Hamiltonian" OR "port Hamiltonian"
  OR "side-channel" OR "SMT execution port"
)

AND NOT TITLE-ABS-KEY (
  "patient*" OR "clinical" OR "cancer" OR "tumor" OR "surgery"
  OR "medical" OR "health care" OR "pharmaceutical" OR "drug"
  OR "protein" OR "cell" OR "tissue" OR "air terminal"
)

AND NOT TITLE-ABS-KEY (
  "Port Vila" OR "Port Moresby" OR "Port Said" OR "Port Harcourt"
  OR "Port-au-Prince" OR "Portsmouth" OR "Newport News"
  OR "Port Elizabeth" OR "Port Louis"
)

AND NOT TITLE-ABS-KEY (
  "bulk terminal*" OR "tanker terminal*" OR "oil terminal*" OR "LNG terminal*"
  OR "coal terminal*" OR "grain terminal*" OR "ore terminal*"
  OR "cruise terminal*" OR "ferry terminal*" OR "passenger terminal*"
  OR "roll-on roll-off" OR "Ro-Ro"
)

AND NOT TITLE-ABS-KEY (
  "port-of-entry" OR "customs clearance"
)

AND ( LIMIT-TO ( SUBJAREA , "ENGI" )
   OR LIMIT-TO ( SUBJAREA , "COMP" )
   OR LIMIT-TO ( SUBJAREA , "DECI" )
   OR LIMIT-TO ( SUBJAREA , "EART" )
   OR LIMIT-TO ( SUBJAREA , "ENER" )
   OR LIMIT-TO ( SUBJAREA , "BUSI" )
   OR LIMIT-TO ( SUBJAREA , "SOCI" ) )
```

| Khối | Mục đích |
|------|----------|
| Năm + Ngôn ngữ + Loại tài liệu | DT trong cảng xuất hiện ≈ 2017; lùi đến 2015 dự phòng |
| NOT 1 — Kỹ thuật (18 từ) | Loại "port" trong USB / mạng / CPU / port-Hamiltonian / Docker |
| NOT 2 — Y tế (13 từ) | Loại bài y tế dùng "terminal / container / operation" theo nghĩa khác |
| NOT 3 — Địa danh (9 từ) | Tên thành phố / thủ đô chứa từ "port" |
| NOT 4 — Bến không phải container (12 từ) | Bulk / tanker / RoRo / cruise / ferry / passenger |
| NOT 5 — Hải quan (2 từ) | Customs clearance / port-of-entry |
| SUBJAREA (7 ngành) | Engineering / CS / Decision Sciences / Earth / Energy / Business / Social Sciences |

## 3.2 Khối bộ lọc IEEE Xplore (áp cho Q1–Q10)

```
AND NOT ("airport" OR "airports" OR "heliport" OR "serial port" OR "I/O port"
         OR "USB port" OR "network port" OR "ethernet" OR "transport layer"
         OR "COM port" OR "port number" OR "wine port" OR "docker"
         OR "kubernetes" OR "port-Hamiltonian"
         OR "side-channel" OR "SMT execution port")

AND NOT ("patient" OR "patients" OR "clinical" OR "cancer" OR "tumor"
         OR "surgery" OR "medical" OR "health care" OR "pharmaceutical"
         OR "drug" OR "protein" OR "cell" OR "tissue" OR "air terminal")

AND NOT ("Port Vila" OR "Port Moresby" OR "Port Said" OR "Port Harcourt"
         OR "Port-au-Prince" OR "Portsmouth" OR "Newport News")

AND NOT ("bulk terminal" OR "tanker terminal" OR "oil terminal"
         OR "LNG terminal" OR "coal terminal"
         OR "cruise terminal" OR "ferry terminal" OR "passenger terminal"
         OR "roll-on roll-off" OR "Ro-Ro"
         OR "port-of-entry" OR "customs clearance")
```

**Bộ lọc giao diện IEEE Xplore:**

| Tiêu chí | Giá trị |
|----------|---------|
| Năm | 2015–2026 |
| Loại nội dung | ☑ Journals  ☑ Conferences  ☑ Early Access |
| Ngôn ngữ | English |

**Lưu ý:** IEEE Xplore không hỗ trợ ký tự thay thế `*`. Ví dụ `"digital twin*"` → `"digital twin" OR "digital twins" OR "digital twin-based"`.

---

# §4. THIẾT KẾ TRUY VẤN — 12 TRUY VẤN CHÍNH

## 4.1 Q1 — CORE NARROW: DT-driven × 12 cụm cảng đặc trưng

**Triết lý:** dùng 12 cụm từ ghép đặc trưng cảng biển (KHÔNG dùng "port" độc lập — tránh nhiễu USB/mạng). Bắt bài DT-driven research với high relevance.

**Phục vụ RQ:** RQ1 (landscape narrow) + RQ2 (Tầng × Lĩnh vực, anchor).

### Scopus

```
TITLE-ABS-KEY (
  ( "digital twin*" OR "digital shadow*" )
  AND
  ( "container terminal" OR "container port" OR "seaport"
    OR "port terminal" OR "port operation*" OR "maritime terminal"
    OR "smart port" OR "port logistics" OR "port system"
    OR "port facility" OR "port area" OR "port infrastructure" )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("digital twin" OR "digital twins" OR "digital twin-based" OR "digital shadow")
AND ("container terminal" OR "container port" OR "seaport"
     OR "port terminal" OR "port operations" OR "port operation"
     OR "maritime terminal" OR "smart port" OR "port logistics"
     OR "port system" OR "port facility" OR "port area"
     OR "port infrastructure")
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.2 Q2 — CORE EXTENDED: DT/CPS × cảng × 21 từ vận hành rộng

**Triết lý:** Q1 narrow bỏ sót bài dùng "port" độc lập + bài DT cho giám sát/bảo trì/visualization/decision-support. Q2 mở rộng:

- Khối A (DT signal): thêm `"cyber-physical"`
- Khối B (cơ sở vật chất): thêm `"crane"`, `"AGV"`, `"wharf"`
- Khối C (vận hành): 21 từ phủ các cụm ứng dụng

**Phục vụ RQ:** RQ1 (landscape broad) + RQ4a (gap analysis input pool).

### Scopus

```
TITLE-ABS-KEY (
  ( "digital twin*" OR "digital shadow*" OR "cyber-physical" )
  AND
  ( "port" OR "terminal" OR "container" OR "maritime" OR "seaport"
    OR "crane" OR "AGV" OR "automated guided vehicle" OR "wharf" )
  AND
  ( operation* OR logistics OR management OR scheduling
    OR optimization OR simulation
    OR monitoring OR maintenance OR visualization OR visualisation
    OR safety OR security OR decision OR dispatching OR routing
    OR allocation OR planning OR infrastructure OR "path planning"
    OR digitali* OR roadmap OR rescheduling )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("digital twin" OR "digital shadow" OR "cyber-physical")
AND ("port" OR "terminal" OR "container" OR "maritime" OR "seaport"
     OR "crane" OR "AGV" OR "wharf")
AND (operation OR logistics OR management OR scheduling OR optimi*
     OR simulation OR planning OR allocation OR dispatching OR routing
     OR monitoring OR maintenance OR decision OR rescheduling
     OR "path planning" OR berth OR "yard crane" OR "quay crane")
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.3 Q3 — T-L1: Khả kiến dữ liệu (Data Visibility)

**Phục vụ RQ:** RQ2a (L1 row), RQ3a (method ↔ tầng L1).

### Scopus

```
TITLE-ABS-KEY (
  ( "smart port" OR "port digitali*" OR "port monitoring"
    OR "port IoT" OR "intelligent port"
    OR "real-time monitoring" OR "sensor network" OR "dashboard" )
  AND ( "container" OR "terminal" OR "seaport" )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("smart port" OR "port digitalization" OR "port digitalisation"
 OR "port monitoring" OR "port IoT" OR "intelligent port"
 OR "real-time monitoring" OR "sensor network" OR "dashboard")
AND ("container" OR "terminal" OR "seaport")
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.4 Q4 — T-L2: Trạng thái vận hành (Operational State) → Paper 1

**Phục vụ RQ:** RQ2a (L2 row), RQ3a (method ↔ tầng L2).

### Scopus

```
TITLE-ABS-KEY (
  ( "data integration" OR "ontology" OR "process mining"
    OR "event log" OR "data model*"
    OR "operational state" OR "state estimation"
    OR "data fusion" OR "knowledge graph" )
  AND ( "container terminal" OR "port" OR "maritime logistics" )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("data integration" OR "ontology" OR "process mining"
 OR "event log" OR "data model" OR "data modeling" OR "data modelling"
 OR "operational state" OR "state estimation" OR "data fusion"
 OR "knowledge graph")
AND ("container terminal" OR "port" OR "maritime logistics")
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.5 Q5 — T-L3: Hỗ trợ quyết định (Decision Support) → Paper 2

**Phục vụ RQ:** RQ2a (L3 row, 4 lĩnh vực berth/yard/QC/AGV), RQ3a (method ↔ tầng L3), RQ4b (method × tầng gap).

### Scopus

```
TITLE-ABS-KEY (
  ( "berth allocation" OR "quay crane scheduling" OR "yard management"
    OR "yard allocation" OR "container scheduling" OR "terminal optimization"
    OR "AGV dispatching" OR "AGV scheduling" OR "AGV routing"
    OR "vehicle scheduling" OR "stack planning" OR "RMG scheduling"
    OR "RTG scheduling" )
  AND
  ( "reinforcement learning" OR "MILP" OR "metaheuristic"
    OR "deep learning" OR "hybrid optimization" OR "rolling horizon"
    OR "deep reinforcement" OR "constraint programming"
    OR "Lagrangian" OR "column generation" )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("berth allocation" OR "quay crane scheduling" OR "yard management"
 OR "yard allocation" OR "container scheduling" OR "terminal optimization"
 OR "AGV dispatching" OR "AGV scheduling" OR "AGV routing"
 OR "vehicle scheduling" OR "stack planning" OR "RMG scheduling"
 OR "RTG scheduling")
AND ("reinforcement learning" OR "MILP" OR "metaheuristic"
     OR "deep learning" OR "hybrid optimization" OR "rolling horizon"
     OR "deep reinforcement" OR "constraint programming"
     OR "Lagrangian" OR "column generation")
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.6 Q6 — T-L4: Mô phỏng và Kiểm chứng (Simulation & V&V) → Paper 3

**Phục vụ RQ:** RQ2a (L4 row), RQ3a (method ↔ tầng L4), RQ4b (sim coverage).

> Q6 gộp 2 nhánh: (A) DES + V&V; (B) 3D/4D Visualization + GIS — vì cả hai đều là cấu phần của L4 (thử nghiệm trước thực thi).

### Scopus

```
TITLE-ABS-KEY (
  (
    ( "discrete event simulation" OR "agent-based simulation"
      OR "simulation model" OR "emulation" OR "hardware-in-the-loop" )
    AND ( "container terminal" OR "port operations" OR "terminal operations" )
    AND ( "valid*" OR "verif*" OR "calibrat*" OR "what-if" )
  )
  OR
  (
    ( "digital twin*" OR "digital shadow*" )
    AND ( "visualization" OR "visualisation" OR "3D" OR "4D"
          OR "mixed reality" OR "augmented reality" OR "virtual reality" )
    AND ( "port" OR "terminal" OR "maritime" OR "seaport" OR "container" )
  )
  OR
  (
    ( "GIS" OR "geographic information" OR "spatiotemporal"
      OR "digital map" OR "spatial analysis" )
    AND ( "seaport*" OR "container terminal*" OR "port operation*"
          OR "smart port*" OR "port terminal*" )
  )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
(
  ( ("discrete event simulation" OR "agent-based simulation"
     OR "simulation model" OR "emulation" OR "hardware-in-the-loop")
    AND ("container terminal" OR "port operations" OR "terminal operations")
    AND ("validation" OR "validate" OR "verification" OR "verify"
         OR "calibration" OR "calibrate" OR "what-if") )
  OR
  ( ("digital twin" OR "digital twins" OR "digital twin-based" OR "digital shadow")
    AND ("visualization" OR "visualisation" OR "3D" OR "4D"
         OR "mixed reality" OR "augmented reality" OR "virtual reality")
    AND ("port" OR "terminal" OR "maritime" OR "seaport" OR "container") )
  OR
  ( ("GIS" OR "geographic information" OR "spatiotemporal"
     OR "digital map" OR "spatial analysis")
    AND ("seaport" OR "container terminal" OR "port operation"
         OR "port operations" OR "smart port" OR "port terminal") )
)
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.7 Q7 — T-L5: Vòng kín tự trị (Closed-Loop Autonomy)

**Phục vụ RQ:** RQ2b (tầng cao nhất L5), RQ4a (heat-map L5 row), RQ5a (priority).

### Scopus

```
TITLE-ABS-KEY (
  ( "digital twin*" OR "digital shadow*" OR "cyber-physical" )
  AND
  ( "closed-loop" OR "closed loop" OR "autonomy" OR "autonomous control"
    OR "feedback control" OR "self-adapt*" OR "self-optimi*"
    OR "self-organi*" OR "self-learning"
    OR "real-time feedback" OR "automated decision-making" )
  AND
  ( "port" OR "terminal" OR "container" OR "maritime"
    OR "seaport" OR "crane" OR "AGV" OR "wharf" )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("digital twin" OR "digital shadow" OR "cyber-physical")
AND ("closed-loop" OR "closed loop" OR "autonomy" OR "autonomous control"
     OR "feedback control" OR "self-adaptive" OR "self-adaptation"
     OR "self-optimizing" OR "self-organizing" OR "self-learning"
     OR "real-time feedback" OR "automated decision-making")
AND ("port" OR "terminal" OR "container" OR "maritime"
     OR "seaport" OR "crane" OR "AGV" OR "wharf")
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.8 Q8 — Lĩnh vực thứ 5: Gate Operations

**Triết lý:** Q5 (T-L3) đã phủ 4 lĩnh vực (berth/yard/quay crane/AGV) nhưng KHÔNG có gate. Gate là 1/5 lĩnh vực vận hành — thiếu cột gate trong heat-map RQ2a sẽ khiến phân tích lệch.

**Phục vụ RQ:** RQ2a (lĩnh vực gate — cột thứ 5 heat-map), RQ4a.

### Scopus

```
TITLE-ABS-KEY (
  ( "digital twin*" OR "digital shadow*" OR "smart"
    OR "automated" OR "intelligent" OR "IoT" OR "RFID" )
  AND
  ( "gate operation*" OR "gate system*" OR "gate scheduling"
    OR "truck appointment*" OR "truck scheduling" OR "container gate"
    OR "terminal gate" OR "gate-in" OR "gate-out"
    OR "drayage" OR "gate congestion" OR "gate throughput" )
  AND
  ( "container" OR "terminal" OR "port" OR "seaport" )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("digital twin" OR "digital shadow" OR "smart"
 OR "automated" OR "intelligent" OR "IoT" OR "RFID")
AND ("gate operation" OR "gate operations" OR "gate system" OR "gate systems"
     OR "gate scheduling" OR "truck appointment" OR "truck appointments"
     OR "truck scheduling" OR "container gate" OR "terminal gate"
     OR "gate-in" OR "gate-out" OR "drayage" OR "gate congestion"
     OR "gate throughput")
AND ("container" OR "terminal" OR "port" OR "seaport")
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.9 Q9 — Bối cảnh: Quy mô cảng + Tên cảng VN/ĐNÁ cụ thể

**Triết lý:** Q1-Q8 không bắt được bài về "small port" / "feeder port" nếu paper KHÔNG dùng "container terminal" / "seaport" trong abstract. Q9 lấp:

1. Quy mô cảng — keyword "small/medium/regional/feeder port"
2. Tên cảng VN/ĐNÁ cụ thể — case study dùng tên cảng có thể bỏ sót Q1-Q8

**Phục vụ RQ:** RQ2c (Tầng × Quy mô), RQ4c (geographic VN/ĐNÁ), RQ5b/c/d (cảng nguồn lực hạn chế).

### Scopus

```
TITLE-ABS-KEY (
  ( "digital twin*" OR "digital shadow*" OR "smart port"
    OR "cyber-physical" OR "industry 4.0" OR "IoT" )
  AND
  (
    ( "small port*" OR "medium port*" OR "medium-sized port*"
      OR "regional port*" OR "secondary port*" OR "feeder port*"
      OR "minor port*" OR "small terminal*" OR "small container terminal*" )
    OR
    ( "Cat Lai" OR "Cai Mep" OR "Hai Phong" OR "Tan Cang"
      OR "Saigon Newport" OR "Da Nang port" OR "Lach Huyen"
      OR "Quy Nhon port" OR "Vung Tau port" OR "VICT"
      OR "Laem Chabang" OR "Bangkok port" OR "Klang"
      OR "Tanjung Pelepas" OR "Singapore port"
      OR "Manila port" OR "Cebu port" OR "Batangas"
      OR "Tanjung Priok" OR "Surabaya"
      OR "Sihanoukville" OR "Yangon port" )
    OR
    ( "Vietnam*" OR "Southeast Asia*" OR "developing countr*"
      OR "emerging econom*" OR "developing port*" )
  )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("digital twin" OR "digital shadow" OR "smart port"
 OR "cyber-physical" OR "industry 4.0" OR "IoT")
AND
(("small port" OR "small ports" OR "medium port" OR "medium ports"
  OR "medium-sized port" OR "regional port" OR "regional ports"
  OR "secondary port" OR "feeder port" OR "feeder ports"
  OR "minor port" OR "small terminal" OR "small container terminal")
 OR
 ("Cat Lai" OR "Cai Mep" OR "Hai Phong" OR "Tan Cang"
  OR "Saigon Newport" OR "Da Nang port" OR "Lach Huyen"
  OR "Laem Chabang" OR "Klang" OR "Tanjung Pelepas"
  OR "Manila port" OR "Tanjung Priok" OR "Sihanoukville")
 OR
 ("Vietnam" OR "Vietnamese" OR "Southeast Asia" OR "Southeast Asian"
  OR "developing country" OR "developing countries"
  OR "emerging economy" OR "emerging economies" OR "developing port"))
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

> Tên cảng cụ thể có thể trả về nhiễu (paper kinh tế cảng / geopolitics) — Pha A `screening.py` cần regex giữ context DT/method.

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.10 Q10 — Bối cảnh: Vintage (Greenfield ↔ Brownfield)

**Triết lý:** Cảng greenfield (xây mới, ví dụ Tanger Med II, Lạch Huyện) khác hẳn cảng brownfield (retrofit cảng cũ, ví dụ Hải Phòng, Hamburg, Felixstowe) về method DT, lộ trình, thách thức triển khai. Chiều này quan trọng cho thực tiễn cảng VN/ĐNÁ — nhiều cảng đang nâng cấp (brownfield) thay vì xây mới.

**Phục vụ RQ:** RQ4d (vintage gap), RQ5b (lộ trình điều kiện hoá theo vintage).

### Scopus

```
TITLE-ABS-KEY (
  ( "digital twin*" OR "digital shadow*" OR "smart port"
    OR "industry 4.0" OR "automated terminal" )
  AND
  ( "greenfield" OR "brownfield" OR "retrofit*" OR "retrofitting"
    OR "legacy system*" OR "legacy infrastructure"
    OR "port modernization" OR "port modernisation"
    OR "port upgrade*" OR "terminal upgrade*"
    OR "incremental digitali*" OR "phased digitali*"
    OR "new terminal" OR "new container terminal"
    OR "existing terminal" OR "existing port" )
  AND
  ( "port" OR "terminal" OR "container" OR "seaport" OR "maritime" )
)
[+ STANDARD FILTER BLOCK §3.1]
```

### IEEE Xplore

```
("digital twin" OR "digital shadow" OR "smart port"
 OR "industry 4.0" OR "automated terminal")
AND ("greenfield" OR "brownfield" OR "retrofit" OR "retrofitting"
     OR "legacy system" OR "legacy systems" OR "legacy infrastructure"
     OR "port modernization" OR "port modernisation"
     OR "port upgrade" OR "terminal upgrade"
     OR "incremental digitalization" OR "phased digitalization"
     OR "new container terminal" OR "existing terminal"
     OR "existing port")
AND ("port" OR "terminal" OR "container" OR "seaport" OR "maritime")
[+ IEEE STANDARD FILTER BLOCK §3.2]
```

- [ ] Scopus — chưa chạy
- [ ] IEEE Xplore — chưa chạy

---

## 4.11 Q11 — Springer Link (bổ trợ, 12 tháng)

**Vai trò:** giảm độ trễ lập chỉ mục Scopus với eBooks và journals đặc thù (FSMJ, WMU JMA, Maritime Economics & Logistics).
**Khoảng:** 12 tháng gần nhất tính từ ngày chạy.
**Triết lý:** ưu tiên độ thu hồi (recall-first) — không thắt cụm từ ghép, dùng filter giao diện.

```text
Springer Link Advanced Search:
  Truy vấn:    "digital twin" AND (port OR terminal OR maritime OR seaport OR container)
  Loại nội dung: ☑ Article  ☑ Chapter  (KHÔNG chọn Conference Paper, Reference Work)
  Khoảng:      12 tháng gần nhất
  Ngôn ngữ:    English
  Sắp xếp:     Newest first

  Discipline TÍCH (10): Engineering, Computer Science, Business & Management,
    Multidisciplinary SHS, Environment, Energy, Earth Sciences, Economics,
    Geography, Social Sciences
  Discipline KHÔNG (6): Materials Science, Chemistry, Medicine & Public Health,
    Physics, Life Sciences, Biomedicine
```

- [ ] Springer Link — chưa chạy

---

## 4.12 Q12 — Taylor & Francis Online (bổ trợ, 6 tháng)

**Vai trò:** bắt Online First trên T&F chưa indexed Scopus, đặc biệt 2 tạp chí Q1 target (Maritime Policy & Management, IJPR).
**Khoảng:** 6 tháng gần nhất.

```text
Taylor & Francis Advanced Search:
  Truy vấn:     "digital twin" AND (port OR terminal OR maritime OR seaport OR container)
  Loại bài:     ☑ Research Article  ☑ Review Article
  Khoảng:       6 tháng gần nhất
  Ngôn ngữ:     English
  Sắp xếp:      Publication date (newest)
```

> **⚠ T&F Online KHÔNG hỗ trợ filter loại trừ Subject ở tầng truy vấn** — toàn bộ exclusion theo lĩnh vực chuyển sang Pha A (Python pre-screen `screening.py` + module `tf_journal_exclusion.py`) và Pha B (Rayyan).

### Danh sách loại trừ T&F-specific (sẽ code trong `tf_journal_exclusion.py`):

| Nhóm loại trừ | Tạp chí điển hình | EC mapping |
|----------------|---------------------|--------------|
| Built Environment / Construction | International Journal of Construction Management, Journal of Asian Architecture and Building Engineering | EC-STRUCT |
| Nondestructive Testing | Nondestructive Testing and Evaluation | EC-STRUCT |
| Civil/Structural | Structure and Infrastructure Engineering | EC-STRUCT |
| Nuclear | Nuclear Technology | EC-NOSCOPE |
| HCI / UI–UX | International Journal of Human–Computer Interaction | EC-NOSCOPE |
| Manufacturing / Engineering Design | International Journal of Computer Integrated Manufacturing, Journal of Engineering Design, Production & Manufacturing Research, Virtual and Physical Prototyping | EC7-mfg |
| Y/sinh (theo PB) | Cogent OA, Dove Medical Press | EC7-health |

### Whitelist target — luôn cho Rayyan đọc:

- International Journal of Production Research — **Q1 target Paper 2**
- Digital Twin — chuyên ngành DT
- International Journal of Logistics Research and Applications
- Maritime Policy & Management — **Q1 target SR**
- International Journal of Sustainable Transportation

- [ ] Taylor & Francis — chưa chạy

---

## 4.13–4.22 Q13–Q22 — Google Scholar (10 sub-queries)

**Vai trò:** bổ sung — bắt grey literature, proceedings chưa indexed, preprints (ArXiv / SSRN), early-access.
**Operator loại trừ chung cho mỗi truy vấn:** `-"port Hamiltonian" -"Port Vila" -"bulk terminal" -"Ro-Ro" -"customs clearance"`

| Mã | Truy vấn | Giới hạn |
|----|----------|----------|
| Q13 (GS-1) | `"digital twin" "container terminal" scheduling optimization` | 100 |
| Q14 (GS-2) | `"digital twin" "port operations" simulation management` | 100 |
| Q15 (GS-3) | `"digital twin" "seaport" logistics optimization` | 100 |
| Q16 (GS-4) | `"digital shadow" port terminal simulation` | 50 |
| Q17 (GS-5) | `"cyber-physical" port maritime operations management` | 50 |
| Q18 (GS-6) | `"digital twin" "automated container terminal" AGV scheduling` | 50 |
| Q19 (GS-7) | `"digital twin" maritime logistics management review` | 50 |
| Q20 (GS-8) | `"digital twin" maritime domain review trends` | 50 |
| Q21 (GS-9) | `"digital twin" AGV dispatching routing "container terminal"` | 50 |
| Q22 (GS-10) | `"smart port" "industry 4.0" framework architecture` | 50 |

**Kỳ vọng tổng:** ≈ 650 records (sau dedup với Scopus/IEEE còn 200–350 unique mới).

- [ ] Q13–Q22 — chưa chạy

---

# §5. PHƯƠNG PHÁP BỔ SUNG

## 5.1 Snowball — 6 hạt giống (lùi và tiến)

### Hạt giống tổng quan (Review Seeds)

- **S1 — Neugebauer, Heilig, Voß (2024)** *"Digital Twins in the Context of Seaports and Terminal Facilities"* — FSMJ (Q2), 174 tham chiếu
- **S2 — Homayouni, Pinho de Sousa, Marques (2025)** *"Unlocking the potential of digital twins to achieve sustainability in seaports"* — WMU JMA, 129 tham chiếu
- **S3 — Çolak, Heilig, Voß (2025)** *"Reinforcement learning in the context of container terminals"* — FSMJ Q2, 104 tham chiếu
- **S4 — Madusanka, Fan, Yang, Xiang (2023)** *"Digital Twin in the Maritime Domain: A Review and Emerging Trends"* — JMSE, 134 tham chiếu

### Hạt giống neo (Anchor Seeds)

- **S5 — Yang, Liu, Xin, Chen, Wang (2024)** *"Towards intuitive visualisation goals for the operation optimisation of automated container terminal based on digital twin technology"* — Maritime Policy & Management (Q1), 46 tham chiếu
- **S6 — (2026)** *"Decision-support systems in container terminal automation: a systematic review of digital twin-expert system integration"* — Australian Journal of Maritime & Ocean Affairs, 59 tham chiếu

### Quy trình

| Hướng | Phương pháp | Output |
|-------|-------------|----------|
| **Lùi (backward)** | Rà references của 6 hạt giống → khử trùng lặp với pool đã có → đánh giá tóm tắt theo IC/EC | `snowball_backward_v5.6.csv` |
| **Tiến (forward)** | "Cited by" Google Scholar cho S1, S2, S4, S5 (S3, S6 quá mới) | `snowball_forward_v5.6.csv` |

## 5.2 Hand search — 10 tạp chí trọng điểm (2024–2026)

| # | Tạp chí | Nhà xuất bản |
|---|---------|---------------|
| 1 | Journal of Marine Science and Engineering | MDPI |
| 2 | Maritime Economics & Logistics | Springer |
| 3 | **Maritime Policy & Management** *(Q1 target SR)* | Taylor & Francis |
| 4 | Flexible Services & Manufacturing Journal | Springer |
| 5 | Transportation Research Part D / E | Elsevier |
| 6 | WMU Journal of Maritime Affairs | Springer |
| 7 | **International Journal of Production Research** *(Q1 target Paper 2)* | Taylor & Francis |
| 8 | IEEE Transactions on Industrial Informatics | IEEE |
| 9 | Advanced Engineering Informatics | Elsevier |
| 10 | Computers & Operations Research | Elsevier |

**Thực hiện:** rà mục lục từng tạp chí giai đoạn 2024–2026 trước Bước 22 (Submit). Output: `hand_search_v5.6.csv`.

## 5.3 Recall validation — 78 hạt giống độc lập (Bước 15.1)

**Mục đích:** đo độ thu hồi (recall = số seed có trong pool / 78) làm bằng chứng cho Item 13f (Sensitivity) + Item 23c (Limitations).

**Ngưỡng quyết định:**

| Recall | Hành động |
|---------|------------|
| ≥ 95% | Giữ nguyên thiết kế |
| 80–95% | Kích hoạt SA-1, SA-2, SA-3 (§6) |
| < 80% | Recovery — tái thiết kế truy vấn |

Danh sách 78 seeds lưu trong `graph_net.md` mục "Seed list cho recall validation".

---

# §6. SENSITIVITY ANALYSIS — 3 truy vấn dự phòng (chỉ chạy khi recall < 95%)

> PRISMA 2020 Item 13f. Bài SR là typology định tính, không có effect estimates → không áp được sensitivity theo nghĩa meta-analysis. Sensitivity ở đây = test recall stability.

| Mã | Logic | Tình huống kích hoạt |
|----|-------|----------------------|
| **SA-1** | DT + scheduling/AGV/crane + (terminal OR yard OR warehouse OR shipyard OR manufacturing) — bắt bài chuyển từ chế tạo | Seeds DT-mfg-transferable bị bỏ sót |
| **SA-2** | (cyber-physical) AND (seaport / container terminal / port operation / maritime port / smart port) | Seeds CPS-port bị bỏ sót |
| **SA-3** | simulation NEAR/3 "port" AND (real-time / IoT / sensor / data-driven / 3D model / virtual / mirror) | Seeds sim-only DT bị bỏ sót |

Cú pháp Scopus đầy đủ lưu trong `graph_net.md` mục "Truy vấn phân tích độ nhạy".

---

# §7. PRISMA 2020 FLOW DIAGRAM — TEMPLATE (cập nhật ở Bước 10)

```text
╔════════════════════════════════════════════════════════════════╗
║                       IDENTIFICATION                           ║
╠════════════════════════════════════════════════════════════════╣
║  Records from databases (n = ____)                             ║
║    Scopus Q1–Q10                              = ____           ║
║    IEEE Xplore Q1–Q10                         = ____           ║
║    Google Scholar Q13–Q22                     = ____           ║
║    Springer Link Q11 (12 tháng)               = ____           ║
║    Taylor & Francis Q12 (6 tháng)             = ____           ║
║                                                                 ║
║  Records from other methods (n = ____)                         ║
║    Snowball backward + forward (6 seeds)                       ║
║    Hand search (10 tạp chí, 2024–2026)                         ║
║                                                                 ║
║  Duplicates removed (n = ____)  — Python 3-layer pipeline     ║
╠════════════════════════════════════════════════════════════════╣
║                       SCREENING                                ║
║  Records screened (n = ____)                                   ║
║  Pha A Python pre-screen → 3 nhãn (INCLUDE/REVIEW/EXCLUDE)    ║
║  Pha B Rayyan formal screen → Excluded (n = ____)             ║
║    EC1, EC2, EC3, EC4, EC5, EC7-{mfg/bim/health/noctx/other}, ║
║    EC8, EC9, EC-CYBER, EC-ENERGY, EC-GENERIC, EC-IT,           ║
║    EC-NOSCOPE, EC-PAX, EC-STRUCT                                ║
╠════════════════════════════════════════════════════════════════╣
║                       ELIGIBILITY (FULLTEXT)                   ║
║  Reports sought for retrieval (n = ____)                       ║
║  Reports not retrieved        (n = ____) — EC6                 ║
║  Reports assessed for eligibility (n = ____)                   ║
║  Reports excluded (n = ____):                                  ║
║    EC-ENV, EC-VESSEL, EC-POLICY, EC-SECUR,                     ║
║    EC-BLOCK, EC-TELECOM, EC-CUSTOMS, EC-AGRI                   ║
╠════════════════════════════════════════════════════════════════╣
║                       INCLUDED                                 ║
║  Studies included in review (n = ____) — kỳ vọng 80–150       ║
║  Reports of included studies (n = ____)                        ║
╚════════════════════════════════════════════════════════════════╝
```

---

# §8. PRESS PEER REVIEW CHECKLIST (McGowan et al. 2016)

> **Yêu cầu Q1:** chiến lược tìm kiếm phải qua peer-review theo PRESS trước khi chạy. Bảng dưới hoàn thành tại Bước 2.5.

| # | Tiêu chí PRESS | Trạng thái | Ghi chú |
|---|------------------|-------------|----------|
| 1 | Translation of question into search concepts | ⬜ | RQ doc §IV ↔ §1.5 mapping ↔ §4 truy vấn |
| 2 | Boolean and proximity operators | ⬜ | AND / OR / AND NOT / NEAR/3 |
| 3 | Subject headings | ⬜ | SUBJAREA Scopus (7 ngành) |
| 4 | Text word searching | ⬜ | TITLE-ABS-KEY trong Q1–Q10 Scopus |
| 5 | Spelling, syntax, line numbers | ⬜ | Cú pháp Scopus / IEEE đã verify; `*` mở rộng thủ công cho IEEE |
| 6 | Limits and filters | ⬜ | §3.1 (Scopus 7 khối) + §3.2 (IEEE 4 khối) |
| 7 | Adapted for each database | ⬜ | 5 cơ sở dữ liệu × cú pháp riêng |
| 8 | Reproducibility | ⬜ | Toàn bộ chuỗi truy vấn nguyên văn trong file này |

**Người review:** NCS HoaTX (self-review trước Bước 4) + Supervisor + Expert thư viện (Bước 21 — Expert Validation).

---

# §9. TRẠNG THÁI TÌM KIẾM (cập nhật theo từng lượt chạy)

| # | Truy vấn | Cơ sở dữ liệu | Bản ghi | Trạng thái | Ngày chạy |
|---|---------|----------------|---------:|-------------|--------------|
| 1 | Q1 CORE NARROW | Scopus | 130 | ✅ `PRIMARY_Scopus.ris` | 2026-05-10 |
| 2 | Q1 CORE NARROW | IEEE Xplore | 50 | ✅ `PRIMARY_IEEE.ris` | 2026-05-10 |
| 3 | Q2 CORE EXTENDED | Scopus | 1518 | ✅ `EXTENDED_Scopus.ris` | 2026-05-10 |
| 4 | Q2 CORE EXTENDED | IEEE Xplore | 1118 | ✅ `EXTENDED_IEEE.ris` | 2026-05-10 |
| 5 | Q3 T-L1 | Scopus | 180 | ✅ `T1_Scopus.ris` | 2026-05-10 |
| 6 | Q3 T-L1 | IEEE Xplore | 53 | ✅ `T1_IEEE.ris` | 2026-05-10 |
| 7 | Q4 T-L2 | Scopus | 246 | ✅ `T2_Scopus.ris` | 2026-05-10 |
| 8 | Q4 T-L2 | IEEE Xplore | 154 | ✅ `T2_IEEE.ris` | 2026-05-10 |
| 9 | Q5 T-L3 | Scopus | 422 | ✅ `T3_Scopus.ris` | 2026-05-10 |
| 10 | Q5 T-L3 | IEEE Xplore | 135 | ✅ `T3_IEEE.ris` | 2026-05-10 |
| 11 | Q6 T-L4 | Scopus | 54 | ✅ `T4_Scopus.ris` | 2026-05-10 |
| 12 | Q6 T-L4 | IEEE Xplore | 10 | ✅ `T4_IEEE.ris` | 2026-05-10 |
| 13 | Q7 T-L5 | Scopus | 34 | ✅ `T5_Scopus.ris` | 2026-05-10 |
| 14 | Q7 T-L5 | IEEE Xplore | 54 | ✅ `T5_IEEE.ris` | 2026-05-10 |
| 15 | Q8 Gate | Scopus | 345 | ✅ `T6_Scopus.ris` | 2026-05-10 |
| 16 | Q8 Gate | IEEE Xplore | 110 | ✅ `T6_IEEE.ris` | 2026-05-10 |
| 17 | Q9 Quy mô + VN/ĐNÁ | Scopus | 483 | ✅ `T7_Scopus.ris` | 2026-05-10 |
| 18 | Q9 Quy mô + VN/ĐNÁ | IEEE Xplore | 246 | ✅ `T7_IEEE.ris` | 2026-05-10 |
| 19 | Q10 Vintage | Scopus | 9 | ✅ `T8_Scopus.ris` (PoP export) | 2026-05-15 |
| 20 | Q10 Vintage | IEEE Xplore | 13 | ✅ `T8_IEEE.ris` (CSV→RIS convert) | 2026-05-15 |
| 21 | Q11 Springer (12 tháng) | Springer Link | 905 | ✅ `SPRINGER.ris` | 2026-05-10 |
| 22 | Q12 T&F (6 tháng) | Taylor & Francis | 928 | ✅ `TF.ris` | 2026-05-10 |
| 23–32 | Q13–Q22 GS-1 → GS-10 | Google Scholar | 650 | ✅ `GS.ris` (gộp 10 sub) | 2026-05-10 |
|   | **Tổng 23 files (Q1–Q12, GS)** | | **7.847** | **✅ Dedup → 5.822 unique** | **2026-05-15** |
| 33 | SA-1 | Scopus | – | ⬜ Hoãn (chỉ nếu recall < 95%) | – |
| 34 | SA-2 | Scopus | – | ⬜ Hoãn | – |
| 35 | SA-3 | Scopus | – | ⬜ Hoãn | – |
|   | Snowball (6 seeds) | – | – | ⬜ Sau Bước 9 | – |
|   | Hand search (10 tạp chí) | – | – | ⬜ Trước Submit | – |

**Ghi chú Q-code → Filename mapping (DEV-002):**
WorkPlan quy ước tên Q1_Scopus.ris — tên thực tế dùng mô tả nội dung (PRIMARY/EXTENDED/T1…T7). Xem DEV-002 trong `SR_Deviation_Log_v5.6.md`.

**Ghi chú phân trang IEEE Xplore:** giới hạn ≈ 100 records/trang xuất → nếu một query trả về > 100 phải xuất theo trang `Q*_IEEE_P1.ris`, `Q*_IEEE_P2.ris`, …

---

# §10. LIÊN KẾT NỘI BỘ

| File | Vai trò |
|------|---------|
| `SR_Research_Questions_v5.6.md` v1.0 | Single Source of Truth cho RQ — Strategy reference §1.3 + §1.5 |
| `WorkPlan_v5.6_FINAL.md` | Bước 4–6 thực thi tìm kiếm; Bước 15 sensitivity; Bước 16 bibliometric |
| `SR_Eligibility_Criteria_v5.6.md` | 28 mã EC/IC + 6 borderline rules + T&F whitelist |
| `SR_Screening_Protocol_v5.6.md` | Pha A Python `screening.py` + Pha B Rayyan |
| `SR_PRISMA_Checklist_v5.6.md` | Items 6, 7, 8, 13c, 13f, 16a, 23c, 24a–c |
| `tf_journal_exclusion.py` | Module exclusion T&F (Bước 8.1) |
| `screening.py` | Pha A pre-screen (Bước 8.1) |
| `dedup.py` | Khử trùng lặp 3 lớp (Bước 7) |
| `graph_net.md` | Đồ thị tri thức trung tâm |

---

# §11. VERSIONING

| Version | Ngày | Thay đổi | Phê duyệt |
|---------|------|-----------|-------------|
| **v1.0** | 2026-05-08 | Chiến lược tìm kiếm thiết kế đầu tiên — 12 truy vấn chính (Q1-Q12) thiết kế chặt theo 5 nguyên tắc §1.2 + 10 GS sub (Q13-Q22) + Snowball + Hand search + Recall validation. Bộ truy vấn phủ đủ 5 chiều: 5 Tầng (Q1-Q7), 5 Lĩnh vực (Q5+Q8), Quy mô (Q9), Vintage (Q10), Geographic (Q9). PRESS 8 tiêu chí self-review. | NCS HoaTX (chờ phê duyệt) |

---

*SR_Search_Strategy_v5.6_FINAL.md — v1.0 — 2026-05-08 — anchored on RQ_v1.0 (`SR_Research_Questions_v5.6.md`) + PRISMA 2020 + PRISMA-S + PRESS + Kitchenham 2007*
