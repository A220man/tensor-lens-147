"""Tests for PowerShell 5.1 UTF-8 encoding compatibility.

These tests verify that .ps1 scripts contain no em-dashes (—) that would
cause parsing errors on Windows PowerShell 5.1 when the file is encoded as
UTF-8 without a BOM.
"""
import pytest


def test_hunt_ps1_no_em_dashes():
    """hunt.ps1 must not contain em-dash characters."""
    with open("scripts/hunt.ps1", "r", encoding="utf-8") as f:
        content = f.read()
    # Em-dash is U+2014; ensure it's not present
    assert "—" not in content, "hunt.ps1 contains em-dash — which breaks PowerShell 5.1"
    # Also check the raw bytes don't have the UTF-8 sequence for em-dash (E2 80 94)
    with open("scripts/hunt.ps1", "rb") as f:
        raw = f.read()
    assert b"\xe2\x80\x94" not in raw, "hunt.ps1 contains UTF-8 em-dash byte sequence"


def test_install_ps1_no_em_dashes():
    """install.ps1 must not contain em-dash characters."""
    with open("scripts/install.ps1", "r", encoding="utf-8") as f:
        content = f.read()
    assert "—" not in content, "install.ps1 contains em-dash — which breaks PowerShell 5.1"
    with open("scripts/install.ps1", "rb") as f:
        raw = f.read()
    assert b"\xe2\x80\x94" not in raw, "install.ps1 contains UTF-8 em-dash byte sequence"


def test_scripts_use_ascii_dashes():
    """Scripts should use ASCII dash (-) not em-dash (—)."""
    for path in ["scripts/hunt.ps1", "scripts/install.ps1"]:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # Each script should contain at least one ASCII dash
        assert "-" in content, f"{path} contains no dash characters at all"
        # Verify no em-dash present
        assert "—" not in content, f"{path} contains em-dash"
