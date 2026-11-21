# evidence-acquisition — detailed conditional method (PD_ACQUISITION_OUTPUT.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 17. Composition boundaries

- `loom-foo-research-design` produces the controlling Evidence Plan.
- `loom-foo-agent-task-design` may project one bounded acquisition step/task into an executor runtime; it is optional rather than mandatory.
- domain-specific acquisition workflows may own their local procedure and emit or map into an Evidence Package.
- `loom-foo-evidence-review` should assess the resulting package without requiring chat/tool-history reconstruction.
- `loom-foo-decision-reconciliation` may later apply the Evidence Assessment to the decision surface.
- bootstrap/runtime bindings resolve material execution access; they do not change evidence semantics.

Avoid recursive ownership.
## 18. Candidate validation requirements

Before promotion, validate at least:

- compact direct-source fast path;
- exact source/version/time provenance;
- `COMPLETE_ZERO` vs acquisition failure;
- partial acquisition with inaccessible source;
- retry that preserves the method;
- mechanically equivalent substitution;
- method-changing substitution -> `PLAN_REVISION_REQUIRED`;
- stale subject/changed source universe;
- transformed extraction with raw-source provenance;
- runtime trace available vs unavailable;
- multi-item plan with one failed item;
- external/human method outside runtime capability;
- private/paid action without authority;
- ordinary factual Q&A negative routing;
- method-design request -> `loom-foo-research-design`;
- evidence-interpretation request -> `loom-foo-evidence-review`;
- attempted unsupported inference from raw evidence;
- domain-specific acquisition workflow composition;
- comparison against no-skill/default execution;
- fresh holdout after candidate freeze.

Behavioral validation may remain deferred by portfolio policy. Static/package construction is not promotion evidence.
## Final checks

Before returning, verify that:

- a controlling acquisition contract exists and is current enough to execute;
- subject/scope are resolved;
- capability and authority are distinct;
- acquisition follows the plan rather than silently improving it;
- valid zero, partial, unavailable, failed, and not-run states are not conflated;
- material deviations/substitutions are visible;
- transformed evidence remains traceable to raw/recoverable input;
- no unsupported interpretation was introduced;
- package readiness is not presented as evidentiary sufficiency;
- the artifact is proportional to the acquisition;
- downstream review can understand what happened without hidden conversation reasoning.
