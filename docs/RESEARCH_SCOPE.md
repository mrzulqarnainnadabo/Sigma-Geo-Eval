# Research scope and claim discipline

## Research question
Can an AI system detect defects in geographical evidence before producing a spatial conclusion, and can it distinguish genuinely insufficient evidence from a valid task where it should proceed?

## Controlled-pair design
Each initial dimension has one defect case and one matched clean control. The pair structure is intended to expose two opposite failure modes:
- **Overclaiming:** producing a conclusion when a material evidence defect should block it.
- **Over-refusal:** abstaining even when the evidence is adequate for the stated task.

The current 12-case suite is a small prototype. It is not a statistically powered benchmark.

## Dimensions
1. Temporal validity: stale versus in-period evidence.
2. CRS integrity: missing CRS metadata versus declared compatible CRS.
3. Missing evidence: absent location fields versus sufficient location fields.
4. Contradictory sources: unresolved disagreement versus agreement.
5. Spatial scale compatibility: district evidence used for a neighbourhood claim versus a district-level task.
6. Metamorphic consistency: valid reprojection should preserve spatial relationships.

## Proposed experimental protocol
1. Expand each pair into multiple independently authored scenarios.
2. Keep task wording and unrelated evidence constant while changing one controlled property.
3. Require structured model output with a label, abstention decision, and rationale.
4. Use the same task set and grader across models.
5. Run 3–5 independent trials per task and model, with clean trial state.
6. Save prompts, raw outputs, model/version, settings, date, runtime, and approximate cost.
7. Review failures to distinguish model errors from ambiguous tasks or grader defects.
8. Report uncertainty and failure cases, not only aggregate scores.

## Limitations
The repository currently provides six synthetic demonstration pairs and a reference pipeline. It has no real geospatial datasets, no GIS execution engine, no independent expert annotation, and no live model measurements. The reference adapter returns expected answers by design and is not a model under test.

## Future validation
Use domain-expert review to verify every prompt, expected answer, and grading rule. Test inter-annotator agreement, grader false-pass/false-fail rates, paraphrase robustness, and reproducibility before comparative model claims.
