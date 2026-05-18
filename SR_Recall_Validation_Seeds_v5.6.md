# RECALL VALIDATION SEED LIST — 78 Seeds
# Digital Twin cho Vận hành Cảng Container

**File:** SR_Recall_Validation_Seeds_v5.6.md
**Phiên bản:** v1.0 — 2026-05-15
**NCS:** HoaTX
**Dùng tại:** Bước 15.1 (Sensitivity Analysis)
**Anchor:** `SR_Search_Strategy_v5.6_FINAL.md` §6

> **Mục tiêu:** Xác minh rằng pool 5.822 records đã bắt được ≥ 95% papers "known to be relevant". Nếu recall < 80% → Recovery R5.
>
> **Cách dùng:** (1) So khớp từng seed với `dedup_unique.ris` qua DOI/title. (2) Tính recall = (seeds found in pool) / 78. (3) Nếu seed KHÔNG có → phân tích tại sao (query gap, year out of range, nguồn không phủ, etc.).

---

## §1. PHƯƠNG PHÁP CHỌN SEEDS

Seeds được chọn theo 6 tiêu chí để cover đủ 5 RQ:

| Tiêu chí | Seeds mục tiêu | Lý do |
|----------|---------------|--------|
| S1: DT + Container port (core) | 20 | Cover RQ1, RQ2 |
| S2: Maturity tiers L1–L5 đặc trưng | 15 | Cover RQ2 per-tier |
| S3: Method (DES, RL, MILP, IoT, AGV) | 15 | Cover RQ3 |
| S4: Geographic (VN, ĐNÁ, châu Á) | 10 | Cover RQ4c |
| S5: Vintage / port modernization | 8 | Cover RQ4d |
| S6: Survey/review paper về DT maritime | 10 | Overlap test |
| **Tổng** | **78** | |

---

## §2. DANH SÁCH SEEDS

> **Ghi chú:** Cột `In Pool?` và `Notes` để NCS điền sau khi so khớp với dedup_unique.ris.
> Các papers dưới đây là tổng hợp từ domain knowledge — NCS cần verify DOI và bổ sung papers đã đọc trong nghiên cứu riêng.

### S1 — DT + Container Port / Terminal (Core)

| # | Authors | Year | Title (rút gọn) | DOI / Identifier | In Pool? | Notes |
|---|---------|------|-----------------|-----------------|----------|-------|
| S1-01 | Binti Che Ibrahim et al. | 2022 | Digital twin framework for container terminal | — | ⬜ | NCS verify DOI |
| S1-02 | Lu et al. | 2023 | Digital twin-driven port operations | — | ⬜ | NCS verify DOI |
| S1-03 | Zhen et al. | 2022 | Autonomous operations in container terminal | — | ⬜ | NCS verify |
| S1-04 | Boschert & Rosen | 2016 | Digital Twin—The Simulation Aspect | 10.1007/978-3-319-32156-1_5 | ⬜ | Foundational DT paper |
| S1-05 | Grieves | 2014 | Digital twin: manufacturing excellence | — | ⬜ | DT concept origin |
| S1-06 | Tao et al. | 2018 | Digital Twin in Industry: State-of-the-Art | 10.1109/TII.2018.2873186 | ⬜ | Core DT paper |
| S1-07 | Jones et al. | 2020 | Characterising the Digital Twin: A systematic literature review | 10.1016/j.cirpj.2020.02.002 | ⬜ | DT definition |
| S1-08 | Lim et al. | 2020 | A state-of-the-art survey of Digital Twin | 10.1016/j.jmsy.2020.06.011 | ⬜ | DT survey |
| S1-09 | Raza et al. | 2022 | Digital twins for port logistics | — | ⬜ | NCS verify |
| S1-10 | Nguyen et al. | 2023 | Digital twin application in seaport | — | ⬜ | VN/maritime focus |
| S1-11 | Bottani et al. | 2022 | Digital twin smart manufacturing | — | ⬜ | Manufacturing → port transfer |
| S1-12 | Dworschak & Jovane | 2021 | Smart port digital twin | — | ⬜ | NCS add known papers |
| S1-13 | (NCS to add) | | | | ⬜ | |
| S1-14 | (NCS to add) | | | | ⬜ | |
| S1-15 | (NCS to add) | | | | ⬜ | |
| S1-16 | (NCS to add) | | | | ⬜ | |
| S1-17 | (NCS to add) | | | | ⬜ | |
| S1-18 | (NCS to add) | | | | ⬜ | |
| S1-19 | (NCS to add) | | | | ⬜ | |
| S1-20 | (NCS to add) | | | | ⬜ | |

### S2 — Maturity Tiers L1–L5 Đặc trưng

| # | Authors | Year | Title (rút gọn) | DOI / Identifier | Tier | In Pool? | Notes |
|---|---------|------|-----------------|-----------------|------|----------|-------|
| S2-01 | (NCS: L1 paper — IoT/sensor port) | | | | L1 | ⬜ | |
| S2-02 | (NCS: L1 paper — dashboard/monitoring) | | | | L1 | ⬜ | |
| S2-03 | (NCS: L1 paper — real-time data port) | | | | L1 | ⬜ | |
| S2-04 | (NCS: L2 paper — ontology port) | | | | L2 | ⬜ | |
| S2-05 | (NCS: L2 paper — digital state model) | | | | L2 | ⬜ | |
| S2-06 | (NCS: L2 paper — data integration) | | | | L2 | ⬜ | |
| S2-07 | (NCS: L3 paper — optimization port RL) | | | | L3 | ⬜ | |
| S2-08 | (NCS: L3 paper — MILP terminal) | | | | L3 | ⬜ | |
| S2-09 | (NCS: L3 paper — decision support DT) | | | | L3 | ⬜ | |
| S2-10 | (NCS: L4 paper — DES port simulation) | | | | L4 | ⬜ | |
| S2-11 | (NCS: L4 paper — 3D/4D visualization) | | | | L4 | ⬜ | |
| S2-12 | (NCS: L4 paper — what-if analysis port) | | | | L4 | ⬜ | |
| S2-13 | (NCS: L5 paper — closed-loop port) | | | | L5 | ⬜ | Rare — may not exist |
| S2-14 | (NCS: L5 paper — autonomous terminal) | | | | L5 | ⬜ | |
| S2-15 | (NCS: L4/L5 paper — AGV closed-loop) | | | | L4/L5 | ⬜ | |

### S3 — Method: DES / RL / MILP / IoT / AGV / Crane

| # | Authors | Year | Title (rút gọn) | DOI | Method | In Pool? | Notes |
|---|---------|------|-----------------|-----|--------|----------|-------|
| S3-01 | (NCS: DES port simulation) | | | | DES | ⬜ | |
| S3-02 | (NCS: RL crane/berth) | | | | RL | ⬜ | |
| S3-03 | (NCS: MILP berth allocation) | | | | MILP | ⬜ | |
| S3-04 | (NCS: IoT container terminal) | | | | IoT | ⬜ | |
| S3-05 | (NCS: AGV path planning DT) | | | | AGV | ⬜ | |
| S3-06 | (NCS: crane scheduling DT) | | | | Crane | ⬜ | |
| S3-07 | (NCS: hybrid MILP-RL) | | | | Hybrid | ⬜ | |
| S3-08 | (NCS: federated DT) | | | | Federated | ⬜ | |
| S3-09 | (NCS: agent-based simulation port) | | | | Agent | ⬜ | |
| S3-10 | (NCS: data-driven DT port) | | | | ML/DL | ⬜ | |
| S3-11 | (NCS: OPC-UA/MQTT port integration) | | | | IIoT | ⬜ | |
| S3-12 | (NCS: gate automation DT) | | | | Gate | ⬜ | |
| S3-13 | (NCS: yard planning DT) | | | | Yard | ⬜ | |
| S3-14 | (NCS: berth planning DT) | | | | Berth | ⬜ | |
| S3-15 | (NCS: predictive maintenance port) | | | | Predictive | ⬜ | |

### S4 — Geographic: VN / ĐNÁ / Châu Á Cảng Nhỏ-Vừa

| # | Authors | Year | Title (rút gọn) | DOI | Country | In Pool? | Notes |
|---|---------|------|-----------------|-----|---------|----------|-------|
| S4-01 | (NCS: Hai Phong port DT/automation) | | | | VN | ⬜ | |
| S4-02 | (NCS: Cai Mep terminal DT) | | | | VN | ⬜ | |
| S4-03 | (NCS: Singapore PSA DT) | | | | SGP | ⬜ | |
| S4-04 | (NCS: Port Klang Malaysia DT) | | | | MYS | ⬜ | |
| S4-05 | (NCS: Laem Chabang Thailand DT) | | | | THA | ⬜ | |
| S4-06 | (NCS: Jakarta Indonesia terminal DT) | | | | IDN | ⬜ | |
| S4-07 | (NCS: ASEAN port digitalization) | | | | ĐNÁ | ⬜ | |
| S4-08 | (NCS: developing country port DT) | | | | General | ⬜ | |
| S4-09 | (NCS: small/medium port smart) | | | | General | ⬜ | |
| S4-10 | (NCS: port digitalization roadmap Asia) | | | | Asia | ⬜ | |

### S5 — Vintage: Greenfield / Brownfield / Port Modernization

| # | Authors | Year | Title (rút gọn) | DOI | Vintage | In Pool? | Notes |
|---|---------|------|-----------------|-----|---------|----------|-------|
| S5-01 | (NCS: greenfield terminal DT) | | | | Greenfield | ⬜ | |
| S5-02 | (NCS: brownfield port retrofit DT) | | | | Brownfield | ⬜ | |
| S5-03 | (NCS: legacy system integration port) | | | | Legacy | ⬜ | |
| S5-04 | (NCS: port modernization DT roadmap) | | | | Moderni. | ⬜ | |
| S5-05 | (NCS: Tanger Med greenfield DT) | | | | Greenfield | ⬜ | |
| S5-06 | (NCS: Hamburg brownfield DT) | | | | Brownfield | ⬜ | |
| S5-07 | (NCS: incremental digitalization port) | | | | Phased | ⬜ | |
| S5-08 | (NCS: port upgrade digital twin) | | | | Upgrade | ⬜ | |

### S6 — Survey / Review Papers về DT Maritime / Port

| # | Authors | Year | Title (rút gọn) | DOI | In Pool? | Notes |
|---|---------|------|-----------------|-----|----------|-------|
| S6-01 | (NCS: SR on DT in ports) | | | | ⬜ | Competing SR — phải in pool để evaluate overlap |
| S6-02 | (NCS: review DT maritime shipping) | | | | ⬜ | |
| S6-03 | (NCS: survey Industry 4.0 port) | | | | ⬜ | |
| S6-04 | (NCS: systematic review smart port) | | | | ⬜ | |
| S6-05 | (NCS: bibliometric DT logistics) | | | | ⬜ | |
| S6-06 | Fuller et al. | 2020 | Digital twin: Enabling technologies, challenges and open research | 10.1109/ACCESS.2020.2998358 | ⬜ | General DT survey |
| S6-07 | Grieves & Vickers | 2017 | Digital Twin: Mitigating Unpredictable Emergent Behavior | 10.1007/978-3-319-38756-7_4 | ⬜ | Foundational |
| S6-08 | (NCS: add known survey paper 1) | | | | ⬜ | |
| S6-09 | (NCS: add known survey paper 2) | | | | ⬜ | |
| S6-10 | (NCS: add known survey paper 3) | | | | ⬜ | |

---

## §3. HƯỚNG DẪN SO KHỚP

### Bước thực hiện (Bước 15.1.3):

```python
# Script so khớp seeds với pool — chạy sau khi điền DOI đầy đủ
# File: recall_validation.py (tạo khi cần)

import pandas as pd

# Load pool
pool = pd.read_csv('dedup_unique_records.csv')

# Load seeds (sau khi NCS điền DOI vào §2)
seeds_doi = [s for s in seed_dois if s]  # list DOIs từ §2

# Match by DOI
found = pool['doi'].str.lower().isin([d.lower() for d in seeds_doi])
recall_doi = found.sum() / len(seeds_doi)

# Match by fuzzy title (cho seeds không có DOI)
from rapidfuzz import fuzz
# ... fuzzy match title

print(f"Recall (DOI): {recall_doi:.1%}")
print(f"Seeds found: {found.sum()}/{len(seeds_doi)}")
```

### Ngưỡng hành động:

| Recall | Hành động |
|--------|-----------|
| ≥ 95% | ✅ Pool đủ — tiếp tục Pha B |
| 80–94% | ⚠️ Chạy SA-1, SA-2, SA-3 (Strategy §6) → merge vào pool → tái dedup |
| < 80% | ❌ Recovery R5 — tái thiết kế truy vấn |

---

## §4. KẾT QUẢ (điền sau khi so khớp)

| Chỉ số | Giá trị |
|--------|---------|
| Seeds có DOI | TBD |
| Seeds không có DOI (dùng fuzzy title) | TBD |
| Seeds tìm thấy trong pool | TBD |
| Seeds không tìm thấy | TBD |
| **Recall** | **TBD** |
| Hành động | TBD |

### Seeds không tìm thấy — phân tích lý do:

| Seed # | Title | Lý do không trong pool | SA trigger? |
|--------|-------|----------------------|------------|
| — | — | — | — |

---

## §5. HƯỚNG DẪN NCS ĐIỀN SEEDS

> NCS cần điền tối thiểu **50 seeds có DOI cụ thể** để recall validation có ý nghĩa thống kê. Các ô "(NCS to add)" là placeholder — hãy điền từ:
> 1. Reference lists của bài NCS đã đọc trong PhD research
> 2. Papers từ Supervisor/Expert recommendations
> 3. Papers từ snowball backward của S1-01 đến S1-08
> 4. Papers từ các SR cạnh tranh (competing reviews) đã tìm được

---

## §6. LIÊN KẾT

| File | Quan hệ |
|------|---------|
| `SR_Search_Strategy_v5.6_FINAL.md` §6 | SA-1/2/3 triggers |
| `dedup_unique_records.csv` | Pool để so khớp |
| `WorkPlan_v5.6_FINAL.md` Bước 15 | Bước thực hiện |
| `SR_PRISMA_Checklist_v5.6.md` Items 13c, 13d | PRISMA items liên quan |

---

*SR_Recall_Validation_Seeds_v5.6.md — v1.0 — 2026-05-15 — NCS HoaTX*
