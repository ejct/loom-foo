# change-review — detailed conditional method (PD_CHANGE_LENSES.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 5. Review the affected surface, not the whole universe

Identify:
- directly changed surfaces;
- dependencies/interfaces they can plausibly affect;
- protected invariants at risk;
- changed failure/recovery paths;
- migration/compatibility consequences;
- user/product behavior affected.

For consequential changes involving dispatchers, mode/variant routing, guarded state transitions, or one-use production budgets, follow the affected caller → actual branch → validator → side effect path. Check whether the correct specialist guard is reachable at the integration point, whether fallback takes a different guard, and whether a failure consumes an immutable attempt or triggers rollback. Isolated tests of adjacent host methods do not establish correct wiring; inspect or execute a proportionate isolated integration trace where feasible. Mark untested routes and mock-only evidence explicitly rather than converting green component tests into a system-level PASS. Avoid broad route archaeology unrelated to the change.

Broaden only where coupling or consequence justifies it.

Do not turn a small change into a whole-project audit by default.
## 6. Use proportional review lenses

Use only lenses material to the change. For consequential reviews read `references/REVIEW_LENSES.md`.

Potential lenses:
- functional/semantic correctness;
- regression/compatibility;
- state/data/concurrency;
- failure/recovery;
- security/privacy/trust boundary;
- performance/resource risk;
- operability/observability;
- maintainability/complexity;
- UX/product behavior/accessibility;
- scope/authority/provenance;
- migration/rollback.

When a changed workflow can invoke external tools, trace the consequential **call chain**, not just each tool separately: initial source authorization, derived data/provenance, destination audience, material payload and side effect, retry/fallback, and effective permission at the actual call. Look for (a) approval drift after an exact approval and (b) aggregate effects that cross a trust/data boundary despite individually permitted steps. Report a finding when an authorized call can be replaced with a materially different call, or privately sourced data can flow to a broader audience without separate disclosure authority. Do not claim a generic skill prompt or an isolated mock proves host-side enforcement; request targeted `change-verification` when closure depends on actual call routing.

When one lens requires specialist expertise, route that material surface to the stronger owner rather than pretending generic review is sufficient.


### Goal Fidelity at product-scope changes

When a change adds a **user-visible mode, feature or behavioral alternative**, compare its claimed value with the controlling **owner-authorized product capability**. Keep three judgments separate:

- **Technical correctness** — does this implementation work according to its own technical contract and tests?
- **Goal fulfillment** — does it actually deliver the authorized product behavior or business outcome? Source preservation, low latency, scans, click-through or green CI alone cannot establish a different semantic or commercial capability.
- **Product scope decision** — is this user-visible behavior within the accepted scope, or is there a traceable owner/product decision authorizing its addition or replacement?

For scope-sensitive changes, trace only the material Owner Intent -> Work Unit/Task Brief -> Execution -> Review -> Decision -> Integration links available for this candidate. Cite the actual authority and evidence for each judgment; missing task briefs or owner decisions remain **unknown**, not assumed consent. A builder or coordinator recommending a useful alternative does not itself authorize adding it as a product feature. An optional new mode can be technically valid, honestly labeled and still need a product-scope decision before acceptance.

Do not confuse method choice with product scope: **a deterministic algorithm is acceptable if it demonstrably fulfills the same authorized capability**. Exploratory prototypes and internal baselines may remain useful without new product authorization; the boundary is their promotion to a user-facing, accepted product feature or claim. Keep already authorized implementation/review work moving; do not demand a large benchmark or independent product approval for a genuinely equivalent method.

If technical checks pass but goal fulfillment is unproven or a new product feature lacks an authorized basis, report the bounded **GOAL_FIDELITY / PRODUCT_SCOPE** finding at the integration decision point. Mark technical verification separately from product acceptance. Recommend either evidence that establishes the authorized capability, explicit product-scope authorization, or retaining the alternative as an unpromoted internal experiment; **do not silently change the controlling goal or acceptance criteria**.
## 11. Targeted probes are allowed

Run/inspect targeted checks when they clarify a suspected defect or changed risk and are authorized.

Do not silently convert change review into a complete verification campaign.

If the primary need becomes criterion-by-criterion conformance closure, route/compose with `loom-foo-change-verification`.
## 12. Stronger owner precedence

Generic change-review is intentionally broad but shallow relative to specialist owners.

Route architecture-centric findings to `loom-foo-architecture-review` when architecture is the primary object.
Use specialist security/privacy/accessibility/scientific/legal review when the task requires expert methodology beyond this skill.

Do not duplicate a stronger owner's full review merely to produce a generic wrapper.
