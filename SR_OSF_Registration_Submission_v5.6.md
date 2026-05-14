# DỰ THẢO REGISTRATION SUBMISSION — OSF

**Phiên bản:** v1.0 — 2026-05-10
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**Mục đích:** Hỗ trợ NCS điền Registration form trên OSF (Bước 1.4–1.5 WorkPlan). Toàn bộ nội dung dưới đây bằng **tiếng Anh** (sẽ paste công khai), tuân thủ PRISMA-P 2015 (Moher et al.) mở rộng thành **20 mục** chuẩn cho OSF Registration.
**Cảnh báo:** ĐÃ STRIP nhãn nội bộ. KHÔNG paste bất kỳ chuỗi `v5.6`/`vN.M`/"RESET 2026-05-08" nào lên OSF. Nội dung này chỉ phản ánh phiên bản hiện tại — không nhắc lịch sử.

---

# §I. CHECKLIST 20 MỤC PRISMA-P (mở rộng cho OSF)

| # | Mục | Trạng thái dự thảo |
|---|------|---------------------|
| 1 | Title | ✅ |
| 2 | Registration | ✅ (placeholder DOI) |
| 3 | Authors and contributions | ⚠️ NCS điền tên Supervisor |
| 4 | Rationale | ✅ |
| 5 | Objectives (PICOC + 5 RQ) | ✅ |
| 6 | Eligibility criteria | ✅ |
| 7 | Information sources | ✅ |
| 8 | Search strategy | ✅ |
| 9 | Study records — data management, selection, collection | ✅ |
| 10 | Data items | ✅ |
| 11 | Outcomes and prioritization | ✅ |
| 12 | Risk of bias / quality appraisal | ✅ |
| 13 | Data synthesis | ✅ |
| 14 | Meta-bias(es) | ✅ |
| 15 | Confidence in cumulative evidence | ✅ |
| 16 | Amendments policy | ✅ |
| 17 | Funding | ⚠️ NCS điền nguồn tài trợ |
| 18 | Conflicts of interest | ⚠️ NCS xác nhận |
| 19 | Support / acknowledgments | ⚠️ NCS điền |
| 20 | Data sharing plan | ✅ |

---

# §II. NỘI DUNG TIẾNG ANH (paste lên OSF Registration form)

## 1. Title

```text
Digital Twin for Container Port Operations: A Systematic Review of Maturity, Methods, and Research Agenda (2015–2026)
```

---

## 2. Registration

```text
This protocol is registered on the Open Science Framework (OSF) Registries.

OSF Project URL: https://osf.io/dxjw9/
OSF Registration DOI: [to be assigned upon successful submission of this Registration]

Registration date: [to be filled by OSF upon submission]
Registration type: OSF Pre-Registration (no specific schema; full PRISMA-P 2015 protocol)
Project visibility: Public
License: CC-BY 4.0 Attribution International

This pre-registered protocol describes the planned methods of the systematic review BEFORE the screening, extraction, and synthesis stages are executed. Any subsequent deviations from this protocol will be transparently logged as OSF Amendments and reported in the published manuscript (PRISMA 2020 Item 24c).
```

---

## 3. Authors and contributions

```text
Lead reviewer (corresponding author):
  HoaTX
  Affiliation: [to be filled by NCS]
  Email: hoatx611@gmail.com
  ORCID: [to be filled by NCS]
  Role: Conceptualization, Methodology, Investigation, Data Curation, Formal Analysis, Writing — Original Draft.

Supervisor 1:
  [Name to be filled by NCS]
  Affiliation: [to be filled]
  Role: Supervision, Methodology, Validation, Writing — Review & Editing.

Supervisor 2 (optional):
  [Name to be filled by NCS]
  Affiliation: [to be filled]
  Role: Supervision, Methodology, Validation, Writing — Review & Editing.

Single-reviewer model: This systematic review is conducted with a single reviewer (the lead PhD candidate) for all stages of screening, extraction, and quality appraisal. To compensate for the absence of a second independent reviewer, the protocol incorporates: (a) intra-rater reliability assessment via blinded re-coding after a ≥14-day interval (Cohen's κ ≥ 0.75 target) at three checkpoints — title/abstract screening (n=30), data extraction (n=5), and maturity classification (n=10); (b) Expert Validation through a Delphi-lite panel of 3–5 senior researchers and port-industry experts to validate the maturity classification scheme and the proposed research agenda; and (c) explicit reporting of the single-reviewer constraint in the Limitations section of the manuscript. This methodological choice is explicitly disclosed in PRISMA 2020 Item 8 (Selection process) and Item 23c (Limitations of the review process).
```

---

## 4. Rationale

```text
Container port operations are entering a profound digital transformation. The number of automated container terminals (ACT) has grown from a handful in 2015 to several dozens by 2026, and the global container throughput is projected to exceed 1 billion TEU/year. In parallel, the concept of Digital Twin (DT) — originally proposed by Grieves (2014) and formalized by Tao et al. (2019) — has emerged as a candidate paradigm to integrate sensor data, decision support, simulation, and closed-loop autonomy into a single mirrored representation of physical port assets and operations.

Despite a rapidly growing body of literature, the field lacks a consolidated and methodologically rigorous overview of: (i) the descriptive landscape of DT-port research (publication trends, geographic distribution, journal venues, methodological mix); (ii) the level of maturity actually achieved across operational areas (berth allocation, yard management, quay crane scheduling, AGV routing, gate operations) and across port-size classes (megaport, large, mid-size, small); (iii) the methodological approaches dominantly used at each maturity level and their resource requirements; (iv) the research gaps, including combinatorial gaps (level × area × size), method-by-level gaps, geographic gaps (e.g., between leading ports and Vietnam / Southeast Asia), vintage gaps (greenfield vs. brownfield), and unresolved theoretical problems; and (v) a research agenda with a realistic, conditional roadmap suitable for resource-constrained ports, rather than a one-size-fits-all assumption that every port should reach Level 5 closed-loop autonomy.

Several prior reviews exist (e.g., on smart port concepts, Industry 4.0 in maritime logistics, and DT in manufacturing). However, none has simultaneously covered the five analytical dimensions above with a transparent eligibility scheme, a registered search strategy, an intra-rater reliability protocol, a quantitative maturity classification scheme aligned with operational areas, and a conditional roadmap that explicitly considers port size, vintage (greenfield vs. brownfield), and resource intensity. The present systematic review aims to fill this gap and to serve as the anchor reference for subsequent doctoral research on DT for container port operations, with a particular focus on Vietnam and Southeast Asia.
```

---

## 5. Objectives — PICOC framework and Research Questions

```text
PICOC framework (operations-research adaptation of PICO):

  Population (P)   : Maritime container ports — including fully automated container
                     terminals (ACT), semi-automated terminals, and conventional
                     terminals adopting digital-twin technologies. All sizes
                     (megaport ≥10M TEU/yr, large 3–10M, mid-size 0.5–3M, small
                     <0.5M) and all vintages (greenfield, brownfield, mixed).

  Intervention (I) : Application of Digital Twin (DT), Digital Shadow, or
                     Cyber-Physical System (CPS) to port operations — including
                     scheduling, optimization, simulation, monitoring,
                     visualization, maintenance, and closed-loop autonomy.

  Comparison (C)   : Traditional methods without DT (rule-based dispatching,
                     standalone simulation without real-time synchronization).
                     Comparison is NOT mandatory: studies that present DT-only
                     contributions are still eligible.

  Outcomes (O)     : Operational efficiency (throughput, dwell time, makespan);
                     accuracy (RMSE, prediction error); quality of decisions;
                     level of automation achieved; and theoretical contributions
                     to DT architecture or framework.

  Context (C)      : Container ports worldwide (no geographic restriction);
                     publication years 2015 — present cut-off; English language;
                     peer-reviewed venues.

Research Questions (5 RQs, ordered by Kitchenham & Charters 2007 logic
"WHAT → HOW MATURE → HOW METHOD → WHERE GAPS → WHAT NEXT"):

  RQ1 — Descriptive Landscape (WHAT)
  How has DT/Digital-Shadow/CPS research for container port operations
  evolved between 2015 and the cut-off date in terms of publication volume,
  temporal trends, geographic distribution, leading journals/venues, dominant
  methodologies, and bibliometric network structure?

  Sub-questions:
    1a — Publication trend by year.
    1b — Geographic distribution (countries / regions; position of Vietnam
         and Southeast Asia).
    1c — Top 10 journals, conferences, publishers.
    1d — Distribution of dominant methodologies (simulation, optimization,
         IoT, AI, hybrid).
    1e — Co-authorship + co-occurrence keyword + co-citation networks
         (VOSviewer).

  RQ2 — Maturity (HOW MATURE)
  At what maturity level (L1 Data Visibility, L2 Operational State,
  L3 Decision Support, L4 Simulation & V&V, L5 Closed-Loop Autonomy)
  has the literature actually demonstrated DT for each of five operational
  areas (berth, yard, quay crane, AGV, gate), and how does this distribution
  differ by port size?

  Sub-questions:
    2a — Distribution Level × Operational Area (2D heat-map).
    2b — Highest level achieved per area.
    2c — Distribution Level × Port Size (2D heat-map).

  RQ3 — Methods and Resource Requirements (HOW METHOD)
  Which methods and technical architectures are being used to achieve each
  maturity level, and what level of resource intensity (data, IoT
  infrastructure, computing, manpower) is required for each method × level
  combination?

  Sub-questions:
    3a — Dominant methods per level (DES, RL, MILP, IoT, ontology,
         hybrid, …).
    3b — Resource intensity (Low / Medium / High) per method × level.
    3c — Lightweight / low-cost DT components feasible for
         resource-constrained ports.

  RQ4 — Research Gaps (WHERE GAPS) — 5 dimensions
  Which combinations remain under-explored along the dimensions: (a)
  combinatorial (level × area × size), (b) method × level, (c) geographic,
  (d) vintage (greenfield vs. brownfield), and (e) open problems?

  Sub-questions:
    4a — Combinatorial empty cells in 3D heat-map (≤ 3 studies = gap).
    4b — Method × level gaps.
    4c — Geographic gap: top 5 leader countries vs. Vietnam / Southeast
         Asia (number of studies, top level, top method).
    4d — Vintage gap: differences between greenfield and brownfield
         deployments.
    4e — Theoretical / open problems unresolved by current literature.

  RQ5 — Research Agenda and Roadmap (WHAT NEXT)
  Among the gaps identified in RQ4, which combinations should be prioritized
  for research over the next 1–5 years, and what realistic roadmaps are
  feasible for resource-constrained ports — without assuming that every
  port must reach Level 5?

  Sub-questions:
    5a — Priority research directions RA1–RA6, ranked by
         Priority_score = w1 × gap_size + w2 × demand + w3 × feasibility
         (default weights w1 = w2 = w3 = 1/3; sensitivity tested).
    5b — Conditional roadmap: for a port at level X with constraint Y
         and vintage Z, what is the next-feasible level (NOT necessarily
         L5)? Each ceiling must be justified as cost-benefit positive
         for that port size — concept of "Realistic Ceiling".
    5c — Technical and organizational challenges to bridge 5a + 5b
         (data, manpower, capital, infrastructure, standardization).
    5d — Lightweight DT architecture proposal for mid-size and small
         ports (minimal components, open-source toolchain, federated
         DT for port clusters).
```

---

## 6. Eligibility criteria

```text
Studies are eligible if they satisfy AT LEAST ONE of five inclusion criteria
(IC1–IC5) AND ALL general conditions, AND DO NOT match any exclusion criterion
(28 codes across two screening layers).

INCLUSION CRITERIA (IC1–IC5):

  IC1 — DT/CPS + container terminal operations.
        Studies that explicitly invoke Digital Twin, Digital Shadow, or
        Cyber-Physical System (with at least 2 of the 3 Grieves 2014
        attributes: physical entity, virtual entity, bidirectional
        connection) AND apply the concept to container port operations.

  IC2 — Optimization / scheduling at container terminal with DT/sim/IoT
        component, in any of five operational areas: berth allocation,
        quay crane scheduling, yard management (RMG/RTG), AGV dispatching/
        routing, or gate operation / truck appointment / drayage.

  IC3 — Simulation / V&V at container terminal — discrete-event simulation,
        agent-based simulation, hardware-in-the-loop, or model verification —
        with synchronization to the real system or as emulation supporting
        a DT.

  IC4 — IoT / monitoring at container terminal that is part of a DT
        framework (data lake feeding DT, IoT as a DT layer). Includes "smart
        port" architectures with at least 2/3 DT attributes.

  IC5 — Visualization / 3D / 4D / GIS for container ports as the digital
        representation layer of a DT.

GENERAL CONDITIONS (apply to all IC1–IC5):

  - Publication year: 2015 ≤ PY ≤ search cut-off year.
  - Language: English (abstract mandatory, full text preferred).
  - Document type: peer-reviewed journal article, conference paper, review
    article, or book chapter.
  - Geographic scope: worldwide.

EXCLUSION CRITERIA — LAYER 1 (Title/Abstract; applied at screening):
  EC1   Vessel / offshore — DT for ship hull, marine engine, offshore.
  EC2   Non-container terminals — bulk, tanker, oil, LNG, coal, grain, ore,
        cruise, ferry, RoRo, passenger.
  EC3   Non-research material — editorial, letter, news, book review,
        conference abstract without full paper, poster.
  EC4   Port context but no DT/sim/optim/IoT — pure policy or governance.
  EC5   Duplicate (Rayyan auto-dedup; Python dedup applied earlier).
  EC7-{mfg,bim,health,noctx,other} — DT outside the port domain
        (manufacturing, BIM/construction, healthcare, no port context,
        other domains such as smart city or agriculture).
  EC8   CPS without port context.
  EC9   Non-English material (no English abstract or full text).
  EC-CYBER     Cybersecurity of port/SCADA/OT — not operations.
  EC-ENERGY    Microgrid, hydrogen/ammonia fuel, cold ironing — energy not
               container operations.
  EC-GENERIC   Maritime trade policy, geopolitics — no DT/operations.
  EC-IT        IT "container" (Docker, Kubernetes) — not shipping.
  EC-NOSCOPE   Port-Hamiltonian dynamics, USB/network port, side-channel.
  EC-PAX       Passenger/ferry/cruise terminals.
  EC-STRUCT    Civil structural health monitoring (bridges, wharf concrete,
               seismic) — not crane/terminal-equipment monitoring.

EXCLUSION CRITERIA — LAYER 2 (Full text):
  EC6          Full text not retrievable within 14 days (after VNU
               institutional access + author email request).
  EC-ENV       Coastal management, biofouling, marine life, ballast water.
  EC-VESSEL    Inland waterway, ship maneuvering, AIS-only tracking.
  EC-POLICY    Port economics, governance, DEA/TOPSIS/AHP-only.
  EC-SECUR    Port security architecture, hazmat, COVID-port.
  EC-BLOCK     Blockchain for trade documents — not operations.
  EC-TELECOM   5G/6G architecture only — communication layer.
  EC-CUSTOMS   Customs clearance, port-of-entry, brokerage.
  EC-AGRI      Agricultural ports, livestock terminals.

BORDERLINE RULES (6): documented decision rules for ambiguous cases —
DT-mention vs. DT-driven; smart port vs. DT; manufacturing transferable to
port; bulk/RoRo with strong DT method; review papers; greenfield vs.
brownfield ambiguity. All borderline decisions are logged with rationale
and, when relevant, an in-paper quote.

The full eligibility scheme (5 IC + 28 EC + 6 borderlines + Taylor & Francis
journal-specific exclusion list + 5 target-journal whitelist) is hosted in
the OSF Project Files as part of the registered protocol (file name
"SR_Eligibility_Criteria.md" in the public release folder).
```

---

## 7. Information sources

```text
Five information sources are searched:

  1. Scopus (Elsevier)         — primary database; broadest engineering
                                 and operations-research coverage.
                                 Queries: Q1–Q10 (10 queries).

  2. IEEE Xplore (IEEE)        — secondary database for engineering and
                                 computer-science venues including
                                 conference proceedings.
                                 Queries: Q1–Q10 mirrored (10 queries).

  3. Springer Link             — supplementary publisher-direct search to
                                 mitigate Scopus indexing lag for recent
                                 Springer eBook content.
                                 Window: most recent 12 months.
                                 Query: Q11 (1 query).

  4. Taylor & Francis Online   — supplementary publisher-direct search
                                 targeting two Q1 venues (International
                                 Journal of Production Research; Maritime
                                 Policy & Management) where Scopus
                                 indexing typically lags 1–3 months.
                                 Window: most recent 6 months.
                                 Query: Q12 (1 query).

  5. Google Scholar (GS)       — supplementary search via Publish-or-Perish
                                 to capture grey literature, preprints, and
                                 cross-publisher coverage.
                                 Queries: Q13–Q22 (10 sub-queries, each
                                 returning approximately 50–100 records
                                 due to the GS 1000-result cap).

Databases EXCLUDED with rationale:
  - Web of Science: institutional access constraints; ≈ 90% overlap with
    Scopus per Mongeon & Paul-Hus (2016).
  - ScienceDirect: already indexed in Scopus.
  - ACM Digital Library: HCI focus, not aligned with port operations.
  - DBLP: metadata only; lacks abstracts required for screening.

To mitigate database non-coverage risk (PRISMA-S Item 5), a recall
validation against 78 a priori seed papers will be executed (see Item 13
"Data synthesis — sensitivity analysis"). Acceptance threshold: recall
≥ 95%. If recall falls below 95%, three pre-specified sensitivity searches
(SA-1, SA-2, SA-3) will be triggered to enlarge the pool.

Supplementary methods (beyond databases):
  - Backward snowballing on 6 seed papers (4 review papers + 2 anchor
    studies) — references screened against IC/EC.
  - Forward snowballing via "Cited by" on Google Scholar for 4 of the
    seed papers.
  - Hand-search of 10 priority journals (table of contents 2024–search
    cut-off year) for any papers not yet indexed.

Search dates and the records identified per source will be recorded in
the search-tracking workbook stored in the OSF Project Files; the search
will be re-run within 12 months prior to manuscript submission to capture
newly indexed records (PRISMA-S Item 9).
```

---

## 8. Search strategy

```text
Search architecture (6 layers, 22 numbered queries):

  Layer 1 — CORE (Scopus + IEEE Xplore)
    Q1  CORE NARROW    : DT-driven + 12 distinctive port term clusters.
    Q2  CORE EXTENDED  : DT/CPS + port + 21 broad operational terms.

  Layer 2 — STRATA BY MATURITY LEVEL (Scopus + IEEE Xplore)
    Q3  T-L1   IoT, smart port, monitoring, dashboard.
    Q4  T-L2   Data integration, ontology, process mining, event log.
    Q5  T-L3   Operations × optimization (RL/MILP/heuristic).
    Q6  T-L4   DES, agent-based, V&V, 3D/4D, GIS (3 sub-branches merged).
    Q7  T-L5   Closed-loop, autonomy, feedback, self-adaptive.

  Layer 3 — STRATA BY OPERATIONAL AREA + CONTEXT (Scopus + IEEE)
    Q8  Gate operations (truck appointment, drayage, container gate).
    Q9  Port size + named Vietnamese / Southeast-Asian ports
        (Cat Lai, Cai Mep, Hai Phong, Lach Huyen, Da Nang, Quy Nhon,
        Laem Chabang, Klang, Tanjung Pelepas, …).
    Q10 Vintage (greenfield, brownfield, retrofit, port modernization).

  Layer 4 — PUBLISHER SUPPLEMENT
    Q11 Springer Link (12 months).
    Q12 Taylor & Francis Online (6 months).

  Layer 5 — GOOGLE SCHOLAR SUPPLEMENT
    Q13–Q22  10 sub-queries (DT + port; lightweight DT; smart container
             terminal; CPS + container; Vietnam port + DT; etc.).

  Layer 6 — SUPPLEMENTARY METHODS
    SNOW    Backward + forward snowballing on 6 seeds.
    HAND    Hand-search of 10 priority journals 2024–cut-off.
    RECALL  Recall validation on 78 seeds.
    SA-1/2/3  Sensitivity searches if recall < 95%.

Standard filter block (applied to Q1–Q10 in Scopus; mirrored in IEEE):
  - Year range: PUBYEAR > 2014 AND PUBYEAR < 2027.
  - Language: English.
  - Document type: Article OR Conference Paper OR Review.
  - NOT block 1 — Technical disambiguation (≈ 18 terms): airport, heliport,
    USB/I-O/serial/network/COM port, ethernet, transport layer, port number,
    wine port, Docker, Kubernetes, port-Hamiltonian, side-channel, SMT
    execution port.
  - NOT block 2 — Medical disambiguation (≈ 13 terms): patient, clinical,
    cancer, tumor, surgery, medical, health care, pharmaceutical, drug,
    protein, cell, tissue, air terminal.
  - NOT block 3 — Place-name disambiguation (≈ 9 terms): Port Vila, Port
    Moresby, Port Said, Port Harcourt, Port-au-Prince, Portsmouth, Newport
    News, Port Elizabeth, Port Louis.
  - NOT block 4 — Non-container terminal types (≈ 12 terms): bulk, tanker,
    oil, LNG, coal, grain, ore, cruise, ferry, passenger, RoRo.
  - NOT block 5 — Customs (2 terms): port-of-entry, customs clearance.
  - Subject area filter (Scopus only): ENGI, COMP, DECI, EART, ENER, BUSI,
    SOCI.

Full literal query strings for Q1–Q22 are stored verbatim in the OSF
Project Files (file "SR_Search_Strategy.md" in the public release folder)
and in the search-tracking workbook (queries copy-paste ready). The OSF
Project record date-stamps the search execution per query — fulfilling
PRISMA-S Items 1–8 (full reproducibility).

The search strategy was designed by the lead reviewer and self-reviewed
against the PRESS 2015 checklist (McGowan et al.). External peer review of
the search strategy is planned via consultation with one academic librarian
at the lead reviewer's institution prior to manuscript submission.
```

---

## 9. Study records — data management, selection process, data collection

```text
Data management:
  - All retrieved records (RIS files) are archived in the OSF Project Files
    under "search_results/" with one folder per database and per query.
  - Reference management: Rayyan QCRI Essentials for screening; CSV exports
    for audit trail; Python scripts (RapidFuzz, pandas) for deduplication
    and pre-screening; Excel/CSV for extraction.
  - All scripts, intermediate files, and decisions are version-controlled
    locally and snapshotted weekly (Sunday 22:00) to encrypted cloud backup.

Deduplication (3-layer pipeline):
  - Layer 1 — DOI exact match after normalization (lowercase, strip
              "https://doi.org/").
  - Layer 2 — Fuzzy title match (RapidFuzz token_sort_ratio ≥ 90 on
              normalized titles); priority-keep order: Scopus > IEEE > GS
              > Springer > T&F.
  - Layer 3 — Author + Year + Title hash (MD5 on lowercase first author +
              year + first 30 characters of title).
  - Cross-validation against Rayyan auto-dedup at DOI-only criterion
              (target: ≥ 99% agreement).

Selection process:
  Phase A — Python pre-screen on title + abstract using regex rules
           reflecting IC/EC. Outputs three labels: LIKELY_INCLUDE,
           REVIEW_NEEDED, LIKELY_EXCLUDE. Calibration pilot (30 records)
           against single-reviewer manual decisions; Cohen's κ ≥ 0.75
           target; if not met, regex rules are refined and Phase A re-run.
  Phase B — Rayyan formal title/abstract screening by the single reviewer.
           Reading order: LIKELY_EXCLUDE (quick confirm) → REVIEW_NEEDED
           (careful) → LIKELY_INCLUDE (confirm). Reasons taxonomy = the
           28 IC/EC codes.
  Phase C — Full-text screening: PDF retrieval (institutional access +
           author email). Records without full text within 14 days → EC6.
           Each retrieved PDF read end-to-end; decision INCLUDE / EXCLUDE
           with one Layer-2 EC code; borderline cases logged.

  Snowballing (backward + forward) and hand-search (10 journals) applied
  after Phase B; resulting candidates pass through the same eligibility
  scheme.

Data collection:
  Pilot extraction on 5 included studies (chosen to span L1, L2, L3, L4,
  and one Southeast-Asian port). Re-extraction blinded after ≥ 14 days
  (intra-rater reliability; Cohen's κ ≥ 0.75). Form refined if κ < 0.75.
  Full extraction follows on the remaining included pool, prioritized
  geographically (Vietnam / Southeast Asia first) and then by maturity
  level diversity.
```

---

## 10. Data items

```text
Six groups, 40 fields per included study:

  Group A — Bibliographic (8 fields): study_id, doi, title, authors, year,
            journal_or_venue, doc_type, country_of_first_author.

  Group B — Methodology (7 fields): dt_method (multi-select: data_integration,
            ontology, simulation_DES, agent_based, RL, MILP, metaheuristic,
            deep_learning, IoT_sensor, visualization_3D_4D, gis, hybrid,
            other), simulation_tool, optimization_algorithm, data_source
            (multi: iot_sensor, ais, tos_log, simulated, historical_record,
            expert_interview, public_dataset), validation_method (none,
            sim_only, real_data_calibration, hardware_in_loop, field_test,
            expert_review), dataset_url, code_availability (none, on_request,
            github, zenodo, osf, supplementary).

  Group C — Maturity (5 fields): maturity_primary (L1–L5),
            maturity_secondary, maturity_evidence (in-paper quote),
            maturity_confidence (high/medium/low), l5_evidence (quote
            justifying closed-loop autonomy if L5).

  Group D — Operational area (5 booleans): area_berth, area_yard,
            area_quay_crane, area_agv, area_gate. A study may have
            multiple True values.

  Group D' — Port size + Vintage + Resource (11 fields): port_size
             (megaport / large / mid_size / small / unspecified),
             port_size_evidence (quote), port_vintage (greenfield /
             brownfield / mixed / unspecified), port_vintage_evidence
             (quote), realistic_ceiling (L1–L5 / not_assessed),
             realistic_ceiling_rationale (quote), resource_intensity
             (Low / Medium / High), resource_components (multi-select:
             sensor_iot, gps_tracking, video_analytics, edge_compute,
             cloud_compute, GPU_cluster, dedicated_team,
             specialized_software, …), lightweight_dt_used (boolean),
             lightweight_components (list), applicable_to_small_port
             (boolean).

  Group E — Geographic + Gap + Future (4 fields): geographic_context
            (global / north_america / europe / east_asia / southeast_asia
            / vietnam / middle_east / africa / south_america /
            theoretical_no_case), gap_identified (paper-stated limitation),
            future_research_proposed (paper-stated future work),
            relevant_to_resource_constrained_port (boolean).

Resource intensity definitions:
  Low    — simple sensors (RFID, GPS), edge compute, ≤ 2 developers,
           free/open-source tools, < $100k initial budget.
  Medium — multi-sensor IoT + moderate cloud compute, 3–8 developers,
           mix of open-source and commercial tools, $100k–$1M.
  High   — multi-layer IoT + GPU cluster + dedicated DT team, 10+
           developers, commercial DT platform (e.g., Siemens MindSphere,
           GE Predix, PTC ThingWorx), > $1M.

The full extraction form is hosted in the OSF Project Files
("SR_Data_Extraction_Form.md" in the public release folder).
```

---

## 11. Outcomes and prioritization

```text
This is a qualitative typology systematic review with a bibliometric layer.
Therefore, "outcomes" are operationalized as the answer-tables, heat-maps,
and the research agenda described below — NOT as effect estimates of an
intervention.

Primary outputs:
  P1  Bibliometric report (RQ1) — descriptive statistics (year, country,
      journal) + 5 VOSviewer maps (co-authorship, co-occurrence keyword,
      co-citation, bibliographic coupling, country collaboration).
  P2  Maturity heat-maps (RQ2): Level × Operational Area; Level × Port Size.
  P3  Method × Maturity × Resource matrix (RQ3) + lightweight DT components
      list.
  P4  3D heat-map (RQ4a) Level × Area × Port Size + ranked list of empty
      cells (≤ 3 studies).
  P5  Method × Level gap matrix (RQ4b).
  P6  Geographic gap table (RQ4c) — top-5 leaders vs. Vietnam / SEA.
  P7  Vintage gap table (RQ4d) — greenfield vs. brownfield.
  P8  Open-problems list (RQ4e).
  P9  Research Agenda RA1–RA6 (RQ5a) ranked by Priority_score.
  P10 Conditional roadmap (RQ5b) by (current level × port size × vintage)
      → next feasible level + open-source toolkit + cost estimate.

Prioritization:
  Among RQ outputs, P9 + P10 are the headline contributions of the review,
  as they translate the analytical findings (P1–P8) into actionable
  research priorities and a roadmap for resource-constrained ports —
  responding to a documented gap in prior reviews (which generally assume
  a uniform L5 trajectory).

No effect-size meta-analysis is planned; therefore PRISMA 2020 Items 12,
13e, 14, 15, 19, 20c, 21, and 22 are flagged as not applicable, with
explicit justification in the manuscript Methods section and the PRISMA
checklist.
```

---

## 12. Risk of bias / quality appraisal

```text
Quality appraisal applies the 8-criterion Kitchenham & Charters (2007)
checklist for systematic reviews in software engineering:

  Q1  Are the aims of the study clearly stated?
  Q2  Is the context (port + DT) adequately described?
  Q3  Is the research design appropriate for the aims?
  Q4  Is the case-study selection / sampling clearly described?
  Q5  Is the data collection rigorous?
  Q6  Is the data analysis appropriate?
  Q7  Are the findings clearly stated?
  Q8  Is the value of the research established?

Each criterion is scored 0 (no) / 0.5 (partial) / 1 (yes); maximum total = 8.

Appraisal is performed by the single reviewer for every included study.
Borderline cases (total score within ±0.5 of a category cut-off, or
disagreement between intra-rater rounds) are logged with rationale.

Studies with total ≤ 4 are flagged as low-quality and excluded from the
synthesis (RQ2–RQ5) but retained for the bibliometric layer (RQ1) for
completeness; this rule is pre-specified to avoid post-hoc selection.

The classification scheme for maturity (L1–L5) is itself subject to
intra-rater reliability assessment (10 random studies re-classified
blinded after ≥ 14 days; Cohen's κ ≥ 0.75 target).
```

---

## 13. Data synthesis

```text
This systematic review uses qualitative typology synthesis combined with a
bibliometric layer (Donthu et al. 2021). NO meta-analysis is performed
because (i) the included studies do not report comparable effect estimates
on a common outcome, (ii) heterogeneity in methods and contexts precludes
pooling, and (iii) the review's purpose is descriptive + agenda-setting,
not effect estimation.

Synthesis steps:
  S1  Bibliometric analysis (RQ1) — descriptive statistics + VOSviewer
      networks (min cluster size = 5; resolution = 1.0).
  S2  Maturity classification (RQ2) — primary + secondary level per study,
      with in-paper evidence quote; aggregation into 2D heat-maps.
  S3  Method × Resource matrix (RQ3) — cross-tabulation of methods by
      maturity level by resource intensity.
  S4  Gap analysis (RQ4) — 3D heat-map for combinatorial gap; method-by-
      level matrix; country comparison; greenfield-vs-brownfield comparison;
      open-problems list extracted by thematic synthesis (Braun & Clarke
      2006: familiarisation → initial coding → theme search → review →
      define).
  S5  Research agenda (RQ5a) — Priority_score = w1 × gap_size + w2 ×
      demand + w3 × feasibility; default w1 = w2 = w3 = 1/3; sensitivity
      analysis by varying weights.
  S6  Conditional roadmap (RQ5b) — table of current level × port size ×
      vintage → recommended next level + open-source toolkit + cost
      estimate.
  S7  Expert validation — Delphi-lite panel of 3–5 senior researchers and
      port-industry experts validates the maturity classification scheme
      and the proposed research agenda; results integrated as a
      methodological triangulation rather than a co-rater process.

Sensitivity analyses:
  - Recall validation against 78 a priori seed papers; if recall < 95%
    → execute SA-1, SA-2, SA-3 enlarged searches.
  - Weight sensitivity in Priority_score (w1, w2, w3 perturbed).
  - Threshold sensitivity for "gap" definition (≤ 3 vs. ≤ 5 studies per
    cell).
```

---

## 14. Meta-bias(es)

```text
Three sources of meta-bias are pre-considered and addressed:

  1. Publication bias — DT-port research is a fast-moving field where
     positive results may be over-reported. Mitigated by:
       - Including conference papers and review articles (not journals only).
       - Supplementary searches via Springer Link and Taylor & Francis to
         capture publisher pipelines lagging in Scopus.
       - Google Scholar supplementary search to capture grey literature
         and preprints (with peer-review check at full text).

  2. Database coverage bias — primary databases (Scopus + IEEE) may miss
     niche venues. Mitigated by:
       - Recall validation on 78 seed papers (recall ≥ 95% threshold).
       - Backward + forward snowballing on 6 seed papers.
       - Hand-search of 10 priority journals.

  3. Selective reporting / language bias — restricting to English may
     miss Chinese-language DT research. Acknowledged as a limitation
     and reported as the count of EC9 exclusions for transparency.

  4. Single-reviewer bias — addressed by intra-rater reliability protocol
     (Cohen's κ ≥ 0.75) and Expert Validation (Delphi-lite panel).
```

---

## 15. Confidence in cumulative evidence

```text
Confidence in the cumulative findings is assessed qualitatively at the
review level (no GRADE for individual outcomes, as no effect estimates
are pooled).

  15a. Per-RQ confidence assessment.
       For each of RQ1–RQ5, confidence in the cumulative evidence is
       reported as High / Moderate / Low / Very Low, based on:
         - Number of included studies.
         - Methodological quality (mean Q1–Q8 score).
         - Consistency across studies (e.g., agreement on maturity
           level for similar contexts).
         - Geographic and contextual diversity.

  15b. Limitations explicitly reported.
       - Single-reviewer model (mitigated as per Item 3 + 12).
       - English-only language scope (count of EC9 exclusions reported).
       - Database coverage (mitigated as per Item 14).
       - Maturity-classification subjectivity (mitigated by published
         rubric + intra-rater κ + Expert Validation).
       - Resource-intensity classification subjectivity (mitigated by
         published 3-tier definition).

  15c. Implications for practice and research.
       The review's primary practical contribution is the conditional
       roadmap (RQ5b) — explicitly cautioned against generalization
       beyond the port size × vintage combinations supported by
       included evidence.
```

---

## 16. Amendments

```text
Any amendments to this protocol after registration will be:
  - Logged internally with version, date, rationale, and impact assessment.
  - Submitted as an OSF Amendment to this Registration (OSF Project
    Registrations tab → Add Amendment).
  - Reported transparently in the manuscript (PRISMA 2020 Item 24c) and
    in the supplementary deviation log.

Amendments will be classified as:
  - Editorial (typo, clarification with no methodological change) —
    documented but no Amendment submission required.
  - Substantive (changes to eligibility, search strategy, extraction
    fields, or analysis plan) — Amendment submission required BEFORE
    the affected stage is executed when feasible.
  - Post-hoc (changes after data collection) — Amendment submission
    required and clearly flagged in the manuscript as a deviation.
```

---

## 17. Funding

```text
[To be filled by NCS — example wording below if no external funding]

This systematic review is conducted as part of the lead reviewer's
doctoral thesis at [Institution]. No external funding has been received
specifically for this review. The lead reviewer's PhD scholarship is
provided by [funding body or "self-funded"].

[If institutional / project funding applies, list grant number + funder
+ role of funder in the review.]
```

---

## 18. Conflicts of interest

```text
The lead reviewer and supervisors declare no conflicts of interest. None
of the authors has financial or non-financial competing interests with
the digital-twin platforms, vendors, or port operators discussed in the
included literature.

[NCS to confirm and update if any supervisor or co-author has consulting
or vendor relationships.]
```

---

## 19. Support / acknowledgments

```text
[To be filled by NCS]

Acknowledgment: [name of academic librarian who reviewed the search
strategy]; [name of port-industry expert(s) consulted during the Delphi-lite
validation]; [name of any colleague who provided feedback on this protocol].
```

---

## 20. Data sharing plan

```text
Open Science Framework (OSF) Project: https://osf.io/dxjw9/

The following artefacts will be hosted in the OSF Project under license
CC-BY 4.0 Attribution International:

  - This pre-registered protocol (PDF + Markdown).
  - Public-release versions of: Research Questions document, Search
    Strategy, Eligibility Criteria, Data Extraction Form, WorkPlan
    (with internal-only labels stripped).
  - All RIS export files from each database query, organized per query
    and per database.
  - Deduplication script + dedup report + cross-validation against
    Rayyan auto-dedup.
  - Phase A pre-screening Python script + decisions CSV.
  - Phase B Rayyan formal screening export + reasons taxonomy.
  - Full-text screening decisions CSV + EC code per excluded study.
  - PRISMA 2020 flow diagram (PNG + source).
  - Data extraction CSV (40 fields × N included studies).
  - Quality appraisal CSV (Q1–Q8 scores).
  - Bibliometric report + 5 VOSviewer maps.
  - Synthesis outputs: 3D heat-map, method matrix, gap tables, research
    agenda, conditional roadmap.
  - Manuscript supplementary package on submission.

Intra-individual identifiers (e.g., expert names in the Delphi-lite
validation) are pseudonymized; only aggregate validation results are
shared. No personal data are collected from human participants beyond
expert opinions; no IRB approval is required as no experimental
intervention is performed.

The OSF Project is set to Public from the start of the registration to
ensure full transparency in line with PRISMA 2020 Items 24a–24c.
```

---

# §III. CHECKLIST CHO NCS — TRƯỚC KHI SUBMIT

NCS làm tuần tự trước khi submit Registration ở Bước 1.5:

- [ ] §3 Authors — điền tên Supervisor 1 + Supervisor 2 + Affiliation + ORCID (nếu có).
- [ ] §17 Funding — chọn 1 trong 3 wording: (a) self-funded; (b) học bổng cấp nhà nước/đơn vị; (c) project funding cụ thể (kèm grant number).
- [ ] §18 Conflicts of interest — xác nhận hoặc bổ sung relationship của co-author.
- [ ] §19 Support — điền tên thư viện / chuyên gia tư vấn (nếu chưa có, để placeholder).
- [ ] Đọc lại §4 Rationale — chỉnh nếu cảm thấy chưa khớp với định hướng luận án.
- [ ] Đọc lại §5 Objectives — verify 5 RQ + sub-questions paste đúng từ SoT.
- [ ] Đọc lại §11 Outcomes — verify P1–P10 reflect đúng output Bước 16–17.
- [ ] **Verify OSF Project `dxjw9` ở chế độ Public** trước khi submit Registration.
- [ ] Sau khi submit → Registration DOI sẽ được phát hành → chuyển NCS → Claude (Bước 1.6 + 1.8 update header 5 file v1.0 + osf_release/).

---

# §IV. CẢNH BÁO QUAN TRỌNG

1. **Pre-registration là binding** — sau Submit ở Bước 1.5, nội dung này trở thành reference public. Mọi sửa đổi phải qua OSF Amendment.
2. **KHÔNG paste chuỗi `v5.6` lên OSF** — nội dung trên đã strip. Nếu NCS edit thêm, kiểm tra lại trước khi submit.
3. **Single-reviewer model phải declare rõ ở §3 + §12** — đã làm. Reviewer Q1 sẽ kiểm tra điểm này nghiêm.
4. **No meta-analysis** declare ở §11 + §13 — đã làm. Đảm bảo PRISMA Items 12, 13e, 14, 15, 19, 20c, 21, 22 được flag N/A trong PRISMA Checklist (Bước 19).
5. **Recall validation 78 seeds** là điều kiện chấp nhận pool ở Bước 15.1 — đã declare ở §7 + §13.

---

# §V. PHIÊN BẢN

| Phiên bản | Ngày | Thay đổi |
|-----------|------|----------|
| v1.0 | 2026-05-10 | Tạo mới — soạn 20 mục PRISMA-P cho OSF Registration của Project `dxjw9` (Bước 1.3 WorkPlan) |
