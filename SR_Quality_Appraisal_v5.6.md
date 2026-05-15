# ĐÁNH GIÁ CHẤT LƯỢNG NGHIÊN CỨU — KITCHENHAM 8 TIÊU CHÍ
# Digital Twin cho Vận hành Cảng Container

**File:** SR_Quality_Appraisal_v5.6.md
**Phiên bản:** v1.0 — 2026-05-14
**NCS:** HoaTX
**OSF Project:** https://osf.io/dxjw9/ (DOI: 10.17605/OSF.IO/DXJW9)
**Tuân thủ:** PRISMA 2020 Item 11 (Quality assessment), Item 18 (Reporting biases)
**Nguồn gốc:** Kitchenham & Charters (2007) "Guidelines for performing SE systematic reviews" — Appendix D.2
**Dùng tại:** Bước 13 (sau data extraction Bước 11 + classification Bước 12)

> Đánh giá chất lượng ở SR định tính dùng để **mô tả landscape** (không dùng để loại bỏ study). Study có điểm thấp vẫn được bao gồm nhưng được ghi chú trong synthesis. Chỉ loại bỏ nếu quality quá thấp đến mức không trích xuất được thông tin có ý nghĩa.

---

# §1. TÁM TIÊU CHÍ CHẤT LƯỢNG

## 1.1 Bảng tiêu chí + câu hỏi + hướng dẫn chấm điểm

| # | Ký hiệu | Tiêu chí | Câu hỏi chấm | 1 (Yes) | 0,5 (Partial) | 0 (No) |
|---|---------|----------|--------------|---------|---------------|--------|
| 1 | **Q1** | Aims clearly stated | Mục tiêu nghiên cứu có được phát biểu rõ ràng không? | Mục tiêu cụ thể, đo lường được, có RQ rõ | Mục tiêu chung chung hoặc chỉ ngầm hiểu | Không có mục tiêu |
| 2 | **Q2** | Context described | Bối cảnh cảng/DT có được mô tả đủ để đánh giá tính tổng quát? | Mô tả rõ cảng (tên/quy mô/vintage), hệ thống DT, dữ liệu | Mô tả một phần; cảng không tên nhưng có thông số | Không mô tả; black-box environment |
| 3 | **Q3** | Research design appropriate | Thiết kế nghiên cứu có phù hợp với mục tiêu không? | Design rõ ràng + phù hợp (vd. DES cho sim; MILP cho optimization; survey cho mapping) | Design phù hợp nhưng không giải thích lý do chọn | Design không phù hợp hoặc không mô tả |
| 4 | **Q4** | Data/case selection clear | Cách chọn dữ liệu/case study có minh bạch không? | Criteria rõ ràng; dữ liệu describe đủ (size, source, period) | Dữ liệu được dùng nhưng không mô tả sampling; "real port data" không rõ | Nguồn dữ liệu không rõ; chỉ synthetic data không khai báo |
| 5 | **Q5** | Data collection rigorous | Quá trình thu thập dữ liệu có chặt chẽ không? | Protocol thu thập rõ; dữ liệu validate; tool describe | Dữ liệu được dùng nhưng protocol mơ hồ | Không mô tả; chỉ "we collected data from port X" |
| 6 | **Q6** | Data analysis appropriate | Phương pháp phân tích có phù hợp với mục tiêu + data không? | Method phù hợp + giải thích lý do chọn; hyperparameter report; convergence show | Method dùng đúng nhưng không justify; kết quả thiếu CI/std | Method không phù hợp; no statistical comparison |
| 7 | **Q7** | Findings stated clearly | Phát hiện có được trình bày rõ ràng với bằng chứng không? | Kết quả số cụ thể; so sánh baseline; bảng/hình rõ | Kết quả định tính + một số số liệu | Kết quả mơ hồ; chỉ tuyên bố "better" không có bằng chứng |
| 8 | **Q8** | Value of research established | Đóng góp của nghiên cứu có được establish rõ ràng không? | Đóng góp rõ vs. baseline/prior work; limitations ghi rõ; future work cụ thể | Đóng góp nêu ra nhưng không so sánh với prior work | Không rõ đóng góp; không có discussion |

## 1.2 Thang điểm

| Điểm tổng | Mức chất lượng | Hàm ý synthesis |
|-----------|----------------|-----------------|
| 7,0 – 8,0 | **Cao (High)** | Tin cậy cao; kết quả trích xuất đầy đủ |
| 5,0 – 6,5 | **Trung bình (Medium)** | Kết quả trích xuất; ghi chú limitation trong synthesis |
| 3,0 – 4,5 | **Thấp (Low)** | Trích xuất có chọn lọc; cảnh báo trong synthesis |
| < 3,0 | **Rất thấp (Very Low)** | Cân nhắc loại nếu không trích xuất được thông tin có ý nghĩa |

---

# §2. HƯỚNG DẪN ĐẶC THÙ CHO SR DT-CẢNG

## 2.1 Q3 — Design phù hợp theo loại bài

| Loại nghiên cứu | Design phù hợp → Q3 = 1 |
|-----------------|--------------------------|
| Optimization | MILP/CP/heuristic + benchmark comparison; convergence plot |
| RL/DRL | Training curve; test environment describe; hyperparameter report |
| DES/Simulation | Warm-up period; run length justification; output analysis (confidence interval) |
| Case study | RQ rõ; data from real port; analysis triangulation |
| Survey/Review | Protocol ghi rõ; mapping logic; classification scheme |
| Prototype | Architecture describe; implementation detail; test scenario |

## 2.2 Q4 — Data real vs. synthetic

- **Real port data (Q4=1):** named port hoặc mô tả đủ để identify; time period; data volume.
- **Synthetic data (Q4=0.5):** clearly stated as synthetic/generated; validation against real distribution.
- **Unknown (Q4=0):** không rõ real hay synthetic; "industry partner" không có detail.

## 2.3 Q6 — Baseline comparison

- Study không có baseline comparison → Q6 tối đa 0.5 (trừ case study một-cảng không có alternative method).
- Study so sánh với state-of-art → Q6 = 1 nếu so sánh fair.

## 2.4 Q8 — Limitations

- Ghi rõ limitations (dataset scope, generalizability, scalability) → +0.5 điểm cho Q8.
- Không ghi limitations → Q8 ≤ 0.5.

---

# §3. QUY TRÌNH CHẤM ĐIỂM

```
Bước 1: Đọc toàn văn (không skip section nào)
Bước 2: Trả lời 8 câu hỏi Q1-Q8 theo bảng §1.1
Bước 3: Gán điểm 0/0.5/1 cho mỗi Q — ghi lý do ngắn gọn (<20 words)
Bước 4: Tính tổng điểm (max 8)
Bước 5: Xếp mức High/Medium/Low/Very Low theo bảng §1.2
Bước 6: Ghi vào quality_appraisal_v5.6.csv
Bước 7: Nếu có borderline → ghi vào borderline_decisions_log.md
```

---

# §4. TEMPLATE CSV OUTPUT

File output: `quality_appraisal_v5.6.csv`

| Column | Mô tả | Giá trị |
|--------|-------|---------|
| `study_id` | ID từ dedup.py | S-XXXXX |
| `doi` | DOI | string |
| `title` | Tiêu đề (truncation nghiêm cấm) | string |
| `Q1` | Aims | 0 / 0.5 / 1 |
| `Q2` | Context | 0 / 0.5 / 1 |
| `Q3` | Design | 0 / 0.5 / 1 |
| `Q4` | Data selection | 0 / 0.5 / 1 |
| `Q5` | Data collection | 0 / 0.5 / 1 |
| `Q6` | Analysis | 0 / 0.5 / 1 |
| `Q7` | Findings | 0 / 0.5 / 1 |
| `Q8` | Value | 0 / 0.5 / 1 |
| `total_score` | Tổng = Q1+…+Q8 | 0.0 – 8.0 |
| `quality_level` | Mức | High / Medium / Low / Very Low |
| `notes` | Ghi chú borderline / cảnh báo | string |
| `reviewer_date` | Ngày chấm | YYYY-MM-DD |

---

# §5. QUY TẮC INTRA-RATER RELIABILITY (Bước 14.2)

Sau Bước 11 hoàn tất — NCS chấm lại 5 studies ngẫu nhiên sau ≥ 14 ngày (không xem kết quả lần 1):
- Tính **weighted Cohen's κ** (weights = linear) cho tổng điểm tứ phân vị (High/Medium/Low/VeryLow).
- Mục tiêu: **κ ≥ 0.75**.
- Nếu κ < 0.75 → review và làm rõ các tiêu chí có disagreement → cập nhật §2 file này → version 1.1.

---

# §6. GHI CHÚ VỀ CHỨC NĂNG CỦA QA TRONG SR NÀY

Vì đây là SR **định tính (qualitative typology)**, không phải meta-analysis:

1. Quality scores KHÔNG dùng để **loại trừ** study (trừ Very Low < 3.0 không trích xuất được gì).
2. Quality scores dùng để:
   - Ghi chú **strength of evidence** trong synthesis tables.
   - Identify papers cần **sensitivity analysis** (Bước 15).
   - Báo cáo trong manuscript Methods §3.5 và Supplementary.
3. Distribution of quality scores ghi vào PRISMA Item 11 và Table 1 manuscript.

---

# §7. VERSIONING

| Version | Ngày | Thay đổi |
|---------|------|----------|
| **v1.0** | 2026-05-14 | Tạo ban đầu — 8 tiêu chí Kitchenham; hướng dẫn DT-cảng; template CSV; intra-rater protocol |

---

# §8. LIÊN KẾT

| File | Quan hệ |
|------|---------|
| `SR_Classification_Rubric_v5.6.md` | Chạy song song — cùng study, cùng Bước 12–13 |
| `SR_Data_Extraction_Form_v5.6.md` | Group E (Quality scores) nhận data từ rubric này |
| `WorkPlan_v5.6_FINAL.md` | Bước 13 + Bước 14.2 |
| `SR_PRISMA_Checklist_v5.6.md` | Item 11 (Quality assessment methods) |

---

*SR_Quality_Appraisal_v5.6.md — v1.0 — 2026-05-14 — NCS HoaTX*
