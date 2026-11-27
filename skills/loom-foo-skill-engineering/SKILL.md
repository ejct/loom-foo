---
name: loom-foo-skill-engineering
description: "Assess, create, revise, compare or deliver Agent Skills and diagnose skill routing. Not ordinary coding or GitHub operations."
metadata:
  family: "engineering"
  version: "0.14.0"
  project: "loom-foo"
compatibility: Agent Skills-compatible clients; existing specialist skills, creator tools, Git, CI, and runtime installation may be unavailable.
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt (when consulted/applied).** End user-facing prose with one compact receipt listing only actually consulted/applied skills and versions, `SKILL.md` delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered reference coverage, sources, material checks, actual actions and limitations. `FULL` requires contiguous **model-visible** exact source through EOF, not merely tool retrieval; comprehension/execution is separate. For material distinct stages use an ordered **Process Trail** (review → repair → recheck), with actual findings, provenance and `SAME_CONTEXT` vs observed separate actors. No invented stages, independent review, tests, runtime telemetry, publication or action success. For detail consult `docs/ANSWER_RECEIPT_V0.3.md` if accessible. Do not append a footer when a strict JSON/code/machine/producer-only contract forbids it; do not run extra logging/tests just for the receipt.

# Skill Engineering

## Critical contract — read first

**Owner:** Assess, create, revise, diagnose, package or deliver a reusable Agent Skill. Preserve user's real outcome and existing skill owners; do not substitute benchmarks, audits, prompt ceremony or speculative infrastructure for a useful skill. Mode: `ASSESS | CREATE | REVISE | DIAGNOSE | PACKAGE/DELIVER | FIRST_USE | PORTFOLIO | EXPLORE`. Do not take over ordinary coding/GitHub work or an adjacent proposal/architecture/project owner.

**Skill delivery:** Exact *installed/selected* version matters. For each required root and conditionally triggered reference, confirm contiguous **model-visible** delivery through EOF before claiming `FULL`. A tool that fetched 30 kB but forwarded only 10 kB proves **PARTIAL**, not FULL; restore missing ranges in separate bounded outputs. For a Code Mode clipped read use `references/FULL_SOURCE_DELIVERY.md`. `AVAILABLE ≠ LOADED ≠ APPLIED ≠ VERIFIED`; a successful package does not prove ChatGPT automatic routing.

## Operational method

1. **Choose surface and owner:** Compare existing skill, targeted revision, project instructions, one-off prompt, reference, deterministic script/tool, native plugin/connector and **no new skill**. Create a new ID only for distinct reusable output, activation and acceptance boundary. Do not invent a central router, mandatory parent skill, global case registry or system service from one failure.
2. **Source truth and alternatives:** Resolve current installed version, accepted constraints, runtime, user-private boundaries, exact candidate/source. For consequential redesign/new skill, explore plausible alternatives *before* bounded external prior art, reconcile findings, and pick smallest useful method. Keep facts, inferred conclusions and unverified claims separate.
3. **Author the smallest usable package:** `SKILL.md` must be concise and executable: positive/negative trigger, goal, authority, main procedure, result, conditional references. Longer methods/examples → `references/`; scripts only for deterministic benefit; fixtures → `tests/`. Preserve frontmatter `name` = folder, `metadata.family` and actual versions; no third-party/private raw data in public skill. Never silently copy untrusted executable package instructions into authority.
4. **Check and use:** Test source/refs/metadata and only material positive, negative, neighboring-owner, authority and privacy regressions. Measure STATIC, DISCOVERY, ROUTING, EXECUTION and FIELD separately; static PASS cannot prove routing. For an automatic-routing claim, require fresh-context observations of the host-selected owner and actual root/reference loading, not merely expected-owner fixtures or the model's own account. Missing host evidence remains NOT_CONFIRMED. Use first in a real authorized task after proportionate checks, not a mandated comparative campaign. Same-context self-review is not independent audit.
5. **Deliver accurately:** Use Behavioral SemVer based on changed contract: PATCH for non-contract repair, MINOR for new compatible behavior/changed default, MAJOR for breaking after 1.x (0.x breaking → next MINOR + explicit note). Preserve old release, consumer pins, plugin identity/private overlays; update only authorized runtime, read back installed bytes. `ZIP ≠ INSTALLED`, `INSTALLED ≠ ROUTED`, `TEST PASS ≠ ACCEPTED`. Do not ship or merge to Git without authority.
6. **Self-failure:** Recover user's active task first. Check `ROUTING`, `DELIVERY`, `COMPOSITION`, source and tool defects before editing a skill because of one output. Fix smallest evidenced cause and rerun affected regression.

**Conditional behavioral coverage.** For a material skill-contract or composition change, identify affected behaviors and neighboring-owner/authority invariants; map each to actual static, execution or field evidence at the claimed fidelity. Preserve untested scenarios and limits, distinguish an expected fixture from a runtime observation, and reopen materially affected checks after contract/revision changes. Do not invent a coverage percentage for the space of possible user prompts, demand an optional comparative campaign, or expand routine bounded repairs into a portfolio-wide audit.

## Progressive disclosure and event-triggered routing

`L0` skill name/description chooses the **subject owner**; do not make every skill compete as a global Adaptive Refinement router. `L1` root `SKILL.md` must include the signal/decision needed to select any conditional `L2` reference **before** that reference is loaded. `L2` may expand methods, never be the only location describing its own activation. A long/complex source is not automatically a positive trigger. Check negative/no-trigger and neighboring-owner cases; static source coverage does not prove runtime routing. Use `references/PD_SKILL_AUTHORING.md` when revising this contract.

## Conditional method index (read BEFORE affected work)

- **Assess creation, owner overlap or discover skills:** `references/PD_SKILL_CHOICES.md` (original §§1–3); for nontrivial ownership `references/COMPOSITION_AND_OWNERSHIP.md`; for search/comparison `references/SKILL_EXPLORER.md`.
- **Design new consequential mechanism/architecture or external research:** additionally `references/SOLUTION_SPACE_AND_DELIVERY.md` and `references/EXTERNAL_PRIOR_ART.md`; check external current source/alternative rather than making up prior art.
- **Draft/change package, progressive disclosure, activation contract or taxonomy:** `references/PD_SKILL_AUTHORING.md` (original §§4–5); `references/SKILL_TAXONOMY.md` for loom-foo-owned skill releases.
- **Verify/install/release or assess automatic activation:** `references/PD_SKILL_VERIFY_AND_RELEASE.md` (original §§6–7); `references/VERIFICATION_AND_CASES.md` (includes optional offline host-observation evaluation); `references/PACKAGE_AND_DELIVERY.md`. For source-forwarding errors `references/FULL_SOURCE_DELIVERY.md`.
- **Diagnose recurring failures, self-apply, or prepare exact final engineering receipt:** `references/PD_SKILL_RECOVERY.md` (original §§8–9). For cross-project historical transfer, `references/EXPERIENCE_AND_EVIDENCE.md`.

## Completion

Return actual decision or artifact, exact base/current version, scoped checks and test gaps, actions vs installation, and remaining runtime limitations. If user authorized installation, complete it in the same episode where feasible; don't request an artificial second approval. Never claim a new chat loaded or selected skills merely because manifest/update readback succeeded. End with one truthful Answer Receipt when applicable.
