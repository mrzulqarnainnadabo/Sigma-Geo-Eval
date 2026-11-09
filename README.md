# SIGMA-GEO
**Geospatial Evidence Integrity under Controlled Perturbation**  
The first benchmark programme under **SIGMA-Eval — Spatial Intelligence & Grounded Model Assessment**.

## What it tests
How reliably can AI systems detect defects in geographical evidence before producing spatial conclusions?

A wrong spatial conclusion can misdirect public-service planning, infrastructure investment, environmental decisions, and emergency response. SIGMA-GEO focuses on an upstream failure: the model may produce a confident answer without noticing that the evidence is stale, incomplete, inconsistent, incorrectly referenced, or too coarse for the requested conclusion.

## Task design
The initial synthetic suite contains 12 cases: six evidence-defect scenarios and six matched clean controls.

| Dimension | Defect case | Matched control |
|---|---|---|
| Temporal validity | TEMP-001 | TEMP-CLEAN-001 |
| CRS integrity | CRS-001 | CRS-CLEAN-001 |
| Missing evidence | MISS-001 | MISS-CLEAN-001 |
| Contradictory sources | CONTRA-001 | CONTRA-CLEAN-001 |
| Spatial scale compatibility | SCALE-001 | SCALE-CLEAN-001 |
| Metamorphic consistency | META-001 | META-CLEAN-001 |

The defect cases test whether a model notices a material limitation. The clean controls help detect indiscriminate refusal: a model should not abstain when the evidence is adequate for the stated task.

## Grading
The deterministic grader checks three dimensions independently:
- **Label correctness** — did the response identify the expected evidence condition?
- **Abstention calibration** — did it abstain when evidence was insufficient, and proceed when it was sufficient?
- **Rationale presence** — did it provide a non-empty explanation?

It also reports false abstentions and missed abstentions separately. The reference adapter returns the known expected answer to verify the pipeline; it is not an AI model and its pass rate is not model performance.

## Run locally
Requires Python 3.10 or newer. The benchmark uses only the Python standard library.

```bash
python run_eval.py --adapter reference
python -m unittest discover -s tests -v
```

A successful reference run confirms only that the local cases, runner, and grader are connected. To evaluate an external model, an adapter and repeated trials must be added; no live model results are currently included.

## Current results and limitations
- 12 synthetic cases across six dimensions; one defect case and one matched control per dimension.
- Automated unit tests and reference pipeline are run in GitHub Actions.
- **No frontier model has been evaluated in this repository.** No model pass rate, comparative ranking, or model-failure claim is made.
- The initial suite is a prototype, not a statistically powered or independently validated benchmark.
- Cases are synthetic and are not Nigerian or other real-world statistics.
- CRS and geometry operations are represented as evidence-integrity scenarios; this is not a full GIS engine.
- One case per side of each dimension is not enough to establish general model capability. Expansion, expert annotation, and validation are required.

## Reproducibility and provenance
- Runtime: Python 3.10+; standard library only.
- Data: authored synthetic demonstration cases; no confidential client data or external geographic dataset is included.
- Run type: deterministic reference-pipeline check.
- See [research scope](docs/RESEARCH_SCOPE.md) for the proposed controlled protocol and limitations.

## AI-tool disclosure
AI assistance was used to draft and implement parts of this prototype. The repository explicitly distinguishes generated reference outputs from real model trials. The author remains responsible for reviewing every task, expected answer, and grading rule before treating this as a validated research benchmark.

## Project structure
- `sigma_geo/cases.json` — synthetic tasks and expected labels.
- `sigma_geo/grader.py` — deterministic structured-output grader.
- `sigma_geo/runner.py` — reference pipeline.
- `run_eval.py` — command-line entry point.
- `tests/` — standard-library tests.
- `docs/` — research protocol and scoring notes.

## Citation
Refer to this work as an early-stage SIGMA-GEO benchmark prototype. Do not report reference-pipeline outcomes as AI model performance.
