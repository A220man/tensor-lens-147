# Changelog

## 1.2.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.1.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

### Added

- `commands/prioritize.md` — `/prioritize` command that operationalizes the
  `high-severity-focus` skill (scope confirmation, prioritization order,
  evidence bars, ranked output; methodology only).
- `tests/test_prioritize_command.py` — verifies command structure, skill
  delegation, guardrails, and absence of secrets.

## 1.0.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

### Added

- `skills/high-severity-focus/SKILL.md` — methodology-only skill for ranking
  authorized testing surfaces and findings by demonstrated security impact
  (authn/authz, sensitive IDOR, impactful SSRF, RCE/injection, meaningful
  business-logic, exploitable stored XSS), with evidence bars and scope
  guardrails.
- `tests/test_high_severity_focus.py` — verifies skill structure, prioritization
  categories, evidence requirements, and guardrails (no secrets/engagement IDs).

### Retained

- `scripts/hunt.ps1`, `scripts/install.ps1` — ASCII-dash PowerShell 5.1
  encoding fix (`tests/test_ps1_encoding.py`).
