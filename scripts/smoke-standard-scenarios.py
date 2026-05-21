#!/usr/bin/env python3
"""Smoke validation for BDA AI Dev Standard coverage.

This script is intentionally dependency-free and safe: it reads this standard
repo only and writes a temporary sandbox under /tmp for scenario-output checks.
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SANDBOX = Path("/tmp/bda-ai-dev-standard-smoke")
EXPECTED_VERSION = "0.5.0"

REQUIRED_SECTIONS = [
    "BDA Standard files used",
    "Pipeline trace",
    "Commands run",
    "Verification / Evidence",
    "Limitations / Risks / Next steps",
]

SCENARIOS = {
    "init": ["commands/init.md", "templates/obsidian-context.md", "templates/obsidian-work-note.md", "workflows/obsidian.md"],
    "bug-fix": ["commands/fix-bug.md", "workflows/bug-fix.md"],
    "review-change": ["commands/review-change.md", "workflows/code-review.md"],
    "write-document": ["commands/write-document.md", "workflows/writing-docs.md"],
    "employee-daily-log-v5": ["commands/employee-daily-log-v5.md", "templates/daily-log-v5.md"],
    "pm-weekly-focus-v2": ["commands/pm-weekly-focus-v2.md", "templates/pm-weekly-focus-v2.md"],
    "update-obsidian": ["commands/update-obsidian.md", "workflows/obsidian.md"],
    "performance-review": ["commands/performance-review.md", "workflows/performance.md"],
    "standard-feedback": ["commands/standard-feedback.md", "templates/standard-feedback.md", "workflows/standard-improvement.md", "FEEDBACK.md"],
    "test-scenario-report": ["commands/test-scenario-report.md", "templates/test-scenario-report.md", "workflows/test-scenario-report.md"],
    "daily-log": ["commands/daily-log.md", "templates/daily-log-v5.md"],
    "weekly-focus": ["commands/weekly-focus.md", "templates/pm-weekly-focus-v2.md"],
    "test-report": ["commands/test-report.md", "templates/test-scenario-report.md", "workflows/test-scenario-report.md"],
}

GLOBAL_FILES = [
    "STANDARD.md",
    "AI-README.md",
    "README.md",
    "claude/CLAUDE.md",
]

CLAUDE_COMMANDS = [
    "claude/commands/init.md",
    "claude/commands/fix-bug.md",
    "claude/commands/review-change.md",
    "claude/commands/build-feature.md",
    "claude/commands/write-document.md",
    "claude/commands/verify-work.md",
    "claude/commands/standard-feedback.md",
    "claude/commands/test-scenario-report.md",
    "claude/commands/daily-log.md",
    "claude/commands/weekly-focus.md",
    "claude/commands/test-report.md",
]

STAFF_COMMAND_PACK = {
    "daily-log": {
        "command": "commands/daily-log.md",
        "claude": "claude/commands/daily-log.md",
        "legacy": "commands/employee-daily-log-v5.md",
        "terms": ["Daily Log", "Daily Log v5", "AI usage", "tomorrow focus"],
    },
    "weekly-focus": {
        "command": "commands/weekly-focus.md",
        "claude": "claude/commands/weekly-focus.md",
        "legacy": "commands/pm-weekly-focus-v2.md",
        "terms": ["Weekly Focus", "weekly focus v2", "priorities", "committed", "stretch"],
    },
    "test-report": {
        "command": "commands/test-report.md",
        "claude": "claude/commands/test-report.md",
        "legacy": "commands/test-scenario-report.md",
        "terms": ["Test Report", "QA/product evidence", "screenshot", "test matrix", "expected", "actual"],
    },
}

# Optional staff adapters: if these files are added by the v0.4.0 implementation,
# validate that they expose the normal staff command names rather than v5/v2 names.
OPTIONAL_STAFF_ADAPTER_GLOBS = [
    "staff/**/*.md",
    "gemini/**/*.md",
    "claude-coworker/**/*.md",
]

FORBIDDEN_CLAIMS = [
    r"test(s)? passed(?!.*(if|when|example))",
    r"ตรวจแล้วผ่าน(?!.*(ถ้า|เมื่อ|ตัวอย่าง))",
]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"missing file: {rel}")
    return path.read_text(encoding="utf-8")


def assert_contains_all(rel: str, terms: list[str]) -> None:
    text = read(rel)
    missing = [term for term in terms if term not in text]
    if missing:
        raise AssertionError(f"{rel} missing required terms: {missing}")


def validate_version_consistency() -> None:
    version = read("VERSION").strip()
    if version != EXPECTED_VERSION:
        raise AssertionError(f"VERSION is {version!r}, expected {EXPECTED_VERSION!r}")

    assert_contains_all("README.md", [f"Version: `{EXPECTED_VERSION}`", f"Current version: `{EXPECTED_VERSION}`"])
    assert_contains_all("CHANGELOG.md", [f"## [{EXPECTED_VERSION}]", "daily-log", "weekly-focus", "test-report"])


def validate_required_sections() -> None:
    for rel in GLOBAL_FILES:
        assert_contains_all(rel, REQUIRED_SECTIONS)

    for rel in sorted((ROOT / "commands").glob("*.md")):
        assert_contains_all(str(rel.relative_to(ROOT)), REQUIRED_SECTIONS)

    for rel in sorted((ROOT / "workflows").glob("*.md")):
        assert_contains_all(str(rel.relative_to(ROOT)), REQUIRED_SECTIONS)

    for rel in CLAUDE_COMMANDS:
        assert_contains_all(rel, REQUIRED_SECTIONS)


def validate_claude_usage_docs() -> None:
    for rel in ["README.md", "claude/CLAUDE.md"]:
        assert_contains_all(
            rel,
            [
                ".claude/commands/",
                "interactive",
                "claude -p",
                "/init",
                "/fix-bug",
                "/review-change",
                "/standard-feedback",
                "/daily-log",
                "/weekly-focus",
                "/test-report",
            ],
        )


def validate_obsidian_init_workflow() -> None:
    init_files = [
        "commands/init.md",
        "templates/obsidian-context.md",
        "templates/obsidian-work-note.md",
        "workflows/obsidian.md",
        "claude/commands/init.md",
    ]
    required_terms = [
        "00-Agent-Context.md",
        "sessions/_index.md",
        "test-evidence/_index.md",
        "Obsidian context manifest",
        "pending evidence",
    ]
    for rel in ["commands/init.md", "workflows/obsidian.md", "claude/commands/init.md"]:
        assert_contains_all(rel, [*REQUIRED_SECTIONS, "00-Agent-Context.md"])

    for rel in [
        "README.md",
        "AI-README.md",
        "claude/CLAUDE.md",
        "codex/AGENTS.md",
        "commands/plan-work.md",
        "commands/fix-bug.md",
        "commands/build-feature.md",
        "commands/write-document.md",
        "commands/update-obsidian.md",
    ]:
        assert_contains_all(rel, ["commands/init.md", "00-Agent-Context.md"])

    assert_contains_all("templates/obsidian-context.md", required_terms[:4])
    assert_contains_all("templates/obsidian-work-note.md", ["Testcase / Evidence", "Obsidian updates"])


def validate_staff_command_pack() -> None:
    for name, spec in STAFF_COMMAND_PACK.items():
        assert_contains_all(spec["command"], [*REQUIRED_SECTIONS, *spec["terms"], spec["legacy"]])
        assert_contains_all(spec["claude"], [f"/{name}", spec["command"], *REQUIRED_SECTIONS])

    # User-facing docs should advertise normal command names. Legacy v5/v2 names
    # may remain as implementation/template details, but not as primary slash commands.
    for rel in ["README.md", "claude/CLAUDE.md"]:
        assert_contains_all(
            rel,
            [
                "commands/daily-log.md",
                "commands/weekly-focus.md",
                "commands/test-report.md",
                "/daily-log",
                "/weekly-focus",
                "/test-report",
            ],
        )
        text = read(rel)
        forbidden = [r"(?<![A-Za-z0-9_.-])/employee-daily-log-v5", r"(?<![A-Za-z0-9_.-])/pm-weekly-focus-v2", r"(?<![A-Za-z0-9_.-])/test-scenario-report"]
        found = [pattern for pattern in forbidden if re.search(pattern, text)]
        if found:
            raise AssertionError(f"{rel} exposes legacy/versioned slash command names: {found}")


def validate_optional_staff_adapters() -> None:
    adapter_paths: list[Path] = []
    for pattern in OPTIONAL_STAFF_ADAPTER_GLOBS:
        adapter_paths.extend(ROOT.glob(pattern))

    # The v0.4.0 pack may add staff/gemini/claude-coworker prompt files; when
    # present, they must point staff users at normal command names. Internal
    # source-of-truth paths may still mention the legacy canonical files.
    for path in sorted(set(adapter_paths)):
        rel = str(path.relative_to(ROOT))
        if path.name == "README.md":
            assert_contains_all(rel, ["daily-log", "weekly-focus", "test-report"])
        elif path.stem in STAFF_COMMAND_PACK:
            assert_contains_all(rel, [path.stem, STAFF_COMMAND_PACK[path.stem]["command"]])

        text = read(rel)
        forbidden_slash = [r"(?<![A-Za-z0-9_.-])/employee-daily-log-v5", r"(?<![A-Za-z0-9_.-])/pm-weekly-focus-v2", r"(?<![A-Za-z0-9_.-])/test-scenario-report"]
        found = [pattern for pattern in forbidden_slash if re.search(pattern, text)]
        if found:
            raise AssertionError(f"{rel} exposes legacy/versioned slash command names: {found}")


def validate_standard_feedback_loop() -> None:
    feedback_files = [
        "FEEDBACK.md",
        "commands/standard-feedback.md",
        "templates/standard-feedback.md",
        "workflows/standard-improvement.md",
        "claude/commands/standard-feedback.md",
    ]
    required_terms = [
        "BDA AI Dev Standard",
        "Employee Daily Log v5",
        "performance",
        "ไม่ใช่",
    ]
    for rel in feedback_files:
        assert_contains_all(rel, required_terms)

    assert_contains_all(
        "templates/standard-feedback.md",
        [
            "Tool used",
            "Command or workflow used",
            "Expected behavior",
            "Actual behavior / friction",
            "Suggested improvement",
            "Non-performance confirmation",
        ],
    )

    assert_contains_all(
        "README.md",
        [
            "FEEDBACK.md",
            "commands/standard-feedback.md",
            "templates/standard-feedback.md",
            "workflows/standard-improvement.md",
            "ไม่ใช่ทุกทีม/ทุก role ใช้มาตรฐานนี้",
        ],
    )


def validate_test_scenario_report_workflow() -> None:
    scenario_files = [
        "commands/test-scenario-report.md",
        "workflows/test-scenario-report.md",
        "templates/test-scenario-report.md",
        "claude/commands/test-scenario-report.md",
    ]
    required_terms = [
        "QA/product evidence",
        "screenshot",
        "test matrix",
        "expected",
        "actual",
        "console",
        "severity",
        "recommendations",
        "visible-menu navigation",
        "technical verification only",
        "Employee Daily Log v5",
        "performance",
    ]
    for rel in scenario_files:
        assert_contains_all(rel, required_terms)

    assert_contains_all(
        "templates/test-scenario-report.md",
        [
            "PASS / FAIL",
            "BLOCKED",
            "NOT_RUN",
            "MEDIA:/absolute/path/to",
            "Console errors",
            "Network/API failures",
            "Non-performance confirmation",
        ],
    )

    assert_contains_all(
        "README.md",
        [
            "commands/test-scenario-report.md",
            "workflows/test-scenario-report.md",
            "templates/test-scenario-report.md",
            "claude/commands/test-report.md",
            "visible-menu navigation",
            "technical verification only",
        ],
    )


def validate_scenario_templates() -> None:
    if SANDBOX.exists():
        shutil.rmtree(SANDBOX)
    SANDBOX.mkdir(parents=True)

    for name, bda_files in SCENARIOS.items():
        for rel in bda_files:
            if not (ROOT / rel).exists():
                raise AssertionError(f"scenario {name} references missing file: {rel}")

        report = f"""# Smoke scenario: {name}

## BDA Standard files used
- STANDARD.md
""" + "\n".join(f"- {rel}" for rel in bda_files) + f"""

## Pipeline trace
- Understand: read scenario context and {bda_files[0]}
- Plan: choose applicable workflow/template
- Execute: no production write; generated smoke report only
- Verify: checked required sections exist
- Handoff: report created in sandbox

## Commands run
- python3 scripts/smoke-standard-scenarios.py (current validation)

## Verification / Evidence
- Required sections present for {name}
- Referenced BDA files exist

## Limitations / Risks / Next steps
- Smoke validation only; it does not run real project tests
"""
        out = SANDBOX / f"{name}.md"
        out.write_text(report, encoding="utf-8")
        generated = out.read_text(encoding="utf-8")
        missing = [section for section in REQUIRED_SECTIONS if section not in generated]
        if missing:
            raise AssertionError(f"generated scenario {name} missing: {missing}")


def validate_no_forbidden_claims() -> None:
    paths = list(ROOT.glob("**/*.md"))
    ignored_parts = {".git"}
    for path in paths:
        if ignored_parts & set(path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_CLAIMS:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if match:
                raise AssertionError(f"potential unsupported pass claim in {path.relative_to(ROOT)}: {match.group(0)!r}")


def main() -> int:
    checks = [
        validate_version_consistency,
        validate_required_sections,
        validate_claude_usage_docs,
        validate_staff_command_pack,
        validate_optional_staff_adapters,
        validate_obsidian_init_workflow,
        validate_standard_feedback_loop,
        validate_test_scenario_report_workflow,
        validate_scenario_templates,
        validate_no_forbidden_claims,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS scenarios: {', '.join(SCENARIOS)}")
    print(f"Sandbox reports: {SANDBOX}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        raise SystemExit(1)
