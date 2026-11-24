"""Tests for the high-severity-focus methodology skill.

Verifies the skill exists, encodes the prioritization methodology, and
stays within its stated guardrails (methodology only: no scanning, no
target payloads, no engagement identifiers).
"""
import os

SKILL_PATH = os.path.join("skills", "high-severity-focus", "SKILL.md")


def _read_skill():
    with open(SKILL_PATH, "r", encoding="utf-8") as f:
        return f.read()


def test_skill_file_exists():
    assert os.path.isfile(SKILL_PATH), f"missing {SKILL_PATH}"


def test_skill_declares_methodology_only():
    content = _read_skill()
    lower = content.lower()
    assert "methodology only" in lower
    assert "human in control" in lower


def test_skill_prioritization_categories_present():
    content = _read_skill()
    lower = content.lower()
    # Each top-priority category from the proposal must be represented.
    for term in [
        "authentication",
        "authorization",
        "idor",
        "ssrf",
        "rce",
        "injection",
        "business-logic",
        "stored xss",
    ]:
        assert term in lower, f"missing prioritization category: {term}"


def test_skill_requires_concrete_evidence_for_high_critical():
    lower = _read_skill().lower()
    assert "concrete evidence" in lower
    assert "high" in lower and "critical" in lower


def test_skill_prefers_two_account_for_access_control():
    lower = _read_skill().lower()
    assert "two-account" in lower or "two account" in lower


def test_skill_deprioritizes_weak_alone_findings():
    lower = _read_skill().lower()
    assert "weak alone" in lower or "weak-alone" in lower


def test_skill_stays_within_scope_and_human_control():
    lower = _read_skill().lower()
    assert "scope" in lower
    assert "human" in lower


def test_skill_has_no_engagement_identifiers_or_secrets():
    """Guardrail: skill must not embed engagement identifiers or secrets."""
    content = _read_skill()
    lower = content.lower()
    # No obvious secret-like tokens or engagement IDs.
    for needle in ["token=", "api_key", "apikey", "secret=", "password="]:
        assert needle not in lower, f"skill appears to contain a secret: {needle}"
