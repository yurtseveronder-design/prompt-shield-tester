# Prompt Shield Tester

A lightweight security testing tool designed to catch prompt injection and jailbreak attempts before they reach your AI models.

## What It Solves
Standard text filters use brittle, static keyword lists that break easily when attacks change slightly. This tool models an organic immune system to test how well your defense layers handle evolving, mutated threats.

## Core Features
* **Bio-Immune Shield (`src/immune_shield.py`):** Scans inputs against known threat antibodies and neutralizes malicious patterns.
* **Mutation Engine:** Automatically generates semantic variations (viral variants) of injection payloads to test your shield's resilience.
* **Automated CI/CD:** Runs tests on every push via GitHub Actions to ensure security rules never regress.

## Project Structure
* `src/`: Core shield logic and bio-immune mutation engine.
* `payloads/`: Sample attack payloads for security testing.
* `tests/`: Automated test suite for continuous validation.
* `.github/workflows/`: CI pipeline configuration.

## Quick Start
1. Clone the repository and install dependencies.
2. Run the test suite locally:
   ```bash
   python -m pytest -v
