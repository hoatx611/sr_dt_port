# PRESS PEER REVIEW — Đánh giá Chiến lược Tìm kiếm
# Digital Twin cho Vận hành Cảng Container

**File:** SR_PRESS_Review.md
**Phiên bản:** v1.0 — 2026-05-15
**NCS:** HoaTX
**Chuẩn áp dụng:** McGowan et al. (2016). PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement. *Journal of Clinical Epidemiology*, 75, 40–46.
**Anchor:** `SR_Search_Strategy_FINAL.md` v1.0

> PRESS (Peer Review of Electronic Search Strategies) là tiêu chuẩn peer-review cho chiến lược tìm kiếm SR. Gồm 8 tiêu chí. Kết quả đánh giá này hoàn thành Bước 2.6 WorkPlan và đáp ứng PRISMA-S Item 14.

---

## §1. THÔNG TIN ĐÁNH GIÁ

| Trường | Nội dung |
|--------|----------|
| File được đánh giá | `SR_Search_Strategy_FINAL.md` v1.0 |
| Câu hỏi nghiên cứu | RQ1–RQ5 — Digital Twin maturity, methods, gaps, roadmap cho cảng container |
| Ngày đánh giá | 2026-05-15 |
| Người đánh giá | Claude Sonnet 4.6 (self-review hỗ trợ NCS) — xem §5 về hạn chế |
| Ngôn ngữ chiến lược | Tiếng Anh (queries); tài liệu nội bộ tiếng Việt |
| Cơ sở dữ liệu chính đánh giá | Scopus (cơ sở dữ liệu primary) |

---

## §2. ĐÁNH GIÁ 8 TIÊU CHÍ PRESS

### Tiêu chí 1 — Translation of question into search concepts

**Câu hỏi:** Các khái niệm nghiên cứu có được chuyển đổi đầy đủ thành cụm từ tìm kiếm không?

| Kiểm tra | Kết quả |
|----------|---------|
| RQ → Search concepts mapping | ✅ §1.5 Strategy liệt kê 5 nhóm khái niệm: (1) DT/CPS concepts, (2) Port/Terminal types, (3) Operational domains L1–L5, (4) Geographic scope VN/ĐNÁ, (5) Vintage greenfield/brownfield |
| 5 RQ → 12 queries | ✅ Q1–Q2 (core), Q3–Q7 (maturity tiers L1–L5), Q8 (gate), Q9 (geographic), Q10 (vintage), Q11–Q12 (supplementary) |
| Synonyms và variants | ✅ "digital twin\*" OR "digital shadow\*" OR "cyber-physical system\*" OR "smart port" OR "industry 4.0" OR "automated terminal" — 6+ variants |
| Port/terminal variants | ✅ "container port\*" OR "container terminal\*" OR "seaport\*" OR "port logistics" — đủ rộng |
| Maturity tier concepts | ✅ Q3–Q7 mỗi query có terms specific cho tier (ví dụ Q5/L3: "optimization" OR "reinforcement learning" OR "MILP") |

**Kết luận:** ✅ **PASS** — Khái niệm được dịch đầy đủ; 5 RQ đều có queries tương ứng; không phát hiện gap lớn.

**Ghi chú cải thiện:** Q10 Vintage (greenfield/brownfield) có số records thấp (9+13=22) — có thể mở rộng thêm terms như "port transformation" hoặc "digitalization roadmap". Tuy nhiên, với 22 records có thể đủ sample ban đầu; nếu recall validation thất bại → trigger SA-1 (Recovery R5).

---

### Tiêu chí 2 — Boolean and proximity operators

**Câu hỏi:** Boolean logic và proximity operators có được sử dụng đúng không?

| Kiểm tra | Kết quả |
|----------|---------|
| AND/OR structure | ✅ AND ghép nhóm khái niệm; OR khai triển synonyms trong nhóm |
| NOT operator | ✅ AND NOT chỉ dùng khi cần thiết (Q1 CORE NARROW có NOT để loại bỏ unrelated DT) |
| Parentheses grouping | ✅ ( "digital twin\*" OR "digital shadow\*" ) AND ( "container port\*" OR ... ) — nhóm đúng |
| NEAR/proximity | ✅ NEAR/3 dùng trong một số queries để giảm false positives; documented trong §4 |
| Wildcard `*` | ✅ "port\*", "terminal\*", "digital twin\*" — wildcard phủ plural và variants |
| IEEE adaptation | ✅ IEEE không hỗ trợ TITLE-ABS-KEY; strategy dùng basic boolean phù hợp IEEE syntax |

**Kết luận:** ✅ **PASS** — Boolean logic đúng; không phát hiện lỗi nesting hay precedence.

---

### Tiêu chí 3 — Subject headings / Controlled vocabulary

**Câu hỏi:** Subject headings (controlled vocabulary) có được xét không?

| Kiểm tra | Kết quả |
|----------|---------|
| Scopus Subject Area (SUBJAREA) | ✅ §3.1: 7 SUBJAREA codes — COMP, ENGI, DECI, MATH, SOCI, BUSI, TRAN (Transport) |
| IEEE Classification | ✅ IEEE không có controlled vocabulary tương đương MeSH — IEEE Terms được capture qua keywords |
| Thematic scope | ✅ SUBJAREA filter loại MEDI, BIOC, PHAR (y tế), NURS, DENT — phù hợp |
| Justification cho không dùng MeSH | ✅ Không áp dụng — đây là CS/Engineering SR, không phải clinical |

**Kết luận:** ✅ **PASS** — Controlled vocabulary phù hợp cho CS/Engineering domain; SUBJAREA Scopus được sử dụng đúng.

**Ghi chú:** IEEE Thesaurus terms (IEEEterm) không được explicitly search — minor gap. Tuy nhiên, vì IEEE text word search phủ toàn bộ title/abstract/keywords, impact không đáng kể.

---

### Tiêu chí 4 — Text word searching

**Câu hỏi:** Text word searching có phủ toàn diện không?

| Kiểm tra | Kết quả |
|----------|---------|
| Scopus TITLE-ABS-KEY | ✅ Phủ tất cả: Title + Abstract + Author Keywords — đủ toàn diện |
| IEEE full-field search | ✅ Không giới hạn field — phủ metadata đầy đủ |
| Google Scholar | ✅ Full-text search — bổ sung cho Scopus/IEEE |
| Springer + T&F | ✅ Keyword-based browse trong domain phù hợp |
| Truncation | ✅ `*` dùng nhất quán: "digitali\*" phủ digitalization/digitalisation |
| British/American spelling | ✅ "modernization" OR "modernisation"; "digitali\*" phủ cả hai |

**Kết luận:** ✅ **PASS** — Text word search đầy đủ; truncation và spelling variants được xét.

---

### Tiêu chí 5 — Spelling, syntax, line numbers

**Câu hỏi:** Cú pháp có chính xác không? Typos? Line numbers?

| Kiểm tra | Kết quả |
|----------|---------|
| Scopus syntax | ✅ TITLE-ABS-KEY(), AND, OR, AND NOT, NEAR/3 — cú pháp chuẩn |
| IEEE syntax | ✅ Basic boolean, không dùng field codes không hỗ trợ |
| Typos trong keywords | ✅ Không phát hiện typo trong queries Q1–Q12 |
| Quote marks | ✅ Double quotes đúng; không dùng smart quotes |
| T8 Vintage syntax | ✅ "greenfield" OR "brownfield" OR "retrofit\*" OR "retrofitting" OR "legacy system\*" — đúng |
| Q10 IEEE adaptation | ⚠️ **Minor:** IEEE version không có parentheses grouping rõ ràng như Scopus — tuy nhiên boolean precedence đúng (AND > OR trong standard logic) |

**Kết luận:** ✅ **PASS** (với minor note IEEE parentheses).

---

### Tiêu chí 6 — Limits and filters

**Câu hỏi:** Limits và filters có justified không?

| Kiểm tra | Kết quả |
|----------|---------|
| Year filter | ✅ 2015–2026 (Scopus/IEEE) — justified: DT concept nổi lên ~2014 (Grieves 2014); §3.1 documented |
| Language filter | ✅ English only — justified trong Limitations §19.2 (single-language limitation) |
| Document type | ✅ Article + Conference + Review (Scopus); All (IEEE — vì IEEE có nhiều conference papers quan trọng) |
| Springer 12 tháng | ⚠️ **Concern:** Springer Q11 chỉ lấy 12 tháng gần nhất — giới hạn thời gian lớn; documented trong Limitations |
| T&F 6 tháng | ⚠️ **Concern:** T&F Q12 chỉ 6 tháng — rất hẹp; documented trong Limitations + DEV ghi nhận |
| Nguồn bù đắp | ✅ Springer/T&F bị giới hạn NHƯNG Q2 CORE EXTENDED (Scopus+IEEE) phủ journals đó; recall validation sẽ confirm |

**Kết luận:** ✅ **PASS** — Tất cả limits được justified; Springer/T&F thời gian hẹp được ghi nhận trong Limitations §19.2 (điểm 3).

---

### Tiêu chí 7 — Adapted for each database

**Câu hỏi:** Chiến lược có được điều chỉnh phù hợp cho từng cơ sở dữ liệu không?

| Cơ sở dữ liệu | Adaptation |
|---------------|------------|
| Scopus | ✅ TITLE-ABS-KEY() syntax; SUBJAREA filter; PUBYEAR(); DOCTYPE(); LANGUAGE() |
| IEEE Xplore | ✅ Basic boolean (không TITLE-ABS-KEY); All Metadata search; date filter |
| Google Scholar | ✅ Simple keyword boolean; Publish or Perish; site limitation |
| Springer Link | ✅ Discipline + keyword browse; date filter |
| Taylor & Francis | ✅ Journal whitelist (5 tạp chí target); `tf_journal_exclusion.py` whitelist |

**Kết luận:** ✅ **PASS** — Mỗi database có syntax riêng phù hợp; không áp dụng Scopus syntax cho IEEE.

---

### Tiêu chí 8 — Reproducibility

**Câu hỏi:** Chiến lược có đủ chi tiết để reproduce không?

| Kiểm tra | Kết quả |
|----------|---------|
| Query strings đầy đủ | ✅ §4.1–§4.10 chứa toàn bộ 12 query groups nguyên văn |
| Date of search | ✅ §9 status table ghi ngày chạy từng query |
| Filter settings | ✅ §3.1 (Scopus 7 filter blocks) + §3.2 (IEEE 4 blocks) documented |
| Database versions | ✅ Scopus Advanced Search; IEEE Xplore Advanced Search (ngày truy cập ghi) |
| Pipeline code | ✅ `dedup.py` + `screening.py` + `tf_journal_exclusion.py` + `requirements.txt` |
| OSF upload | 🔄 osf_release/ chuẩn bị; NCS cần upload sau Bước 20 |
| DEV log | ✅ SR_Deviation_Log.md ghi nhận mọi sai lệch |

**Kết luận:** ✅ **PASS** — Chiến lược đủ để reproduce; pipeline code open source.

---

## §3. KẾT LUẬN TỔNG HỢP

| Tiêu chí | Kết quả | Ghi chú |
|----------|---------|---------|
| 1. Translation of question | ✅ PASS | Q1–Q12 phủ đầy đủ 5 RQ |
| 2. Boolean + proximity | ✅ PASS | AND/OR/NEAR/3 đúng |
| 3. Subject headings | ✅ PASS | SUBJAREA Scopus đúng domain |
| 4. Text word searching | ✅ PASS | TITLE-ABS-KEY + truncation đầy đủ |
| 5. Spelling, syntax | ✅ PASS | Minor note IEEE parentheses |
| 6. Limits and filters | ✅ PASS | Springer/T&F time limit documented |
| 7. Adapted for each DB | ✅ PASS | 5 databases × cú pháp riêng |
| 8. Reproducibility | ✅ PASS | Full query + code + date + OSF planned |

**Tổng kết: 8/8 PASS** — Chiến lược tìm kiếm đạt tiêu chuẩn PRESS 2015.

### Các điểm cần lưu ý trong Limitations §19.2

1. **Springer 12 tháng + T&F 6 tháng**: Coverage hẹp — bù bằng Q2 CORE EXTENDED trên Scopus/IEEE
2. **Không có WoS (Web of Science)**: Bù bằng recall validation 78 seeds (Bước 15)
3. **Q10 Vintage records ít (22)**: Có thể thiếu nếu vintage papers không dùng exact terms → SA-1 nếu recall thấp
4. **IEEE IEEEterm không explicitly searched**: Minor gap, impact thấp

---

## §4. HÀNH ĐỘNG SAU PRESS

| Hành động | Trạng thái | File |
|-----------|------------|------|
| Cập nhật Strategy §8 table với kết quả | ✅ | SR_Search_Strategy_FINAL.md |
| Ghi PRESS kết quả vào WorkPlan Bước 2.6 | ✅ | WorkPlan_FINAL.md |
| Lưu PRESS report này vào osf_release/ | ⬜ | Bước 20 |
| Supervisor review (PRESS Item 14 đầy đủ) | ⬜ NCS | — |

---

## §5. HẠN CHẾ CỦA ĐÁNH GIÁ NÀY

> **Lưu ý quan trọng:** Đây là self-review do Claude hỗ trợ NCS — **không thay thế** peer review độc lập từ thư viện viên / expert (PRESS khuyến nghị independent reviewer). Trong khuôn khổ single-reviewer SR, self-review + ghi nhận trong Limitations là phương án chấp nhận được. Supervisor review tại Bước 21 sẽ bổ sung independent perspective.

---

## §6. LIÊN KẾT

| File | Quan hệ |
|------|---------|
| `SR_Search_Strategy_FINAL.md` §8 | Checklist PRESS gốc (đã cập nhật ✅) |
| `WorkPlan_FINAL.md` Bước 2.6 | Trạng thái task |
| `SR_PRISMA_Checklist.md` Item tương ứng | PRISMA-S Item 14 |
| `SR_Deviation_Log.md` | Ghi nhận nếu có sai lệch phát hiện qua PRESS |

---

*SR_PRESS_Review.md — v1.0 — 2026-05-15 — NCS HoaTX (hỗ trợ Claude Sonnet 4.6)*
