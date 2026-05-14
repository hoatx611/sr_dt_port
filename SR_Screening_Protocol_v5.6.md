# PROTOCOL SÀNG LỌC

**Phiên bản:** v1.0 — 2026-05-11
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**OSF DOI:** [10.17605/OSF.IO/DXJW9](https://doi.org/10.17605/OSF.IO/DXJW9)
**Anchor:** [SR_Eligibility_Criteria_v5.6.md](SR_Eligibility_Criteria_v5.6.md) v1.0 — 5 IC + 28 EC + 6 borderline rules
**Tuân thủ:** PRISMA 2020 Items 8 (Selection process), 16a–16b (Records); PRISMA-S 16 (Deduplication).
**Vai trò:** Quy trình chi tiết Pha A (Python pre-screen) + Pha B (Rayyan formal) + Pha C (Fulltext) cho Bước 8–9 WorkPlan.

---

# §I. KHUNG TỔNG THỂ

## 1.1 Ba pha sàng lọc

```text
                    ┌─────────────────────────────┐
Bước 7 dedup_unique │ Pool unique ≈ 5.000–7.000   │
                    └────────────────┬────────────┘
                                     │
                                     ▼
        ┌──────────────────────────────────────────────────┐
        │ PHA A — Python pre-screen (regex 13 priority)    │
        │ • LIKELY_INCLUDE / REVIEW_NEEDED / LIKELY_EXCLUDE│
        │ • Calibration pilot 30 records → κ ≥ 0.75        │
        └────────────────────────┬─────────────────────────┘
                                 │
                                 ▼
        ┌──────────────────────────────────────────────────┐
        │ PHA B — Rayyan formal T/A screening              │
        │ • Single reviewer NCS                            │
        │ • Reading order EXC → REV → INC                  │
        │ • Reasons taxonomy 28 EC/IC                      │
        │ • Output ta_screening.csv                        │
        └────────────────────────┬─────────────────────────┘
                                 │
                                 ▼
        ┌──────────────────────────────────────────────────┐
        │ PHA C — Fulltext screening                       │
        │ • PDF retrieval ≤ 14 ngày → EC6 nếu fail         │
        │ • Layer 2 EC codes                               │
        │ • Borderline log                                 │
        │ • Snowball + hand-search                         │
        └────────────────────────┬─────────────────────────┘
                                 │
                                 ▼
                       included_studies.csv
                       (kỳ vọng 80–150 studies)
```

## 1.2 Mục tiêu giảm gánh chấm tay

| Stage | Pool size kỳ vọng | Loại hình loại trừ | Reduction |
|-------|--------------------|---------------------|-----------|
| Sau Bước 7 dedup | 5.000–7.000 | – | – |
| Sau Pha A (Python pre-screen) | 5.000–7.000 (giữ nguyên, chỉ gắn label) | Không loại bài, chỉ ưu tiên đọc | – |
| Sau Pha B (Rayyan T/A) | 300–800 | EC1–EC9 + EC7-* + EC-CYBER/ENERGY/GENERIC/IT/NOSCOPE/PAX/STRUCT | ≈ 90% |
| Sau Pha C (Fulltext) | 80–150 | EC6 + EC-ENV/VESSEL/POLICY/SECUR/BLOCK/TELECOM/CUSTOMS/AGRI | ≈ 70–85% |

---

# §II. PHA A — PYTHON PRE-SCREEN

## 2.1 Mục đích

- KHÔNG thay thế Pha B Rayyan — chỉ sắp thứ tự đọc cho NCS.
- Output 3 nhãn `PRE_LABEL` ghi vào RIS N1 field → upload Rayyan.
- Calibration κ ≥ 0.75 với NCS trên pilot 30 records → đảm bảo regex chuẩn.

## 2.2 Pipeline architecture

```text
dedup_unique.ris
       │
       ▼
┌─────────────────────────────────────────┐
│ tf_journal_exclusion.py                 │
│ - Apply T&F whitelist + journal block   │
│ - Output: TF_PRE_LABEL nếu source là TF │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ screening.py (13 priority rules)        │
│ - Regex IC1-IC5 + 19 EC Layer 1         │
│ - Compute PRE_LABEL                     │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ Output:                                 │
│ - screening_pre.csv (full audit)        │
│ - screening_pre.ris (PRE_LABEL ở N1)    │
│ - screening_distribution.txt            │
└─────────────────────────────────────────┘
```

## 2.3 Regex rules (13 priority — top-down)

Áp dụng theo thứ tự; rule trước wins. Mỗi rule = (regex pattern, label, EC code).

| # | Pattern | Label | EC | Lý do |
|---|---------|-------|-----|-------|
| 1 | `\b(digital twin|digital shadow|cyber-physical)\b.*\b(container terminal|container port)\b` (cả 2 đảo) | LIKELY_INCLUDE | IC1 | DT-driven + container terminal — strong signal |
| 2 | `\b(berth|quay crane|yard|AGV|gate)\b.*\b(scheduling|allocation|optim|routing|monitor)\b.*\b(digital twin|simulation|IoT)\b` | LIKELY_INCLUDE | IC2/IC3 | Operations × DT/sim/IoT |
| 3 | `\b(simulation|DES|agent-based|hardware-in-loop)\b.*\b(container|terminal|port)\b.*\b(validat|verif|calibrat|emulat)\b` | LIKELY_INCLUDE | IC3 | Simulation V&V |
| 4 | `\bport-Hamiltonian\b\|\bport Hamiltonian\b` | LIKELY_EXCLUDE | EC-NOSCOPE | Toán điều khiển, không phải cảng |
| 5 | `\b(USB|serial|I/O|network|COM|ethernet|transport layer|port number)\s*port\b` | LIKELY_EXCLUDE | EC-NOSCOPE | Port kỹ thuật |
| 6 | `\b(docker|kubernetes|side-channel|SMT execution port)\b` | LIKELY_EXCLUDE | EC-IT/EC-NOSCOPE | Container CNTT / CPU |
| 7 | `\b(airport|heliport|air terminal)\b` | LIKELY_EXCLUDE | EC-NOSCOPE | Hàng không |
| 8 | `\b(Port Vila|Port Moresby|Port Said|Port Harcourt|Port-au-Prince|Portsmouth|Newport News|Port Elizabeth|Port Louis)\b` | LIKELY_EXCLUDE | EC-NOSCOPE | Tên thành phố |
| 9 | `\b(bulk\|tanker\|oil\|LNG\|coal\|grain\|ore\|cruise\|ferry\|passenger\|RoRo\|roll-on)\s*terminal\b` | LIKELY_EXCLUDE | EC2 | Bến không phải container |
| 10 | `\b(patient\|clinical\|cancer\|tumor\|surgery\|medical\|pharmaceutical\|drug\|protein\|cell\|tissue)\b` | LIKELY_EXCLUDE | EC7-health | Y tế |
| 11 | `\b(ship hull\|marine engine\|offshore platform\|vessel routing)\b\|\b(structural health monitoring)\b.*\b(bridge\|wharf\|seismic)\b` | LIKELY_EXCLUDE | EC1/EC-STRUCT | Tàu / kết cấu dân dụng |
| 12 | `\b(BIM\|Building Information Modeling)\b.*\b(construction\|civil)\b` (không có port keyword) | LIKELY_EXCLUDE | EC7-bim | Construction BIM |
| 13 | _(default)_ | REVIEW_NEEDED | – | Mọi case khác |

**Lưu ý implementation:**

- Regex case-insensitive (`re.IGNORECASE`).
- Match trên `title + abstract + author_keywords` concat.
- KHÔNG truncate title/abstract — match toàn bộ string sau lowercase + strip whitespace (memory rule §0.3 toàn vẹn dữ liệu).
- Rule 1 + 2 + 3 OR-merge để bắt LIKELY_INCLUDE (≥ 1 trong 3 match).
- Rule 4–12 OR-merge để bắt LIKELY_EXCLUDE.
- Một bài có thể match nhiều EC; ghi tất cả nhưng `PRE_LABEL` ưu tiên rule cao nhất theo thứ tự bảng.

## 2.4 tf_journal_exclusion.py — module riêng cho T&F pool

T&F không có Subject filter ở tầng truy vấn → toàn bộ exclusion theo journal name chuyển sang script này.

```text
WHITELIST (5 tạp chí — luôn LIKELY_INCLUDE bypass rule 4–12):
  - International Journal of Production Research
  - Digital Twin
  - International Journal of Logistics Research and Applications
  - Maritime Policy & Management
  - International Journal of Sustainable Transportation

BLACKLIST (LIKELY_EXCLUDE với EC code mapping):
  - International Journal of Construction Management        → EC-STRUCT
  - Journal of Asian Architecture and Building Engineering  → EC-STRUCT
  - Nondestructive Testing and Evaluation                   → EC-STRUCT
  - Structure and Infrastructure Engineering                → EC-STRUCT
  - Nuclear Technology                                      → EC-NOSCOPE
  - International Journal of Human–Computer Interaction     → EC-NOSCOPE
  - International Journal of Computer Integrated Manufact.  → EC7-mfg
  - Journal of Engineering Design                          → EC7-mfg
  - Production & Manufacturing Research                    → EC7-mfg
  - Virtual and Physical Prototyping                       → EC7-mfg
  - Cogent OA (medical)                                    → EC7-health
  - Dove Medical Press                                     → EC7-health
```

## 2.5 Output schema

### `screening_pre.csv`

| Cột | Type | Mô tả |
|-----|------|-------|
| study_id | string | UUID từ dedup |
| doi | string | DOI chuẩn hoá |
| title | string | Title đầy đủ |
| abstract | string | Abstract đầy đủ (KHÔNG truncate) |
| source | enum | scopus/ieee/gs/springer/tf |
| journal | string | Tạp chí |
| year | int | – |
| pre_label | enum | LIKELY_INCLUDE / REVIEW_NEEDED / LIKELY_EXCLUDE |
| ec_candidate | string | Mã EC nếu pre_label = LIKELY_EXCLUDE |
| matched_rules | string | List rule numbers đã match (audit trail) |

### `screening_pre.ris`

Full RIS metadata + thêm field `N1 - PRE_LABEL: <label> | EC: <ec_code>` (Rayyan đọc N1 vào Notes).

### `screening_distribution.txt`

```text
Total records: NNNN
LIKELY_INCLUDE  : NNN  (XX.X%)   [kỳ vọng 15–25%]
REVIEW_NEEDED   : NNNN (XX.X%)   [kỳ vọng 40–60%]
LIKELY_EXCLUDE  : NNNN (XX.X%)   [kỳ vọng 20–40%]

By source:
  scopus   : NNN
  ieee     : NNN
  gs       : NNN
  springer : NNN
  tf       : NNN

Top 10 EC codes (LIKELY_EXCLUDE):
  EC-STRUCT : NN
  EC2       : NN
  ...
```

## 2.6 Calibration pilot (Bước 8.1.4)

| Bước | Mô tả |
|------|-------|
| 8.1.4.1 | NCS chọn 30 records ngẫu nhiên (10 từ mỗi nhãn LIKELY_INCLUDE/REVIEW_NEEDED/LIKELY_EXCLUDE) |
| 8.1.4.2 | NCS chấm thủ công 30 bài: INCLUDE / REVIEW / EXCLUDE (mù với pre_label) |
| 8.1.4.3 | Tính Cohen's κ giữa pre_label và NCS thủ công |
| 8.1.4.4 | Nếu κ ≥ 0.75 → confirm Pha A; tiếp Bước 8.2 |
| 8.1.4.5 | Nếu κ < 0.75 → Recovery R3 — refine 13 rules + re-run Pha A |

**Phân tích discrepancy:**

| Pre vs NCS | Hành động |
|------------|-----------|
| Pre INC, NCS EXC | False positive — kiểm tra rule 1–3 quá broad không |
| Pre EXC, NCS INC | False negative critical — kiểm tra rule 4–12 over-aggressive |
| Pre REV, NCS INC/EXC | Không phải lỗi — REV nghĩa là cần manual; NCS xác định |

---

# §III. PHA B — RAYYAN FORMAL SCREENING

## 3.1 Pool import

| Bước | Mô tả |
|------|-------|
| 8.2.1.1 | NCS upload `screening_pre.ris` (PRE_LABEL trong N1) lên Rayyan project `SR_DT_Port` |
| 8.2.1.2 | Rayyan auto-import + auto-dedup DOI (cross-validate; expected 0 dup vì đã Bước 7) |
| 8.2.1.3 | Verify Rayyan đọc PRE_LABEL từ N1 → hiển thị trong Notes panel |

## 3.2 Reading order — tối ưu effort

| Order | PRE_LABEL | Mode | Mục tiêu |
|-------|-----------|------|----------|
| 1 | LIKELY_EXCLUDE | Quick confirm | NCS đọc title nhanh ≤ 30 giây/bài; nếu xác nhận EXC → click Exclude với EC code; nếu nghi ngờ → đẩy sang REV |
| 2 | REVIEW_NEEDED | Careful | NCS đọc title + abstract đầy đủ; quyết định INC / EXC / Maybe; ghi note nếu Maybe |
| 3 | LIKELY_INCLUDE | Confirm | NCS đọc abstract chi tiết; quyết định INC / EXC; nếu EXC → ghi rõ tại sao Pre-screen sai |

**Thời gian dự kiến:**

- Order 1 (≈ 30%): 30s × N → ~1.500–2.000 bài × 30s = 12–17 giờ
- Order 2 (≈ 50%): 90s × N → ~2.500–3.500 bài × 90s = 60–90 giờ
- Order 3 (≈ 20%): 60s × N → ~1.000–1.500 bài × 60s = 17–25 giờ

**Tổng:** 90–130 giờ ≈ 4–6 tuần với 4 giờ/ngày.

## 3.3 Custom Reasons taxonomy (28 codes)

Nạp vào Rayyan ở Bước 1.12. Format:

```text
INCLUDE codes:
  IC1 — DT/CPS + container terminal operations
  IC2 — Optimization/scheduling × 5 areas + DT/sim/IoT
  IC3 — Simulation/V&V at container terminal
  IC4 — IoT/monitoring as DT layer
  IC5 — Visualization/3D/4D/GIS for container ports

EXCLUDE Layer 1 codes (T/A):
  EC1, EC2, EC3, EC4, EC5
  EC7-mfg, EC7-bim, EC7-health, EC7-noctx, EC7-other
  EC8, EC9
  EC-CYBER, EC-ENERGY, EC-GENERIC, EC-IT, EC-NOSCOPE, EC-PAX, EC-STRUCT

EXCLUDE Layer 2 codes (Fulltext — apply Pha C):
  EC6 (no fulltext), EC-ENV, EC-VESSEL, EC-POLICY, EC-SECUR
  EC-BLOCK, EC-TELECOM, EC-CUSTOMS, EC-AGRI
```

## 3.4 Pilot calibration (Bước 8.2.2)

NCS chấm 30 records (10 từ mỗi PRE_LABEL); tính κ Pha A vs NCS chính thức:

| Outcome | Hành động |
|---------|-----------|
| κ ≥ 0.85 | Excellent — tiếp Bước 8.2.4 chấm full pool |
| 0.75 ≤ κ < 0.85 | Acceptable — tiếp Bước 8.2.4; ghi note refine rule sau cho v1.1 |
| κ < 0.75 | Recovery R3 — refine `screening.py` + re-run Pha A; re-pilot 30 mới |

## 3.5 Borderline handling

| Case | Hành động |
|------|-----------|
| Smart port (Borderline 2 Eligibility) | NCS đọc abstract kỹ; có ≥ 2/3 DT attributes → INC; chỉ IoT thuần → MAYBE → review fulltext (Pha C) |
| Bulk/RoRo + DT method tốt (Borderline 4) | Default EXC EC2; ghi MAYBE trong Notes nếu method tổng quát; quyết định fulltext |
| Review paper (Borderline 5) | INC nếu DT-port scope; EXC nếu narrative review về maritime general |
| Greenfield/brownfield không nêu rõ (Borderline 6) | INC; classify port_vintage = unspecified ở Bước 11 extraction |

Mọi quyết định MAYBE → ghi vào `borderline_decisions_log.md` (Bước 13) với evidence quote.

## 3.6 Snapshot weekly (Backup §0.5)

| Bước | Mô tả |
|------|-------|
| Sunday 22:00 | Export Rayyan project state → `rayyan_snapshot_YYYYMMDD.csv` lưu vào `03_screening/Rayyan_weekly_snapshots/` |
| Mỗi snapshot lưu | Title, DOI, decision, reasons, notes, timestamp |
| Audit trail | 1 năm sau publication mới được xoá |

## 3.7 Output Bước 8

`ta_screening.csv` schema:

| Cột | Mô tả |
|-----|-------|
| study_id | UUID |
| doi | DOI |
| title | Title |
| ta_decision | INCLUDE / EXCLUDE / MAYBE |
| ta_ec_code | Mã EC nếu EXCLUDE |
| ta_notes | NCS note (đặc biệt cho MAYBE) |
| timestamp | Decision timestamp |

---

# §IV. PHA C — FULLTEXT SCREENING

## 4.1 Retrieval gating (Bước 9.1)

| Bước | Mô tả | Ngưỡng |
|------|-------|--------|
| 9.1.1 | VNU institutional access (Scopus full-text + IEEE Xplore + Springer + T&F) | – |
| 9.1.2 | Email tác giả (template EN, request PDF) | 7 ngày từ pre-screening pass |
| 9.1.3 | ResearchGate / academia.edu | 14 ngày từ pre-screening pass |
| 9.1.4 | Sci-Hub last resort | KHÔNG ưu tiên; nếu dùng → ghi rõ Limitations |
| 9.1.5 | Sau 14 ngày không có → EC6 | – |

PDF lưu trong `04_fulltext/<authoryear_firstword>.pdf`.

## 4.2 Fulltext decision

NCS đọc PDF → quyết định:

| Decision | Note |
|----------|------|
| INCLUDE | Đủ điều kiện cuối; tiếp Bước 11 extraction |
| EXCLUDE Layer 2 | EC6 (no fulltext) hoặc EC-ENV/VESSEL/POLICY/SECUR/BLOCK/TELECOM/CUSTOMS/AGRI |
| Borderline | Ghi vào `borderline_decisions_log.md` với quote + 1 trong 6 borderline rules áp dụng |

## 4.3 Snowball + Hand-search (Bước 9.3 + 9.4)

Áp dụng *sau* Pha C trên pool included sơ bộ:

| Method | Source | Output |
|--------|--------|--------|
| Backward snowball | References của 6 seed papers | Candidates → IC/EC → bổ sung |
| Forward snowball | "Cited by" GS cho 4 seeds | Candidates → IC/EC → bổ sung |
| Hand-search | TOC 10 tạp chí 2024–2026 | Candidates → IC/EC → bổ sung |

Pool included cuối = Phase C decisions ∪ Snowball additions ∪ Hand-search additions.

## 4.4 Output Bước 9

`fulltext_decisions.csv` + `included_studies.csv` (subset INCLUDE).

```text
fulltext_decisions.csv schema:
  study_id, doi, title, fulltext_decision, fulltext_ec_code,
  fulltext_notes, pdf_retrieved (yes/no), retrieval_method,
  retrieval_date, decision_date

included_studies.csv schema:
  study_id, doi, title, authors, year, journal, doc_type, source
  (subset của fulltext_decisions.csv với decision = INCLUDE,
   thêm bài từ snowball + hand-search)
```

---

# §V. METRICS + PRISMA FLOW

## 5.1 Conttrol metrics theo dõi qua Pha A → C

| Metric | Pha A | Pha B | Pha C | Notes |
|--------|-------|-------|-------|-------|
| Pool size in | 5.000–7.000 | 5.000–7.000 | 300–800 | – |
| LIKELY_INCLUDE % | 15–25% | – | – | Kiểm trigger ở 8.1.4 |
| Cohen's κ (Pre vs NCS) | – | ≥ 0.75 | – | Bước 14.1 |
| EXCLUDE rate | – | ≈ 90% | ≈ 70–85% | – |
| Time per record | < 1s | 30–90s | 5–10 phút | – |
| EC6 rate | – | – | < 20% | Trigger R08 nếu vượt |

## 5.2 PRISMA 2020 Flow Diagram (Bước 10)

```text
                     IDENTIFICATION
       ┌─────────────────────────────────────────────┐
       │ Records identified from databases:          │
       │   Scopus (10 queries)        : NNNN         │
       │   IEEE Xplore (10 queries)   : NNNN         │
       │   Springer Link (Q11)        : NNN          │
       │   Taylor & Francis (Q12)     : NNN          │
       │   Google Scholar (Q13–Q22)   : NNN          │
       │ Total                        : NNNNN        │
       └─────────────────────────────────────────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ Removed before screen │
               │   Duplicates (Bước 7)│
               │     -NNNN            │
               └──────────┬───────────┘
                          │
                          ▼ NNNN unique records
                       SCREENING
       ┌─────────────────────────────────────────────┐
       │ Pha A pre-screen (Python regex)             │
       │   LIKELY_INCLUDE   : NNN                    │
       │   REVIEW_NEEDED    : NNNN                   │
       │   LIKELY_EXCLUDE   : NNNN                   │
       │ Pha B Rayyan T/A formal screening           │
       │   Excluded (EC1–EC9, EC7-*, EC-CYBER, …)    │
       │     -NNNN                                   │
       └─────────────────────────────────────────────┘
                          │
                          ▼ NNN records sought retrieval
                          │
               ┌──────────────────────┐
               │ Not retrieved (EC6)  │
               │   -NNN               │
               └──────────┬───────────┘
                          │
                          ▼ NNN records assessed for eligibility
                       FULLTEXT
       ┌─────────────────────────────────────────────┐
       │ Excluded Layer 2:                           │
       │   EC-ENV/VESSEL/POLICY/SECUR/BLOCK/TELECOM/ │
       │   CUSTOMS/AGRI : -NNN                       │
       └─────────────────────────────────────────────┘
                          │
                          ▼ NN core included
       ┌─────────────────────────────────────────────┐
       │ + Snowball (backward + forward) : +NN       │
       │ + Hand-search (10 journals)     : +NN       │
       └─────────────────────────────────────────────┘
                          │
                          ▼ N (80–150) studies included in synthesis
```

---

# §VI. LIÊN KẾT THAM CHIẾU

| File | Quan hệ |
|------|---------|
| [SR_Eligibility_Criteria_v5.6.md](SR_Eligibility_Criteria_v5.6.md) | 5 IC + 28 EC + 6 borderlines (anchor) |
| [SR_Research_Questions_v5.6.md](SR_Research_Questions_v5.6.md) | RQ doc — Eligibility align với 5 RQ |
| [WorkPlan_v5.6_FINAL.md](WorkPlan_v5.6_FINAL.md) | Bước 8 (Pha A + B); Bước 9 (Pha C); Bước 10 (PRISMA Flow) |
| [SR_Risk_Register_v5.6.md](SR_Risk_Register_v5.6.md) | R03–R09 trigger condition |
| `screening.py` | Implementation Pha A 13 priority rules (Bước 8.1.2) |
| `tf_journal_exclusion.py` | T&F whitelist + journal exclusion (Bước 8.1.1) |
| `borderline_decisions_log.md` | Audit trail borderline (Bước 13) |

---

# §VII. PHIÊN BẢN

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-05-11 | Tạo mới — Protocol Pha A Python regex (13 rules) + tf_journal_exclusion module + Pha B Rayyan formal screening + Pha C Fulltext + Snowball/Hand-search + PRISMA Flow template (Bước 8.1 chuẩn bị WorkPlan) |
