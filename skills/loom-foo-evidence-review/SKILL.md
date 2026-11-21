---
name: loom-foo-evidence-review
description: "Assess an existing evidence package against claims, contradictions and uncertainty. Not acquisition or decision authority."
compatibility: Agent Skills-compatible clients. Evidence Packages, source artifacts, specialist review frameworks, and connected sources are optional. The skill must remain usable with a bounded evidence body supplied inline.
metadata:
  family: "research"
  project: "loom-foo"
  version: "0.5.1"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Evidence Review

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Assess what an existing body of evidence can defensibly establish, within what scope, and with what limitations. The primary artifact is an **Evidence Assessment**.

The core boundary is:

`Evidence Package -> Evidence Assessment`

Do not turn evidence review into new evidence acquisition or into the final project/action decision.

## L1 — ordinary execution and L2 selection

Map exact claims to attributable evidence point by point, preserve counterevidence, express SUPPORT/CONTRADICTION/INCONCLUSIVE only at justified scope, and issue a bounded Evidence Assessment. Do not silently collect new evidence, change criteria or make the owner decision.

**Conditional method index (read the selected file before its detailed method is needed):**

- **Material package-integrity, absence/equivalence, independent-source, specialist or contradiction issues arise** → `references/PD_EVIDENCE_REVIEW_LENSES.md` (source H2 sections 6,8,10,11,12,13).
- **The assessment is handed to a downstream decision owner and decision/acceptance boundaries must remain explicit** → `references/PD_EVIDENCE_REVIEW_HANDOFF.md` (source H2 sections 18).

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

## 1. Routing gate

Use this skill when:
- an Evidence Package or equivalently bounded evidence body already exists;
- the primary review object is the evidence itself;
- the desired output is a reusable assessment of what that evidence supports, contradicts, fails to establish, or cannot discriminate.

Do **not** use this skill as the primary owner when:
- evidence still needs to be collected -> `loom-foo-evidence-acquisition`;
- the evidence method/design is unresolved -> `loom-foo-research-design`;
- architecture is the review object -> `loom-foo-architecture-review`;
- a code/change candidate is the review object -> change-review when available;
- a proposal is being iteratively refined -> `loom-foo-proposal-refinement`;
- the user asks what project/action decision to take -> decision-reconciliation/project authority;
- a specialist domain has a stronger validated evidence-assessment workflow that should remain primary.

Generic evidence review is optional composition. Do not invoke it merely because another review happens to cite evidence.

## 2. Authority and side-effect boundary

An evidence-review request authorizes analysis of the supplied/controlling evidence and creation of an Evidence Assessment.

It does not by itself authorize:
- collecting a new evidence universe;
- changing the Evidence Plan after outcomes are visible;
- accepting/rejecting a proposal or architecture;
- promoting a skill;
- modifying code/configuration/project state;
- committing, merging, publishing, deploying, releasing, or purchasing anything;
- overriding specialist review authority.

Evidence support is not project authority.

## 3. Resolve the review contract

Before assessing, establish the smallest current contract needed to interpret the evidence:
- exact Evidence Package/body and identity when material;
- controlling Evidence Plan/question/claim/outcome;
- intended scope/population/environment/timeframe;
- predeclared interpretation criteria or thresholds when they materially govern the conclusion;
- claim limits already established by the plan;
- relevant specialist framework, if one applies.

If a materially necessary threshold/criterion is a project/user decision and is missing, return `NEED_CONTEXT` rather than inventing it.

Not every review requires a numeric threshold. Descriptive/documentary evidence can support scoped qualitative relations.

For consequential reviews, read `references/EVIDENCE_ASSESSMENT_CONTRACT.md`.

## 4. Preserve evidence provenance and epistemic roles

Distinguish when material:
- direct/observed evidence;
- transformed/derived evidence;
- producer self-report;
- reviewer inference;
- authoritative decision/contract;
- assumption/unknown.

A structured or repeated self-report does not become independent evidence merely because it is formalized.

Do not count two artifacts as corroboration before checking lineage enough to know whether they are independently informative for the claim.

## 6. Pointwise before aggregate

For consequential multi-item evidence:
1. identify the material claim(s)/outcome(s);
2. map material evidence items to those claims;
3. assess relevance, validity, scope, uncertainty, and provenance/independence as needed;
4. preserve contradictions and missingness;
5. only then synthesize a body-level relation.

Do not let evidence quantity, citation count, or a polished summary substitute for evidentiary strength.

## 8. Establish claim-level evidence relation

Use the narrowest defensible relation. Helpful semantic vocabulary includes:

- **SUPPORTED_WITHIN_SCOPE** — evidence materially supports the claim within explicit scope and no unresolved material counterevidence invalidates that scoped support.
- **CONTRADICTED_WITHIN_SCOPE** — evidence materially conflicts with the claim within the tested scope.
- **MIXED** — relevant evidence supports and contradicts different parts/conditions, or comparable results conflict without a justified synthesis.
- **INSUFFICIENT** — the available evidence cannot support or contradict the claim to the required strength because of missingness, weak validity, indirectness, imprecision, incomplete acquisition, or another material limitation.
- **NON_DISCRIMINATING** — evidence was validly acquired but does not separate the decision-relevant alternatives enough to answer the question.

These are semantic relations, not required universal schema enums.

Critical distinctions:

`NOT_SUPPORTED != CONTRADICTED`

`NO_OBSERVED_EFFECT != EVIDENCE_OF_NO_EFFECT`

See `references/SUPPORT_AND_UNCERTAINTY.md`.

## 13. Express uncertainty without fake precision

When useful, state qualitative confidence in the **assessment**, with reasons.

Keep uncertainty sources distinguishable when material:
- acquisition incompleteness;
- measurement error/imprecision;
- sampling uncertainty;
- model/parser uncertainty;
- source bias;
- confounding;
- indirectness;
- scope/generalization;
- temporal drift;
- contradiction.

Use valid domain-specific quantitative uncertainty where available. Do not manufacture a universal numeric confidence score.

## 14. Produce the Evidence Assessment

Use the smallest form that remains decision-usable downstream.

When material, make these dimensions recoverable:
- reviewed package/body identity;
- controlling evidence question/claim/outcome;
- review scope;
- package completeness relevant to the question;
- claim -> evidence mapping;
- support relation(s);
- supporting evidence;
- counterevidence/tensions;
- material validity/quality limitations;
- provenance/independence limitations;
- uncertainty/precision limits;
- scope/generalization limits;
- unresolved alternatives;
- specific evidence gaps;
- assessment confidence/limits;
- stop reason/disposition.

Do not append a final project recommendation unless another owner explicitly requests/authorizes decision reconciliation.

## 15. Fast path

For a direct high-integrity one-source review, a compact Evidence Assessment may contain only:
- claim/question;
- evidence pointer;
- support relation;
- one material scope/uncertainty limit;
- disposition.

Do not manufacture matrices, scores, or multi-artifact ceremony.

## 16. Skill-local dispositions

Use exactly one primary disposition:

### `EVIDENCE_ASSESSMENT_READY`
The requested evidence question has been assessed to the strongest defensible conclusion under the current package and scope. The underlying claim relation may be SUPPORTED, CONTRADICTED, MIXED, INSUFFICIENT, or NON_DISCRIMINATING.

### `PARTIAL_EVIDENCE_ASSESSMENT`
Some requested claims/dimensions can be assessed, but a material package/reference/context limitation prevents full assessment of the requested review surface.

### `ACQUISITION_REPAIR_REQUIRED`
A material Evidence Package integrity/acquisition defect prevents credible assessment and requires repair/reacquisition by the appropriate owner.

### `NEED_CONTEXT`
A controlling claim, scope, interpretation criterion/threshold, or other non-acquisition review input is missing and materially blocks the requested assessment.

### `BLOCKED`
A required referenced artifact/source is inaccessible and no defensible bounded assessment can proceed.

Do not add a workflow disposition that automatically commands further evidence collection. Evidence gaps are assessment content; the choice to acquire more belongs downstream.

## 18. Final checks

Before returning, verify that:
- the evidence question is explicit enough to assess;
- provenance/independence is not overstated;
- unfavorable evidence and contradictions remain visible;
- null/zero evidence is not overinterpreted;
- support is scoped to the actual population/environment/time tested;
- quality limitations affect the support relation rather than being decorative caveats;
- no post-hoc evidence shopping occurred;
- specialist judgments were not improvised when specialist methodology was required;
- the final artifact does not choose the project decision;
- the amount of ceremony is proportional to the evidence body and stakes.
