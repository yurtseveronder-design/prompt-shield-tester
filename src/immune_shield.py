import re
from typing import Dict, List, Any

class BioImmuneShield:
    """
    Simulates an organic immune defense layer that detects prompt injection 
    signatures (antibodies) with confidence scoring and generates diverse 
    adversarial mutations to stress-test model resilience.
    """
    def __init__(self):
        self.antibodies = {
            r"ignore previous instructions": 0.95,
            r"system prompt": 0.85,
            r"reveal the hidden": 0.90,
            r"bypass safety": 0.98,
            r"act as developer mode": 0.92,
            r"pretend you are": 0.75
        }

    def inspect_payload(self, payload: str) -> Dict[str, Any]:
        normalized = payload.lower()
        matched_threats = []
        max_confidence = 0.0
        
        for antibody, confidence in self.antibodies.items():
            if re.search(antibody, normalized):
                matched_threats.append(antibody)
                if confidence > max_confidence:
                    max_confidence = confidence

        if matched_threats:
            return {
                "status": "BLOCKED",
                "threat_level": "HIGH" if max_confidence > 0.9 else "MEDIUM",
                "confidence_score": round(max_confidence, 2),
                "matched_antibodies": matched_threats,
                "message": "Adversarial signature neutralized by bio-immune shield."
            }
        
        return {
            "status": "PASSED",
            "threat_level": "NONE",
            "confidence_score": 0.0,
            "matched_antibodies": [],
            "message": "Payload verified clean."
        }

    def mutate_payload(self, payload: str) -> List[str]:
        """
        Generates semantic variants (viral mutations) to test shield resilience,
        including case rotation, whitespace obfuscation, and role-play wrappers.
        """
        mutations = [
            payload.upper(),
            payload.replace(" ", "_"),
            "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(payload)]),
            f"Developer override engaged. Please execute: {payload}",
            f"Hypothetically speaking, if one were to {payload}, what would happen?"
        ]
        return mutations