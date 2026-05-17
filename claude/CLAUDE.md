# CLAUDE.md — BDA AI Dev Standard

ใช้เอกสารนี้เมื่อทำงานในโปรเจกต์ BDA

1. อ่าน `AI-README.md`
2. เลือก command ใน `commands/`
3. ทำงานตาม `STANDARD.md`
4. ตรวจด้วย policies และ checklists
5. สรุปภาษาไทยพร้อม evidence

## ติดตั้งใน target repo

1. Copy ไฟล์นี้ไปเป็น `CLAUDE.md` ที่ root ของ target repo
2. Copy `claude/commands/*.md` ไปไว้ที่ `.claude/commands/` ของ target repo
3. เปิด Claude Code แบบ interactive ใน target repo แล้วใช้ slash commands ได้ เช่น `/fix-bug`, `/review-change`, `/build-feature`, `/write-document`, `/verify-work`

หมายเหตุ: slash commands ใช้กับ interactive Claude Code เท่านั้น; ใน print mode (`claude -p`) ให้ reference path ของ command หรือ paste เนื้อหา command แทน เพราะ `/command` จะไม่ทำงานแบบ interactive

## Output บังคับ

ทุกคำตอบ/รายงานต้องมีหัวข้อเหล่านี้ครบ:

- **BDA Standard files used**: path ของไฟล์มาตรฐาน BDA ที่ใช้จริง
- **Pipeline trace**: Understand → Plan → Execute → Verify → Handoff พร้อม command/workflow ที่ใช้
- **Commands run**: คำสั่งหรือ tool ที่รันจริง พร้อมผลสรุป; ถ้าไม่ได้รันให้ระบุเหตุผล
- **Verification / Evidence**: หลักฐานตรวจจริง
- **Limitations / Risks / Next steps**: ข้อจำกัด ความเสี่ยง และงานต่อ
