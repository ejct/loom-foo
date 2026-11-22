# Project Integration — exact Codex handoff clauses

This is a reference for an already-selected integration task. Do not add these clauses to unrelated Task Briefs or generic AGENTS.md. A selected/disabled Skill is controlled by the runtime, not by instructions inside another Skill.

## When ChatGPT lacks the local project

Append a small **read-only preflight** to the existing agent task, not a standalone stop:

> In the authorized local project, inspect actual instructions (`AGENTS.md` and relevant subdirectory instructions), `.foo-loom/foo-loom.lock`, historical `.loomloom/loomloom.lock`, `.agents/skills/foo-loom-bootstrap/`, and accepted project policies. Verify components separately; a lock alone does not prove a complete install, and absence of coordinator access does not prove absence of Core. Classify the observed condition as coherent, absent, partial/drifted or conflicting, recording the exact pin only if verified. Do not install, upgrade, adopt policies or change configuration without precise permission covering the affected managed paths and exact source. Proceed with independently safe in-scope work toward the original task outcome.

If evidence shows partial setup, the executor must follow `PROJECT_STATE_RECOVERY.md` (read from the installed Project Integration skill when available), compare observed vs expected managed parts, and **not** run an unconditional fresh install. If this reference is unavailable to the executor, give a minimal non-destructive read-only discrepancy report rather than pretending it has read the method.

## When setup or repair is explicitly authorized

Carry the exact approved project path, permitted managed files, immutable `foo-loom` source commit/package, approved policy-adoption choices (possibly none), and side-effect limitations. If anything material is missing, preview a safe change and ask once for only the missing approval; do not infer it from the user requesting unrelated implementation.

> In the actual local workspace, inspect existing instructions and Core/legacy pins, and compare lock/Bootstrap/managed block independently. Preview the exact proposed managed-file delta. If the installer has no dry-run support, do not claim it did; use safe staging or an equivalent read-only plan. With the stated project-scoped authority only, use the verified installer from the approved exact Core subject. Preserve unrelated files and halt on conflicting managed content, incompatible legacy pin or unexpected symlink. Read back exact lock, Bootstrap, AGENTS block, and unaffected neighboring text. Policy copies are not automatic adoption. Default to no custom agent profiles. Then perform primary implementation work and relevant verification within the original task scope. Return setup/repair and primary-task results separately, with evidence of actual execution, discovery, loading, application and verification.

## If foo-loom is already installed

No install or upgrade. Use the exact verified lock and accepted policies; do not substitute a newer release because one exists. For a new agent session, follow the project Bootstrap entrypoint. An unverified or unreadable pin remains an uncertainty, not an inferred release.

## Actual permission boundary

A broad request to develop a feature or prepare a prompt authorizes neither new Core installation nor changes to project policy. Access to GitHub, shell tools or Codex custom-agent support does not grant consent. Do not require repeated confirmation when a precise active authorization covers the exact operation, but revalidate material changes to source, scope or effects.
