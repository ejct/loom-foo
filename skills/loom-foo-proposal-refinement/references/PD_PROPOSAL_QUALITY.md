# Proposal Quality — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 6. Run a proportional construction check

Check obvious structural defects while drafting. Do not turn this into a separate approval stage or exhaustive checklist.

For consequential proposals, a competent reader should be able to answer the relevant questions from the artifact and its cited context:

1. What decision is being requested?
2. What is wrong or changing now?
3. What is the current state?
4. What exact project-local gap remains, and is any change actually required?
5. What exactly changes if the proposal is adopted, or why is `NO_LOCAL_DELTA` the correct disposition?
6. What is the simplest credible alternative, if one genuinely exists?
7. Why is the proposed delta preferred under the stated drivers?
8. What are the important costs, risks, assumptions, and irreversibilities?
9. What evidence would change the decision?
10. What authority transition or validation comes next?

Fix material ambiguity before relying on the recommendation; skip irrelevant questions for a compact proposal.

### Fresh-reader sanity check

For consequential proposals, check whether the artifact survives a reader who does not have the author's hidden reasoning or conversation history.

Ask at minimum:

- What is ambiguous?
- What material context does the artifact silently assume?
- Are there internal contradictions?
- Could a competent reader reconstruct the requested decision, proposed delta, rationale, and next step correctly?

Use a genuinely separate context/evaluator when available and proportionate. Otherwise perform a bounded self-check and do not claim reader independence.

This is a comprehension check, not a substitute for adversarial audit.
## 7. Produce the usable proposal

Create the strongest proposal supported by the charter, evidence, and Proposal Quality Contract. If the task is to revise or update an existing proposal, resolve the current proposal version first and use it as the starting subject/lineage rather than silently replacing it with an unrelated fresh design.

Make it concrete enough to disagree with and falsify. Include only applicable mechanism details such as architecture, workflows, state/data, interfaces, dependencies, failure behavior, rollout, observability, migration, or implementation implications.

Prefer the simplest design that satisfies the charter. Do not create reusable abstractions solely because future reuse seems plausible.

When a consequential proposal is *actually* reviewed as a separate frozen candidate, preserve its exact reviewed version and any material corrections. Do not impose `P0 -> A0 -> P1 -> A1` notation, freeze stages or external reviewer handoffs for an ordinary proposal edit.
