# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

ps1-encoding-fix

## Roadmap

### ps1-encoding-fix — Fix PowerShell 5.1 UTF-8 encoding compatibility

Status: done

Acceptance:
- hunt.ps1 contains no em-dashes (—), only ASCII dash (-)
- install.ps1 contains no em-dashes (—), only ASCII dash (-)
- Scripts are valid UTF-8 without BOM issues on PowerShell 5.1

Implementation: `scripts/hunt.ps1`, `scripts/install.ps1`

Tests: `tests/test_ps1_encoding.py`

