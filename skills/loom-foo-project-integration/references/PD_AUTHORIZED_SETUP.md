# project-integration — conditional method

> Preserved sections from private Loom-foo 0.35.1 SKILL.md. Referenced `references/...` paths are relative to the owning skill root. L1 activation and authority remain controlling. Expanded in 0.5.0 for safe partial-state handling.

## 4. Authorized installation and continuation

When the project is explicitly approved for Core setup:

1. Resolve the **exact, available** foo-loom source commit or immutable package and compatible installer. Do not point a new install at mutable branch HEAD, and do not change historical Core/legacy pins.
2. Inspect state separately for current/legacy lock, Bootstrap, managed portion of `AGENTS.md`, policy adoption and intended managed paths. A partial or conflicting installation is **not an empty project**. Read `references/PROJECT_STATE_RECOVERY.md` for missing/changed files, interrupted setup, edited managed block or inconsistent pins.
3. Preview proposed changes to `.foo-loom/`, `.agents/skills/foo-loom-bootstrap/` and the managed portion of `AGENTS.md` using available safe reads/diffs. If the actual installer has no native `--dry-run`, do **not** invent one; use a safe copy/snapshot or equivalent preflight. Protect symlinks, changed managed blocks and unrelated instructions. Confirm scoped write authority for the actual delta; halt on conflicts or uncertain source identity.
4. Apply only explicitly approved project-local writes using the actual available installer, verify exact pin, installed files, managed block and preserved neighboring content. Any new Core policies remain **unadopted** until the project authority explicitly accepts them. Never silently upgrade. Do not claim rollback/atomicity without an observed supported mechanism.
5. Default to **one ordinary primary agent and no custom `.codex/agents/*.toml` profiles**. Native delegation remains on demand. Install optional specialized profiles only with separate specific authorization and host-supported runtime validation.
6. Continue the **original authorized task** after setup where the executor can do so. If setup is blocked, continue safe independent work; escalate only the blocked write/authority dependency. Do not close the original task with `SETUP_DONE`.
7. On subsequent sessions, use the existing project entrypoint/Bootstrap, not a repeated installation. Report actual skill discovery/load/use and task checks only when observed.

Read `references/PROJECT_SETUP_HANDOFF.md` when producing a Codex or other agent handoff that includes local inspection or setup.
