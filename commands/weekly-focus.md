# Command: Weekly Focus

Weekly planning and coordination command. This is the canonical `weekly-focus` command and uses `templates/weekly-focus.md`.

## ใช้เมื่อ

ต้องการวาง weekly focus และ priorities สำหรับ PM/team coordination โดยใช้ชื่อปกติ `weekly-focus`.

## Files

- Command: `commands/weekly-focus.md`
- Template: `templates/weekly-focus.md`
- Claude Code slash command: `/weekly-focus` จาก `claude/commands/weekly-focus.md`

## Non-performance guardrail

Weekly Focus เป็น planning/coordination artifact เท่านั้น ไม่ใช่ performance review, score, KPI scoring, ranking, disciplinary evidence, หรือการประเมินรายบุคคล. ห้ามเปลี่ยน priorities/owner/risk ให้กลายเป็นคะแนนผลงาน.

## Copy this into AI

```text
ทำงาน: Weekly Focus
Context: <วางเป้าหมายสัปดาห์, priorities, owner, date, blocker, decision needed>
โปรดทำตามขั้นตอนนี้:
1. อ่านและใช้ standard `commands/weekly-focus.md` กับ `templates/weekly-focus.md`
2. รวบรวม priorities และแยก committed vs stretch
3. ระบุ owner/date/risk/success metric เท่าที่ทราบ
4. เชื่อม blockers กับ decision needed
5. ตรวจว่า output เป็นแผน/coordination ไม่ใช่ performance scoring
6. ถ้าข้อมูลไม่ครบ ให้ mark missing/pending แทนการเดา

Output ที่ต้องส่ง: Weekly Focus ตาม template
Output ที่ต้องส่งต้องมีหัวข้อ: BDA Standard files used, Pipeline trace, Commands run, Verification / Evidence, Limitations / Risks / Next steps
```

## Checklist

- [ ] ใช้ `commands/weekly-focus.md` และ `templates/weekly-focus.md`
- [ ] ระบุ committed vs stretch
- [ ] ระบุ owner/date/risk/success metric เท่าที่มีจริง
- [ ] ระบุ blockers และ decisions needed
- [ ] ไม่มี performance score/ranking/การประเมินรายบุคคล
- [ ] Missing info ถูก mark เป็น pending/missing ไม่เดา

## Required report sections

ทุกครั้งที่ใช้ command นี้ ต้องส่งรายงานท้ายงานเป็นภาษาไทยและมีหัวข้อเหล่านี้ครบถ้วน:

1. **BDA Standard files used** — ระบุ path เช่น `commands/weekly-focus.md`, `templates/weekly-focus.md`
2. **Pipeline trace** — Understand → Plan → Execute → Verify → Handoff พร้อม command/workflow ที่ใช้จริง
3. **Commands run** — คำสั่ง/tool/search ที่รันจริง พร้อมผลสรุป; ถ้าไม่ได้รันให้ระบุเหตุผล
4. **Verification / Evidence** — แหล่งข้อมูลจริง เช่น roadmap/ticket/link/meeting note หรือระบุ pending/missing
5. **Limitations / Risks / Next steps** — ข้อจำกัด ความเสี่ยง และสิ่งที่ต้องตามต่อ

---
ใช้ `weekly-focus` เป็น canonical command สำหรับ weekly planning/coordination.
