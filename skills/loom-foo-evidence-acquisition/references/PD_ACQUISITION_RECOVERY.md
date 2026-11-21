# evidence-acquisition — detailed conditional method (PD_ACQUISITION_RECOVERY.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 8. Retry, recover, and substitute without redesigning the method

Recover from ordinary operational failure when doing so preserves the plan.

Normally safe when authorized and semantically equivalent:

- retry after transient failure;
- alternate transport/tool for the same source/property;
- resolve a stale locator to the same exact subject;
- move execution to another runtime that preserves required environment semantics;
- change serialization/storage while preserving evidence meaning/provenance;
- perform lossless or plan-approved normalization.

Do not silently continue when a change would materially alter:

- subject/population/case set;
- inclusion/exclusion or source-selection logic;
- comparator/control;
- intervention/treatment;
- metric/oracle/measured property;
- direct-vs-proxy evidence strength;
- confirmatory stop/adaptation rule;
- privacy/spend/external-action authority.

Return `PLAN_REVISION_REQUIRED` when credible continuation requires such a change.

Read `references/ADAPTATION_AND_FAILURES.md` for detailed boundaries.
## 14. Natural/specialist executor boundary

This skill is not a universal research operations department.

If the plan requires work outside the current runtime's credible/authorized capability—such as physical measurement, participant recruitment, regulated procedures, specialist lab/statistical work, or inaccessible private systems:

- execute independent in-scope parts when useful;
- identify the exact missing natural/specialist executor;
- preserve evidence returned from that executor with provenance;
- do not simulate the unavailable procedure;
- return `PARTIAL_EVIDENCE_PACKAGE` or `BLOCKED` as appropriate.
