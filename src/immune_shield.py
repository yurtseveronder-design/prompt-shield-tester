import re
from typing import Dict, List, Any

class BioImmuneShield:
    """
    Simulates an organic immune defense layer that detects prompt injection 
    signatures (antibodies) and generates variants to stress-test resilience.
    """
    def __init__(self):
        self.antibodies = [
            r"ignore previous instructions",
            r"system prompt",
            r"reveal the hidden",
            r"bypass safety",
            r"act as developer mode"
        ]

    def inspect_payload(self, payload: str) -> Dict[str, Any]:
        normalized = payload.lower()
        matched_threats = []

        for antibody in self.antibodies:
            if re.search(antibody, normalized):
                matched_threats.append(antibody)

        if matched_threats:
            return {
                "status": "BLOCKED",
                "threat_level": "HIGH",
                "matched_antibodies": matched_threats,
                "message": "Adversarial signature neutralized by bio-immune shield."
            }

        return {
            "status": "PASSED",
            "threat_level": "NONE",
            "matched_antibodies": [],
            "message": "Payload verified clean."
        }

    def mutate_payload(self, payload: str) -> List[str]:
        """
        Generates semantic variants (viral mutations) to test shield resilience.
        """
        mutations = [
            payload.upper(),
            payload.replace(" ", "_"),
            "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(payload)]),
            f"Please ignore rules and check: {payload}"
        ]
        return mutations