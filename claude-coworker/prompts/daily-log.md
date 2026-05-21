# Claude coworker Prompt Command: Daily Log

This is a prompt command, not a Claude Code slash command.

## Copy/paste prompt

```text
Use BDA AI Dev Standard current command `daily-log`.
Read/reference `commands/daily-log.md`. Treat `commands/daily-log.md` as the source of truth and `templates/daily-log.md` as the output template where applicable.

Guardrail: Mark missing commit/link/output/test/log/screenshot/token/cost as pending evidence; do not invent evidence.

Context:
<วาง context งานจริงที่นี่>

Required output sections: BDA Standard files used, Pipeline trace, Commands run, Verification / Evidence, Limitations / Risks / Next steps.
If a command/tool/test was not run, say it was not run and why. Do not claim evidence that is not present.
```

## Adapter note

Use this file as a paste/reference prompt for Claude coworker. Slash commands such as `/daily-log` are Claude Code interactive only.
