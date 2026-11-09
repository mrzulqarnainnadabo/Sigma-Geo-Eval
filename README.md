# SIGMA-GEO

**Geospatial Evidence Integrity under Controlled Perturbation**  
A benchmark programme under **SIGMA-Eval — Spatial Intelligence & Grounded Model Assessment**.

## Research question
How reliably can AI systems detect defects in geographical evidence before producing spatial conclusions?

This early-stage benchmark prototype tests whether a system can identify evidence problems, explain their consequence, and abstain when supplied evidence cannot support a conclusion.

## Initial benchmark dimensions
1. **Temporal validity** — evidence is outside the required time window.
2. **CRS integrity** — coordinate reference systems are missing, incompatible, or incorrectly handled.
3. **Missing evidence** — required fields or sources are absent.
4. **Contradictory sources** — supplied sources materially disagree.
5. **Spatial scale compatibility** — evidence is used at a finer or different geographic scale than it supports.
6. **Metamorphic consistency** — a valid transformation should not change the underlying spatial conclusion.

Unsupported claims and appropriate abstention are cross-cutting evaluation concerns.

## Current status
The repository contains a deterministic reference benchmark scaffold and six synthetic demonstration cases. **Reference-run scores are software-pipeline checks, not AI model performance.** No live model results are claimed.

## Quick start
Requires Python 3.10 or newer.

```bash
python run_eval.py --adapter reference
python -m unittest discover -s tests -v
```

The reference adapter returns expected answers by design. It tests the grader and runner only; it is not an external AI model.

## Research integrity and limitations
- All initial examples are synthetic; they are not Nigerian or other real-world statistics.
- No real-world prevalence, risk, or geographic performance claims are made.
- A benchmark score is conditional on the test set, task wording, grader, and model configuration.
- Deterministic checks cannot fully assess nuanced geographic reasoning.
- CRS and geometry operations are represented as evidence-integrity scenarios; this starter version is not a complete GIS engine.
- Live model adapters, independent validation, broader literature review, and expert review remain future work.

## Repository layout
- `sigma_geo/cases.json` — synthetic cases and expected labels.
- `sigma_geo/runner.py` — deterministic evaluation runner.
- `sigma_geo/grader.py` — structured-output grading.
- `run_eval.py` — command-line entry point.
- `tests/` — standard-library tests.
- `docs/RESEARCH_SCOPE.md` — proposed controlled protocol and limitations.

## Citation
Describe this as an early-stage SIGMA-GEO benchmark scaffold. Do not cite reference-run outcomes as model results.
