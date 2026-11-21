---
name: loom-foo-decision-reconciliation
description: "Reconcile an already bounded decision with hard constraints, evidence and alternatives. Not proposing or designing an open solution space."
compatibility: Agent Skills-compatible clients. Can consume Evidence Assessments, review findings, proposal artifacts, accepted policies/constraints, and owner preferences supplied inline or through connected project sources.
metadata:
  family: "planning"
  project: "loom-foo"
  version: "0.5.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Decision Reconciliation

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Reconcile existing decision-relevant inputs into a bounded **Decision Surface**. Support the decision authority; do not become the decision authority.

Core boundary:

`Evidence Assessment(s) + decision context -> Decision Surface`

## L1 — ordinary execution and L2 selection

Resolve an already-bounded choice, apply hard constraints before preferences, keep evidence and preferences distinct, and describe the actual decision surface and remaining uncertainty without fabricating weights or a winner. This output cannot accept a decision for its owner.

**Conditional method index (read the selected file before its detailed method is needed):**

- **An existing Evidence Assessment materially affects a decision and needs claim-bounded consumption** → `references/PD_DECISION_EVIDENCE.md` (source H2 sections 9).
- **Sensitive uncertainty, reversibility, switch conditions or consequential final claims need explicit analysis** → `references/PD_DECISION_UNCERTAINTY.md` (source H2 sections 10,11,15).

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

## 1. Routing gate

Use this skill when:
- alternatives/dispositions are already bounded enough to compare;
- relevant evidence/review artifacts already exist or their absence is explicit;
- the primary output is a reusable decision-ready synthesis;
- no stronger domain-specific owner cleanly owns the full choice.

Do **not** use as the primary owner when:
- the task is to create/refine a proposal -> `loom-foo-proposal-refinement`;
- architecture alternatives are being designed/selected -> `loom-foo-architecture-design`;
- evidence must still be acquired -> `loom-foo-evidence-acquisition`;
- the evidence body itself must be assessed -> `loom-foo-evidence-review`;
- the work must be decomposed into executable units -> work-decomposition when available;
- the user only asks for ordinary lightweight advice that does not need a durable Decision Surface.

Generic decision reconciliation is optional composition. Prefer the strongest applicable primary semantic owner.

## 2. Authority boundary

A decision-reconciliation request authorizes analysis and production of a Decision Surface.

It does **not** by itself authorize:
- accepting/canonicalizing the recommendation;
- modifying project authority/state;
- implementation, merge, release, deployment, publication, purchase, spend, or external action;
- new evidence collection;
- reopening accepted decisions unless that reconsideration is explicitly in scope.

Critical invariant:

`RECOMMENDATION != AUTHORITY TRANSITION`

If the user/project authority explicitly decides, record/apply that decision only through the separately authorized project mechanism.

## 3. Resolve the decision contract

Establish the smallest current decision context:
- exact decision to be made;
- subject/version/scope;
- actual decision authority;
- viable alternatives/dispositions;
- current baseline/status quo when meaningful;
- hard constraints / mandatory gates;
- owner objectives/preferences/risk tolerance that can materially change the choice;
- relevant Evidence Assessments/review findings;
- material assumptions and unresolved inputs.

If a value/priority only the owner can supply materially controls the choice, return `NEED_OWNER_CRITERION` rather than inventing it.

For consequential work, read `references/DECISION_SURFACE_CONTRACT.md`.

## 4. Preserve input types

Do not flatten all inputs into “evidence”. Distinguish when material:
- **EVIDENCE ASSESSMENT** — what current evidence defensibly establishes;
- **HARD CONSTRAINT / REQUIREMENT** — a non-negotiable condition and its authority;
- **OWNER VALUE / PREFERENCE** — normative priority, not empirical fact;
- **WORKING ASSUMPTION** — provisional input;
- **AUTHORITY / POLICY** — who may decide and what transition is required;
- **RECOMMENDATION** — the decision-support conclusion produced here.

Read `references/CRITERIA_AND_AUTHORITY.md` for material multi-criteria decisions.

## 5. Apply stronger-owner precedence

Do not duplicate a domain owner merely because it compares alternatives.

Examples:
- architecture selection -> `loom-foo-architecture-design` COMPARISON;
- proposal creation/refinement -> `loom-foo-proposal-refinement`;
- evidence interpretation -> `loom-foo-evidence-review`;
- specialist scientific/security/product method -> that specialist owner when established.

Use this skill when the choice spans multiple assessments/domains, applies owner criteria after reviews, or requires a reusable governance/promotion/acceptance surface.

## 6. Apply hard constraints before preferences

A true hard-constraint violation makes an option non-viable. Do not compensate with a higher score elsewhere.

Do not manufacture options just to populate a matrix. Include status quo/do-nothing only when it is actually available.

Preserve decisive rejection reasons when useful for auditability.

## 7. Do not invent weights

For each material criterion, keep its origin recoverable:
- accepted requirement;
- explicit owner preference;
- policy;
- budget/deadline;
- evidence-derived feasibility limit;
- working assumption.

Weighted scoring is optional and only appropriate when weights/scale semantics are legitimately supplied and useful.

Never invent weights to make a recommendation look objective.

Prefer dominance, constraint elimination, trade-off explanation, or switch conditions when sufficient.

## 11. Do not force a winner

A complete Decision Surface may state:
- one option is recommended;
- two options remain non-dominated and an owner criterion is decisive;
- current evidence is non-discriminating and the real choice is whether to accept risk, defer, or run a reversible experiment.

Do not hide value conflict or insufficient evidence behind arbitrary ranking.

## 12. Produce the Decision Surface

Use the smallest form that remains decision-usable.

When material, make recoverable:
- decision and subject;
- authority transition required;
- alternatives/status quo;
- hard constraints;
- criteria/preferences and provenance;
- relevant Evidence Assessments;
- key assumptions;
- costs/benefits/risks/trade-offs;
- uncertainty and switch conditions;
- reversibility/option value/delay cost;
- recommendation or unresolved owner choice;
- stop reason.

Fast path for a small reversible choice:
- Decision
- Options
- Decisive constraints/evidence
- Recommendation or unresolved owner choice
- One material uncertainty/switch condition
- Authority boundary

## 13. Skill-local dispositions

Use the narrowest applicable state:

- `DECISION_SURFACE_READY` — the authority has a bounded decision-ready synthesis; may contain a recommendation or unresolved owner choice.
- `NEED_OWNER_CRITERION` — a normative preference/priority/risk-tolerance input only the authority can supply materially changes the choice.
- `NEED_CONTEXT` — a resolvable factual, subject, authority, alternative-identity, or constraint input is missing.
- `BLOCKED` — controlling evidence/authority/subject state is inaccessible or materially contradictory enough that no defensible bounded surface can be produced.

Do **not** add an automatic “need more evidence” terminal. Insufficient/non-discriminating evidence belongs in the Decision Surface; whether to acquire more evidence is itself a later decision.
