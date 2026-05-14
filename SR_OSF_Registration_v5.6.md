# THEO DÕI OSF PROJECT + REGISTRATION + RAYYAN

**Phiên bản:** v1.0 — 2026-05-11
**NCS:** HoaTX
**OSF Project:** <https://osf.io/dxjw9/> (Project ID: `dxjw9`)
**OSF DOI:** [10.17605/OSF.IO/DXJW9](https://doi.org/10.17605/OSF.IO/DXJW9)
**Vai trò:** Internal tracker (workspace-only) cho mọi tương tác OSF + Rayyan. KHÔNG public lên OSF — đây là sổ sự kiện nội bộ. Mỗi sự kiện ghi đầy đủ ngày + người + chi tiết để truy vết khi cần.
**Tuân thủ:** PRISMA 2020 Items 24a (Registration), 24b (Protocol accessibility), 24c (Amendments).

---

# §I. OSF PROJECT — TÌNH TRẠNG

## 1.1 Thông tin chính

| Trường | Giá trị | Cập nhật |
|--------|---------|----------|
| Project ID | `dxjw9` | 2026-05-10 |
| Project URL | <https://osf.io/dxjw9/> | 2026-05-10 |
| Project DOI | `10.17605/OSF.IO/DXJW9` | 2026-05-11 (NCS thông báo) |
| Visibility | _[NCS verify Public state]_ | – |
| License | CC-BY 4.0 Attribution International | 2026-05-10 (kế hoạch) |
| Category | Project | 2026-05-10 (kế hoạch) |
| Affiliated Institution | _[NCS điền]_ | – |

## 1.2 Cấu hình metadata (Bước 1.2)

| Trường OSF | Trạng thái | Tham chiếu |
|------------|------------|------------|
| Title | ⬜ Chờ NCS paste | [SR_OSF_Project_Metadata_v5.6.md](SR_OSF_Project_Metadata_v5.6.md) §I |
| Description | ⬜ Chờ NCS paste | §II |
| Category | ⬜ Chờ NCS chọn dropdown | §III |
| Tags (10) | ⬜ Chờ NCS paste | §IV |
| License | ⬜ Chờ NCS chọn dropdown | §V |
| Affiliated Institution | ⚠️ Chờ NCS điền | §VIII |
| Contributors | ⚠️ Chờ NCS điền tên Supervisor | §VII |
| Public state | ⬜ Verify ON trước Registration | §X.2 |

## 1.3 Components (sub-projects) — tạo dần theo Pha

| Component | Category | Bước tạo | Trạng thái |
|-----------|----------|----------|------------|
| 01_protocol | Procedure | Bước 1.9 | ⬜ |
| 02_search | Data | Bước 7 | ⬜ |
| 03_screening | Data | Bước 8 | ⬜ |
| 04_extraction | Data | Bước 11 | ⬜ |
| 05_synthesis | Analysis | Bước 16 | ⬜ |

---

# §II. OSF REGISTRATION — TÌNH TRẠNG

## 2.1 Registration submissions

| ID | Date | Type | DOI | Status | Notes |
|----|------|------|-----|--------|-------|
| R-001 | _chưa submit_ | _[Pre-Registration / Standard]_ | _chờ_ | ⬜ Pending | Cần NCS điền 4 trường ⚠️ trong [SR_OSF_Registration_Submission_v5.6.md](SR_OSF_Registration_Submission_v5.6.md) trước Submit |

## 2.2 ⚠️ Câu hỏi verify với NCS

DOI hiện tại `10.17605/OSF.IO/DXJW9` trùng Project ID → có 2 khả năng:

- **Khả năng A (cao):** Đây là **Project DOI** (mutable) cấp qua Settings → Create DOI. Bước 1.5 (Submit Registration) chưa hoàn thành. Cần submit Registration thực sự sau khi điền 4 trường ⚠️.
- **Khả năng B (thấp):** Đây là **Registration DOI** (immutable). Bước 1.5 đã hoàn thành.

**Cách verify:** NCS check trên OSF:

1. Project `dxjw9` → Settings → DOI section: nếu thấy "DOI: 10.17605/OSF.IO/DXJW9" với option "Manage DOI" → Project DOI.
2. Project `dxjw9` → Tab **Registrations**: nếu có entry với DOI riêng (Registration ID khác `dxjw9`) → Registration DOI thực sự.

**Note kết quả:** _[chờ NCS verify và update]_

## 2.3 Amendments log

| Mã | Date | Loại | Trigger | Tham chiếu | Status |
|----|------|------|---------|------------|--------|
| AM-001 | _none_ | – | – | – | – |

> Quy ước: AM-001, AM-002, … submit theo thứ tự thời gian. Mỗi Amendment kèm justification trong `SR_Deviation_Log_v5.6.md` (sẽ tạo khi có sai lệch đầu tiên).

---

# §III. RAYYAN PROJECT — TÌNH TRẠNG

## 3.1 Project info

| Trường | Giá trị | Cập nhật |
|--------|---------|----------|
| Project name | `SR_DT_Port` | _chưa tạo_ |
| Project ID Rayyan | _[NCS điền sau Bước 1.10]_ | – |
| URL | _[NCS điền]_ | – |
| Owner | NCS HoaTX | – |
| Plan | Rayyan Essentials | – |

## 3.2 Verify Essentials features (Bước 1.11)

| Feature | Hỗ trợ? | Note | Cập nhật |
|---------|---------|------|----------|
| Custom reasons taxonomy | ⬜ | Cần verify hỗ trợ ≥ 28 mã EC/IC | – |
| PDF attachment | ⬜ | Nếu KO → fallback Excel + local PDF | – |
| AI ranking | ⬜ | Optional; nếu có → tận dụng | – |
| Blinded mode | ⬜ | Single-reviewer KO cần | – |
| Auto-dedup DOI | ⬜ | Đã biết Essentials có DOI auto-dedup | – |
| Export CSV | ⬜ | Yêu cầu cho audit trail | – |
| Inclusion notes | ⬜ | Optional | – |

## 3.3 Reasons taxonomy (Bước 1.12)

NCS nạp 28 mã EC/IC từ [SR_Eligibility_Criteria_v5.6.md](SR_Eligibility_Criteria_v5.6.md) §III + §IV làm Reasons trong Rayyan project. Format gợi ý:

```text
INCLUDE:
  IC1, IC2, IC3, IC4, IC5

EXCLUDE Layer 1 (T/A):
  EC1, EC2, EC3, EC4, EC5, EC7-mfg, EC7-bim, EC7-health, EC7-noctx, EC7-other,
  EC8, EC9, EC-CYBER, EC-ENERGY, EC-GENERIC, EC-IT, EC-NOSCOPE, EC-PAX, EC-STRUCT

EXCLUDE Layer 2 (Fulltext):
  EC6, EC-ENV, EC-VESSEL, EC-POLICY, EC-SECUR, EC-BLOCK, EC-TELECOM, EC-CUSTOMS, EC-AGRI
```

**Trạng thái:** ⬜ Chờ NCS thực hiện sau khi tạo project.

## 3.4 Rayyan weekly snapshot (Backup Policy §0.5)

| Tuần | Date | CSV file | Pool size | Notes |
|------|------|----------|-----------|-------|
| – | _chưa có pool_ | – | – | Chỉ áp dụng từ sau Bước 8.2 (formal screening) |

---

# §IV. OSF FILES — UPLOAD MAPPING

## 4.1 Mapping `osf_release/` → OSF Files folder

| File local `osf_release/` | OSF Files path đề xuất | Status |
|---------------------------|------------------------|--------|
| [SR_Research_Questions.md](osf_release/SR_Research_Questions.md) | `01_protocol/SR_Research_Questions.md` | ⬜ |
| [SR_Search_Strategy.md](osf_release/SR_Search_Strategy.md) | `01_protocol/SR_Search_Strategy.md` | ⬜ |
| [SR_WorkPlan.md](osf_release/SR_WorkPlan.md) | `01_protocol/SR_WorkPlan.md` | ⬜ |
| [SR_Eligibility_Criteria.md](osf_release/SR_Eligibility_Criteria.md) | `01_protocol/SR_Eligibility_Criteria.md` | ⬜ |
| [SR_Data_Extraction_Form.md](osf_release/SR_Data_Extraction_Form.md) | `01_protocol/SR_Data_Extraction_Form.md` | ⬜ |
| (Registration submission text) | (paste vào Tab Registrations, không upload file) | – |

**Trạng thái Bước 1.9:** ⬜ Chờ NCS upload 5 file lên OSF Tab Files → folder `01_protocol/`.

## 4.2 Upload sequence cho các Pha sau

| Pha | Bước | File upload | OSF Files folder |
|-----|------|-------------|---------------------|
| Pha 2 | Sau 7 | `dedup_unique.ris`, `dedup_report.txt`, `dedup_strict_report.txt` | `02_search/` |
| Pha 3 | Sau 8 | `screening_pre.csv`, `ta_screening.csv`, Rayyan export | `03_screening/` |
| Pha 3 | Sau 9 | `fulltext_decisions.csv`, `included_studies.csv` | `03_screening/` |
| Pha 3 | Sau 10 | `prisma_flow.png` + source | `03_screening/` |
| Pha 4 | Sau 11–13 | `extraction.csv`, `quality_appraisal.csv`, `borderline_decisions_log.md` | `04_extraction/` |
| Pha 5 | Sau 16–17 | bibliometric report + 5 PNG VOSviewer + heat-maps + research_agenda | `05_synthesis/` |
| Pha 6 | Sau 22 | manuscript supplementary package | top-level |

---

# §V. SNAPSHOT HISTORY — BACKUP POLICY §0.5

## 5.1 Workspace weekly snapshot (Sundays 22:00)

| Tuần | Date | Đích | Pool/state size | Notes |
|------|------|------|------------------|-------|
| Tuần 1 | _chưa có_ | Google Drive / GitHub private | – | Bắt đầu sau Bước 4 |

## 5.2 OSF Project state snapshot (sau mỗi mốc Bước)

| Mốc | Date | DOI Project + Registration | Files count | Notes |
|-----|------|----------------------------|-------------|-------|
| Sau 1.1 | 2026-05-10 | Project DOI: `10.17605/OSF.IO/DXJW9` | 0 | Project tạo, chưa upload |
| Sau 1.9 | _chờ_ | – | 5 (osf_release) | Sẽ upload sau Bước 1.9 |

---

# §VI. CHECKLIST OSF/RAYYAN CHO NCS

NCS làm tuần tự để hoàn tất Bước 1:

- [ ] Verify DOI: Project DOI vs Registration DOI (§II.2.2 cách verify) → báo Claude.
- [ ] Bước 1.2: cấu hình metadata Project `dxjw9` (§I.1.2) bằng [SR_OSF_Project_Metadata_v5.6.md](SR_OSF_Project_Metadata_v5.6.md) §IX checklist.
- [ ] Bước 1.4: review + chỉnh 4 trường ⚠️ trong [SR_OSF_Registration_Submission_v5.6.md](SR_OSF_Registration_Submission_v5.6.md) (§3 Authors / §17 Funding / §18 CoI / §19 Support).
- [ ] Bước 1.5: nếu DOI hiện tại là Project DOI → submit Registration thực sự (Tab Registrations → Add registration → paste 20 mục).
- [ ] Bước 1.9: upload 5 file `osf_release/` lên OSF Files → folder `01_protocol/` (theo §IV.4.1).
- [ ] Bước 1.10: tạo Rayyan project trống `SR_DT_Port` — KHÔNG upload pool RIS (Recovery R1).
- [ ] Bước 1.11: verify 7 Essentials features (§III.3.2) → ghi nhận vào table.
- [ ] Bước 1.12: nạp 28 mã EC/IC làm Reasons (§III.3.3).
- [ ] Bước 1.13: cập nhật Rayyan project ID + URL vào §III.3.1.
- [ ] Báo Claude → Claude tiếp Bước 2 phê duyệt Eligibility v1.0.

---

# §VII. CẢNH BÁO QUAN TRỌNG

1. **Phân biệt Project DOI vs Registration DOI** — KHÔNG cite Project DOI làm "pre-registration DOI" trong manuscript. Chỉ Registration DOI (immutable) thoả PRISMA Item 24a.
2. **Public state** — Project phải bật Public TRƯỚC khi submit Registration để Registration valid.
3. **Recovery R1** — KHÔNG upload pool RIS lên Rayyan ở Bước 1. Pool sẽ upload sau Bước 7 dedup.
4. **License CC-BY 4.0 KHÔNG đổi** sau Registration.
5. **Title KHÔNG đổi** sau Registration. Đổi nhỏ qua Amendment, đổi lớn → Withdraw Registration + Registration mới.

---

# §VIII. PHIÊN BẢN

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-05-11 | Tạo mới — internal tracker cho OSF Project `dxjw9` + Registration + Rayyan project (Bước 1.13 WorkPlan) |
