# /daily-log

Claude Code slash alias for staff-facing Daily Log.

ใช้ command หลัก `commands/daily-log.md` ซึ่ง map ไป internal canonical `commands/employee-daily-log-v5.md` และ `templates/daily-log-v5.md` แล้วตอบตาม BDA AI Dev Standard เป็นภาษาไทย.

Evidence guardrail: ห้ามสร้างหลักฐานปลอม ถ้าไม่มี commit/link/output/test/screenshot/log/token/cost ให้ระบุ `pending evidence` หรือ `not available` และบอกสิ่งที่ต้องตามต่อ.

ติดตั้ง slash command โดย copy ไฟล์นี้ไปไว้ที่ `.claude/commands/daily-log.md` ของ target repo แล้วเรียก `/daily-log` ใน Claude Code แบบ interactive เท่านั้น.

หมายเหตุ: ใน print mode (`claude -p`) slash command แบบ interactive จะไม่ถูกรันโดยตรง ให้ reference ไฟล์ `commands/daily-log.md` หรือ paste prompt จาก command แทน.

ต้องรายงานหัวข้อบังคับ: BDA Standard files used, Pipeline trace, Commands run, Verification / Evidence, Limitations / Risks / Next steps
