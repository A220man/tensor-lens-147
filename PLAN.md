# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

prioritize-command

## Roadmap

### ps1-encoding-fix — Fix PowerShell 5.1 UTF-8 encoding compatibility

Status: done

Acceptance:
- hunt.ps1 contains no em-dashes (—), only ASCII dash (-)
- install.ps1 contains no em-dashes (—), only ASCII dash (-)
- Scripts are valid UTF-8 without BOM issues on PowerShell 5.1

Implementation: `scripts/hunt.ps1`, `scripts/install.ps1`

Tests: `tests/test_ps1_encoding.py`

### high-severity-prioritization-skill — High-severity prioritization methodology skill

Status: done

Acceptance:
- Skill file exists at skills/high-severity-focus/SKILL.md
- Methodology ranks surfaces by demonstrated impact (authn/authz, sensitive IDOR, impactful SSRF, RCE/injection, business-logic, exploitable stored XSS)
- Deprioritizes weak-alone findings unless a demonstrated chain exists
- Requires concrete evidence for High/Critical and two-account demos for access-control issues
- Stays methodology-only: no scanning, no target payloads, no engagement identifiers; human in control

Implementation: `skills/high-severity-focus/SKILL.md`

Tests: `tests/test_high_severity_focus.py`

### prioritize-command — /prioritize command for high-severity-focus skill

Status: done

Acceptance:
- Command doc exists at commands/prioritize.md
- Delegates to high-severity-focus skill and applies its prioritization order
- Methodology only: no scanning/payloads; human in control; scope confirmation required
- Contains no secrets or engagement identifiers

Implementation: `commands/prioritize.md`

Tests: `tests/test_prioritize_command.py`

