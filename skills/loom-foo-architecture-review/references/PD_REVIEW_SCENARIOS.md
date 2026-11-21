# architecture-review — detailed conditional method (PD_REVIEW_SCENARIOS.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 5. Challenge framing

Declared drivers, invariants, workloads, and scenarios are claims to inspect.

Ask:
- Is the stated driver material?
- Is a critical driver missing?
- Is workload plausible?
- Is a failure scenario omitted?
- Is architecture optimizing a non-driving concern?
- Are accepted constraints silently reopened?

A system can implement its declared design perfectly and still be based on wrong framing.
## 6. Make quality claims scenario-shaped

When useful:

`source -> stimulus -> environment -> artifact -> response -> response measure`

Prefer concrete/falsifiable scenarios over labels like "scalable" or "resilient".
## 7. Select adaptive lenses

Do not run every lens deeply.

Core lens families:
1. correctness/invariants, including semantic domains/units/reference frames/timebases when material;
2. boundaries/ownership;
3. state/consistency/concurrency, including accidentally collapsed orthogonal state dimensions;
4. dependencies/coupling;
5. failure/recovery;
6. performance/capacity;
7. security/trust;
8. operability/observability;
9. evolvability/accidental complexity.

Conditional examples:
- multiple writers -> consistency/concurrency;
- external dependencies -> dependency/failure;
- untrusted input/privileges -> security;
- explicit scale/latency -> performance;
- production readiness -> operability;
- new service/layer/framework -> complexity/identity.
## 8. Scenario x decision analysis

For each critical scenario trace:

`scenario -> involved decisions -> expected behavior -> evidence -> failure/cost path -> finding or non-risk`

Evaluate interactions, not isolated components.
## 9. Failure walk

For critical flows, apply relevant cases:
- unavailable dependency;
- slow dependency;
- stale data;
- duplicate input/result;
- partial success;
- out-of-order behavior;
- retry;
- cancellation;
- crash between steps;
- restart/recovery;
- concurrent mutation;
- network partition where relevant.

Ask whether invariants survive, recovery is possible, and duplicate/contradictory effects are prevented.
## 10. Specialist lenses

Read `references/LENSES.md` for consequential reviews or material specialist areas.

Use smells as probes, not automatic verdicts. A cycle, shared model, large component, etc. is only a finding when consequence is demonstrated.
