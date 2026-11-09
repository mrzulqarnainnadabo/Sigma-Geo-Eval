"""Deterministic grader for the SIGMA-GEO structured response contract."""
from typing import Any

def grade(expected_label: str, expected_abstain: bool, response: Any) -> dict[str, Any]:
    if not isinstance(response, dict):
        response = {}
    label = response.get("label")
    abstain = response.get("abstain")
    label_ok = isinstance(label, str) and label == expected_label
    abstain_ok = isinstance(abstain, bool) and abstain is expected_abstain
    rationale_ok = isinstance(response.get("rationale"), str) and bool(response["rationale"].strip())
    return {"label_correct": label_ok, "abstention_correct": abstain_ok,
            "rationale_present": rationale_ok, "passed": label_ok and abstain_ok and rationale_ok,
            "false_abstention": abstain is True and expected_abstain is False,
            "missed_abstention": abstain is False and expected_abstain is True}
