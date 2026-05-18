# Command: Daily Log

Staff-facing alias for the internal canonical daily log v5 standard `commands/employee-daily-log-v5.md` and template `templates/daily-log-v5.md`.

## ใช้เมื่อ

ต้องการสรุปงานรายวันแบบตรวจสอบได้ โดยใช้ชื่อปกติ `daily-log` แทนชื่อ internal/versioned `employee-daily-log-v5`.

## Mapping

- Staff command name: `daily-log`
- Internal source of truth: `commands/employee-daily-log-v5.md`
- Template: `templates/daily-log-v5.md`
- Claude Code slash alias: `/daily-log` จาก `claude/commands/daily-log.md`

## Evidence guardrail

ห้ามสร้างหลักฐานปลอม ถ้าไม่มี commit/link/output/test/screenshot/log ให้เขียนว่า `pending evidence` หรือ `ยังไม่มีหลักฐานแนบ` พร้อมระบุสิ่งที่ต้องตามต่อ ห้ามเดา commit hash, PR link, ticket link, token/cost หรือผลตรวจ.

## Copy this into AI

```text
ทำงาน: Daily Log
Context: <วางงานวันนี้, commit/link/output ที่มี, blocker, tomorrow focus, AI usage ถ้ามี>
โปรดทำตามขั้นตอนนี้:
1. อ่านและใช้ internal standard `commands/employee-daily-log-v5.md` กับ `templates/daily-log-v5.md`
2. รวบรวมงานวันนี้และแยก output/result/blocker
3. ระบุ evidence ต่อ item: commit/link/output/test/screenshot/log/manual check เท่าที่มีจริง
4. ถ้า evidence ใดไม่มีหรือยังไม่ได้ส่งมา ให้ mark เป็น pending evidence; ห้าม invent หรือ assume
5. ระบุ AI usage ทุกวัน: ถ้าใช้ AI ต้องใส่ tool/model และ token/cost ถ้ามีจริง; ถ้าไม่มีข้อมูล token/cost ให้ใส่ pending/not available; ถ้าไม่ได้ใช้ AI ต้องยืนยัน "No AI used / ไม่ได้ใช้ AI"
6. ระบุ tomorrow focus และ confidence พร้อมเหตุผลจากหลักฐานจริง

Output ที่ต้องส่ง: Daily Log ตาม internal Employee Daily Log v5 template แต่ใช้หัวข้อ/ชื่อ staff-facing ว่า Daily Log ได้
Output ที่ต้องส่งต้องมีหัวข้อ: BDA Standard files used, Pipeline trace, Commands run, Verification / Evidence, Limitations / Risks / Next steps
```

## Checklist

- [ ] ใช้ internal source `commands/employee-daily-log-v5.md`
- [ ] แยกงาน/result/blocker ชัดเจน
- [ ] ใส่ evidence จริงต่อ item หรือ mark pending evidence
- [ ] ไม่ fabricate commit/link/output/test/token/cost
- [ ] ระบุ AI usage ครบ หรือยืนยัน no-AI
- [ ] ระบุ tomorrow focus และ confidence

## Required report sections

ทุกครั้งที่ใช้ command นี้ ต้องส่งรายงานท้ายงานเป็นภาษาไทยและมีหัวข้อเหล่านี้ครบถ้วน:

1. **BDA Standard files used** — ระบุ path ของไฟล์มาตรฐาน BDA ที่เปิด/อ้างอิงจริง เช่น `commands/daily-log.md`, `commands/employee-daily-log-v5.md`, `templates/daily-log-v5.md`
2. **Pipeline trace** — Understand → Plan → Execute → Verify → Handoff พร้อม command/workflow ที่ใช้จริง
3. **Commands run** — คำสั่ง/tool/search ที่รันจริง พร้อมผลสรุป; ถ้าไม่ได้รันให้ระบุ `ไม่ได้รัน` และเหตุผล
4. **Verification / Evidence** — หลักฐานจริง หรือ `pending evidence` สำหรับสิ่งที่ยังไม่มี
5. **Limitations / Risks / Next steps** — ข้อจำกัด ความเสี่ยง และสิ่งที่ต้องตามต่อ

---
ใช้ `daily-log` เป็นชื่อปกติสำหรับ staff; เก็บ `employee-daily-log-v5` เป็น internal canonical standard.
