# Research Handoff — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 15. End at the execution boundary

`loom-foo-research-design` ends when the evidence-acquisition contract is sufficient for the natural executor.

Possible next owners:
- direct inspection/search;
- a human study owner;
- `loom-foo-agent-task-design` for a bounded probe/benchmark task;
- Inspect / OpenAI Evals / Braintrust / custom harness;
- a specialist statistical/causal/DOE workflow;
- a device/browser/environment probe.

If the user explicitly asks for both design and execution, execution may follow only when it is within current authority and capability. Keep the pre-evidence plan distinct from post-result interpretation.
## 16. Output states

Use exactly one primary skill-local disposition:

### `EVIDENCE_PLAN_READY`
A bounded credible plan is ready for execution.

### `NO_NEW_EVIDENCE_NEEDED`
Current evidence or decision state does not justify additional evidence acquisition.

### `NEED_CONTEXT`
A specific missing decision, subject, constraint, or source prevents a defensible plan.

### `NEED_SPECIALIST_METHOD`
The question is sufficiently clear, but correct design requires domain methodology the general skill should not improvise.

### `NO_CREDIBLE_METHOD`
Under current constraints no credible observation can discriminate the live alternatives.

### `PLANNING_REQUIRED`
The request contains multiple materially independent evidence questions that should be decomposed first.

These are skill-local workflow states, not LoomLoom Kernel states and not project acceptance decisions.
## 17. Composition boundaries

- `loom-foo-proposal-refinement` may hand off a `VALIDATION_REQUIRED` uncertainty to `loom-foo-research-design`.
- architecture workflows may hand off unresolved empirical assumptions or failure questions.
- `loom-foo-cross-context-transfer` may supply external lessons or precedent; `loom-foo-research-design` still owns target-local evidence acquisition.
- `loom-foo-research-design` may hand an accepted Evidence Plan to `loom-foo-agent-task-design` for executable task compilation.
- evidence collected later should be interpreted by an evidence-review owner when available, not retroactively by changing the original plan.

Do not create recursive ownership or silently absorb adjacent skills.
## Final checks

Before returning `EVIDENCE_PLAN_READY`, verify that:
- the decision that could change is explicit;
- the uncertainty is narrower than the whole project problem;
- a plausible result can distinguish the live alternatives;
- a cheaper credible method was considered;
- the method fits the intended claim;
- measurement/oracle limitations are visible;
- rigor is proportional to consequence and uncertainty;
- positive results cannot silently license broader claims;
- stop/adaptation rules are sufficient where optional stopping matters;
- the plan ends at a clear execution boundary;
- no project authority or external-action permission was invented.
