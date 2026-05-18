# Changelog

All notable changes to BDA AI Dev Standard are tracked here.

This project uses Semantic Versioning: `MAJOR.MINOR.PATCH`.

- MAJOR: breaking changes to command names, required outputs, or installation layout
- MINOR: new commands, workflows, templates, adapters, or substantial behavior improvements
- PATCH: clarifications, typo fixes, safer wording, and non-breaking documentation updates

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

- Staff command pack with normal, non-versioned command names:
  - `commands/daily-log.md` maps to internal `commands/employee-daily-log-v5.md`.
  - `commands/weekly-focus.md` maps to internal `commands/pm-weekly-focus-v2.md`.
  - `commands/test-report.md` maps to internal QA/product evidence standard `commands/test-scenario-report.md`.
- Claude Code slash aliases: `/daily-log`, `/weekly-focus`, `/test-report`.
- Staff documentation under `staff/commands/` and adapter prompt packs for Gemini and Claude coworker.
- Codex/Claude/general AI docs now describe staff command aliases and adapter-specific usage.

### Changed

- Updated current version metadata to `0.4.0`.
- Kept canonical versioned standards internal while exposing staff-friendly aliases.

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

- This workflow is explicitly separate from Employee Daily Log v5 and performance evaluation.
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
  - Employee Daily Log v5
  - PM Weekly Focus v2
- Codex adapter: `codex/AGENTS.md`
- Claude adapter and slash-command files: `claude/CLAUDE.md`, `claude/commands/*.md`
- Required reporting trace for every standard-driven task:
  - BDA Standard files used
  - Pipeline trace
  - Commands run
  - Verification / Evidence
  - Limitations / Risks / Next steps
- Feedback loop for improving the standard, separate from Employee v5 and performance evaluation:
  - `FEEDBACK.md`
  - `commands/standard-feedback.md`
  - `templates/standard-feedback.md`
  - `workflows/standard-improvement.md`
- Smoke validation script: `scripts/smoke-standard-scenarios.py`
- MIT License

### Notes

This release is a curated internal-practice standard made public for reuse and feedback. It is not presented as original invention; it combines practical patterns, lessons learned, and open-source-friendly documentation into a versioned workflow standard.
