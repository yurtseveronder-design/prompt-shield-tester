import re

class PromptShield:
    def __init__(self):
        # Common adversarial patterns and injection keywords
        self.forbidden_patterns = [
            r"ignore previous instructions",
            r"bypass safety",
            r"system prompt",
            r"reveal secret",
            r"you are now in developer mode"
        ]

    def scan(self, user_input: str) -> bool:
        """
        Scans input string for prompt injection patterns.
        Returns True if safe, False if an injection threat is detected.
        """
        lower_input = user_input.lower()
        for pattern in self.forbidden_patterns:
            if re.search(pattern, lower_input):
                return False  # Threat detected
        return True  # Input is clean