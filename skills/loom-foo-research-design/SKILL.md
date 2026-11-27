---
name: loom-foo-research-design
description: "Design the smallest credible evidence or experiment plan for a material decision uncertainty. Not routine checking or evidence collection."
compatibility: Agent Skills-compatible clients. External sources, project context, specialist research methods, and execution harnesses are optional. The skill must remain useful without foo-loom Core.
metadata:
  family: "research"
  project: "loom-foo"
  version: "0.9.0"
---

<!-- Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt (when a skill is consulted/applied):** Finish prose with one concise receipt of actual skills and versions, `FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED` model-visible SKILL.md delivery, required reference coverage, sources, checks, changes and remaining limitations. Distinct material passes may use ordered Process Trail; self-review is `SAME_CONTEXT`, not an independent agent. Do not claim runtime routing, tests, fresh reading or independent verification without observed evidence; preserve strict machine-only output formats.

**Core boundaries.** Preserve the user's actual result, current controlling sources and accepted decisions. Tool access, source possession and ability to write do **not** grant authority to mutate project state, adopt a proposal/specification/architecture, spend money, publish, merge, change permissions or disclose private data. Stop only for a real material missing authority/source/decision; continue independently safe work. Use the smallest useful artifact and proportionate evidence; neither a successful reader call nor a named method proves execution. For durable text-first work, prefer native project conventions (often Markdown), keep provenance and distinguish a draft, saved artifact, project acceptance and publication.

# Research Design

**Owner / normal outcome.** Design the smallest credible **Evidence Plan** for a decision-relevant uncertainty, before data collection. Do not take over routine direct checks, implementation, evidence review or broad project strategy.

## L1 — normal path

1. Identify the **actual decision** an observation could change. If current evidence is sufficient, a direct check settles it, or no plausible result would change the decision, return `NO_NEW_EVIDENCE_NEEDED` — no artificial study.
2. Name the narrow uncertainty and genuinely live alternative explanations. First establish **identifiability**: what would distinguish them sufficiently to affect the decision? If no credible observable difference exists, return `NO_CREDIBLE_METHOD`; if specialized expertise is necessary, `NEED_SPECIALIST_METHOD`.
3. Choose the least costly credible method (source inspection, capability probe, measurement, replication, qualitative study, controlled experiment only when justified). Specify actual subject/version, relevant environment and evidence source; add baseline, controls, repetition and measurement validation only when needed for the intended claim.
4. State a fit-for-purpose oracle/measurement and what it misses; separate exploratory from confirmatory work and protect frozen treatments/stopping rules where required. Include positive, refuting and inconclusive interpretations plus claims that evidence can **never** license.
5. Specify stopping/adaptation conditions and a natural execution handoff. Do not commence recruitment, spending, real experiments, publication or external state changes without proper authority. A plan's success is not evidence that the test ran.
6. End `EVIDENCE_PLAN_READY`, `NO_NEW_EVIDENCE_NEEDED`, `NEED_CONTEXT`, `NEED_SPECIALIST_METHOD`, `NO_CREDIBLE_METHOD` or `PLANNING_REQUIRED`, with minimal useful detail.

**Conditional coverage design.** For a materially multi-source, multi-question or multi-session Evidence Plan, define the intended coverage surface: questions/categories, closed corpus or open discovery space, source/segment and required method/fidelity, inclusion/exclusion, scope-change handling, and sufficient completion/stopping criteria. Name material unknown areas separately from known remaining units. Require a recoverable map of planned checks to observed results, valid negative results, gaps and blockers; an open search has no defensible global percentage. Plan alternative discovery channels or challenge checks when material; do not require a coverage register for a single direct check or impose an exhaustive review for a decision-sufficient experiment.

**Conditional participant-data constraints.** When a plan collects or reuses identifiable or otherwise restricted participant material, bind the applicable consent/policy, permitted purposes, data classes, recipients/processors, retention and handling before selecting collection, reuse or sharing methods. Minimize collection and use approved de-identification where appropriate. If permission is unknown, exclude or isolate the affected use and continue authorized work; do not infer permission from access or claim legal compliance. Respect actual policy rather than imposing a universal consent or retention rule.

**Hard rules:** no fixed research ceremony, numeric value-of-information scores, comparative benchmark or arbitrary number of trials for a cheap reversible question. No research design can imply acceptance, project authority or deployment. Don't confuse reproducibility, replicability, generalization, causality and validity.

## Conditional method index

- **Consequential uncertainty, disputable need for new evidence or complex alternative explanations:** read `references/PD_RESEARCH_DECISION.md`; detailed existing `references/EVIDENCE_PLAN_CONTRACT.md` if an actual Evidence Plan is warranted.
- **Method selection beyond obvious direct inspection, AI/agent variability, contamination, controlled or confirmatory method:** read `references/PD_RESEARCH_METHOD.md`; use existing `references/METHOD_ROUTING.md` or `references/AI_AGENT_EVAL_PROFILE.md` when their scenario is triggered.
- **Nontrivial measurement/oracle validity, possible bias, optional stopping or interpretation under uncertainty:** read `references/PD_RESEARCH_INTERPRETATION.md` and existing `references/VALIDITY_CHECKS.md` when material.
- **Execution handoff, complex result state or cross-skill ownership boundary:** read `references/PD_RESEARCH_HANDOFF.md`.

**Non-triggers:** no mandatory study when a single factual check, current evidence or reversible first use suffices. No frozen evaluation campaign unless the decision/claim really requires it.
