# loom-foo

Portable Agent Skills for design, research, product development, planning, writing, verification and agent workflows.

**Status: private release candidate, not published.** The current generic distribution candidate contains **40 independently versioned Skills**; bundle candidate version **0.42.0**. It does not require any Core runtime, paid service or centralized agent orchestrator.

**Publisher identity (email-free candidate):** [`ejct`](https://github.com/ejct). No personal email is included in public-bound manifests; final publisher approval and public GitHub contact availability remain separate release gates.

## What is inside

- `skills/<skill-id>/SKILL.md`: task-specific behavior and activation boundaries.
- Each skill may include `references/`, `scripts/`, `assets/` and `agents/` if needed.
- `SKILL_INVENTORY.json`: exact skill IDs and versions.
- Native host manifests: `plugin.json`, `.codex-plugin/`, `.claude-plugin/`, `.antigravity-plugin/`, `gemini-extension.json`.
- `scripts/validate_distribution.py`: static and relative-link checks.
- `scripts/build_public_release.py`: fail-closed packager using a separately reviewed, owner-approved per-file SHA-256 index.

## Using a Skill

Choose `skills/<skill-id>/SKILL.md` for the actual task and load its conditional references only when needed. Each host has its own supported installation and discovery mechanisms; a Git checkout or passing static test does not demonstrate runtime discovery, routing or execution.

The independent `foo-loom` Core project is optional and is **not** required to use these portable Skills.

## Optional creative composition

The 0.42.0 private candidate integrates Creative Reasoning 0.3.0 with optional, explicitly named collaboration routes for Design, Icon Design, Experience Design, Architecture Design, Drafting, Narrative Design and Proposal Refinement. These are conceptual-method links, **not required dependencies, a global dispatcher or observed agent invocations**.

## Release readiness

The current source is **not cleared for publication**. Project icons are intentionally deferred and not yet referenced in generic manifests. A public plugin package requires a separately approved icon pass; publication also requires a semantic privacy/legal review, verification of publisher identity and public support channels, an owner-approved exact file index, and a clean publishable Git history.

**Do not change repository visibility or create a public release based only on this candidate or its passing CI.**

[License](LICENSE) · [Publisher](PUBLISHER.md) · [Attribution](ATTRIBUTION.md) · [Support](SUPPORT.md) · [Privacy](PRIVACY.md) · [Security](SECURITY.md) · [Terms](TERMS.md) · [Release status](RELEASE_STATUS.md)
