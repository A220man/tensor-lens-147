# tensor-lens-147

Current version: `1.0.0`.

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


A Claude Code skill bundle for bug hunting and external red-team work.

## Status
This is an initial checkpoint. The first bounded implementation addresses PowerShell 5.1 UTF-8 encoding compatibility.

## PowerShell 5.1 UTF-8 Fix
**Problem:** Scripts `scripts/hunt.ps1` and `scripts/install.ps1` were using em-dashes (—),
which on Windows PowerShell 5.1 decode incorrectly when the file is UTF-8 without BOM,
causing parsing errors like: `Token ')' inesperado na expressão ou instrução`.

**Fix:** Replaced all em-dashes (—) with ASCII dashes (-) in the .ps1 source files.
This ensures the scripts parse correctly on PowerShell 5.1 regardless of the system
ANSI code page setting.

**Affected files:**
- `scripts/hunt.ps1` - em-dashes replaced with ASCII dashes
- `scripts/install.ps1` - em-dashes replaced with ASCII dashes

## Installation
```bash
# The repository is newly initialized; scripts are in the scripts/ directory
# PowerShell users should ensure scripts are saved with proper encoding
# or use the ASCII-dash version provided here.
```

## Development
- See `feature-plan.json` for the planned feature roadmap
- Tests are in `tests/test_ps1_encoding.py`
- Next features: high-severity-prioritization-skill, subagent-pipeline

Maintainer: Ryan Vo <ryandtvo@gmail.com>
