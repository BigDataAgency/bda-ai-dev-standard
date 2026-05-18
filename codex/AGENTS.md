# AGENTS.md — BDA AI Dev Standard for Codex

ใช้ไฟล์นี้เป็น project instruction สำหรับ Codex โดย copy ไปไว้ที่ root ของ repo เป้าหมายเป็น `AGENTS.md`.

## Entry point

- ถ้า repo เป้าหมายมี `AI-README.md` ให้ใช้ไฟล์นั้นเป็น entrypoint เพิ่มเติม
- ถ้าไม่มี `AI-README.md` ให้ทำตามกติกาในไฟล์นี้ได้ทันที ห้ามหยุดงานเพราะหา entrypoint ไม่เจอ

## Staff command pack v0.4.0

Codex uses this file as agent instruction; it does not use Claude Code slash commands. When asked for staff commands, reference normal command names:

- `daily-log` → `commands/daily-log.md` → internal `commands/employee-daily-log-v5.md`; mark missing commit/link/output as pending evidence.
- `weekly-focus` → `commands/weekly-focus.md` → internal `commands/pm-weekly-focus-v2.md`; do not turn planning into performance scoring.
- `test-report` → `commands/test-report.md` → internal `commands/test-scenario-report.md`; QA/product evidence only, not individual evaluation.

## Working rules

- สำรวจก่อนแก้เสมอ: files, tests, scripts, git status
- สรุปความเข้าใจและความเสี่ยงก่อนลงมือ เมื่อ scope ไม่ชัดให้ระบุ assumption
- ใช้ patch/edit แบบ targeted หลีกเลี่ยง refactor นอก scope
- งาน bug fix ต้อง reproduce หรืออธิบายให้ชัดว่าทำไม reproduce ไม่ได้, หา root cause, แก้แบบ minimal, และทำ regression check
- รัน verification ที่เกี่ยวข้องก่อนสรุป
- ห้าม claim ว่ารัน test หรือใช้งานได้ ถ้าไม่ได้รัน/ตรวจจริง

## Final response

ตอบภาษาไทยแบบกระชับ พร้อมหัวข้อ:

- Summary
- Files changed
- Tests / Evidence
- Risks / Limitations
- Next steps
