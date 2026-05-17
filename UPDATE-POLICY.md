# Update Policy

Repo นี้คือ source of truth สำหรับ BDA AI Dev Standard

## กติกา
- Future updates ต้องเริ่มจาก repo นี้ก่อน
- ห้ามแก้สำเนาในเครื่องมืออื่นแล้วถือเป็น canonical โดยไม่ sync กลับ repo นี้
- ทุก change ควรมีเหตุผล, วันที่, ผู้แก้ และผลกระทบ
- Employee-facing files ต้องใช้ถ้อยคำ neutral และไม่อ้างแหล่งภายนอก
- ถ้ามีการ adapt แนวคิดหรือไฟล์ที่มี license ให้ใส่ใน `THIRD_PARTY_NOTICES.md`

## Release flow
1. แก้ใน branch หรือ commit ที่ชัดเจน
2. Review ด้วย `commands/review-change.md`
3. Verify ด้วย `commands/verify-work.md`
4. Tag หรือประกาศ version ถ้าเป็น update ใหญ่
5. Rollout ไปยัง AI tools / team docs จาก repo นี้เท่านั้น

## Feedback-driven improvements
- รับ feedback เพื่อปรับปรุงมาตรฐานผ่าน `FEEDBACK.md`, `commands/standard-feedback.md`, และ `templates/standard-feedback.md`
- ถ้า feedback นำไปสู่การแก้ repo ให้ใช้ `workflows/standard-improvement.md` และ verify ก่อน commit/rollout
- Feedback นี้เป็น product-improvement loop ของ BDA AI Dev Standard เท่านั้น ไม่ใช่ Employee Daily Log v5, performance review, KPI, score, daily performance หรือการประเมินบุคคล
- ห้ามใช้ role/team/context ใน feedback เพื่อประเมินผลงานรายบุคคล; ใช้เพื่อเข้าใจ adoption และ scenario ของมาตรฐานเท่านั้น
