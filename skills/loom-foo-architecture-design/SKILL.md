---
name: loom-foo-architecture-design
description: "Design or evolve software/system architecture with explicit alternatives and constraints. Not review-only assessment of existing architecture."
compatibility: Agent Skills-compatible clients. Can use repository/project sources, connected tools, empirical probes, and a separate architecture-review skill when available; must remain usable without cross-skill invocation.
metadata:
  family: "engineering"
  project: "loom-foo"
  version: "0.7.0"
---

<!-- Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt (when a skill is consulted/applied):** Finish prose with one concise receipt of actual skills and versions, `FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED` model-visible SKILL.md delivery, required reference coverage, sources, checks, changes and remaining limitations. Distinct material passes may use ordered Process Trail; self-review is `SAME_CONTEXT`, not an independent agent. Do not claim runtime routing, tests, fresh reading or independent verification without observed evidence; preserve strict machine-only output formats.

**Core boundaries.** Preserve the user's actual result, current controlling sources and accepted decisions. Tool access, source possession and ability to write do **not** grant authority to mutate project state, adopt a proposal/specification/architecture, spend money, publish, merge, change permissions or disclose private data. Stop only for a real material missing authority/source/decision; continue independently safe work. Use the smallest useful artifact and proportionate evidence; neither a successful reader call nor a named method proves execution. For durable text-first work, prefer native project conventions (often Markdown), keep provenance and distinguish a draft, saved artifact, project acceptance and publication.

# Architecture Design

**Owner / normal outcome.** Create, compare or evolve a coherent system architecture. Use `loom-foo-architecture-review` instead for read-only evaluation. This skill produces an architectural artifact; it does not automatically accept, implement or canonicalize it.

## L1 — normal path

1. Choose `GREENFIELD`, `EVOLUTION` or `COMPARISON`. Reconstruct the actual system objective, accepted design decisions, source truth, authority, constraints, critical flows, state/semantics and relevant quality drivers. For evolution, distinguish intended architecture, observed runtime and stale documents.
2. **Local delta gate (EVOLUTION):** does existing architecture already satisfy the pressure? If so return `NO_ARCHITECTURE_DELTA`, without inventing services or migrations. Choose quality drivers and scenario/response measures only when they change the decision.
3. Where design space is genuinely open, compare a simplest credible solution with materially different alternatives, including existing products, reusable components, instructions, local scripts or no added layer if relevant. Do not force alternatives or external searches when one bounded solution is plainly sufficient.
4. State the selected candidate's responsibilities, state owners, key decisions, critical paths, constraints, failure/recovery, interfaces, trade-offs and assumptions. Use `SELECTED_FOR_REFINEMENT` as workflow status, **not** project adoption.
5. Challenge consequential assumptions and failure cases in a bounded **same-context adversarial self-review** by default. Repair a specific wrong decision; reopen the whole architecture only for invalid thesis/drivers. Recheck affected invariants after revision. Defer premature choices; never require a reviewer agent or fixed multi-pass ritual.
6. Close as `CONVERGED`, `VALIDATION_REQUIRED`, `BLOCKED` or `NON_CONVERGING` with a usable architecture and concise Design Closure. Empirical unknowns require an honest smallest probe, not theoretical PASS or automatic halt of independent safe work.

**Hard rules:** architecture design does not authorize canonical changes, commits, migration, deployment or release. A tool or separate skill being available does not establish actor independence. No guessed metrics, premature services or unrequested project-wide redesign. Preserve units/state/timebases when materially relevant.

## Conditional method index

- **Evolution, source/authority ambiguity, failure-driven architecture or complex driver analysis:** read `references/PD_ARCH_FOUNDATIONS.md`.
- **Materially open design space or new architecture pattern/component choice:** read `references/PD_ARCH_DISCOVERY.md`; simple constrained work skips this exploration.
- **Multiple legitimate candidates, deferred/phase choices, trade-off-sensitive selection:** read `references/PD_ARCH_SELECTION.md`.
- **Consequential correction, invalidated invariant, critical risk or empirical assumption:** read `references/PD_ARCH_REFINEMENT.md`; a separate architecture-review skill only if available and genuinely useful.
- **Consequential terminal status, fitness function or material accepted risk:** read `references/PD_ARCH_CLOSURE.md`.

**Non-triggers:** no automatic architecture-review agent, alternate design enumeration, benchmark or deep candidate funnel for a trivial local decision. An empirical gap limits claims, not authorized progress by itself.
