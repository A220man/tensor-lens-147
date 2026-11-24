# high-severity-focus

A methodology skill for ranking authorized testing surfaces and findings by
demonstrated security impact rather than by ease of testing or report volume.

This skill is **methodology only**. It contains no autonomous scanning, no
fuzzing, no target-specific payloads, and no engagement identifiers. It guides a
human operator (with their tooling of choice) to focus effort where impact is
highest and evidence is strongest.

## When to use

- A human tester is choosing which authorized surfaces to test first.
- A tester is triaging candidate findings to decide which deserve High or
  Critical severity.
- A tester wants to avoid inflating severity or chasing low-impact noise.

Out of scope: automated exploitation, scanning, or any action against a target
the tester is not explicitly authorized to test.

## Prioritization order

Rank authorized testing surfaces and findings by **demonstrated impact**, in
this order:

1. **Authentication / authorization failures** - bypass of auth, privilege
   escalation, missing access control that exposes another tenant's data or
   function.
2. **Sensitive IDOR** - insecure direct object references that expose sensitive
   data (PII, credentials, financial, health) or enable state change across
   authorization boundaries.
3. **Impactful SSRF** - server-side request forgery that reaches an internal
   service, cloud metadata endpoint, or otherwise crosses a trust boundary.
4. **RCE / injection** - remote code execution, command injection, SQL/NoSQL
   injection, template injection, or deserialization flaws that yield code
   execution.
5. **Meaningful business-logic flaws** - logic errors with real financial or
   data-integrity impact (e.g., price manipulation, workflow bypass, race that
   mints value).
6. **Exploitable stored XSS** - stored cross-site scripting that executes in a
   privileged context and can take meaningful action.

## Deprioritize weak-alone findings

Deprioritize findings that are weak on their own (e.g., a single reflected
parameter with no demonstrated impact, a missing header with no exploitable
chain) **unless** a concrete chain to higher impact is demonstrated. State the
chain explicitly; do not assert one without evidence.

## Evidence bars

- **High / Critical claims require concrete evidence.** Reproducible steps,
  request/response captures, or recorded output that demonstrates the impact.
  No severity label is final without a demonstration.
- **Access-control issues prefer two-account demonstrations.** Show the action
  succeeding from account A against account B's resource, to prove the boundary
  is actually crossed rather than merely suspected.

## Guardrails

- Stay strictly within confirmed program / engagement scope.
- Keep the human in control; this skill advises, it does not act.
- Do not collect or store engagement identifiers, tokens, or secrets in skill
  output. Use clearly synthetic fixtures for any examples.
