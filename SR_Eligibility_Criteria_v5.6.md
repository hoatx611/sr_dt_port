# TIÊU CHÍ BAO GỒM / LOẠI TRỪ
# Digital Twin cho Vận hành Cảng Container

**Phiên bản:** v1.0 — 2026-05-08
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**OSF DOI:** [10.17605/OSF.IO/DXJW9](https://doi.org/10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 Item 5 (Eligibility criteria)
**Anchor:** `SR_Research_Questions_v5.6.md` v1.0 — IC2-IC5 align với 5 lĩnh vực vận hành (RQ2)

---

# §I. KHUNG PICOC

Tổng quan hệ thống thuộc lĩnh vực Engineering / Operations Research nên dùng khung **PICOC** thay cho PICO truyền thống của y học:

| Thành phần | Định nghĩa cho SR DT-Cảng |
|------------|---------------------------|
| **P — Population** | Cảng container biển (container terminal, seaport) — bao gồm Automated Container Terminal (ACT), semi-automated, conventional CT có công nghệ DT. Áp với mọi quy mô (megaport / lớn / vừa / nhỏ) và mọi vintage (greenfield / brownfield) |
| **I — Intervention** | Ứng dụng Digital Twin (DT), Digital Shadow, Cyber-Physical System (CPS) cho vận hành cảng — bao gồm: lập lịch (scheduling), tối ưu (optimization), mô phỏng (simulation), giám sát (monitoring), trực quan hoá (visualization), bảo trì (maintenance), closed-loop autonomy (L5) |
| **C — Comparison** | Phương pháp truyền thống không dùng DT (rule-based, mô phỏng đơn lẻ không sync real-time) — không bắt buộc; bài chỉ trình bày DT vẫn được bao gồm |
| **O — Outcome** | Hiệu quả vận hành (throughput, dwell time, makespan); độ chính xác (accuracy, RMSE); chất lượng quyết định; cấp độ tự động hoá; hoặc đóng góp lý thuyết về kiến trúc/framework DT |
| **C — Context** | Cảng container biển trên thế giới (toàn cầu, không giới hạn vùng); 2015–2026; tiếng Anh |

---

# §II. TIÊU CHÍ BAO GỒM (Inclusion Criteria — IC)

Một bài được bao gồm nếu **thoả mãn ≥ 1 trong 5 tiêu chí IC1–IC5** kèm điều kiện chung (§V).

## IC1 — DT/CPS + container terminal operations

**Định nghĩa:** Bài có (a) khái niệm Digital Twin / Digital Shadow / Cyber-Physical System rõ ràng (≥ 2/3 thuộc tính DT theo Grieves 2014 — xem RQ doc §2.1), AND (b) áp dụng cho vận hành cảng container.

**Ví dụ tích cực:** "Digital twin-driven real-time collaborative scheduling for U-shaped automated container terminals" (IJPR 2025).

**Ví dụ tiêu cực:** "Digital twin for ship hull structural monitoring" → áp DT cho tàu (vessel), không phải cảng → loại theo EC1.

## IC2 — Optimization / scheduling tại container terminal

**Định nghĩa:** Bài về tối ưu hoá hoặc lập lịch tại CT có **tích hợp với DT/sim/IoT** ở **bất kỳ trong 5 lĩnh vực vận hành**:

1. **Berth** — berth allocation, berth scheduling
2. **Quay crane** — quay crane scheduling, crane assignment
3. **Yard** — yard management, yard allocation, stack planning, RMG/RTG operation
4. **AGV / horizontal transport** — AGV dispatching, AGV scheduling, AGV routing
5. **Gate** — gate operation, truck appointment system, gate scheduling, drayage

Không bao gồm bài thuần OR/MILP/heuristic không có cấu phần DT.

**Ví dụ tích cực:** Bài dùng DT để feed dữ liệu real-time vào solver berth allocation; bài thiết kế truck appointment system với DT-based gate prediction.

**Ví dụ tiêu cực:** Bài thuần MILP tối ưu berth allocation, không dùng DT → loại theo EC4.

## IC3 — Simulation / V&V tại container terminal

**Định nghĩa:** Bài về mô phỏng rời rạc (DES), agent-based simulation, hardware-in-the-loop, validation/verification của mô hình cảng container — có yếu tố DT (sync với hệ thống thực) hoặc emulation phục vụ DT.

## IC4 — IoT / monitoring tại container terminal

**Định nghĩa:** Bài về IoT, sensor networks, real-time monitoring tại CT — có liên kết với DT (data lake feeding DT, hoặc IoT là cấu phần của DT framework). Bao gồm cả **smart port** với architecture đầy đủ (đáp ứng ≥ 2/3 thuộc tính DT).

## IC5 — Visualization / 3D / 4D / GIS tại container terminal

**Định nghĩa:** Bài về trực quan hoá 3D/4D, GIS-based representation cho cảng container — có yếu tố DT (3D model là digital representation của thực thể vật lý).

---

# §III. TIÊU CHÍ LOẠI TRỪ LỚP 1 (Title/Abstract — EC)

Áp dụng ở Bước 8 — Pha A `screening.py` regex pre-screen + Pha B Rayyan formal screen.

## EC1 — Tàu / ngoài khơi, không phải vận hành cảng

DT cho ship hull, marine engine, offshore platform, vessel routing không liên quan đến terminal operations.

## EC2 — Cảng rời / tàu chở dầu, không phải container

Bulk terminal, tanker terminal, oil terminal, LNG terminal, coal terminal, grain terminal, ore terminal, cruise terminal, ferry terminal, RoRo terminal — không phải container terminal.

## EC3 — Không phải bài nghiên cứu

Editorial, letter, news, book review, conference abstract (không có full paper), poster, magazine article không có methodology.

## EC4 — Có bối cảnh cảng nhưng không có DT/sim/optim/IoT

Bài về cảng container nhưng nội dung là policy, governance, port economics thuần — không có cấu phần DT/method liên quan.

## EC5 — Trùng nội dung (deduplication)

Bài đã bị Rayyan auto-dedup hoặc Python dedup phát hiện. Chỉ dùng EC5 cho dup phát hiện trong Rayyan; dup từ Python đã loại trước Bước 8.

## EC6 — Không truy cập được toàn văn

Áp dụng ở Bước 9 (Fulltext) — không phải Bước 8.

## EC7-{mfg, bim, health, noctx, other} — DT ngoài lĩnh vực cảng

- **EC7-mfg:** DT manufacturing (Industry 4.0 cho nhà máy, không phải cảng)
- **EC7-bim:** DT construction / Building Information Modeling cho dân dụng
- **EC7-health:** DT healthcare (digital twin của cơ thể người, bệnh nhân)
- **EC7-noctx:** DT định nghĩa nhưng không có ngữ cảnh cảng container
- **EC7-other:** DT cho domain khác (smart city, agriculture, retail) không liên quan cảng

## EC8 — CPS không có ngữ cảnh cảng

Cyber-Physical System nói chung, không áp cụ thể cho cảng container. Lưu ý: CPS + cảng container vẫn IC1.

## EC9 — Ngôn ngữ không phải tiếng Anh

Không có abstract tiếng Anh, hoặc full paper không phải tiếng Anh. Đếm số bài bị loại để minh bạch (PRISMA Item 23c, Limitations).

## EC-CYBER — An toàn thông tin (cybersecurity)

Bài về cybersecurity của cảng / SCADA / OT security — không phải vận hành (operations).

## EC-ENERGY — Năng lượng / lưới điện nhỏ / giảm phát thải

Microgrid cảng, hydrogen/ammonia maritime fuel, cold ironing, all-electric ship power sharing — không phải vận hành container.

## EC-GENERIC — Chính sách / thương mại hàng hải

Maritime trade policy, port governance, geopolitical analysis, Belt-Road Initiative — không có cấu phần DT/operations.

## EC-IT — Container công nghệ thông tin (Kubernetes/Docker)

"Container" trong ngữ cảnh CNTT (Docker container, Kubernetes orchestration) — không phải shipping container.

## EC-NOSCOPE — Không có từ khoá nào trong phạm vi

Bài về port-Hamiltonian dynamics, port (USB/network/COM), port number, wine port, side-channel CPU port — không phải cảng biển.

## EC-PAX — Phà / hành khách / du lịch

Passenger terminal, ferry, cruise — không phải container.

## EC-STRUCT — Giám sát kết cấu dân dụng

Structural health monitoring của cầu, wharf concrete, seismic analysis — không phải crane/terminal equipment monitoring tại CT.

---

# §IV. TIÊU CHÍ LOẠI TRỪ LỚP 2 (Fulltext — EC tiếp tục)

Áp dụng ở Bước 9 (Fulltext Screening) — sau khi đọc toàn văn.

## EC-ENV — Môi trường / sinh thái

Coastal management, biofouling, marine life, ballast water treatment, ecology of port — không phải DT operations.

## EC-VESSEL — Vận hành tàu không tại bến

Inland waterway, ship maneuvering, AIS-only tracking, ship voyage, ship inspection — xa terminal interface.

## EC-POLICY — Kinh tế / chính sách / quản trị cảng

Port economics, port governance, port concession, DEA/TOPSIS/AHP-only papers — không có DT/method core.

## EC-SECUR — An ninh cảng

Port security architecture, hazmat handling, COVID-port — không phải DT operations.

## EC-BLOCK — Chuỗi khối ngoài vận hành

Blockchain for trade documents, smart contract for shipping — không phải DT operations.

## EC-TELECOM — Viễn thông / 5G ngoài vận hành

5G/6G architecture cho cảng — chỉ tập trung communication layer, không phải DT operations.

## EC-CUSTOMS — Hải quan / cửa khẩu

Customs clearance, port-of-entry, import/export brokerage — không phải DT terminal operations.

## EC-AGRI — Nông nghiệp / chăn nuôi

Bài liên quan đến agricultural ports, livestock terminals — out of scope.

---

# §V. ĐIỀU KIỆN CHUNG (áp cho mọi IC1–IC5)

| Điều kiện | Giá trị |
|------------|---------|
| Khoảng năm xuất bản | **2015 ≤ PY ≤ 2026** |
| Ngôn ngữ | English — abstract bắt buộc, full paper ưu tiên |
| Loại tài liệu | Journal article, Conference paper, Review article, Book chapter (peer-reviewed) |
| Loại tài liệu LOẠI TRỪ | Editorial, Letter, News, Magazine (non-peer-reviewed), Conference abstract không kèm full paper, Poster, Patent, Thesis (trừ khi có tạp chí kèm theo), Preprint chưa peer-reviewed |
| Phạm vi địa lý | Toàn cầu, không hạn chế |
| Quy mô cảng | Mọi quy mô (megaport / lớn / vừa / nhỏ / unspecified) — phục vụ RQ2c |
| Vintage | Mọi vintage (greenfield / brownfield / mixed / unspecified) — phục vụ RQ4d |
| Tính tiếp cận | Có abstract tiếng Anh tối thiểu để sàng lọc T/A; toàn văn cần có để qua Bước 9 (nếu không có → EC6) |

---

# §VI. QUY TẮC XỬ LÝ BORDERLINE — 6 RULES

Một số bài rơi vào ranh giới khó quyết định. Áp các quy tắc dưới đây nhất quán; mọi quyết định ghi vào `borderline_decisions_log.md` (Bước 13).

## Borderline 1 — DT mention nhẹ vs DT-driven

**Tình huống:** Bài đề cập "digital twin" trong abstract nhưng không phải core method.

**Quy tắc:**
- DT là chỉ motivation/buzzword → EC4
- DT là cấu phần của framework đề xuất nhưng không implement → giữ lại nếu có simulation/optim core (IC2/IC3)
- DT được implement (architecture, prototype, case study) → IC1 chắc chắn

## Borderline 2 — Smart port vs DT

**Tình huống:** Bài về "smart port" với IoT + automation nhưng không gọi tên "digital twin".

**Quy tắc:**
- Có sync real-time giữa physical/cyber + có data model + có decision support → tương đương IC1 (giữ)
- Chỉ IoT thuần (sensor + cloud) không có data model/feedback loop → IC4 (giữ ở Lớp 1, đánh giá lại Lớp 2)

## Borderline 3 — Manufacturing transferable to port

**Tình huống:** Bài DT cho manufacturing/warehouse có potential apply to port.

**Quy tắc:**
- Bài bàn rõ application to port → IC1
- Chỉ generic manufacturing không mention port → EC7-mfg

## Borderline 4 — Bulk/RoRo terminal có cấu phần DT mạnh

**Tình huống:** Bài về DT cho bulk terminal hoặc RoRo có method rất tốt.

**Quy tắc:**
- Mặc định EC2 (không phải container)
- Ngoại lệ: nếu method có thể chuyển trực tiếp (DT framework tổng quát cho any terminal type với case study là bulk) → giữ ở Lớp 1, note ở Lớp 2 để quyết định cuối

## Borderline 5 — Review paper

**Tình huống:** Bài là review/survey về DT cảng.

**Quy tắc:**
- Giữ ở Lớp 1 nếu scope phù hợp (DT + container terminal)
- Ở Lớp 2: nếu là systematic review chính thức → giữ làm reference (cited in Discussion); nếu là narrative review/perspective → có thể giữ làm bài bao gồm hoặc reference tuỳ chất lượng

## Borderline 6 — Greenfield vs Brownfield không xác định

**Tình huống:** Bài DT cảng nhưng không nêu rõ cảng là greenfield (mới xây) hay brownfield (retrofit).

**Quy tắc:**
- Nếu paper mô tả case study tại cảng existing có TOS legacy → classify `port_vintage = brownfield`
- Nếu paper mô tả case study tại cảng mới hoàn toàn (như Tanger Med II, Lạch Huyện, Cái Mép-Thị Vải mới phase 2) → classify `port_vintage = greenfield`
- Nếu paper là theoretical framework không gắn case study cụ thể → classify `port_vintage = unspecified`
- Nếu case study mix (vd. DT cho cảng existing nhưng AGV greenfield deployment) → classify `port_vintage = mixed` + note evidence

**Tại sao cần rule này:** RQ4d (vintage gap) yêu cầu phân biệt rõ greenfield ↔ brownfield. Nếu rule không nhất quán → phân tích RQ4d không đáng tin cậy.

---

# §VII. LIÊN KẾT VỚI T&F-SPECIFIC EXCLUSION

Ngoài 28 mã EC/IC trên, riêng pool T&F (Q12 Strategy — không có Subject filter ở tầng truy vấn) áp thêm bảng exclusion theo tên tạp chí (chi tiết trong `tf_journal_exclusion.py` Bước 8.1):

| Nhóm loại trừ | Tạp chí điển hình | Mã EC mapping |
|----------------|---------------------|------------------|
| Built Environment / Construction | International Journal of Construction Management, Journal of Asian Architecture and Building Engineering | EC-STRUCT |
| Nondestructive Testing | Nondestructive Testing and Evaluation | EC-STRUCT |
| Civil/Structural | Structure and Infrastructure Engineering | EC-STRUCT |
| Nuclear | Nuclear Technology | EC-NOSCOPE |
| HCI / UI–UX | International Journal of Human–Computer Interaction | EC-NOSCOPE |
| Manufacturing / Engineering Design | International Journal of Computer Integrated Manufacturing, Journal of Engineering Design, Production & Manufacturing Research, Virtual and Physical Prototyping | EC7-mfg |
| Y/sinh (theo PB) | Cogent OA, Dove Medical Press | EC7-health |

**Whitelist 5 tạp chí target — luôn cho Rayyan đọc, ngay cả khi Pha A đề xuất EXCLUDE:**

- International Journal of Production Research — Q1 target Paper 2
- Digital Twin — chuyên ngành DT
- International Journal of Logistics Research and Applications
- Maritime Policy & Management — Q1 target SR
- International Journal of Sustainable Transportation

---

# §VIII. VERSIONING

| Version | Ngày | Thay đổi | Phê duyệt |
|---------|------|-----------|-------------|
| **v1.0** | 2026-05-08 | Phiên bản đầu — PICOC khung; 5 IC (IC1-IC5 align 5 lĩnh vực vận hành); 28 mã EC; 6 borderline rules (bao gồm vintage greenfield/brownfield); T&F-specific exclusion + 5 target whitelist | NCS HoaTX (chờ phê duyệt) |

**Quy tắc cập nhật:**

- Sau Bước 8.5 pilot 30 bài — nếu cần sửa định nghĩa IC/EC → version 1.1, ghi lý do
- Sau Bước 14 intra-rater feedback — nếu κ < 0.75 → version 1.2 với clarification
- Mỗi version mới đính kèm OSF Amendments log (Bước 20.3)

---

# §IX. LIÊN KẾT THAM CHIẾU

| File | Quan hệ |
|------|---------|
| `SR_Research_Questions_v5.6.md` | RQ doc — IC2-IC5 align với 5 lĩnh vực vận hành (RQ2) + Borderline 6 align với RQ4d |
| `WorkPlan_v5.6_FINAL.md` | Bước 2 (soạn deliverable này); Bước 8 (Pha A + Pha B áp T/A); Bước 9 (Fulltext áp Lớp 2) |
| `SR_Search_Strategy_v5.6_FINAL.md` §4.12 | T&F-specific exclusion list chi tiết |
| `SR_PRISMA_Checklist_v5.6.md` | Item 5 mapping |
| `SR_Data_Extraction_Form_v5.6.md` | Group D (5 boolean lĩnh vực) + Group D' (port_size, port_vintage) align với IC2 + Borderline 6 |
| `screening.py` | Pha A pre-screen — regex IC/EC implement |
| `tf_journal_exclusion.py` | T&F whitelist + journal exclusion (Bước 8.1) |
| Rayyan Reasons Taxonomy | Bước 1.10 nạp 28 mã EC/IC từ file này |

---

*SR_Eligibility_Criteria_v5.6.md — v1.0 — 2026-05-08 — anchored on RQ_v1.0*
