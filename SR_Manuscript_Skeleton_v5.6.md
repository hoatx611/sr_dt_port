# MANUSCRIPT SKELETON — IMRaD
# Digital Twin for Container Port Operations: A Systematic Review

**File:** SR_Manuscript_Skeleton_v5.6.md
**Phiên bản:** v0.1 — 2026-05-15 (skeleton — viết sau Bước 17)
**NCS:** HoaTX
**Target journal:** International Journal of Production Research (IF ≈ 9.2, Q1, T&F)
**Word limit:** 8.000–12.000 words (not counting references/supplementary)
**Dùng tại:** Bước 18 (Manuscript drafting)

> Skeleton này cung cấp cấu trúc, word target, PRISMA item liên quan, và hướng dẫn nội dung cho từng section. Điền vào sau khi Bước 9–17 hoàn tất. Các ô [TBD] được điền dần.

---

## TITLE PAGE

**Proposed Title:**
> *Digital Twin Maturity in Container Port Operations: A Systematic Review of Evidence, Gaps, and a Conditional Roadmap for Resource-Constrained Ports*

**Alternative Title (shorter):**
> *Digital Twin for Container Port Operations: Systematic Review and Maturity Roadmap*

**Corresponding author:** [NCS điền: Họ tên, Affiliation, ORCID, Email]
**Co-author / Supervisor:** [Điền sau]
**Keywords (6–8):** digital twin; container port; systematic review; maturity level; port operations; research agenda; [TBD 2 more]
**Word count:** [TBD] words (excl. references)
**Number of figures:** 7 (Figure 1: PRISMA flow; Figures 2–6: VOSviewer maps; Figure 7: Heat-map 3D)
**Number of tables:** 4 (Table 1: included studies summary; Table 2: extraction per study; Table 3: quality appraisal; Table 4: Research Agenda)

---

## ABSTRACT (250 words | PRISMA Item 2)

**Background:** Container ports are critical logistics nodes requiring operational efficiency at multiple layers — berth, yard, crane, AGV, and gate. Digital Twin (DT) technology offers transformative potential for port operations, yet the maturity and scope of DT adoption remain poorly characterised.

**Objectives:** This systematic review maps the current state of DT research in container port operations across five maturity levels (L1 Data Visibility to L5 Closed-Loop Autonomy), identifies methodological patterns and geographic gaps, and derives a conditional implementation roadmap for resource-constrained ports.

**Methods:** We conducted a PRISMA 2020-compliant systematic review of literature published 2015–2026 across five databases (Scopus, IEEE Xplore, Google Scholar, Springer Link, Taylor & Francis). After 3-layer automated deduplication (n = 7,847 → 5,822 unique records) and title/abstract screening, [n] studies were included following full-text review. Quality was assessed using Kitchenham & Charters (2007) eight criteria.

**Results:** [n] studies were included. [TBD after Bước 9–17] The majority clustered at L2–L3 (Operational State and Decision Support). Critical gaps were identified at L4–L5 and in Southeast Asian / small-medium ports. Brownfield-specific DT research remained severely underrepresented.

**Discussion:** Six research priorities (RA1–RA6) were derived from gap analysis. A conditional roadmap provides tier-progression pathways based on port size and vintage context.

**Registration:** OSF pre-registration DOI: [10.17605/OSF.IO/DXJW9 — NCS verify]

---

## 1. INTRODUCTION (1.000–1.500 words | PRISMA Items 3, 4)

### 1.1 Bối cảnh và tầm quan trọng

*(Gợi ý nội dung — viết hoàn chỉnh tại Bước 18)*

- Container port throughput toàn cầu: [số liệu 2024 UNCTAD]. Tắc nghẽn hậu-COVID, chi phí logistics gia tăng.
- Port 4.0 / Industry 4.0 in maritime: xu hướng automation và digitalization.
- DT là công nghệ enabler quan trọng nhất (Tao et al. 2018; Jones et al. 2020) — nhưng adoption không đồng đều.
- Khoảng cách giữa "DT for mega-ports" (Shanghai, Rotterdam) và "DT for developing-country ports" (ĐNÁ, châu Phi).

### 1.2 Gap hiện có trong literature

*(Derive từ RQ4 sau Bước 17 — placeholder)*

- Thiếu SR hệ thống về DT + cảng container (không phải smart port tổng quát).
- Không có framework maturity đồng nhất áp dụng cho context cảng.
- Geographic gap ĐNÁ / brownfield underrepresented.
- Không có roadmap điều kiện hoá theo vintage/quy mô.

### 1.3 Mục tiêu tổng quan

Bài SR này nhằm:
1. Xây dựng bức tranh toàn cảnh (RQ1 — WHAT)
2. Đánh giá maturity level L1–L5 theo lĩnh vực và quy mô (RQ2 — HOW MATURE)
3. Phân tích phương pháp và nguồn lực (RQ3 — HOW METHOD)
4. Xác định 5 chiều khoảng trống (RQ4 — WHERE GAPS)
5. Đề xuất chương trình nghiên cứu + lộ trình (RQ5 — WHAT NEXT)

**Contribution:** *(3 bullet điểm mới lạ — viết sau Bước 17)*
- Contribution 1: First SR to apply L1–L5 maturity framework to container port DT landscape
- Contribution 2: First evidence-based vintage gap analysis (greenfield vs brownfield)
- Contribution 3: Conditional roadmap grounded in empirical evidence for resource-constrained ports

---

## 2. THEORETICAL FRAMEWORK (1.000 words | PRISMA Item 3)

### 2.1 Digital Twin — 3 Core Properties

*(Grieves 2014; Tao et al. 2018; Jones et al. 2020)*

| Property | Định nghĩa | Relevance cho cảng |
|----------|-----------|---------------------|
| Physical entity | Cảng thực, thiết bị, quy trình | Berth, yard, crane, AGV, gate |
| Virtual model | Mô hình số hóa phản ánh trạng thái | DES, 3D/4D, ontology, state model |
| Data connection | Luồng dữ liệu 2 chiều real-time | IoT, OPC-UA, MQTT, ERP integration |

**IC1 operationalization:** Cả 3 properties phải hiện diện để đủ điều kiện là DT (không chỉ IoT dashboard hay simulation đơn lẻ).

### 2.2 Maturity Framework L1–L5 (Contribution)

*(Derived from Boschert & Rosen 2016; Grieves 2017; adapted for port operations)*

| Level | Tên | Core capability | Port example |
|-------|-----|-----------------|--------------|
| L1 | Data Visibility | Real-time sensor data + dashboard | Vessel tracking, crane load monitoring |
| L2 | Operational State | Integrated model + computed state | Terminal Operating System + DT layer |
| L3 | Decision Support | Optimization using DT data | RL berth assignment, MILP yard planning |
| L4 | Simulation & V&V | DES + what-if + 3D/4D validation | Full terminal simulation with calibration |
| L5 | Closed-Loop Autonomy | Data→decision→execute→verify→adapt | Fully autonomous AGV + automated verification |

**Realistic Ceiling concept:** Không phải mọi cảng cần L5. Trần thực tế phụ thuộc vintage (brownfield → L3 thực tế; greenfield → L4/L5 khả thi), quy mô, và nguồn lực.

### 2.3 Port Operations 5 Domains

| Domain | Abbreviation | Key processes |
|--------|-------------|---------------|
| Berth planning | op_berth | Vessel arrival, berth allocation, departure |
| Yard management | op_yard | Container storage, retrieval, stacking |
| Crane operations | op_crane | Loading/unloading, crane scheduling |
| AGV/transport | op_agv | Horizontal transport, path planning |
| Gate & hinterland | op_gate | Truck gate, customs, hinterland logistics |

---

## 3. METHODOLOGY (2.000–3.000 words | PRISMA Items 5–11)

### 3.1 Protocol and Registration (PRISMA Items 24a, 24b)

This review was pre-registered on OSF (DOI: [10.17605/OSF.IO/DXJW9]). The full protocol, search strategy, eligibility criteria, and data extraction form are publicly available at [OSF URL]. Deviations from the protocol are documented in the Deviation Log (Supplementary).

### 3.2 Eligibility Criteria (PRISMA Item 5)

**Inclusion Criteria (PICOC):**
- **Population:** Container ports or container terminals (operational context)
- **Intervention:** Digital Twin technology (L1–L5 maturity, IC1 requires all 3 DT properties)
- **Comparison:** N/A (no comparator required — typology SR)
- **Outcome:** DT design, implementation, validation, or performance evidence
- **Context:** Any scale, geography, vintage; English; peer-reviewed; 2015–2026

**Exclusion Criteria (Lớp 1 — T/A level):** [Summarize from SR_Eligibility_Criteria.md — 28 codes]

**Borderline rules:** Six borderline rules applied per SR_Eligibility_Criteria.md §VI (B1: DT-driven vs mention; B2: Smart port; B3: Manufacturing transfer; B4: Bulk/RoRo; B5: Review papers; B6: Vintage unspecified).

### 3.3 Information Sources (PRISMA Item 6)

Searches conducted on five databases: Scopus (primary), IEEE Xplore, Google Scholar, Springer Link, and Taylor & Francis. Search dates: 2026-05-10 (Q1–Q9, Q11–Q12, GS) and 2026-05-15 (Q10 Vintage). Full search strategies available in Supplementary (PRISMA-S Item 8).

### 3.4 Search Strategy (PRISMA Item 7)

Twelve query groups (Q1–Q12) were designed following five principles: (1) RQ-driven design, (2) coverage of all 5 analytical dimensions, (3) two-layer Core+Strata structure, (4) parsimony, and (5) full reproducibility. The strategy underwent PRESS peer review (McGowan et al. 2016) with 8/8 criteria passed (see SR_PRESS_Review.md).

**Core queries** (Q1–Q2): Broad DT + container port coverage.
**Strata queries** (Q3–Q10): Per-maturity-tier (Q3–Q7), gate operations (Q8), geographic (Q9), vintage (Q10).
**Supplementary** (Q11–Q12): Domain-specific journals (Springer/T&F).

### 3.5 Selection Process (PRISMA Item 8)

Records were screened by a single reviewer (NCS HoaTX) using a two-phase approach:
- **Phase A (automated):** 13-rule regex pre-screening using `screening.py` → 477 records excluded (LIKELY_EXCLUDE), 5,345 forwarded to Phase B
- **Phase B (manual):** Full title/abstract review in Rayyan Essentials with 28 EC/IC reason codes

Intra-rater reliability was assessed by re-screening 50 records after ≥ 14 days; Cohen's κ [TBD] ≥ 0.75 target (Bước 14). Single-reviewer limitation is acknowledged in §5.2 Limitations.

### 3.6 Data Collection (PRISMA Item 9)

Data were extracted using a structured form (6 groups × 40 fields): Group A (Bibliographic), Group B (Methodology), Group C (Maturity Level), Group D (Operational Area), Group D' (Port Context), Group E (Geographic + Gap). Pilot extraction on 5 studies (Bước 11) preceded full extraction.

### 3.7 Data Items (PRISMA Items 10a, 10b)

*(Table — viết sau Bước 11)*

### 3.8 Quality Appraisal (PRISMA Item 11)

Study quality was assessed using Kitchenham & Charters (2007) eight criteria (Q1–Q8), scored 0 (No) / 0.5 (Partial) / 1 (Yes), maximum 8 points. Quality levels: High (7–8), Medium (5–6.5), Low (3–4.5), Very Low (<3). Full appraisal documented in quality_appraisal.csv (Supplementary).

### 3.9 Synthesis Methods (PRISMA Items 13a–13d)

This review employs **typology synthesis** (Gough et al. 2012): narrative synthesis organized by L1–L5 maturity levels and operational domains, complemented by:
- **Bibliometric analysis** (Donthu et al. 2021): co-authorship, keyword co-occurrence, citation networks via VOSviewer 1.6.20
- **Heat-map 3D**: Maturity × Operational Domain × Port Size gap visualization
- **Thematic synthesis** (Braun & Clarke 2006): Research Agenda RA1–RA6

**Recall validation** (sensitivity): Pool recall tested against 78 seed papers; SA-1/2/3 triggered if recall < 95% (Bước 15).

---

## 4. RESULTS (2.500–3.500 words | PRISMA Items 14–22)

### 4.1 Study Selection — PRISMA Flow (PRISMA Item 14)

*(Điền sau Bước 9 + 10)*

> [Figure 1: PRISMA 2020 Flow Diagram — tạo từ SR_PRISMA_FlowDiagram.md dữ liệu]

| Stage | n |
|-------|---|
| Records identified (raw, 23 files) | 7,847 |
| After automated deduplication | 5,822 |
| Excluded Phase A (automated regex) | 477 |
| Forwarded to Phase B | 5,345 |
| Excluded Phase B (T/A manual) | [TBD] |
| Full-text assessed | [TBD] |
| Full-text not retrieved (EC6) | [TBD] |
| Full-text excluded (with reasons) | [TBD] |
| **Studies included in synthesis** | **[TBD]** |

### 4.2 Study Characteristics (PRISMA Item 15) [RQ1]

*(Điền sau Bước 11 + 16)*

**Publication trends:** *(line chart 2015–2026)*
**Geographic distribution:** *(choropleth — top 10 countries)*
**Venue distribution:** Top 10 journals/conferences
**Document type:** Journal article / Conference / Review

> [Figure 2–6: VOSviewer maps (co-authorship, keyword, co-citation, coupling, country)]

### 4.3 Quality Appraisal Results (PRISMA Items 16a, 16b)

*(Điền sau Bước 13)*

| Quality level | n | % |
|---------------|---|---|
| High (7–8) | TBD | TBD |
| Medium (5–6.5) | TBD | TBD |
| Low (3–4.5) | TBD | TBD |
| Very Low (<3) | TBD | TBD |

### 4.4 RQ2 — Maturity Level × Operational Area × Port Size

*(Điền sau Bước 12 + 17)*

> [Figure 7: Heat-map 3D — Maturity L1–L5 × 5 Operational Domains × Port Size]

**Key findings:**
- Dominant tier: [TBD]
- Underrepresented tiers: [TBD]
- Operational domain gaps: [TBD]

### 4.5 RQ3 — Methods and Resources

*(Điền sau Bước 17.4)*

**Method × Maturity matrix:** [Table]

### 4.6 RQ4 — Gap Analysis

*(Điền sau Bước 17.2–17.5)*

**RQ4a — Operational domain gaps:** [TBD]
**RQ4b — Method gaps:** [TBD]
**RQ4c — Geographic gaps:** VN/ĐNÁ underrepresentation [TBD]
**RQ4d — Vintage gaps:** Brownfield severely underrepresented [TBD]
**RQ4e — Open problems:** [TBD]

---

## 5. DISCUSSION (1.500–2.000 words | PRISMA Items 20a–20c)

### 5.1 Summary of Evidence (PRISMA Item 20a)

*(Điền sau kết quả — trả lời 5 RQ tổng hợp)*

### 5.2 Limitations (PRISMA Item 20b)

1. **Single reviewer:** Intra-rater reliability assessed (κ = [TBD]); not fully equivalent to independent dual-reviewer process. Expert Validation (Bước 21) provides partial mitigation.
2. **Database coverage:** WoS and ACM Digital Library not searched; partially mitigated by recall validation (recall = [TBD]%).
3. **Time-limited supplementary sources:** Springer (12 months), T&F (6 months); may miss older relevant work in these venues.
4. **Language restriction:** English-only; relevant Chinese, Spanish, or German DT-port literature excluded.
5. **Qualitative synthesis:** No meta-analysis possible due to outcome heterogeneity; quantitative comparisons limited.

### 5.3 Implications for Research — Research Agenda RA1–RA6 (RQ5a)

*(Điền sau Bước 17.5)*

| Code | Research Agenda | Priority | Gap dimension |
|------|----------------|---------|---------------|
| RA1 | DT-Edge Lightweight Architecture for Small Ports | [TBD] | RQ4b+c |
| RA2 | Multi-source Data Integration Ontology | [TBD] | RQ4a |
| RA3 | Hybrid MILP-RL with Resource Constraints | [TBD] | RQ4b |
| RA4 | Open-source Simulation Framework for Mid-size Ports | [TBD] | RQ4a+c |
| RA5 | Federated DT for Regional Port Clusters | [TBD] | RQ4c |
| RA6 | Validation Protocol for Low-data Environments | [TBD] | RQ4d |

### 5.4 Implications for Practice — Conditional Roadmap (RQ5b)

*(Điền sau Bước 17.6 — Bảng điều kiện hoá)*

> Table X: Conditional roadmap — Current tier × Port size × Vintage → Recommended next tier + Open-source toolkit + Cost estimate

---

## 6. CONCLUSION (300 words)

*(Viết sau toàn bộ content — tóm tắt 3–4 câu mỗi đoạn)*

This systematic review has mapped [n] studies on Digital Twin applications in container port operations published 2015–2026 across five maturity levels and five operational domains.

**Key findings:** [3 bullet]

**Practical contribution:** The conditional roadmap provides port operators — particularly those in resource-constrained contexts — with empirically grounded guidance for DT implementation planning.

**Future research:** RA1–RA6 priorities derived from this review point to [most critical gap].

---

## REFERENCES (≥ 100 references)

*(BibTeX export từ dedup_unique.ris sau Bước 11 — lọc included studies + key background)*

> Format: [Target journal style — IJPR uses APA 7th or numbered? Check author guidelines]

---

## SUPPLEMENTARY MATERIALS

| Item | File | Description |
|------|------|-------------|
| S1 | SR_Search_Strategy.md | Full query strings Q1–Q12 |
| S2 | SR_Eligibility_Criteria.md | 28 IC/EC codes + 6 borderline rules |
| S3 | SR_PRISMA_Checklist.md | 27/27 PRISMA items + 8 N/A justified |
| S4 | dedup.py + screening.py | Pipeline code |
| S5 | dedup_unique.ris | Full deduplicated pool |
| S6 | included_studies.csv | [TBD] included studies metadata |
| S7 | extraction.csv | Full extraction data |
| S8 | quality_appraisal.csv | Q1–Q8 scores per study |
| S9 | borderline_decisions_log.md | Audit trail borderline decisions |
| S10 | vos_*.png | 5 VOSviewer network maps |
| S11 | SR_Deviation_Log.md | Protocol deviations DEV-001–DEV-004 |

---

## AUTHOR CONTRIBUTIONS (CRediT taxonomy)

| Role | NCS HoaTX | Supervisor |
|------|-----------|-----------|
| Conceptualization | ● | ● |
| Methodology | ● | Advisory |
| Investigation | ● | — |
| Formal analysis | ● | — |
| Writing – original draft | ● | — |
| Writing – review & editing | ● | ● |
| Supervision | — | ● |
| Funding acquisition | [TBD] | [TBD] |

---

## CHECKLIST TRƯỚC KHI SUBMIT (Bước 22)

- [ ] Word count ≤ 12.000 (check target journal limit)
- [ ] Abstract structured ≤ 250 words
- [ ] All figures ≥ 300 DPI (TIFF/PNG)
- [ ] All tables fit page width
- [ ] PRISMA 2020 Checklist 27/27 items → section/page numbers filled
- [ ] OSF DOI verified và accessible
- [ ] Supplementary ZIP complete
- [ ] Cover letter draft ready
- [ ] ORCID iDs for all authors
- [ ] Competing interests declaration
- [ ] Funding statement
- [ ] Data availability statement: "Data available on OSF: [DOI]"
- [ ] Turnitin plagiarism check < 15%
- [ ] Language polish (native English editor)
- [ ] Target journal: IJPR author guidelines checked

---

## VERSIONING

| Version | Ngày | Thay đổi |
|---------|------|----------|
| **v0.1** | 2026-05-15 | Skeleton tạo — cấu trúc IMRaD + word targets + PRISMA mapping + guidance |
| v0.2 | TBD | Sau Bước 9–11: điền Results §4.1–4.2 |
| v0.3 | TBD | Sau Bước 13–17: điền §4.3–4.6, §5 |
| v1.0 | TBD | Draft 1 hoàn chỉnh → submit cho Supervisor review |
| v1.1 | TBD | Draft 2 sau Supervisor comments |
| v1.2 | TBD | Draft 3 sau Expert Validation |
| v2.0 | TBD | Submission ready |

---

*SR_Manuscript_Skeleton_v5.6.md — v0.1 — 2026-05-15 — NCS HoaTX*
