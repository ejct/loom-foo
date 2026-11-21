# Adaptive Refinement — Optional Agent Delegation

Conditional reference for `loom-foo-agent-task-design` §15A. Applies only if a substantive refinement pass benefits from a distinct execution context. This document is **runtime-neutral**; Codex-specific capabilities are examples, not guaranteed hooks. It does not change the one-Task-Brief owner or require a new skill/agent profile.

## 1. Decide whether to delegate

Stay in one agent for small, clear, low-risk or tightly sequential work. Consider a separate context only when at least one *material* benefit is plausible: unanchored counterexamples, independent source/criteria inspection, bounded parallel evidence work, or context separation for a consequential decision. Consider token/context cost, repeated source loading, unavailable tools, and risk of shared writable state. A custom role profile is optional; use native agents if actually available. Never install TOML, change a project, or spawn a worker merely because a skill was loaded.

## 2. Preserve roles and ownership

- **Root/owner**: retains authorized outcome, source precedence, scope, side-effect permissions, candidate integration, finding adjudication and final delivery. Delegation does not create acceptance or release authority.
- **Author/Builder/Designer**: constructs and repairs the one artifact within the approved writable scope; normally keeps editing ownership.
- **Reviewer/Challenger**: finds *unknown* failure modes, source/goal gaps, counterexamples, scope or authority leaks. Returns evidence-bearing findings, not a blanket PASS; does not repair the candidate during review.
- **Verifier/Evaluator**: checks *predeclared* properties against the exact subject with an identified oracle, returning PASS / FAIL / INCONCLUSIVE / NOT_COVERED per criterion. Does not invent acceptance conditions, change fixtures/goldens to pass, or claim owner acceptance.
- **Researcher / Architect**: only when the domain actually requires distinct source evidence or a bounded specialist design; do not add agents merely to populate the existing role catalog.

An agent can hold multiple functional roles; a different role name in the same context is not independent evaluation.

## 3. Task-local delegation envelope

Before actual delegation, bind the smallest sufficient:
1. **Question and lens**: a concrete suspected risk or unknown-defect surface and the requested output;
2. **Subject**: exact candidate version/commit/document and base when material;
3. **Controlling intent**: original owner goal, accepted decisions, constraints, source precedence, and relevant reachable source locations;
4. **Permissions**: real read/write/tool scope and external effects; review instructions are not an OS sandbox;
5. **Evidence**: what direct observations, counterexamples or criterion checks would count, with limits/oracle identity;
6. **Return**: findings with consequences/resolution criteria or per-criterion observations, source coverage, identity, and uncertainty.

Prefer not to pass the author's advocacy or detailed self-justification into a first adversarial review when a clean context is material. But **do not omit accepted product decisions, protected invariants or facts needed for a fair review**. A fresh context with no relevant evidence is worse than a well-grounded self-check.

## 4. Execution pattern

`owner + source -> C0 -> [reviewer unknown-defects; verifier fixed criteria if material] -> root adjudication -> author C1 -> targeted regression/verification -> owner outcome`

Bracketed reviews may be parallel only after C0 is stable and the reviews do not write conflicting shared state. Verifier may instead run **after** repair when its main purpose is closure. Do not run an always-on parallel Reviewer+Verifier pair. Findings are hypotheses until adjudicated against the controlling sources and observed artifact.

Rebind checks after an actual content/commit change; old PASS does not carry automatically. The owner repairs valid defects, rejects invalid findings with evidence, preserves existing decisions, and stops when remaining issues are bounded and another pass has low information value. If all agents share the same oracle, summary or copied source, qualify claims of independence.

## 5. Codex runtime projection (optional)

Codex supports native subagent workflows and optional project-local custom agent profiles. Use actual host-discovered roles and tool signatures; never assume a skill, connector, sandbox capability or agent profile is installed from a generated instruction. The independent source/module `foo-loom/role-setup` offers opt-in `minimal`, `review` and `specialists` profiles when available and explicitly authorized; its default is a single agent with no custom TOML.

For a materially clean review, select the runtime-supported fresh/isolated-context mechanism **and confirm the actual input/context mode**. Merely spawning or naming a reviewer does not establish a blind or independent evaluation. Subagents can inherit permissions, skills, model limitations, tool access and shared filesystem state; a prose read-only instruction is not enforced isolation. A source accessible to the ChatGPT coordinator is not necessarily accessible to Codex; stage permitted exact material or report a genuine source gap. Do not paste private source into an unapproved recipient/context.

The root reports actual spawn/role/skill use and candidate-bound checks only from visible events and artifacts. Without that evidence, report `NOT_CONFIRMED`; without capability, execute the same relevant checks locally and label them `SAME_CONTEXT`. Never claim host activation, independent review, Codex setup or runtime PASS from a static Task Brief or staged TOML alone.

## 6. Example cases (for use-first diagnosis)

- **No-spawn:** one reversible local typo/rename with obvious verification; integrated author check is enough.
- **Complex specification:** author drafts S0; a distinct Reviewer seeks missing interruption/failure semantics against the same accepted source, then author repairs and checks affected acceptance. Verifier handles exact specified obligations only if criterion-level evidence matters.
- **Change review:** reviewer finds an unforeseen authorization leak; root confirms actual source/boundary; builder repairs; verifier checks the frozen corrected candidate and relevant negative case.
- **False independence:** two agent threads inherit the author rationale and quote the same unsupported summary. They are distinct executions but not independent evidence; report the limitation.
- **Moving target:** reviewer inspects SHA A while author updates to SHA B. Findings remain scoped to A; targeted recheck is needed before claiming B clean.
- **Permission confusion:** reviewer instructions say read-only but actual tools allow writes. No sandbox guarantee may be claimed; avoid unauthorized mutations.
- **Unavailable custom role:** project has no reviewer TOML. Native review may still be possible; absence of a preset is not a required setup or blocker.
- **Cost control:** expensive extra agent cannot access the necessary source. Do not spawn it merely to repeat a low-evidence self-review.
