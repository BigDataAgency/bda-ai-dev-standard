# Changelog

All notable changes to BDA AI Dev Standard are tracked here.

This project uses Semantic Versioning: `MAJOR.MINOR.PATCH`.

- MAJOR: breaking changes to command names, required outputs, or installation layout
- MINOR: new commands, workflows, templates, adapters, or substantial behavior improvements
- PATCH: clarifications, typo fixes, safer wording, and non-breaking documentation updates

## [0.6.0] - 2026-05-21

### Removed

- Removed legacy versioned daily/weekly command files and Claude adapters.
- Removed legacy daily/weekly template filenames and replaced them with normal template names:
  - `templates/daily-log.md`
  - `templates/weekly-focus.md`
- Removed legacy self-contained wording from report-sender command docs.

### Changed

- `daily-log` and `weekly-focus` are now direct canonical commands, not aliases to versioned internal commands.
- Updated README, AI, Claude, Codex, staff, Gemini, and Claude coworker docs to reference only normal command names.
- Updated smoke validation to fail if removed legacy daily/weekly terms or files return.
- Updated current version metadata to `0.6.0`.

## [0.5.0] - 2026-05-21

### Added

- `commands/init.md` for initializing Obsidian/project context before running normal work commands.
- `templates/obsidian-context.md` as the canonical context manifest template.
- `templates/obsidian-work-note.md` for session notes and testcase/evidence notes.
- Claude Code slash adapter `claude/commands/init.md`.

### Changed

- `plan-work`, `fix-bug`, `build-feature`, `write-document`, and `update-obsidian` now read Obsidian context when present and update session/evidence notes by default.
- `workflows/obsidian.md`, `AI-README.md`, `README.md`, `claude/CLAUDE.md`, and `codex/AGENTS.md` now document the init-to-context flow.
- Updated current version metadata to `0.5.0`.

## [0.4.1] - 2026-05-18

### Added

- Public-repo ingress protection hardening:
  - `.env.example` with local-only defaults and empty InnoHub ingest placeholders.
  - `SECURITY.md` documenting public repository boundaries, local-output default mode, and private production-ingest requirements.
  - `docs/public-ingest-guardrails.md` for future private InnoHub connector controls.
  - `scripts/security-public-repo-check.sh` to block production endpoint/secret patterns in public files.

### Changed

- Expanded `.gitignore` coverage for local env files, credentials, secrets, and private key material while keeping `.env.example` tracked.
- Added README security notice for public repository usage and no auto-ingest defaults.
- Updated current version metadata to `0.4.1`.

## [0.4.0] - 2026-05-18

### Added

- Command pack with normal, non-versioned command names:
  - `commands/daily-log.md`
  - `commands/weekly-focus.md`
  - `commands/test-report.md`
- Claude Code slash aliases: `/daily-log`, `/weekly-focus`, `/test-report`.
- Staff documentation under `staff/commands/` and adapter prompt packs for Gemini and Claude coworker.
- Codex/Claude/general AI docs now describe command aliases and adapter-specific usage.

### Changed

- Updated current version metadata to `0.4.0`.
- Added friendly aliases for daily, weekly, and test report workflows.

### Guardrails

- Daily Log requires missing commit/link/output evidence to be marked as pending evidence instead of invented.
- Weekly Focus remains a planning/coordination artifact and must not become performance scoring.
- Test Report keeps QA/product evidence behavior and must not be used for individual performance evaluation.

## [0.3.0] - 2026-05-18

### Changed

- Improved `test-scenario-report` based on an InnoHub production trial:
  - Added production read-only guardrails and no-mutation pass criteria.
  - Added Auth/RBAC matrix and test account classification.
  - Added route source trace, technical-verification-only wording, route drift checks, and SPA 404 detection.
  - Added blocked reason taxonomy and evidence manifest with screenshot/console/network/PII masking fields.
  - Reinforced InnoHub/user-facing visible-menu navigation rule.

## [0.2.0] - 2026-05-17

### Added

- QA/product evidence workflow for test case/scenario execution with screenshot capture and Markdown report generation:
  - `commands/test-scenario-report.md`
  - `workflows/test-scenario-report.md`
  - `templates/test-scenario-report.md`
  - `claude/commands/test-scenario-report.md`
- Smoke validation coverage for the new test scenario report workflow and Claude slash command.

### Notes

- This workflow is explicitly separate from Daily Log and performance evaluation.
- User-facing checks, including InnoHub scenarios, should use visible-menu navigation by default; hidden/direct routes must be labeled technical verification only.

## [0.1.0] - 2026-05-17

Initial public release.

### Added

- Core BDA AI Dev Standard documentation: `README.md`, `AI-README.md`, `STANDARD.md`
- Neutral commands for common work types:
  - pending work
  - new work / feature work
  - bug fix
  - code review
  - small / medium / large tasks
  - writing and documents
  - Obsidian updates
  - performance review
  - Daily Log
  - Weekly Focus
- Codex adapter: `codex/AGENTS.md`
- Claude adapter and slash-command files: `claude/CLAUDE.md`, `claude/commands/*.md`
- Required reporting trace for every standard-driven task:
  - BDA Standard files used
  - Pipeline trace
  - Commands run
  - Verification / Evidence
  - Limitations / Risks / Next steps
- Feedback loop for improving the standard, separate from Daily Log and performance evaluation:
  - `FEEDBACK.md`
  - `commands/standard-feedback.md`
  - `templates/standard-feedback.md`
  - `workflows/standard-improvement.md`
- Smoke validation script: `scripts/smoke-standard-scenarios.py`
- MIT License

### Notes

This release is a curated internal-practice standard made public for reuse and feedback. It is not presented as original invention; it combines practical patterns, lessons learned, and open-source-friendly documentation into a versioned workflow standard.
