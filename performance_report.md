# RAG Performance & Cognitive Resonance Report
*Generated on: 2026-11-03 19:09:05 UTC*

## Executive Summary
* **Total Evaluation Queries:** 2
* **Passed Compliance:** 2/2
* **Average P95 Latency:** 275.0 ms
* **Average Cognitive Resonance:** 0.85 / 1.00

## Detailed Execution Log

| Query ID | Latency (ms) | Faithfulness | Relevancy | Resonance Score | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Q-101 | 240 | 0.95 | 0.9 | 0.88 | **PASS** |
| Q-102 | 310 | 0.89 | 0.85 | 0.82 | **PASS** |

## Architectural Notes
* **Resonance Integration:** Scored using lexical overlap and structural pacing metrics (`src/resonance.py`).
* **Pacing Protection:** Rate-limit controls successfully avoided throttling during bulk execution.
