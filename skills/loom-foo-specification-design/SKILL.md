---


name: loom-foo-specification-design


description: "Define precise behavioral specifications from accepted intent, obligations and edge cases. Not architecture, implementation or verification."


compatibility: Agent Skills-compatible clients. Project sources, accepted proposals/decisions, existing specifications, external standards, schemas, and formal modeling tools are optional. The skill remains useful without LoomLoom.


metadata:


  family: "engineering"
  project: "loom-foo"


  version: "0.6.0"
---

<!-- Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt (when a skill is consulted/applied):** Finish prose with one concise receipt of actual skills and versions, `FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED` model-visible SKILL.md delivery, required reference coverage, sources, checks, changes and remaining limitations. Distinct material passes may use ordered Process Trail; self-review is `SAME_CONTEXT`, not an independent agent. Do not claim runtime routing, tests, fresh reading or independent verification without observed evidence; preserve strict machine-only output formats.

**Core boundaries.** Preserve the user's actual result, current controlling sources and accepted decisions. Tool access, source possession and ability to write do **not** grant authority to mutate project state, adopt a proposal/specification/architecture, spend money, publish, merge, change permissions or disclose private data. Stop only for a real material missing authority/source/decision; continue independently safe work. Use the smallest useful artifact and proportionate evidence; neither a successful reader call nor a named method proves execution. For durable text-first work, prefer native project conventions (often Markdown), keep provenance and distinguish a draft, saved artifact, project acceptance and publication.

# Specification Design

**Owner / normal outcome.** Construct or evolve the smallest independently usable semantic **Specification**: *what must hold*, not architectural *how*. The input must be accepted/otherwise authoritative intent. Do not assume a brainstorm, implementation convenience or reviewer suggestion is authoritative.

## L1 — normal path

1. Route semantic contracts here; proposal adoption -> Proposal Refinement, system implementation design -> Architecture Design, actual conformance -> Change Verification, evidence method -> Research Design, runnable delegated task -> Agent Task Design.
2. Choose `NEW_SPEC` or `EVOLVE_SPEC`, bind subject/baseline, actors, controlling authority, scope, constraints and relevant unknowns. Before evolving, check whether the requested semantics are already represented: if so, return `NO_SPEC_DELTA`, not a ceremonial rewrite.
3. Derive independently referenceable required behavior, allowed/disallowed states, event/transition semantics, preconditions, invariants, failure/cancellation/edge behavior, compatibility and acceptance where material. Keep architectural implementation choices out unless *explicitly mandated* by controlling authority.
4. Make conformance decidable **in principle** but do not turn requirement construction into a benchmark or pick unaccepted product behavior. Provenance and unaffected obligations survive revisions; use an explicit semantic Delta when the accepted contract changes.
5. Perform a proportionate author-owned quality check: necessity, ambiguity, completeness, consistency, verifiability, overconstraint and solution leakage. If material product authority conflicts or is missing, surface `NEED_CONTEXT`/`BLOCKED`; if discriminating empirical evidence is necessary, `VALIDATION_REQUIRED`.
6. Return `SPEC_READY`, `NO_SPEC_DELTA`, `VALIDATION_REQUIRED`, `NEED_CONTEXT`, `PLANNING_REQUIRED` or `BLOCKED` as applicable. Neither `SPEC_READY` nor a generated delta makes the specification canonical.

**Hard rules:** preserve accepted intent and existing obligations, never invent requirements or silently rewrite adjacent projects. **Use-first** applies to ordinary skill changes: do not require a no-skill comparison, blind holdout or promotion campaign unless a separate frozen evaluation/explicit comparative claim requires one. Integrity, authority, semantic and target-specific regression checks remain mandatory as appropriate.

## Conditional method index

- **Existing spec/change, provenance, multiple semantic subjects or uncertain authority:** read `references/PD_SPEC_FOUNDATIONS.md` and existing `references/SPECIFICATION_CONTRACT.md`.
- **Material state/transition/failure obligations, acceptance complexity or disputed solution leakage:** read `references/PD_SPEC_OBLIGATIONS.md`; for detailed checks `references/REQUIREMENT_QUALITY.md`, and for nonprose representation `references/BEHAVIORAL_PATTERNS.md`.
- **Consequential quality dispute, nontrivial revision, uncertainty or a terminal-state ambiguity:** read `references/PD_SPEC_QUALITY.md`; for evolving durable traceability `references/TRACEABILITY.md`.
- **Cross-owner handoff, reused downstream requirements, candidate/skill-evaluation concern:** read `references/PD_SPEC_HANDOFF.md`.

**Non-triggers:** a short accepted requirement change does not force reading every profile, external research or a comparative campaign. A specification is not one implementation task.
