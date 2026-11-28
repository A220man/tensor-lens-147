# /prioritize

Operational entry point for the `high-severity-focus` methodology skill.

Use this command when a human tester wants to rank authorized testing surfaces
or triage candidate findings by demonstrated security impact. It does not act
against any target; it only structures the human's own analysis.

## Usage

```
/prioritize [surface-or-finding]
```

If no argument is given, ask the tester which authorized surface or candidate
finding to rank. Never assume scope.

## Procedure

1. Confirm the surface or finding is inside confirmed program / engagement
   scope. If scope is unconfirmed, stop and ask.
2. Load the `high-severity-focus` skill and apply its prioritization order:
   authn/authz, sensitive IDOR, impactful SSRF, RCE/injection, meaningful
   business-logic, exploitable stored XSS.
3. For each candidate, record the demonstrated impact and the evidence that
   supports it. Weak-alone findings are deprioritized unless a concrete chain
   to higher impact is stated.
4. Apply the evidence bars: High/Critical claims need concrete evidence;
   access-control issues prefer a two-account demonstration.
5. Output a ranked list with, per item: category, demonstrated impact, evidence
   on hand, and the next concrete step the human should take.

## Guardrails

- Methodology only. No scanning, fuzzing, exploitation, or target payloads.
- Stay within confirmed scope; keep the human in control.
- Do not print or store secrets, tokens, or engagement identifiers. Use
  clearly synthetic fixtures for any examples.
