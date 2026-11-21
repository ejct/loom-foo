# Arch Discovery — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 7. Open only load-bearing design space

Identify architectural decisions that are genuinely open and consequential, e.g.:

- canonical vs derived state;
- ownership boundary;
- sync vs async coordination;
- local vs remote processing;
- eager vs lazy materialization;
- consistency model;
- persistence boundary;
- single-process vs distributed execution;
- orchestration vs choreography.

Do not enumerate the Cartesian product of all choices.

If constraints already determine one simple credible architecture, do not manufacture alternatives.

When a consequential choice is genuinely open, first derive a **provisional internal solution-space sketch** from the system outcome, semantic distinctions, accepted constraints, material drivers and current architecture: the simplest credible baseline and any materially different mechanism families. Keep it brief and revisable, not a mandatory document or claim of independence from the agent's prior exposure. Do not treat an example implementation as the definition of the problem. `loom-foo-problem-understanding` owns only framing ambiguity that actually blocks architecture work.

Then consider relevant existing products, libraries, platforms, architecture patterns, and mechanisms from adjacent domains before specifying a custom component or boundary. External factual checks about safety, standards, APIs, known constraints and current behavior can happen immediately; only example-led solution discovery follows the provisional sketch when meaningful. Start with the system outcome and forces rather than a predetermined technology category; broaden search terminology or sources when new approaches could change the choice.

Prefer reuse, adaptation, or composition where they satisfy the drivers. Evaluate the actual integration constraints and costs rather than assuming that an available component is a fit. Be clear about source/solution classes not inspected; never infer market or ecosystem exhaustiveness from a narrow search. Stop discovery once it is sufficient for the next architectural choice, or try a cheap reversible implementation when that is more informative. Do not turn this check into mandatory external research, comparative benchmarking, or a gate before routine implementation.

**Reconcile, then converge:** compare newly discovered mechanism classes and failures with the initial alternatives on the same drivers/scenarios. Retain, revise, combine or drop candidates, and reopen the framing/drivers if external evidence materially invalidates them. Record only decision-relevant changes; avoid both initial-idea fixation and uncritical copying of outside examples. If outside evidence does not change a material choice, say so briefly and continue; use `NO_ARCHITECTURE_DELTA` only when the actual existing architecture needs no change. A user request specifically for prior-art landscape work may route directly to `loom-foo-cross-context-transfer`; do not force this architecture sequence on that request.

For architecture involving reusable agent instructions or knowledge delivery, conditionally compare scoped standing instructions, selective skills, canonical retrieval, scripts, authorized APIs/connectors and no additional surface. Consider invocation reliability, freshness/versioning, runtime availability, context cost, security and permissions; this is architecture-local selection, not a new `knowledge-delivery` skill or global router.
