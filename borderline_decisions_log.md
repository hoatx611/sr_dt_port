# BORDERLINE DECISIONS LOG
# Digital Twin cho Vận hành Cảng Container

**File:** borderline_decisions_log.md
**Phiên bản:** v1.0 — 2026-05-15 (template)
**NCS:** HoaTX
**Dùng tại:** Bước 9.2.2 (Fulltext screening) + Bước 8.2 (Pha B T/A borderline)
**OSF Project:** https://osf.io/dxjw9/

> File này ghi lại MỌI quyết định borderline trong suốt quá trình screening + extraction. Là audit trail quan trọng cho single-reviewer SR. Ghi ngay khi gặp — không để sau. Kết quả tổng hợp báo cáo tại Bước 19 (Limitations §19.2).

---

## §1. ĐỊNH NGHĨA BORDERLINE

Một quyết định borderline xảy ra khi:
1. **Không chắc chắn IC/EC**: Bài vừa đáp ứng IC1 (DT-driven) vừa có dấu hiệu EC
2. **6 Borderline Rules** trong `SR_Eligibility_Criteria_v5.6.md` §VI:
   - **B1** — DT-driven vs DT-mention (ranh giới IC1)
   - **B2** — Smart port / port 4.0 không rõ có DT
   - **B3** — Bài manufacturing có thể transfer sang port
   - **B4** — Bulk/RoRo hybrid terminal (EC2)
   - **B5** — Review paper (IC2 — nếu evidence của 5 RQ thì include)
   - **B6** — Vintage: greenfield/brownfield không nêu rõ
3. **Eligibility không rõ** sau khi đọc fulltext (EC6 uncertainty)
4. **L-level tranh cãi** giữa hai lần chấm (intra-rater)

---

## §2. CẤU TRÚC MỖI MỤC (11 trường)

| Trường | Mô tả |
|--------|--------|
| **BDL-ID** | Mã định danh (BDL-001, BDL-002, …) |
| **study_id** | ID từ dedup_unique.ris (N1 field) |
| **DOI** | DOI bài báo |
| **Title** | Tiêu đề đầy đủ |
| **Ngày gặp** | YYYY-MM-DD |
| **Giai đoạn** | T/A Pha A / T/A Pha B / Fulltext / Extraction / Quality |
| **Borderline type** | B1–B6 hoặc EC-uncertain / L-level |
| **Lý do borderline** | Mô tả cụ thể vì sao khó quyết định |
| **Quyết định** | INCLUDE / EXCLUDE + mã IC/EC |
| **Justification** | Lý do cho quyết định cuối |
| **Trạng thái** | Open / Resolved |

---

## §3. NHẬT KÝ BORDERLINE

*(Điền khi gặp — bắt đầu từ Pha B Rayyan)*

---

### BDL-001 — [TEMPLATE — xóa khi dùng thực]

| Trường | Nội dung |
|--------|----------|
| **BDL-ID** | BDL-001 |
| **study_id** | — |
| **DOI** | — |
| **Title** | — |
| **Ngày gặp** | YYYY-MM-DD |
| **Giai đoạn** | T/A Pha B |
| **Borderline type** | B1 — DT-driven vs DT-mention |
| **Lý do borderline** | Bài đề cập "digital twin" trong abstract nhưng thực tế chỉ mô tả sensor network + dashboard. Không có closed-loop hay decision support. |
| **Quyết định** | EXCLUDE — EC1 (không phải DT thực sự theo IC1) |
| **Justification** | Sau khi đọc fulltext: không có mô hình số hoá phản ánh trạng thái thực. Chỉ là data visualization. IC1 không đạt. |
| **Trạng thái** | Resolved |

---

## §4. PHÂN BỐ BORDERLINE (điền sau khi hoàn thành Pha B)

| Borderline type | Số lượng | INCLUDE | EXCLUDE |
|-----------------|----------|---------|---------|
| B1 (DT-driven vs mention) | TBD | TBD | TBD |
| B2 (Smart port no DT) | TBD | TBD | TBD |
| B3 (Manufacturing transfer) | TBD | TBD | TBD |
| B4 (Bulk/RoRo hybrid) | TBD | TBD | TBD |
| B5 (Review paper) | TBD | TBD | TBD |
| B6 (Vintage unclear) | TBD | TBD | TBD |
| EC-uncertain | TBD | TBD | TBD |
| L-level dispute | TBD | TBD | TBD |
| **Tổng** | **TBD** | **TBD** | **TBD** |

---

## §5. LIÊN KẾT

| File | Quan hệ |
|------|---------|
| `SR_Eligibility_Criteria_v5.6.md` §VI | 6 borderline rules tham chiếu |
| `SR_Classification_Rubric_v5.6.md` | L-level rubric khi tranh cãi |
| `dedup_borderline_pairs.csv` | 19 cặp dedup borderline (score 85–89) |
| `SR_Deviation_Log_v5.6.md` | Nếu borderline dẫn đến sai lệch protocol |
| `SR_PRISMA_Checklist_v5.6.md` Item 23c | Amendments audit trail |

---

*borderline_decisions_log.md — v1.0 template — 2026-05-15 — NCS HoaTX*
