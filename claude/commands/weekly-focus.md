# /weekly-focus

Claude Code slash alias for staff-facing Weekly Focus.

ใช้ command หลัก `commands/weekly-focus.md` ซึ่ง map ไป internal canonical `commands/pm-weekly-focus-v2.md` และ `templates/pm-weekly-focus-v2.md` แล้วตอบตาม BDA AI Dev Standard เป็นภาษาไทย.

Non-performance guardrail: Weekly Focus เป็น planning/coordination artifact เท่านั้น ไม่ใช่ performance review, score, KPI scoring, ranking, disciplinary evidence, หรือการประเมินรายบุคคล.

ติดตั้ง slash command โดย copy ไฟล์นี้ไปไว้ที่ `.claude/commands/weekly-focus.md` ของ target repo แล้วเรียก `/weekly-focus` ใน Claude Code แบบ interactive เท่านั้น.

หมายเหตุ: ใน print mode (`claude -p`) slash command แบบ interactive จะไม่ถูกรันโดยตรง ให้ reference ไฟล์ `commands/weekly-focus.md` หรือ paste prompt จาก command แทน.

ต้องรายงานหัวข้อบังคับ: BDA Standard files used, Pipeline trace, Commands run, Verification / Evidence, Limitations / Risks / Next steps
