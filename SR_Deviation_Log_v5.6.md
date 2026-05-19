# SR DEVIATION LOG
# Digital Twin cho Vận hành Cảng Container

**File:** SR_Deviation_Log_v5.6.md
**OSF Project:** https://osf.io/dxjw9/ (DOI: 10.17605/OSF.IO/DXJW9)
**Tạo:** 2026-05-14
**Cập nhật lần cuối:** 2026-05-14
**Người duy trì:** NCS HoaTX

> §0.9: Mọi sai lệch so với WorkPlan/Protocol phải được ghi vào file này.
> File này là nguồn duy nhất cho Bước 20.3 OSF Amendments.

---

## Cấu trúc mỗi mục (8 trường)

| Trường | Mô tả |
|--------|--------|
| **DEV-ID** | Mã định danh (DEV-001, DEV-002, …) |
| **Ngày phát hiện** | YYYY-MM-DD |
| **Bước liên quan** | Bước X.Y trong WorkPlan |
| **Mô tả sai lệch** | Điều gì khác so với kế hoạch |
| **Nguyên nhân** | Tại sao xảy ra |
| **Tác động** | Ảnh hưởng đến tính hợp lệ / PRISMA |
| **Hành động khắc phục** | Đã làm gì để xử lý |
| **Trạng thái** | Open / Resolved / OSF Amendment submitted |

---

## Nhật ký sai lệch

---

### DEV-001 — Thứ tự thực hiện: Script code trước khi hoàn tất Bước 1–3 chính thức

| Trường | Nội dung |
|--------|----------|
| **DEV-ID** | DEV-001 |
| **Ngày phát hiện** | 2026-05-11 |
| **Bước liên quan** | Bước 1–3 (Pha 1 chưa hoàn tất) → Bước 7–8 (Pha 2–3) |
| **Mô tả sai lệch** | Các scripts `check_ris_integrity.py`, `dedup.py`, `screening.py`, `tf_journal_exclusion.py` đã được viết và chạy trên corpus thực tế TRƯỚC KHI Bước 1.10–1.13 (Rayyan setup) và Bước 2–3 (Eligibility + Pilot) hoàn tất chính thức theo WorkPlan. Kết quả pipeline đã có sẵn: 7.825 → 5.811 unique → 284/5.051/476 (Pha A). |
| **Nguyên nhân** | NCS ưu tiên test pipeline kỹ thuật sớm để phát hiện lỗi format; dữ liệu tìm kiếm (Bước 4–6) đã thu thập trước khi workflow chính thức được ghi nhận. |
| **Tác động** | **Thấp — không ảnh hưởng tính hợp lệ khoa học.** (i) Search strategy và Eligibility Criteria đã được thiết kế trước khi chạy search; (ii) Scripts sử dụng đúng quy tắc IC/EC từ `SR_Eligibility_Criteria_v5.6.md`; (iii) Không có records nào bị loại bỏ trước khi có criteria; (iv) Toàn bộ audit trail được lưu. |
| **Hành động khắc phục** | (1) Ghi nhận chính thức vào file này (DEV-001); (2) Cập nhật WorkPlan trạng thái phản ánh thực tế; (3) Calibration pilot 30 records (Bước 8.2.2) PHẢI hoàn tất trước khi bắt đầu Pha B Rayyan để đảm bảo κ ≥ 0.75; (4) Ghi vào Limitations manuscript §19.2 rằng pilot search (Bước 3) được thực hiện đồng thời với thiết kế script. |
| **Trạng thái** | **Resolved** — Khắc phục nội bộ; không cần OSF Amendment (pipeline code được đính kèm OSF supplementary bất kể thứ tự, §20.1). |

---

### DEV-002 — Tên file RIS không theo quy ước WorkPlan

| Trường | Nội dung |
|--------|----------|
| **DEV-ID** | DEV-002 |
| **Ngày phát hiện** | 2026-05-11 |
| **Bước liên quan** | Bước 4–6 |
| **Mô tả sai lệch** | WorkPlan quy ước tên file: `Q1_Scopus.ris`, `Q2_Scopus.ris`, … Tên file thực tế: `PRIMARY_Scopus.ris`, `EXTENDED_Scopus.ris`, `T1_Scopus.ris`, …, `T7_IEEE.ris`. |
| **Nguyên nhân** | NCS sử dụng tên mô tả nội dung thay vì tên query số. |
| **Tác động** | **Không ảnh hưởng.** `dedup.py` nhận diện source từ tên file qua `detect_source()` — pattern matching linh hoạt, không phụ thuộc tên cụ thể. Toàn bộ 21 files được đọc đúng. |
| **Hành động khắc phục** | Ghi nhận mapping Q-code → filename trong Strategy §9 (Bước 4.12). Script `dedup.py` đã inject `N1: source=<src>; study_id=<id>` vào mỗi record → truy xuất đầy đủ. |
| **Trạng thái** | **Resolved** — Không cần OSF Amendment. |

---

### DEV-003 — T5_Scopus.ris (Q7 T-L5 Scopus) tồn tại với 34 records

| Trường | Nội dung |
|--------|----------|
| **DEV-ID** | DEV-003 |
| **Ngày phát hiện** | 2026-05-14 |
| **Bước liên quan** | Bước 4.8 |
| **Mô tả sai lệch** | File T5_Scopus.ris ban đầu được cho là thiếu, nhưng thực tế file tồn tại với 34 records (nhỏ hơn kỳ vọng, nhưng không thiếu). |
| **Nguyên nhân** | Nhầm lẫn trong đánh giá ban đầu. |
| **Tác động** | **Không ảnh hưởng.** File đã được đưa vào pipeline, 34 records đã được xử lý. |
| **Hành động khắc phục** | Cập nhật Strategy §9 status table. |
| **Trạng thái** | **Resolved** |

---

### DEV-004 — Q10 Vintage chưa được chạy tìm kiếm (thiếu T8 files)

| Trường | Nội dung |
|--------|----------|
| **DEV-ID** | DEV-004 |
| **Ngày phát hiện** | 2026-05-14 |
| **Bước liên quan** | Bước 4.11 (Q10 Vintage — Scopus + IEEE) |
| **Mô tả sai lệch** | Q10 Vintage (Greenfield ↔ Brownfield — §4.10 Strategy) đã được thiết kế trong Search Strategy nhưng CHƯA được chạy tìm kiếm. Không có files `T8_Scopus.ris` / `T8_IEEE.ris` trong `search_results_v5.6/`. Pool 7.825 records hiện tại bao gồm Q1–Q9, Q11–Q12, GS nhưng thiếu Q10. |
| **Nguyên nhân** | NCS thu thập data theo thứ tự T1–T7 (Q3–Q9) rồi dừng trước khi chạy Q10. Có thể do Q10 được xem là ít ưu tiên hơn hoặc bị bỏ qua trong phiên thu thập dữ liệu. |
| **Tác động** | **Trung bình.** (i) Q10 phục vụ RQ4d (vintage gap analysis — greenfield vs brownfield). (ii) Bài về vintage có thể đã được bắt qua Q1 (CORE NARROW) và Q9 (Quy mô) vì cảng lớn/mới thường là greenfield. (iii) Tuy nhiên, không có đảm bảo độ phủ đầy đủ cho RQ4d nếu thiếu Q10. (iv) PRISMA-S yêu cầu liệt kê rõ tất cả truy vấn đã thực thi. |
| **Hành động khắc phục** | (1) Ghi nhận vào DEV-004 này; (2) NCS cần chạy Q10 trên Scopus + IEEE (xem §4.10 Strategy) → thêm T8_Scopus.ris + T8_IEEE.ris vào `search_results_v5.6/`; (3) Tái chạy `dedup.py` để merge T8 vào pool; (4) Tái chạy `screening.py` để cập nhật Pha A; (5) Nếu không thể chạy Q10 (deadline), ghi vào Limitations rằng vintage search chưa đầy đủ và kết quả RQ4d có thể underrepresent brownfield papers. |
| **Trạng thái** | **Resolved** — 2026-05-15: NCS chạy Q10 Scopus (9 records → `T8_Scopus.ris`) + IEEE (13 records → `T8_IEEE.ris`). Dedup tái chạy: 7.847→5.822. Screening tái chạy: 284/5.061/477. DEV-004 đóng. |

---

### DEV-005 — Upload dedup_unique.ris (5.822) thay vì screening_pre.ris (5.345) lên Rayyan

| Trường | Nội dung |
|--------|----------|
| **DEV-ID** | DEV-005 |
| **Ngày phát hiện** | 2026-05-19 |
| **Bước liên quan** | Bước 7.6–7.8 (Upload pool lên Rayyan) |
| **Mô tả sai lệch** | WorkPlan quy định upload `03_screening/screening_pre.ris` (5.345 records = LIKELY_INCLUDE + REVIEW_NEEDED) lên Rayyan. Thực tế NCS upload `dedup_unique.ris` (5.822 records = toàn bộ pool unique, bao gồm cả 477 LIKELY_EXCLUDE từ Pha A). |
| **Nguyên nhân** | Nhầm file trong hộp thoại upload Rayyan — `dedup_unique.ris` nằm ở thư mục gốc, dễ chọn nhầm hơn `03_screening/screening_pre.ris`. |
| **Tác động** | **Thấp.** 477 records LIKELY_EXCLUDE từ Pha A nay có mặt trong Rayyan và sẽ xuất hiện trong hàng đợi screening thủ công. NCS có thể exclude nhanh 477 records này khi gặp (nhận diện qua tiêu đề rõ ràng ngoài phạm vi). Audit trail đầy đủ hơn. PRISMA flow sẽ ghi "5.822 records screened in Rayyan" thay vì "5.345". |
| **Hành động khắc phục** | (1) Giữ nguyên 5.822 records trong Rayyan — không xóa và upload lại; (2) Khi gặp 477 LIKELY_EXCLUDE trong Rayyan, exclude nhanh với EC code tương ứng; (3) Cập nhật PRISMA Flow Diagram: ô "Records screened" = 5.822 (không phải 5.345); ô "Phase A auto-excluded" = 0 (merge vào Rayyan screening); (4) Ghi nhận trong manuscript Limitations. |
| **Trạng thái** | **Resolved** — Xử lý nội bộ; không cần OSF Amendment. |

---

## Template trống cho DEV mới

```
### DEV-XXX — [Tiêu đề ngắn]

| Trường | Nội dung |
|--------|----------|
| **DEV-ID** | DEV-XXX |
| **Ngày phát hiện** | YYYY-MM-DD |
| **Bước liên quan** | Bước X.Y |
| **Mô tả sai lệch** | |
| **Nguyên nhân** | |
| **Tác động** | |
| **Hành động khắc phục** | |
| **Trạng thái** | Open / Resolved / OSF Amendment submitted |
```

---

## Tóm tắt OSF Amendments cần submit (Bước 20.3)

| DEV-ID | Cần Amendment? | Lý do |
|--------|----------------|--------|
| DEV-001 | Không | Resolved nội bộ; Limitations ghi rõ |
| DEV-002 | Không | Không ảnh hưởng kết quả |
| DEV-003 | Không | Không ảnh hưởng kết quả |
| DEV-004 | Không | Resolved 2026-05-15 — Q10 đã chạy và merge vào pool |

*Cập nhật bảng này mỗi khi thêm DEV entry mới.*

---

*SR_Deviation_Log_v5.6.md — tạo 2026-05-14 — NCS HoaTX*
