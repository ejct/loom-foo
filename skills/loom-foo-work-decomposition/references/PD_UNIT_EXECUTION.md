# work-decomposition — detailed conditional method (PD_UNIT_EXECUTION.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 12. Keep planning separate from orchestration

This skill creates a semantic plan artifact. It does not:
- dispatch agents;
- create branches/worktrees;
- monitor progress continuously;
- retry jobs;
- assign people/models;
- manage sprints/boards;
- mutate GitHub/Linear/Jira by default.

Runtime/project-management systems may later project the plan into their native task structures under separate authority.

### Execution episode versus Work Unit

Work Units are semantic planning/acceptance boundaries, not automatic new user interaction boundaries. Multiple ready units with compatible authority, the same executor and a common user milestone may execute continuously in a single delegated episode while retaining distinct acceptance gates. Do not manufacture extra owner prompts, return cycles or Work Units for routine diagnosis, repair and retry inside a delegated outcome. Preserve true acceptance, safety, authority, independent-review and frozen-experiment boundaries.
## 13. Build the Work Plan

Use the smallest form that remains useful.

When material, include:
- controlling accepted sources;
- target scope/non-goals;
- Work Unit Set;
- dependencies/gates;
- parallelizable units;
- integration/reconciliation points;
- plan completion condition;
- unresolved upstream blockers.

For 2–3 simple units, a compact ordered list may be enough. Do not force IDs, milestones, DAG diagrams, or tables unless useful.

For consequential plans, read `references/WORK_PLAN_CONTRACT.md`.
