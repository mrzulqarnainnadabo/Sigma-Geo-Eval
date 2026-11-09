# Research scope and claim discipline

SIGMA-GEO studies whether a model notices defects in supplied geographical evidence before making a spatial claim. It is narrower than general geospatial question answering.

## Proposed controlled protocol
1. Define a clean scenario and evidence manifest.
2. Create a matched perturbed scenario with one known defect.
3. Keep wording and unrelated evidence constant.
4. Require a structured response: label, abstention decision, rationale, and evidence identifiers.
5. Grade label accuracy, abstention calibration, unsupported claims, and evidence traceability separately.
6. Repeat across models and prompt conditions; publish model/version, date, parameters, raw outputs, and grader version.
7. Report uncertainty and failure cases, not only aggregate scores.

## Key distinctions
- Publication does not establish that a source is current or correct.
- A coordinate pair without a CRS is not safely interpretable as a location.
- A regional aggregate does not establish a local condition.
- Conflicting sources require reconciliation.
- A valid coordinate transformation should preserve represented spatial relationships within an appropriate tolerance.

## Limitations
This early prototype contains six synthetic demonstration cases and a reference pipeline. It is not a statistically powered benchmark, has no real geospatial datasets, no GIS execution engine, no independent expert annotation, and no live model measurements. The reference adapter returns expected answers by design and is not a model under test.

## Future validation
Expand each dimension with multiple clean/perturbed pairs, edge cases, realistic metadata, geographic diversity, and expert-reviewed labels. Evaluate inter-annotator agreement, grader validity, paraphrase robustness, and reproducibility before comparative model claims.
