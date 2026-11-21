# Research Decision — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Turn a decision-relevant uncertainty into the smallest credible **Evidence Plan** that can distinguish the live alternatives and state what the resulting evidence can and cannot justify.

This skill operates **before evidence collection**. It owns research/evidence design, not result interpretation or final authority.
## Durable documentation format and provenance

When the outcome is a **durable text-first document**, prefer real Markdown (`.md`) if the project's current conventions and the available authoring surface support it. Preserve the project-native destination and controlling source; an explicit format request, pinned/project policy, or a material need for rich layout, native comments, collaborative controls, or structured data overrides this preference. Do not create a file merely because the workflow produced an answer. Existing native documents stay native unless a separately authorized migration has a material benefit. Exports are derived copies, not automatic replacement authorities.

For substantive new or revised durable artifacts, record the artifact's own version/date where appropriate and the **actually loaded contributing skill IDs and versions** (or `unexposed` when unknowable). Distinguish execution from reference consultation; never fabricate historical skill provenance. Prefer short YAML frontmatter in raw Markdown or a compact native-format provenance note. Keep source IDs/links, substantive headings and semantic status intact. Materialization and status/canon transitions remain separate authorized operations.
## 1. Determine whether this skill owns the request

Use `loom-foo-research-design` when the primary output is a plan for acquiring evidence.

Typical triggers:
- "How should we test this?"
- "What experiment/research do we need before deciding?"
- "How can we verify whether this is actually true?"
- "What evidence would distinguish these explanations?"
- "Design a probe / benchmark / user study / validation plan."
- a proposal, architecture, or review reaches an empirical boundary.

Do not use this skill as the primary owner when the requested output is:
- a project proposal — use the proposal workflow;
- an architecture — use the architecture-design workflow;
- a review of evidence already collected — use an evidence-review workflow when available;
- one already-bounded executable implementation task — use task-design/execution workflow;
- broad project/portfolio strategy where the main question is what project to pursue;
- literature synthesis as the end product.

If the request contains several materially independent evidence questions, return `PLANNING_REQUIRED` with the decomposition pressure rather than producing one mega-study.
## 2. Preserve authority and side-effect boundaries

A request to design research authorizes analysis and creation of an Evidence Plan.

It does not itself authorize:
- external outreach or participant recruitment;
- spending money;
- production experiments;
- destructive or irreversible probes;
- modifying shared systems;
- exposing private project information;
- implementing the proposed product/architecture;
- accepting a claim or project decision;
- publishing, releasing, or promoting anything.

Execution requires the authority appropriate to that action.

The Evidence Plan is episodic by default. It does not become project authority merely because this skill produced it.
## 3. Resolve the decision before the method

State the smallest concrete decision, transition, or claim the evidence could change.

Then ask:
- What exactly is uncertain?
- Which live alternatives matter to that decision?
- Could any plausible new result materially change the decision?

If current evidence is already sufficient, a bounded direct check has answered the question, or no plausible result would change the decision, return:

`NO_NEW_EVIDENCE_NEEDED`

Do not manufacture a study to satisfy the appearance of rigor.

For consequential plans, read `references/EVIDENCE_PLAN_CONTRACT.md`.
## 4. Identify the discriminating evidence

**Claim Challenge, when decision-relevant.** For a material, testable claim define its exact scope and the observation, counterexample or alternative explanation that would genuinely weaken or refute it. Prefer a direct source inspection, trusted negative test or small probe if that can resolve the question under existing authority; keep it in the current work episode rather than inventing a separate study. Check that the proposed falsifier itself is valid: the observation must target the same claim, relevant conditions and trustworthy oracle. An untestable preference or value judgment is not a failed falsification. Do not create a Challenge Record by default.

Before choosing a method, establish **identifiability**:

> What observation would distinguish the live alternatives strongly enough to affect the decision?

If the alternatives cannot be discriminated under the available constraints:
- return `NO_CREDIBLE_METHOD` when no credible observation is currently available; or
- return `NEED_SPECIALIST_METHOD` when the question is clear but correct design requires methodology beyond the general skill's competence.

Do not continue with a study whose likely outcomes are non-diagnostic.
## 5. Run the evidence-value gate

Prefer the cheapest credible evidence that can support the intended claim.

Ask:
- Is the uncertainty decision-relevant?
- Is there a cheaper direct check?
- Is the action reversible enough to learn by doing safely?
- Does the consequence of a wrong conclusion justify stronger rigor?
- Is the expected information worth the time, cost, risk, and ceremony?

This is qualitative by default. Do not require a numerical value-of-information calculation unless the domain already has a useful economic model.
