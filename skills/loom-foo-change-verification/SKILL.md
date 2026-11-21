---
name: loom-foo-change-verification
description: "Verify an exact candidate against authoritative acceptance criteria with property-level evidence. Not open-ended defect review or release approval."
compatibility: Agent Skills-compatible clients. Repository/project sources, tests, build/runtime tools, browser/device checks, connected evidence, clean checkouts, and separate evaluators are optional. The skill remains proportional and runtime-neutral.
metadata:
  family: "engineering"
  project: "loom-foo"
  version: "0.8.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Change Verification

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Establish what specified properties hold for one exact candidate and what remains unproven.

Primary artifact: **Verification Report**.

Core boundary:

`exact candidate + controlling criteria -> property-specific evidence/checks -> Verification Report`

A verification PASS is bounded to the declared verification surface. It is not exhaustive defect discovery and is not owner acceptance.

## L1 — ordinary execution and L2 selection

Freeze candidate and criteria; map each property to a check at the required fidelity; run only authorized relevant checks; return PASS, FAIL, INCONCLUSIVE or NOT_COVERED for each material property. A passing test or report is never automatic acceptance, release permission or exhaustive correctness.

**Conditional method index (read the selected file before its detailed method is needed):**

- **A nontrivial check requires choosing methods, environment fidelity, specialist evidence composition or a fast-path example** → `references/PD_VERIFICATION_METHODS.md` (source H2 sections 7,8,9,15,19).
- **Verifier/golden integrity, candidate-editable acceptance tests, claimed read-only agent permissions, regression across interfaces, negative probes, builder claims or independent-verifier status materially affect a verdict** → `references/PD_VERIFICATION_INTEGRITY.md` (source H2 sections 11–17,21–23). If oracle mutation or host-enforced permissions are in question, also read `references/VERIFIER_INTEGRITY.md`.

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

## 1. Routing gate

Use this skill when:
- a concrete candidate/change subject exists;
- explicit controlling acceptance criteria/contract properties exist or can be resolved from authority;
- the requested primary output is criterion-level verification/conformance for that candidate.

Typical triggers:
- verify this exact candidate against the acceptance criteria;
- independently re-run/check this remediation;
- establish whether these required properties hold;
- produce a bounded PASS/FAIL/INCONCLUSIVE verification report.

Do not use as primary owner when:
- the user asks what defects/risks the change introduces -> `loom-foo-change-review`;
- architecture is the primary verification/review object -> `loom-foo-architecture-review` when its modes fit;
- the verification method itself needs research design -> `loom-foo-research-design`;
- evidence itself is the primary review object -> `loom-foo-evidence-review`;
- no authoritative criteria exist and creating them would be a product/design decision;
- the user asks for merge/release/acceptance authority.

## 2. Authority boundary

Verification authorizes inspection/execution needed for the requested bounded verification only within current action authority.

It does not by itself authorize:
- candidate mutation/remediation;
- changes to acceptance criteria;
- verifier/golden updates unless separately authorized;
- merge/push/release/deploy;
- owner acceptance/promotion.

Capability is not authority.

## 3. Freeze exact subject and contract

Resolve when material:
- exact candidate identity;
- base/parent identity;
- controlling specification/contract/version;
- acceptance criteria / protected predicates;
- relevant environment/fidelity requirements;
- verifier/test/oracle baseline where verdict integrity depends on it;
- evaluator mutation authority.

Do not issue a candidate-level verdict for a moving or ambiguous subject.

## 4. Criteria authority

Criteria must come from current controlling sources such as:
- Specification;
- accepted architecture invariant/constraint;
- Task Brief acceptance criteria;
- review finding resolution criterion;
- remediation contract;
- release/promotion gate;
- explicitly applicable external standard.

Do not invent, strengthen, weaken, or reinterpret material acceptance criteria merely to close verification.

If material criteria are missing/contradictory, use `NEED_CRITERIA` / `NEED_CONTEXT` / `BLOCKED` as appropriate.

## 5. Build the smallest criterion map

For every material declared property record enough to answer:
- what exactly must hold?
- what subject/scope does it apply to?
- what evidence/check can establish or falsify it?
- what environment/fidelity matters?
- what result relation is allowed?

Do not create a large verification matrix when two lines suffice.

For detailed guidance read `references/CRITERIA_AND_COVERAGE.md`.

## 9. Criterion-level result semantics

Use the narrowest defensible relation for each material property:

- `PASS` — sufficient evidence establishes the property for the exact subject/scope at required fidelity.
- `FAIL` — sufficient evidence establishes non-conformance.
- `INCONCLUSIVE` — evidence/check cannot resolve the property to the required confidence/fidelity.
- `NOT_COVERED` — the property is outside the executed verification surface or required check was not run.

Do not convert NOT_COVERED or INCONCLUSIVE into PASS.

A test command returning zero is not automatically criterion PASS unless it actually covers the property.

## 10. Verification coverage is claim-bounded

Map evidence to properties explicitly enough to know what is covered.

Distinguish:
- declared criterion covered by direct check;
- indirectly supported property;
- partial/fidelity-limited coverage;
- property not covered.

Passing all executed checks does not license claims about undeclared/uncovered properties.

## 17. No remediation during read-only verification

If the evaluator is read-only, do not fix the candidate to make it pass.

Report the failing property and sufficient evidence.

If remediation is authorized in the same broader workflow, bind any later verification verdict to the corrected exact candidate, not the original subject.

## 19. Dispositions

Use one primary disposition.

### `VERIFIED_WITHIN_SCOPE`
All material declared criteria on the requested verification surface are PASS with sufficient evidence for the exact candidate.

### `NON_CONFORMING`
At least one material declared criterion is FAIL.

### `INCONCLUSIVE`
At least one material criterion required for closure cannot be resolved to required confidence/fidelity, and no stronger overall result is defensible.

### `PARTIALLY_VERIFIED`
Useful criterion-level results exist, but a material part of the declared verification surface is NOT_COVERED or otherwise incomplete.

### `NEED_CRITERIA`
Controlling acceptance/property criteria are missing or contradictory in a way that prevents defensible verification.

### `NEED_CONTEXT`
A resolvable subject/base/environment/authority input is missing.

### `BLOCKED`
A material capability/authority/access conflict prevents credible verification.

`VERIFIED_WITHIN_SCOPE` is technical/evidentiary. It does not mean accepted, merged, releasable, or defect-free.

## 20. Output contract

Return the Verification Report as primary artifact.

For consequential verification include:
- candidate/base/contract identity;
- verification surface;
- property -> check/evidence -> result mapping;
- verifier/oracle integrity notes when material;
- regression surface;
- environment/fidelity;
- unsupported/not-covered properties;
- disposition;
- exact claim limits.

For the detailed artifact contract read `references/VERIFICATION_REPORT_CONTRACT.md`.
