import json
import pytest
from pathlib import Path
from src.shield import PromptShield

# Locate and load the external JSON payloads file relative to this test file
PAYLOAD_PATH = Path(__file__).parent.parent / "payloads" / "injections.json"

with open(PAYLOAD_PATH, "r", encoding="utf-8") as f:
    payloads = json.load(f)

@pytest.fixture
def shield():
    return PromptShield()

@pytest.mark.parametrize("malicious_input", payloads["malicious"])
def test_prompt_shield_blocks_injections(shield, malicious_input):
    """Test that the shield successfully identifies and blocks malicious prompt patterns from JSON."""
    is_safe = shield.scan(malicious_input)
    assert is_safe is False, f"Failed to block malicious input: {malicious_input}"

@pytest.mark.parametrize("benign_input", payloads["benign"])
def test_prompt_shield_allows_safe_inputs(shield, benign_input):
    """Test that standard user prompts from JSON pass through the shield cleanly."""
    is_safe = shield.scan(benign_input)
    assert is_safe is True, f"Incorrectly flagged safe input as threat: {benign_input}"