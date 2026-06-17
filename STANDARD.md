# BDA AI Operating Standard

## 1. Understand
- อ่าน task, issue, PR, branch, docs ที่เกี่ยวข้อง
- แยกเป้าหมาย, non-goals, constraints, deadline
- ระบุ assumption ถ้าข้อมูลไม่ครบ

## 2. Plan
- งานเล็ก: 3-5 bullet
- งานกลาง: แผนเป็น phase และไฟล์หลัก
- งานใหญ่: discovery, design, implementation, verification, rollout
- ระบุ success criteria ก่อนแก้ เพื่อให้ทุกขั้นตอนตรวจกลับได้
- วางแผน minimum correct change: ทำสิ่งที่จำเป็นให้ถูกต้องก่อน ไม่เพิ่ม abstraction/config/feature เผื่ออนาคต
- รักษา command/slash command เดิมเป็น default; เพิ่ม discipline ใน workflow ภายในแทนการเปลี่ยน UX โดยไม่จำเป็น

## 3. Execute
- แก้เฉพาะ scope ที่เกี่ยวข้อง
- เก็บ backward compatibility ถ้าเป็นระบบใช้งานจริง
- อย่า format หรือ refactor ใหญ่โดยไม่จำเป็น
- ทำตาม pattern เดิมของ repo ก่อนสร้าง pattern ใหม่
- ทุกบรรทัดที่แก้ต้อง trace กลับไปยัง request, bug, success criteria, หรือ verification ได้
- ห้ามเพิ่ม speculative abstraction, configuration, dependency, หรือ feature ที่ผู้ใช้ไม่ได้ขอ
- ถ้ามี assumption/ambiguity ให้หยุดถามเฉพาะเมื่อมีผลต่อ scope, data safety, security, หรือ correctness; ถ้าไม่กระทบให้ระบุ assumption แล้วทำต่อแบบเล็กที่สุด

## 4. Verify
- ใช้ test/lint/build/manual check จริง
- ถ้ารันไม่ได้ ให้บอก blocker และทางเลือกตรวจ
- เก็บ command และผลลัพธ์ไว้ในรายงาน
- map verification กลับไปยัง success criteria ทีละข้อ และระบุส่วนที่ยังไม่มี evidence

## 5. Handoff
- สรุปให้คนรับงานทำต่อได้ทันที
- ระบุไฟล์, behavior ที่เปลี่ยน, verification, risk, next step
- งานเล็กใช้ handoff สั้นได้ แต่ต้องยังมี success criteria/evidence/risk ที่ตรวจกลับได้
- ทุก handoff/report ของ BDA ต้องมีหัวข้อบังคับ: `BDA Standard files used`, `Pipeline trace`, `Commands run`, `Verification / Evidence`, `Limitations / Risks / Next steps`
- `BDA Standard files used` ต้องระบุ path ของไฟล์มาตรฐานที่เปิด/อ้างอิงจริง ไม่ใช่ชื่อกว้าง ๆ
- `Pipeline trace` ต้องตามรอย Understand → Plan → Execute → Verify → Handoff และบอก command/workflow ที่ใช้ในแต่ละช่วง
- `Commands run` ต้องเป็นคำสั่งหรือ tool ที่รันจริงพร้อมผลสรุป ถ้าไม่ได้รันต้องเขียนว่าไม่ได้รันและเหตุผล

## 6. Gateway-First Usage
- สำหรับ mapped BDA work แบบ non-trivial ให้ใช้ gateway-first-by-default: หลัง `bda start` ต้องพยายามมี Gateway checkpoint อย่างน้อย 1 ครั้งก่อนปิด session เว้นแต่มีเหตุผล skip/fail ที่ชัดเจน
- สถานะ Gateway ต่อ session ต้องเป็น `gateway_used`, `gateway_deferred`, `gateway_skipped`, หรือ `gateway_failed`
- ใช้ Gateway เมื่อเป็น bounded subtask ที่ควรมี usage ใน audit trail หรือช่วยลดความเสี่ยงจริง เช่น requirement/risk/test-plan/evidence/PM wording/release/deploy/security/auth/schema review
- ใช้ `gateway_deferred` เมื่อ Codex/AI หลักต้องเก็บ deterministic repo/tool evidence ก่อน แต่ยังต้องวาง checkpoint ก่อน closeout
- ห้ามยิง Gateway เปล่าเพื่อสร้าง usage; ต้องมี model call จริง สำเร็จ และนำผลมาใช้ก่อน log `used_bda_gateway=true`
- Codex/Claude/Gemini/AI อื่นที่ไม่ได้ route ผ่าน Gateway ต้องใช้ metadata จริงของ runtime นั้น และ keep `used_bda_gateway=false`
- ถ้า skip หรือ fail ให้บอกเหตุผลใน outcome/blocker/final summary แทนการปลอมว่าใช้ Gateway
- Gateway target ranges เป็น guidance ไม่ใช่ KPI แข็ง: 80-100% สำหรับ PM/reporting และ delivery evidence, 70-100% สำหรับ security/auth/schema/CI/CD/high-risk, 50-80% สำหรับ ambiguous multi-module, 30-60% สำหรับ bug/feature ปกติ, 0-20% สำหรับ deterministic checks, และ 0% สำหรับ casual/setup/secrets-sensitive/Codex-only
- Direct BDA Gateway API ใช้ตรวจ model availability ได้เมื่อ Hermes oneshot มีข้อจำกัด เช่น `bda/qwen3.7-max-paid-cloud` อยู่บน Gateway แต่ Hermes oneshot ไม่คืน final response

## 7. Standard Feedback Loop
- ใช้ `FEEDBACK.md`, `commands/standard-feedback.md`, `templates/standard-feedback.md`, และ `workflows/standard-improvement.md` เมื่อต้องการ feedback เพื่อปรับปรุง BDA AI Dev Standard เอง
- รับ feedback ประเภท bug report, confusion, missing command, feature request, scenario request, adoption friction, AI output issue หรือข้อเสนออื่น ๆ ที่ทำให้ standard ดีขึ้น
- Feedback loop นี้แยกจาก performance process โดยสิ้นเชิง: ไม่ใช่ score, KPI, daily performance, หรือการประเมินบุคคล
- role/team ใน feedback เป็น optional usage context เท่านั้น ไม่ใช้ตัดสินผลงานรายบุคคล
- ทุกการแก้มาตรฐานต้องทำใน repo นี้ก่อน แล้ว verify ตาม `UPDATE-POLICY.md`

## Definition of Done
- Requirement หลักครบ
- Success criteria ทุกข้อมีผลลัพธ์หรือข้อจำกัดที่ระบุชัด
- Change เป็น minimum correct change และไม่มี speculative abstraction/config/feature
- ทุก changed line trace กลับไปยัง request หรือ verification ได้
- ไม่มี unrelated refactor, format churn, หรือ style-only change นอก scope
- ไม่มี fake evidence
- มี verification ที่เหมาะสมและ map กลับไปยัง success criteria
- มี handoff/report
- handoff/report มี BDA files used, pipeline trace, commands run, evidence, limitations ครบถ้วน
- ถ้าเป็น production-facing ต้องมี rollback หรือ mitigation
