"""Tests for the /prioritize command doc.

Verifies the command exists, delegates to the high-severity-focus skill,
encodes the methodology-only guardrails, and carries no secrets.
"""
import os

CMD_PATH = os.path.join("commands", "prioritize.md")


def _read():
    with open(CMD_PATH, "r", encoding="utf-8") as f:
        return f.read()


def test_command_file_exists():
    assert os.path.isfile(CMD_PATH), f"missing {CMD_PATH}"


def test_command_references_skill():
    lower = _read().lower()
    assert "high-severity-focus" in lower


def test_command_is_methodology_only():
    lower = _read().lower()
    assert "methodology only" in lower
    assert "human in control" in lower


def test_command_requires_scope_confirmation():
    lower = _read().lower()
    assert "scope" in lower


def test_command_has_no_secrets():
    lower = _read().lower()
    for needle in ["token=", "api_key", "apikey", "secret=", "password="]:
        assert needle not in lower, f"command appears to contain a secret: {needle}"
