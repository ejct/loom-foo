# work-decomposition — detailed conditional method (PD_UNIT_STRUCTURE.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 7. Represent dependencies thinly

Dependencies explain why work is blocked or sequenced, not just preferred order.

Helpful semantic concepts include:
- requires artifact;
- requires decision;
- requires evidence;
- requires acceptance;
- integrates after;
- can run in parallel.

These are guidance, not mandatory universal enum/schema.

Use a short ordered list when a graph adds no value.

Read `references/DEPENDENCIES_AND_GATES.md` for larger plans.
## 8. Distinguish gates from tasks

A gate is not automatically executable work.

Examples:
- owner acceptance;
- evidence result;
- architecture decision;
- credential/permission availability;
- integration compatibility result.

Represent the gate explicitly. Do not fabricate a Work Unit just to make the plan look complete.
## 9. Expose integration/reconciliation points

Independently executable units are not automatically independently integrable or shippable.

Identify where outputs must be integrated/reconciled.

Create a dedicated integration Work Unit only when actual executable integration work exists. If the boundary is only review/acceptance/decision, represent a gate instead.
## 11. Allow bounded probe units only when justified

A discovery/probe Work Unit is allowed only when:
- the probe need is already accepted/authorized or directly required by the controlling plan;
- it has one explicit outcome;
- its result has a real downstream gate effect.

Do not use “research” as a placeholder for unclear planning. If method design is primary, route to `loom-foo-research-design`.
