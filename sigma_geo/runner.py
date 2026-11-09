"""Reference evaluation runner; no external model is called."""
import json
from pathlib import Path
from .grader import grade

def load_cases(path: Path | None = None) -> list[dict]:
    source = path or Path(__file__).with_name("cases.json")
    payload = json.loads(source.read_text(encoding="utf-8"))
    if payload.get("data_status") != "synthetic_demonstration_only":
        raise ValueError("Dataset must declare synthetic demonstration status.")
    return payload["cases"]

def reference_response(case: dict) -> dict:
    return {"label": case["expected_label"], "abstain": case["expected_abstain"], "rationale": case["rationale"]}

def run() -> dict:
    results = []
    for case in load_cases():
        response = reference_response(case)
        results.append({"case_id": case["id"], "dimension": case["dimension"],
                        "grade": grade(case["expected_label"], case["expected_abstain"], response)})
    total = len(results)
    passed = sum(item["grade"]["passed"] for item in results)
    return {"benchmark": "SIGMA-GEO", "run_type": "REFERENCE_PIPELINE_CHECK_NOT_MODEL_RESULT",
            "total_cases": total, "passed": passed, "failed": total-passed, "results": results}
