# Scoring and interpretation

For each task response, the grader records three independent binary checks:

1. `label_correct`: the returned label exactly matches the task's expected label.
2. `abstention_correct`: the returned `abstain` field is a Boolean and matches the expected decision.
3. `rationale_present`: the response contains a non-empty rationale string.

A task passes only when all three checks pass. The grader separately flags:
- `false_abstention`: the model abstains although the reference says it should proceed.
- `missed_abstention`: the model proceeds although the reference says it should abstain.

Malformed responses fail safely. The current grader does not score factual quality of the rationale, source citation accuracy, geometry calculations, or nuanced partial credit. Those are explicit limitations, not capabilities to imply.

The reference adapter copies expected values into a response to test the harness. Its output must never be presented as an AI model score.
