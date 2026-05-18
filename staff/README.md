# Staff Command Pack — BDA AI Dev Standard v0.4.0

Staff should use normal command names without internal version suffixes.

## Commands

- `daily-log` — daily work summary with evidence; internal source `employee-daily-log-v5`
- `weekly-focus` — weekly planning/focus; internal source `pm-weekly-focus-v2`
- `test-report` — QA/product test evidence; internal source `test-scenario-report`

## Adapter usage

- Claude Code: slash commands are available only in interactive Claude Code after copying `claude/commands/*.md` to `.claude/commands/`. Use `/daily-log`, `/weekly-focus`, `/test-report`.
- Gemini: use prompt command files in `gemini/prompts/`; do not use slash-command syntax as if it were Claude Code.
- Claude coworker: use prompt command files in `claude-coworker/prompts/`; these are paste/reference prompts.
- Codex: use `codex/AGENTS.md` as agent instruction and reference `commands/daily-log.md`, `commands/weekly-focus.md`, or `commands/test-report.md`.

## Guardrails

- No fake evidence: missing commit/link/output/test/log/screenshot must be marked pending evidence.
- Weekly Focus is not performance scoring or ranking.
- Test Report is QA/product evidence, not individual performance evaluation.

## Required BDA output sections

Every staff command output must include: BDA Standard files used, Pipeline trace, Commands run, Verification / Evidence, Limitations / Risks / Next steps.
