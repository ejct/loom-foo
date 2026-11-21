---
name: loom-foo-change-review
description: "Review a specific code, UI, or integration change for defects, side effects and scope drift. Not criterion-level verification or architecture redesign."
compatibility: Agent Skills-compatible clients. Repository/project sources, diffs, tests, runtime probes, screenshots, logs, and separate reviewer contexts are optional. Stronger specialist review skills retain precedence.
metadata:
  family: "engineering"
  project: "loom-foo"
  version: "0.7.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Change Review

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Review a bounded change as a change: inspect what changed, what it can affect, and what material defects or unintended consequences remain.

Primary artifact: **Change Review**.

Core boundary:

`bounded change candidate -> adversarial changed-surface review -> Change Review`

A review may find defects that were never enumerated in acceptance criteria. It does not prove complete conformance.

## L1 — ordinary execution and L2 selection

Bind the exact candidate and base, inspect the actual delta, select the smallest risk-relevant review surface, identify evidence-supported defects and material non-risks, and return a bounded Change Review. A review is not criterion-level PASS, remediation, independent audit or merge approval.

**Conditional method index (read the selected file before its detailed method is needed):**

- **The diff has material user-facing, product-scope, integration or specialist-review risks requiring focused lenses or escalation** → `references/PD_CHANGE_LENSES.md` (source H2 sections 6,7,12,13).
- **There are consequential findings, targeted probes, independent-review claims, detailed report or candidate regression questions** → `references/PD_CHANGE_FINDINGS.md` (source H2 sections 9,10,11,14,17,18,19).

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

## 1. Routing gate

Use this skill when the primary review object is a concrete bounded implementation/change candidate and the requested output is critical findings about the change.

Typical triggers:
- review this PR/change/candidate critically;
- find regressions or unintended consequences;
- inspect this implementation for defects before acceptance;
- review what changed and what could break.

Do not use as primary owner when:
- architecture properties are the review object -> `loom-foo-architecture-review`;
- evidence itself is the review object -> `loom-foo-evidence-review`;
- the user asks whether exact acceptance criteria are satisfied -> `loom-foo-change-verification`;
- the user wants remediation implementation -> `loom-foo-agent-task-design` / `loom-foo-work-decomposition` / relevant design owner;
- a stronger specialist security/legal/scientific/domain review owns the requested surface.

A mixed review+verification request may compose both skills; do not collapse their conclusions into one PASS.

## 2. Authority boundary

A review request authorizes evaluation and production of review findings. It does not by itself authorize:
- changing the candidate;
- accepting/rejecting the change as a project decision;
- merging, pushing, deploying, publishing or releasing;
- changing canonical requirements/architecture;
- applying remediation.

Technical access is not mutation authority.

## 3. Freeze the review subject

Resolve when material:
- exact candidate/change identity;
- base/parent identity;
- current controlling requirements/specification/decisions;
- intended change outcome;
- scope and explicit exclusions;
- known protected invariants;
- reviewer mutation authority, normally read-only.

Do not review a moving candidate as if findings refer to one stable subject.

If the candidate changes materially, bind subsequent review claims to the new identity.

## 4. Reconstruct the actual delta

Use the smallest reliable representation of what changed:
- diff/commit/PR;
- changed config/schema/data;
- UI/runtime behavior;
- artifact version delta;
- relevant tests/results.

Do not trust the builder summary as a substitute for the actual delta when direct inspection is available.

Treat builder explanations and test reports as claims/evidence, not inherited truth.

## 7. Evidence semantics

Distinguish where material:
- authoritative requirement/decision;
- observed candidate fact;
- builder/self-report;
- test/tool result;
- reviewer inference;
- assumption;
- unknown.

Severity is consequence. Confidence is evidence strength. Do not collapse them.

A passing test suite is evidence, not proof that no other defect exists.

## 14. Proportional fast path

For a small low-risk change, a sufficient review can be:
- exact subject/base;
- changed surfaces;
- findings/non-risks;
- one-line limits/disposition.

Do not manufacture matrices, many headings, or exhaustive lenses.

## 15. Dispositions

Use one primary disposition.

### `REVIEW_COMPLETE`
The bounded review surface has been examined proportionately and no open material finding remains.

### `REVIEW_WITH_FINDINGS`
The review is complete enough for the requested scope and one or more material findings remain open.

### `UPSTREAM_REVIEW_REQUIRED`
A stronger specialist/domain owner is required for a material review surface before the generic review can close credibly.

### `NEED_CONTEXT`
A resolvable candidate/base/scope/authority input is missing.

### `BLOCKED`
A material subject/authority/access contradiction prevents credible review.

Review completion is not merge/release/owner acceptance.
