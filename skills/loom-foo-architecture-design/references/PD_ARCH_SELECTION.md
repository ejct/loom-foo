# Arch Selection — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 8. Generate coherent candidates

A candidate is a coherent architectural thesis, not a technology bundle. Where external discovery is material, each candidate follows the **reconciled** solution space, not automatically the first internal favorite or the first retrieved pattern.

Each serious candidate should make clear:
- thesis;
- load-bearing decisions;
- boundaries/ownership;
- state/source-of-truth model;
- critical flows;
- key interfaces/dependencies;
- why it fits drivers;
- costs/trade-offs;
- sensitivity points;
- assumptions;
- likely validation needs.

Prefer the simplest sufficient candidate.

Do not introduce a named reusable architectural concept unless it owns a distinct semantic responsibility or lifecycle/authority boundary that cannot fit an existing owner.
## 9. Construction gate

Before deeper comparison/review, ensure a competent reviewer can reconstruct, where applicable:

1. system objective;
2. relevant constraints/drivers;
3. critical invariants;
4. workload assumptions;
5. responsibilities/boundaries;
6. quantitative/time/state semantics are unambiguous where material, including units, clocks, reference frames and cyclic domains;
7. state owners/sources of truth;
8. critical flows;
9. interfaces/dependencies;
10. key decisions/rationale;
11. important failure behavior;
12. assumptions/unknowns;
13. validation needs.

Fix obvious construction defects before review.
## 10. Candidate funnel

Use:

`Design Space -> Candidate Generation -> Construction Gate -> Cheap Screening -> Selection Gate -> Deep Review`

Screen out candidates that violate hard constraints, are internally incoherent, are obviously dominated, differ only cosmetically, add complexity without a driver, or depend on contradicted assumptions.

### Small-system / bounded-probe fast path

If hard constraints and current evidence leave one simple credible architecture, do not force multiple candidates or ceremony. Move directly from the construction gate to a bounded adversarial review and, when the remaining question is empirical, to the smallest useful probe.

A probe architecture should implement only what is required to test the load-bearing claim. Do not generalize test fixtures/controllers into future platform abstractions unless the probe actually creates that pressure.

### Deferred decisions and stage gates

Do not force an architecture decision before its driver or evidence exists.

A material decision may remain explicitly `DEFERRED` with:
- why it is not required now;
- what future condition or evidence should reopen it;
- what current architecture boundary preserves the option without implementing it prematurely.

A staged architecture may deliberately choose a simple Phase 0 while reserving later decisions such as native integration, distributed execution, graph representation, model providers, or generalized pack/plugin systems.
## 11. Compare finalists on the same basis

Use the same material drivers, scenarios, assumptions, and workload envelope.

Avoid a universal numeric architecture score.

Prefer conclusions like:
- A dominates B under current constraints;
- A trades operability for throughput;
- B becomes preferable above threshold X;
- the winner depends on unresolved evidence.
## 12. Selection gate

### Dominant candidate
Recommend it and continue refinement.

### Value-dependent choice
Explain decisive trade-offs and recommend. If the user chooses differently, preserve the choice unless reopened.

### Evidence-dependent choice
Return `VALIDATION_REQUIRED` with the smallest discriminating experiment.

Track candidate and revision separately, e.g. `A@0`, `B@0`, `A@1`.

Use `SELECTED_FOR_REFINEMENT` for the workflow choice. Do not use `SELECTED` or similar wording to imply project acceptance unless an external project authority has actually accepted it.
