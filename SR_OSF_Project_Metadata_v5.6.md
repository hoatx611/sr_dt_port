# DỰ THẢO METADATA OSF PROJECT

**Phiên bản:** v1.0 — 2026-05-10
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**Mục đích:** Hỗ trợ NCS điền các trường metadata trên giao diện OSF Project (Bước 1.2 WorkPlan). NCS có thể chỉnh trước khi paste lên OSF.
**Lưu ý:** Toàn bộ nội dung dưới đây ĐÃ STRIP nhãn nội bộ (theo memory rule). KHÔNG paste bất kỳ chuỗi `v5.6` hoặc `vN.M` nào lên OSF.

---

# §I. TITLE (1 dòng, ≤ 200 ký tự)

```text
Digital Twin for Container Port Operations: A Systematic Review of Maturity, Methods, and Research Agenda (2015–2026)
```

**Đếm:** 117 ký tự — trong giới hạn OSF.

**Ghi chú:**

- "Container Port" — phạm vi hẹp đúng theo eligibility (KHÔNG bao gồm bulk/RoRo/cruise terminal).
- "Maturity, Methods, and Research Agenda" — mirror trực tiếp 5 RQ (RQ2 maturity, RQ3 methods, RQ5 research agenda).
- "(2015–2026)" — temporal scope giúp reviewer Q1 nhanh nắm phạm vi.

---

# §II. DESCRIPTION (≤ 1000 ký tự khuyến nghị, OSF không hard-limit)

```text
This Open Science Framework project hosts the protocol, search artifacts, screening decisions, extraction data, and supplementary materials of a systematic review (SR) on the use of Digital Twin (DT), Digital Shadow, and Cyber-Physical Systems for the operations of container ports, covering peer-reviewed literature published between January 2015 and the cut-off date of the search.

The review is conducted in strict adherence to the PRISMA 2020 statement (Page et al. 2021), the PRISMA-S extension for literature search reporting (Rethlefsen et al. 2021), the PRESS peer-review checklist (McGowan et al. 2016), and the Kitchenham & Charters (2007) guidelines for systematic reviews in software engineering. The SR is a qualitative typology synthesis with a bibliometric layer (Donthu et al. 2021); no meta-analysis is performed.

The review answers five research questions: (RQ1) the descriptive landscape of DT-port research; (RQ2) maturity levels (L1 Visibility, L2 State, L3 Decision Support, L4 Simulation with V&V, L5 Closed-Loop Autonomy) across five operational areas (berth, yard, quay crane, AGV, gate) and four port-size classes (megaport, large, mid-size, small); (RQ3) methodological approaches and resource requirements; (RQ4) research gaps along five dimensions (combinatorial, method, geographic, vintage, open problems); and (RQ5) a research agenda and a conditional roadmap for resource-constrained ports in Vietnam and Southeast Asia.

The repository will host: (i) the registered protocol and amendments; (ii) reproducible search strategies for Scopus, IEEE Xplore, Google Scholar, Springer Link, and Taylor & Francis; (iii) the deduplication pipeline and audit trail; (iv) screening and extraction decisions with intra-rater reliability evidence; (v) PRISMA 2020 flow diagram; (vi) thematic synthesis, heat-maps, and the research agenda; and (vii) the final manuscript supplementary package.

Target outlet: Q1 journal (preferred: International Journal of Production Research; alternative: Maritime Policy & Management).

License: CC-BY 4.0.
```

**Đếm:** ~2.090 ký tự — vẫn nằm trong khuyến nghị (OSF cho phép tới ~5.000 ký tự thực tế).

**Ghi chú:**

- KHÔNG nhắc "v5.6" hoặc "RESET 2026-05-08" (memory rule).
- Có nêu `target outlet` để reviewer/visitor OSF biết định hướng.
- Đã liệt kê 5 RQ rõ ràng — phục vụ pre-registration transparency.

---

# §III. CATEGORY (chọn 1 trong dropdown OSF)

```text
Project
```

**Lý do:** OSF "Project" là umbrella cho hoạt động nhiều giai đoạn (search → screen → extract → synthesize → write). Các category con (Analysis, Methods and Measures, Communication, Data, Hypothesis, Instrumentation, Procedure, Software) sẽ được dùng cho các **Component** con bên dưới Project (xem §VI).

---

# §IV. TAGS (free text, OSF cho phép nhiều — đề xuất 10)

```text
digital twin
container port
port operations
systematic review
PRISMA 2020
maritime logistics
cyber-physical systems
bibliometric analysis
maturity model
research agenda
```

**Lý do chọn:** Mix giữa (i) công nghệ — DT, CPS; (ii) lĩnh vực — port operations, maritime logistics; (iii) phương pháp — SR, PRISMA, bibliometric; (iv) đầu ra — maturity model, research agenda. Bao quát keyword search trên OSF + Google.

---

# §V. LICENSE (chọn 1 trong dropdown OSF)

```text
CC-BY 4.0 Attribution
```

**Tên đầy đủ:** Creative Commons Attribution 4.0 International.

**Lý do:**

- Tuân thủ WorkPlan §0.5 Backup Policy (đã pre-định CC-BY 4.0).
- CC-BY là yêu cầu mặc định của hầu hết Q1 journal mở (open data + open materials).
- Cho phép reviewer + cộng đồng tái sử dụng artifacts SR (search query, extraction CSV) với attribution.

---

# §VI. COMPONENTS (cấu trúc Project — Tab "Files" + sub-projects)

OSF cho phép tạo Component con trong Project. Đề xuất cấu trúc 5 Component để mirror 6 Pha WorkPlan:

| Component | Category | Mục đích |
|-----------|----------|----------|
| **01_protocol** | Procedure | Chứa file protocol đã strip nhãn nội bộ (RQ + Strategy + WorkPlan + Eligibility + Extraction Form) — paste từ `osf_release/` ở Bước 1.7+1.9 |
| **02_search** | Data | RIS files raw từ Scopus/IEEE/GS/Springer/T&F + dedup output (Bước 4–7) |
| **03_screening** | Data | screening_pre.csv + ta_screening.csv + fulltext_decisions.csv + Rayyan export (Bước 8–9) |
| **04_extraction** | Data | extraction.csv + quality_appraisal.csv + classification rubric output (Bước 11–13) |
| **05_synthesis** | Analysis | bibliometric figures (PNG) + heat-map 3D + research agenda + thematic synthesis (Bước 16–17) |

**Lưu ý:** Component có thể tạo dần theo từng Pha — KHÔNG cần tạo hết ở Bước 1.2. Hiện tại Bước 1.2 chỉ cần cấu hình metadata Project chính. Component sẽ tạo khi đến Bước tương ứng.

---

# §VII. CONTRIBUTORS (NCS chỉ định)

OSF cho phép thêm contributor với 3 quyền: Read / Read+Write / Administrator. NCS điền theo thực tế:

| Vai trò | Tên | OSF account | Quyền | Bibliographic |
|---------|-----|-------------|-------|---------------|
| Lead reviewer (NCS) | HoaTX | _[NCS điền]_ | Administrator | ✅ |
| Supervisor 1 | _[GS hướng dẫn 1]_ | _[NCS điền]_ | Read+Write | ✅ |
| Supervisor 2 (nếu có) | _[GS hướng dẫn 2]_ | _[NCS điền]_ | Read+Write | ✅ |
| Co-author (nếu có) | _[NCS điền]_ | _[NCS điền]_ | Read+Write | ✅ |

**Ghi chú:**

- "Bibliographic ✅" = sẽ xuất hiện trong citation OSF Project. NCS phải xác nhận từng người đồng ý làm bibliographic contributor TRƯỚC khi check.
- Lead reviewer (NCS) bắt buộc Administrator để có quyền Submit Registration ở Bước 1.5.
- Supervisor đánh `Read+Write` để có thể review/sửa file trong Project trước khi NCS submit Registration.

---

# §VIII. AFFILIATED INSTITUTION (1 hoặc nhiều)

```text
_[NCS điền tên đơn vị]_
```

**Ví dụ:**

- Đại học Quốc gia Hà Nội (Vietnam National University, Hanoi) — VNU
- Đại học Bách khoa Hà Nội (Hanoi University of Science and Technology) — HUST
- Đại học Giao thông Vận tải (University of Transport and Communications) — UTC
- Đại học Hàng hải Việt Nam (Vietnam Maritime University) — VMU

**Khuyến nghị:** Điền tên tiếng Anh để reviewer Q1 quốc tế nhận diện. NCS có thể thêm nhiều affiliation nếu hợp tác nhiều đơn vị.

---

# §IX. CHECKLIST CẤU HÌNH OSF PROJECT (Bước 1.2)

NCS làm tuần tự trên giao diện OSF Project `dxjw9`:

- [ ] Mở <https://osf.io/dxjw9/settings/>
- [ ] Trường **Title** → paste §I
- [ ] Trường **Description** → paste §II
- [ ] Trường **Category** → chọn `Project` (§III)
- [ ] Trường **Tags** → paste 10 tags từ §IV (mỗi tag enter 1 lần)
- [ ] Trường **License** → chọn `CC-BY 4.0 Attribution` (§V)
- [ ] Trường **Affiliated Institution** → điền §VIII
- [ ] Tab **Contributors** → thêm theo §VII (xác nhận quyền + bibliographic)
- [ ] Tab **Wiki** → tạo trang `Home` ngắn (~100 từ) trỏ tới Description + link Component (sẽ tạo dần)
- [ ] Project status → giữ **Public** ngay từ đầu (yêu cầu pre-registration OSF transparency)
- [ ] Save tất cả thay đổi

**Sau khi xong 1.2:** Báo Claude → chuyển sang Bước 1.3 (Claude soạn Registration submission text PRISMA-P 20 mục).

---

# §X. CẢNH BÁO QUAN TRỌNG

1. **KHÔNG nhắc "v5.6" trên OSF Project** — toàn bộ nội dung trên OSF là công khai, phục vụ Q1 manuscript quốc tế.
2. **Public từ đầu** — OSF pre-registration yêu cầu Project ở chế độ Public (nếu để Private, Registration submit Bước 1.5 sẽ không tạo DOI hợp lệ về tính minh bạch).
3. **License CC-BY 4.0 KHÔNG đổi sau Registration** — chọn dứt khoát ở 1.2.
4. **Title KHÔNG đổi sau Registration** — nếu sau này manuscript đổi title, Project title vẫn giữ. Nếu thay đổi lớn về scope, dùng OSF Amendment (Bước 20.3).
5. **Contributors KHÔNG xoá người sau Registration** — chỉ thêm. Nếu thực sự cần xoá, dùng OSF Amendment.

---

# §XI. PHIÊN BẢN

| Phiên bản | Ngày | Thay đổi |
|-----------|------|----------|
| v1.0 | 2026-05-10 | Tạo mới — soạn metadata cho OSF Project `dxjw9` (Bước 1.2 WorkPlan) |
