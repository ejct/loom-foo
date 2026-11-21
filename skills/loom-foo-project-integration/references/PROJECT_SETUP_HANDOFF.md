# Project Integration — exact Codex handoff clauses

This is a reference for an already-selected integration task. Do not add these clauses to unrelated Task Briefs or generic AGENTS.md. A selected/disabled Skill is controlled by the runtime, not by instructions inside another Skill.

## When ChatGPT lacks the local project

Append a small **read-only preflight** to the existing agent task, not a standalone stop:

> Inspect the actual local project instructions (`AGENTS.md` and relevant subdirectory instructions), `.foo-loom/foo-loom.lock`, `.loomloom/loomloom.lock`, existing `.agents/skills/` and accepted project policy sources. Do not assume foo-loom is absent because the coordinator cannot access local files. Respect an existing exact Core pin, owner customizations and policies. Report the observed status; do not install or change project configuration unless the task's authority explicitly covers that operation. Proceed with independent in-scope work toward the original task outcome.

## When setup is explicitly authorized

Carry the exact approved project path, permitted managed files, selected `foo-loom` source commit/package, approved policy-adoption choices (possibly none), and side-effect limitations. If any are materially missing, prepare the change preview and ask once for just the missing approval; do not infer it from the user requesting implementation.

> In the actual local workspace, inspect existing instructions and Core/legacy pins. Preview the exact proposed managed-file delta. If the installer has no dry-run support, do not claim it did; use a safe staging copy or an equivalent read-only plan. With the stated project-scoped authority only, use the verified installer from the approved exact Core subject. Preserve unrelated files and halt on conflicting managed content or incompatible legacy pin. Read back exact lock, Bootstrap and AGENTS.md changes. Policy copies are not automatic adoption. Default to no custom agent profiles. Then perform the primary implementation work and relevant verification within the original task scope. Return setup and work results separately, with exact evidence of what was executed, discovered, loaded, applied and verified.

## If foo-loom is already installed

No install or upgrade. Use the exact lock and accepted policies; do not substitute a newer release because one exists. For a new agent session, follow the project Bootstrap entrypoint. Report a missing or unreadable source as a specific limitation, not a reconstructed substitute.

## Actual permission boundary

A broad request to develop a feature or prepare a prompt authorizes neither new Core installation nor changes to project policy. Access to GitHub, shell tools or Codex custom-agent support does not grant consent. Do not require repeated confirmation when a precise active authorization covers the exact operation, but revalidate material changes to source, scope or effects.
