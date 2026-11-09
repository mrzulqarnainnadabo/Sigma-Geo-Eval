# Hackathon submission notes

## Short description

SIGMA-GEO is a reproducible benchmark prototype for testing whether AI systems detect defects in geographical evidence before producing spatial conclusions. Its 12 synthetic cases form six matched defect/control pairs across temporal validity, coordinate reference system integrity, missing evidence, contradictory sources, spatial scale compatibility, and metamorphic consistency. A deterministic grader checks classification, abstention calibration, and rationale presence. The prototype's reference run validates the evaluation pipeline only; no live model performance results are claimed.

## Five-minute walkthrough outline

- **0:00–0:40 — Problem:** Explain why a confident spatial answer can still be unsafe when its evidence is stale, incomplete, conflicting, or used at the wrong scale.
- **0:40–1:30 — Research question and dimensions:** Introduce the six evidence-integrity dimensions and matched clean controls.
- **1:30–2:40 — Task examples:** Show one defect case and its clean control. Explain why a model must sometimes abstain and sometimes proceed.
- **2:40–3:40 — Grader:** Show the label, abstention, rationale, false-abstention, and missed-abstention checks.
- **3:40–4:30 — Reproducibility:** Show the repository, unit tests, and GitHub Actions workflow.
- **4:30–5:00 — Limitations:** State clearly that all cases are synthetic, the reference adapter is not an AI model, and live model testing/expert validation are next steps.

Do not claim live model results or show reference-pipeline pass rates as model performance.

## Submission checklist

- [ ] Check the HackerRank Instructions tab for any additional required format or fields.
- [ ] Download the code-only ZIP artifact from the GitHub Actions run.
- [ ] Confirm the ZIP contains source, tests, docs, and README only; no API keys, .env files, virtual environments, or videos.
- [ ] Record a walkthrough of no more than five minutes and make the link accessible without sign-in.
- [ ] Paste the short description above into the submission form.
- [ ] Accept the required Participant Agreement.
