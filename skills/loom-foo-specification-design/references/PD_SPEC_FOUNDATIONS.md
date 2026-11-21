# Spec Foundations — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.


Turn accepted or otherwise authoritative intent into the smallest coherent **Specification** that makes required semantics explicit enough for architecture, planning, execution, and verification to consume without silently inventing product behavior.


The primary distinction is:


**Specification = what must hold. Architecture = how the system makes it hold.**


This skill owns semantic contract construction and evolution. It does not create project authority, choose whether the project should pursue the change, or prove that an implementation conforms.
## Durable documentation format and provenance

When the outcome is a **durable text-first document**, prefer real Markdown (`.md`) if the project's current conventions and the available authoring surface support it. Preserve the project-native destination and controlling source; an explicit format request, pinned/project policy, or a material need for rich layout, native comments, collaborative controls, or structured data overrides this preference. Do not create a file merely because the workflow produced an answer. Existing native documents stay native unless a separately authorized migration has a material benefit. Exports are derived copies, not automatic replacement authorities.

For substantive new or revised durable artifacts, record the artifact's own version/date where appropriate and the **actually loaded contributing skill IDs and versions** (or `unexposed` when unknowable). Distinguish execution from reference consultation; never fabricate historical skill provenance. Prefer short YAML frontmatter in raw Markdown or a compact native-format provenance note. Keep source IDs/links, substantive headings and semantic status intact. Materialization and status/canon transitions remain separate authorized operations.
## 1. Routing gate


Use `loom-foo-specification-design` when the requested primary output is a semantic contract, requirements/specification artifact, or explicit semantic delta.


Typical triggers:


- "turn this accepted proposal into a specification";


- "define exactly what this feature/system must do";


- "formalize the behavior/invariants/edge cases";


- "update the current specification for this accepted change";


- "make this contract testable without prescribing implementation";


- a proposal or decision is accepted/bounded enough that downstream architecture or implementation needs stable semantics.


Do not use this skill as the primary owner when the requested output is:


- whether a project-local change should be adopted -> `loom-foo-proposal-refinement`;


- a new or changed architecture -> `loom-foo-architecture-design`;


- an architecture audit -> `loom-foo-architecture-review`;


- an evidence-acquisition plan for an empirical uncertainty -> `loom-foo-research-design`;


- dependency-aware implementation/work decomposition -> `loom-foo-work-decomposition` when available;


- one already-bounded executable agent task -> `loom-foo-agent-task-design`;


- conformance of an exact implementation candidate -> `loom-foo-change-verification` when available;


- a pure independent frozen-spec audit -> a specification-review capability if one exists.


If the request is broad but still one coherent semantic contract, keep it here. Do not return `PLANNING_REQUIRED` merely because the specification contains many requirements.
## 2. Preserve authority


Specification construction does not create authority.


Resolve the controlling source for the intended semantics. Possible sources include:


- an accepted proposal or decision;


- explicit user-authorized intent;


- an accepted external standard or contract;


- an existing Specification plus an accepted change;


- an accepted architecture-derived constraint;


- another authoritative project source.


Do not silently turn:


- a brainstorming idea;


- an architecture convenience;


- an implementation detail;


- an old draft;


- a model inference;


- a reviewer suggestion


into a required behavior.


When sources conflict materially, preserve the conflict and return `BLOCKED` or `NEED_CONTEXT` rather than choosing authority by convenience.
## 3. Determine mode and baseline


Choose the narrowest mode.


### NEW_SPEC


Use when no current authoritative Specification exists for the semantic subject.


Input:


authoritative intent


Output:


Specification


### EVOLVE_SPEC


Use when a current Specification exists and an accepted change modifies its semantics.


Input:


current Specification + accepted change


Output:


Specification Delta, or a Specification Delta Set when the change legitimately spans several semantic subjects.


Before elaborating a delta, compare the requested behavior with the current Specification.


If the accepted requested semantics are already fully represented, return:


`NO_SPEC_DELTA`


Do not rewrite a specification merely because this workflow was invoked.


For artifact details and delta semantics, read `references/SPECIFICATION_CONTRACT.md`.
## 4. Establish the semantic subject


Define only what is needed to keep the contract coherent:


- subject / capability / protocol / workflow being specified;


- baseline/version when evolving an existing contract;


- relevant actors or external systems;


- scope and non-goals;


- controlling authority/provenance;


- accepted constraints;


- material assumptions and unresolved decisions.


A Specification is one coherent semantic contract, not one implementation task.


Split only when parts have materially independent:


- semantic subjects;


- authority/provenance;


- lifecycle/versioning;


- compatibility or conformance boundaries;


- downstream consumers.


This is semantic decomposition, not implementation planning.
