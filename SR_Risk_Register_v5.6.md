# SỔ ĐĂNG KÝ RỦI RO

**Phiên bản:** v1.0 — 2026-05-11
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**OSF DOI:** [10.17605/OSF.IO/DXJW9](https://doi.org/10.17605/OSF.IO/DXJW9)
**Vai trò:** Sổ đăng ký 15 rủi ro của bài Tổng quan hệ thống — likelihood × impact × mitigation × Recovery trigger. NCS review hàng tháng + cập nhật likelihood khi thay đổi.
**Tuân thủ:** PRISMA 2020 Items 22 (Risk of bias due to missing results), 23c (Limitations), 24c (Amendments).

---

# §I. KHUNG ĐÁNH GIÁ RỦI RO

## 1.1 Likelihood (5 mức)

| Mức | Tên | Diễn giải | Ngưỡng (xác suất xảy ra trong vòng đời SR) |
|-----|-----|-----------|---------------------------------------------|
| 1 | Rare | Hiếm gặp | < 5% |
| 2 | Unlikely | Ít khả năng | 5–25% |
| 3 | Possible | Có thể | 25–50% |
| 4 | Likely | Khả năng cao | 50–75% |
| 5 | Almost certain | Gần chắc chắn | > 75% |

## 1.2 Impact (5 mức)

| Mức | Tên | Diễn giải |
|-----|-----|-----------|
| 1 | Negligible | Trễ < 3 ngày, không ảnh hưởng deliverable |
| 2 | Minor | Trễ 3–14 ngày hoặc cần re-do 1 sub-step |
| 3 | Moderate | Trễ 2–4 tuần hoặc cần re-do 1 Bước |
| 4 | Major | Trễ 1–3 tháng hoặc cần re-design 1 Pha |
| 5 | Catastrophic | Đe doạ pre-registration / phải withdraw / không thể publish |

## 1.3 Risk Score = Likelihood × Impact (1–25)

| Score | Phân loại | Hành động |
|-------|-----------|-----------|
| 1–4 | Low | Theo dõi định kỳ |
| 5–9 | Medium | Có mitigation; review hàng tháng |
| 10–14 | High | Mitigation chủ động + Recovery procedure ready |
| 15–25 | Very High | Mitigation + Recovery + escalate to NCS supervisor |

---

# §II. 15 RỦI RO — DANH MỤC CHI TIẾT

## R01 — OSF outage trong giai đoạn search/screening

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 2–6 |
| Likelihood | 2 (Unlikely) |
| Impact | 2 (Minor) |
| Score | 4 (Low) |
| Mô tả | OSF down → không upload được artefact, không truy cập Registration. |
| Mitigation | Backup local + Google Drive private; không phụ thuộc OSF cho daily work. |
| Recovery | Đợi OSF up; nếu > 7 ngày → escalate OSF support. |
| Trigger | OSF status page hiển thị degraded/outage. |

## R02 — Mất quyền truy cập Scopus/IEEE (institutional)

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 2 |
| Likelihood | 2 (Unlikely) |
| Impact | 4 (Major) |
| Score | 8 (Medium) |
| Mô tả | VNU institution thay đổi gói subscription → mất Scopus hoặc IEEE access mid-search. |
| Mitigation | Chạy tất cả 22 query càng sớm càng tốt; lưu RIS ngay sau mỗi query. |
| Recovery | Liên hệ thư viện VNU + tận dụng GS supplementary; nếu mất Scopus → cân nhắc re-design dùng WoS. |
| Trigger | Authentication fail trên giao diện Scopus/IEEE. |

## R03 — Pool unique ngoài range kỳ vọng [5.000, 7.000]

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 2 (Bước 7) |
| Likelihood | 3 (Possible) |
| Impact | 3 (Moderate) |
| Score | 9 (Medium) |
| Mô tả | Pool < 5.000 → có thể search miss; Pool > 7.000 → screening overload. |
| Mitigation | Recall validation 78 seeds (Bước 15.1) phát hiện sớm; NOT block design balanced (5 blocks). |
| Recovery | Pool < 5.000 → SA-1/2/3 enlarge searches; Pool > 7.000 → tightening NOT block 4 (non-CT terminal). |
| Trigger | Bước 7 dedup output `dedup_report.txt` báo unique pool size. |

## R04 — Rayyan Essentials thiếu features

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 1 (Bước 1.11), 3 (Bước 8) |
| Likelihood | 2 (Unlikely) — giảm từ 3 sau verify 2026-05-11 |
| Impact | 3 (Moderate) |
| Score | 6 (Medium) — giảm từ 9 |
| Mô tả | Essentials không hỗ trợ ≥ 28 custom reasons, hoặc PDF attachment, hoặc CSV export đầy đủ. |
| Mitigation | Verify features ngay Bước 1.11; có fallback Excel sẵn. **Verified 2026-05-11:** Pha A pipeline hiện tại (Rayyan UI manual + Python local) đã đủ cho 28 EC/IC qua reason field — không phụ thuộc features advanced. |
| Recovery | Recovery R2 — chuyển hoàn toàn sang Excel + local PDF nếu Essentials không đủ. |
| Trigger | Bước 1.11 verify report. |
| Note 2026-05-11 | API access KHÔNG có ở Essentials (chỉ Enterprise); TOS cấm reverse-engineering. Quyết định: giữ Pha A pipeline manual UI + local Python. KHÔNG triển khai code gọi Rayyan API. |

## R05 — Recall < 95% trên 78 seeds

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 5 (Bước 15.1) |
| Likelihood | 3 (Possible) |
| Impact | 4 (Major) |
| Score | 12 (High) |
| Mô tả | Search strategy missed > 5% seed papers → reviewer Q1 sẽ challenge completeness. |
| Mitigation | Strategy phủ 5 chiều (Q1–Q10) + GS supplementary + Springer + T&F + snowball + hand-search. |
| Recovery | **Recovery R5** — chạy SA-1 (loosened NOT block) + SA-2 (added DBs e.g. WoS) + SA-3 (extended snowball depth 2). |
| Trigger | Bước 15.1 báo recall % vs 78 seeds. Ngưỡng: ≥ 95% chấp nhận; 80–95% trigger SA-1/2/3; < 80% trigger Recovery R5. |

## R06 — Intra-rater κ < 0.75

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 3 (Bước 8.2.2), 4 (Bước 11.2), 5 (Bước 14) |
| Likelihood | 3 (Possible) |
| Impact | 3 (Moderate) |
| Score | 9 (Medium) |
| Mô tả | Self-consistency thấp → reviewer Q1 hoài nghi single-reviewer reliability. |
| Mitigation | Form/rubric/protocol chi tiết + pilot 30 + 5 + 10 records + gap ≥ 14 ngày. |
| Recovery | **Recovery R6** — refine định nghĩa IC/EC + form v1.x + re-pilot; nếu 3 lần vẫn < 0.75 → escalate supervisor + add second rater hỗ trợ pilot. |
| Trigger | Cohen's κ tính ở Bước 8.2.2, 11.2.4, 14.1–14.3. |

## R07 — Single-reviewer bias bị reviewer Q1 challenge

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 6 (Bước 22) |
| Likelihood | 4 (Likely) |
| Impact | 4 (Major) |
| Score | 16 (Very High) |
| Mô tả | Reviewer Q1 yêu cầu second independent reviewer cho screening — không có sẽ reject. |
| Mitigation | (a) Declare ngay từ §3 Registration text + Limitations manuscript; (b) Intra-rater κ ≥ 0.75 evidence; (c) Expert Validation Delphi-lite 3–5 chuyên gia; (d) Cite precedent SR single-reviewer trong SE/OR (Cruzes & Dybå 2011). |
| Recovery | Nếu reviewer Q1 reject → tuyển 1 second rater chấm 20% random sample (validation) → submit revision. |
| Trigger | Reviewer comment ở vòng 1 manuscript review. |

## R08 — PDF retrieval failure > 20% records

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 3 (Bước 9.1) |
| Likelihood | 2 (Unlikely) |
| Impact | 3 (Moderate) |
| Score | 6 (Medium) |
| Mô tả | Quá nhiều fulltext bị EC6 → giảm pool included xuống dưới ngưỡng. |
| Mitigation | VNU institutional access + email tác giả + ResearchGate + Sci-Hub (last resort, ghi rõ Limitations). |
| Recovery | Mở rộng retrieval window từ 14 ngày → 21 ngày; ưu tiên seed papers + cảng VN/ĐNÁ. |
| Trigger | Bước 9.1 báo % PDF không lấy được. |

## R09 — Eligibility criteria mới phát sinh giữa screening

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 3 (Bước 8) |
| Likelihood | 3 (Possible) |
| Impact | 3 (Moderate) |
| Score | 9 (Medium) |
| Mô tả | Trong screening phát hiện loại noise mới chưa có EC code → cần thêm EC. |
| Mitigation | Borderline log + `borderline_decisions_log.md` từ đầu; check pattern weekly. |
| Recovery | Submit OSF Amendment AM-00X mô tả EC mới + re-screen pool đã chấm theo EC mới. |
| Trigger | Borderline log accumulates ≥ 5 cases cùng pattern không match 28 EC hiện có. |

## R10 — IJPR/MPM scope reject (desk reject)

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 6 (Bước 22) |
| Likelihood | 3 (Possible) |
| Impact | 4 (Major) |
| Score | 12 (High) |
| Mô tả | Editor IJPR/MPM cho rằng SR không fit scope → desk reject sau 1–2 tuần. |
| Mitigation | Cover letter chi tiết về fit + cite recent SR trong target journal + check Author Guidelines mới nhất trước submit. |
| Recovery | Escalate fallback Q1: *Computers in Industry* (Elsevier) → *Annual Reviews in Control* (Elsevier) → *Journal of Marine Science and Engineering* (MDPI). |
| Trigger | Desk-reject email từ editor. |

## R11 — Software dependency breakage

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 2 (Bước 7), 3 (Bước 8.1), 5 (Bước 16) |
| Likelihood | 2 (Unlikely) |
| Impact | 2 (Minor) |
| Score | 4 (Low) |
| Mô tả | RapidFuzz / pandas / VOSviewer update breaking change → script fail. |
| Mitigation | Pin Python version + `requirements.txt` + virtual env + backup script weekly. |
| Recovery | Rollback dependency version; nếu cần → rewrite script với version stable. |
| Trigger | Script error log. |

## R12 — Data corruption / lost work

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | All |
| Likelihood | 1 (Rare) |
| Impact | 5 (Catastrophic) |
| Score | 5 (Medium) |
| Mô tả | Disk failure / accidental delete → lost extraction/screening data. |
| Mitigation | Backup Policy §0.5: weekly Sundays 22:00 → Google Drive + GitHub private; Rayyan weekly snapshot CSV; OSF state snapshot sau mỗi mốc Bước. |
| Recovery | Restore từ backup gần nhất; tối đa lost 1 tuần work. |
| Trigger | Disk error / file missing. |

## R13 — OSF Amendment rejected

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 6 (Bước 20.3) |
| Likelihood | 1 (Rare) |
| Impact | 3 (Moderate) |
| Score | 3 (Low) |
| Mô tả | OSF reject Amendment do quá nhiều thay đổi hoặc submit timing không phù hợp. |
| Mitigation | Submit Amendment NGAY khi quyết định (BEFORE thực hiện); kèm justification chi tiết. |
| Recovery | Submit Amendment riêng cho từng thay đổi nhỏ; không gộp. |
| Trigger | OSF reject notification. |

## R14 — Reviewer Q1 disagree với Maturity classification

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 6 (Bước 22 review round) |
| Likelihood | 3 (Possible) |
| Impact | 3 (Moderate) |
| Score | 9 (Medium) |
| Mô tả | Reviewer cho rằng L3 vs L4 boundary chưa chặt → đòi re-classify. |
| Mitigation | Rubric L1–L5 chi tiết kèm evidence quote + Expert Validation Delphi-lite cho 10–20 random studies. |
| Recovery | Re-classify với rubric refined; ghi vào Methods + Limitations rubric refinement. |
| Trigger | Reviewer comment yêu cầu re-classify. |

## R15 — PRISMA 2020 standards updated mid-review

| Field | Giá trị |
|-------|---------|
| Pha ảnh hưởng | 6 (Bước 19) |
| Likelihood | 1 (Rare) |
| Impact | 2 (Minor) |
| Score | 2 (Low) |
| Mô tả | PRISMA 2020 hoặc PRISMA-S phát hành revision mid-2026. |
| Mitigation | Subscribe PRISMA mailing list; check version trước submit. |
| Recovery | Update checklist + reflect mới nhất trong manuscript; flag deviation nếu cần. |
| Trigger | PRISMA website announcement. |

---

# §III. RISK SUMMARY MATRIX

| Mã | Tên | Likelihood | Impact | Score | Recovery |
|----|-----|------------|--------|-------|----------|
| R01 | OSF outage | 2 | 2 | 4 (Low) | – |
| R02 | DB access loss | 2 | 4 | 8 (Med) | Library escalate |
| R03 | Pool size off | 3 | 3 | 9 (Med) | SA-1/2/3 hoặc tighten NOT block |
| R04 | Rayyan features missing | 3 | 3 | 9 (Med) | **R2** — Excel fallback |
| R05 | Recall < 95% | 3 | 4 | 12 (**High**) | **R5** — SA-1/2/3 |
| R06 | κ < 0.75 | 3 | 3 | 9 (Med) | **R6** — refine + re-pilot |
| R07 | Single-reviewer challenge | 4 | 4 | 16 (**Very High**) | Add second rater 20% |
| R08 | PDF retrieval fail | 2 | 3 | 6 (Med) | Extend window |
| R09 | New EC during screen | 3 | 3 | 9 (Med) | **R9** — Amendment + re-screen |
| R10 | IJPR/MPM desk reject | 3 | 4 | 12 (**High**) | Escalate fallback Q1 |
| R11 | Dep breakage | 2 | 2 | 4 (Low) | Rollback |
| R12 | Data corruption | 1 | 5 | 5 (Med) | Restore backup |
| R13 | Amendment rejected | 1 | 3 | 3 (Low) | Submit smaller Amendments |
| R14 | Reviewer disagree maturity | 3 | 3 | 9 (Med) | Re-classify with refined rubric |
| R15 | PRISMA update | 1 | 2 | 2 (Low) | Update checklist |

**Top 3 rủi ro cần giám sát chặt:**

1. **R07 (Score 16)** — Single-reviewer challenge: chuẩn bị evidence Intra-rater κ + Delphi panel + cite precedent.
2. **R05 (Score 12)** — Recall validation: chạy SA-1/2/3 trigger sẵn sàng.
3. **R10 (Score 12)** — Q1 desk reject: chuẩn bị fallback journal list + cover letter robust.

---

# §IV. RECOVERY PROCEDURES R1–R7 (mapping với WorkPlan §V)

| Recovery | Trigger | Procedure |
|----------|---------|-----------|
| **R1** | Pool RIS upload nhầm vào Rayyan trước Bước 7 | Delete pool, re-create Rayyan project trống, dedup local trước rồi mới upload. |
| **R2** | Rayyan Essentials thiếu feature critical | Switch sang Excel + local PDF + custom CSV reasons; Rayyan dùng read-only audit trail. |
| **R3** | Pre-screen Pha A regex coverage thấp (κ < 0.75) | Refine 13 priority rules + thêm patterns từ borderline log; re-run Pha A. |
| **R4** | NCS chấm chậm (< 100 records/tuần ở Bước 8) | Ưu tiên LIKELY_EXCLUDE (xác nhận nhanh) → REVIEW_NEEDED → LIKELY_INCLUDE; mỗi ngày 4 giờ deep work. |
| **R5** | Recall < 95% trên 78 seeds | SA-1 (loosen NOT block 4) → SA-2 (add WoS hoặc DOAJ) → SA-3 (snowball depth 2). |
| **R6** | Intra-rater κ < 0.75 (1 trong 3 vòng) | Refine định nghĩa field/EC + form/rubric v1.x; re-pilot; nếu 3 lần fail → escalate supervisor + 1 second rater. |
| **R7** | Pool dedup unique > 7.000 (overload) | Tighten NOT block 4 (thêm specific terms) hoặc Q2 EXTENDED Block C giảm scope; re-run dedup. |

---

# §V. LỊCH REVIEW RỦI RO

| Tần suất | Hoạt động | Người |
|----------|-----------|-------|
| Hàng tuần | Check trigger conditions của R03, R05, R06 (qua dashboard Bước 7, 8, 14, 15) | NCS |
| Hàng tháng | Review toàn bộ likelihood + cập nhật score | NCS |
| Sau mỗi mốc Bước | Update Risk Register với trigger evidence | Claude + NCS |
| Trước Submit (Bước 22) | Final review — ensure top 3 rủi ro mitigated đầy đủ | NCS + Supervisor |

---

# §VI. PHIÊN BẢN

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-05-11 | Tạo mới — 15 rủi ro với Likelihood × Impact × Mitigation × Recovery; mapping với 7 Recovery procedures R1–R7 trong WorkPlan §V (Bước 0.9 WorkPlan) |
