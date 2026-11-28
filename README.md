# tensor-lens-147 — Ryan Vo

Current version: `1.2.0`.

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


A Claude Code skill bundle for bug hunting and external red-team work.

## Status
This is an initial checkpoint. Completed bounded features so far:

- **PowerShell 5.1 UTF-8 fix** — `scripts/hunt.ps1` and `scripts/install.ps1` use
  ASCII dashes so they parse under Windows PowerShell 5.1 (which decodes BOM-less
  UTF-8 using the system ANSI code page). Verified by `tests/test_ps1_encoding.py`.
- **high-severity-focus skill** — a methodology-only skill for ranking authorized
  testing surfaces and findings by demonstrated security impact. Verified by
  `tests/test_high_severity_focus.py`.
- **/prioritize command** — `commands/prioritize.md` operationalizes the skill:
  confirms scope, applies the prioritization order, applies evidence bars, and
  emits a ranked list. Methodology only. Verified by
  `tests/test_prioritize_command.py`.

## high-severity-focus skill
`skills/high-severity-focus/SKILL.md` prioritizes, in order: authentication /
authorization failures, sensitive IDOR, impactful SSRF, RCE/injection,
meaningful business-logic flaws, and exploitable stored XSS. It deprioritizes
weak-alone findings unless a concrete chain to higher impact is demonstrated,
requires concrete evidence for High/Critical claims, and prefers two-account
demonstrations for access-control issues. It is **methodology only**: no
autonomous scanning, no fuzzing, no target payloads, no engagement identifiers.
The human stays in control.

## Installation
```bash
# The repository is newly initialized; scripts are in the scripts/ directory
# PowerShell users should ensure scripts are saved with proper encoding
# or use the ASCII-dash version provided here.
```

## Development
- See `feature-plan.json` for the planned feature roadmap
- Tests are in `tests/`
- Run tests: `python3 -m pytest tests/ -q`
- Next feature: subagent-pipeline (planned)

Maintainer: Ryan Vo <ryandtvo@gmail.com>
