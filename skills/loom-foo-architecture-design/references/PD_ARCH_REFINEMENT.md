# Arch Refinement — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 13. Deep review

Use a focused self-review by default for consequential design. Prefer a genuinely separate `loom-foo-architecture-review` evaluator only when the runtime supports it and the additional independence would materially change the decision or address a real high-risk blind spot. Do not create a separate reviewer or repeated passes as a standard requirement.

Otherwise perform a fresh adversarial architecture self-review across relevant lenses:
- framing/drivers/scenarios;
- correctness/invariants;
- boundaries/ownership;
- state/consistency/concurrency;
- dependencies/coupling;
- failure/recovery;
- performance/capacity;
- security/trust;
- operability/observability;
- evolvability/complexity.

Call same-context review **fresh adversarial self-review**, not independent review.
## 14. Adjudicate before redesign

Review findings are hypotheses, not implementation commands.

For each material finding:
1. decide validity;
2. identify the violated invariant/driver/scenario;
3. reopen the smallest affected decision;
4. prefer the smallest coherent correction;
5. check new assumptions/dependencies/complexity;
6. replay affected scenarios;
7. regression-check whole architecture when propagation is possible.

Do not reflexively invent a coordinator/service/layer to resolve an ownership or consistency finding.
## 15. Local vs architecture-level refinement

Use local decision refinement when one bounded decision is wrong.

Reopen the whole design space only when candidate thesis, framing, or driver model is materially invalid.
## 16. Refinement loop

Revise the selected architecture when new evidence or a valid material defect changes a load-bearing decision; check affected invariants and regressions. Preserve exact reviewed versions and stable finding identities only when there is an actual separate review. Do not require an `A@0 -> R0 -> A@1` paper trail or extra audit iterations for ordinary design work. Stop when further critique cannot improve the next practical decision.
## 17. Empirical boundary

When a material question depends on facts reasoning cannot establish—throughput, latency, contention, sensor separability, model quality, provider behavior, etc.—do not invent theoretical certainty. Identify the smallest credible observation, and continue unaffected authorized implementation or a reversible probe when safe. Only a genuine load-bearing risk or external constraint should block the route.

Return:
- hypothesis;
- smallest useful probe;
- measurement;
- pass/fail or discriminating boundary;
- architectural consequence.

Use `VALIDATION_REQUIRED` as a bounded epistemic description of the unresolved architectural claim, **not** an automatic new project phase or stop to otherwise authorized safe work.
