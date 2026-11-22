# Partial setup, drift and safe recovery

Read only when a project may have an interrupted/partial foo-loom installation, inconsistent managed files, modified managed blocks or an explicit repair request. This is a **method for project-local observation and handoff**, not an installer or authority to write.

## Observe independently; never infer the missing parts

For the exact authorized workspace, record whether the following are present, readable and internally consistent:

1. Existing `AGENTS.md` (including any known managed block and unrelated instructions); check whether a managed block is modified, duplicated, truncated or ambiguous. Respect nested instructions where relevant.
2. `.foo-loom/foo-loom.lock`: exact source identity, pin and any recorded managed-file hashes; verify against actual content where possible.
3. Historical `.loomloom/loomloom.lock`: whether a legacy pin or migration decision already governs this project. Never overwrite it or silently translate it to a new pin.
4. `.agents/skills/foo-loom-bootstrap/` and other explicitly managed paths: actual files, version identity, symlinks and expected contents, not merely directory existence.
5. Approved project policies and permissions: copied policy files do not mean adopted authority; historical owner edits and consumer pins remain authoritative unless changed explicitly.
6. Installer and runtime capability evidence: actual interface/flags, immutable source and what local readback can prove. Do not invent `--dry-run`, rollback support, Codex spawn or runtime activation.

If the environment is inaccessible, do not assign observed states from guesses. Use `LOCAL_INSPECTION_NEEDED` and transfer these checks as read-only preflight to the same task.

## Branch after observation

| Evidence | Disposition | Next step |
| --- | --- | --- |
| Complete exact lock, consistent Bootstrap, accepted managed block | `EXISTING_CORE` | Preserve pin; use existing Bootstrap; no install/upgrade |
| No Core material, real gap, no exact source or write approval | `SETUP_PROPOSED` | Specify exact proposed files/source and needed approval |
| Lock present but Bootstrap missing, interrupted managed update or ambiguous partial installation | `PARTIAL_SETUP` | Compare expected vs observed, preview smallest repair; do not rerun installer blindly |
| Old pin conflicts with proposed new source, modified managed block, unexpected symlink or concurrent changes | `PARTIAL_SETUP` (conflict) | Stop writes; preserve local changes; ask narrow decision; continue unrelated safe primary work |
| Exact approved immutable source, bounded managed-path authorization and clean preview | `SETUP_AUTHORIZED` | Verified installer applies scoped changes; read back lock/Bootstrap/AGENTS; resume original task |
| Workspace not visible to coordinator | `LOCAL_INSPECTION_NEEDED` | Attach preflight; executor classifies locally before any optional setup |

These dispositions are current findings, not persistent switches. Do not promote `PARTIAL_SETUP` to `EXISTING_CORE` or `SETUP_AUTHORIZED` without direct evidence.

## Repair plan: minimum reversible effect

1. Identify exact approved Core subject and expected managed file set. If uncertain, stop setup writes; do not select latest `main` or an arbitrary archive.
2. Capture only the relevant pre-change contents/hashes and a clean diff for the files authorized to change. Protect symlinks, path traversal, unexpected files, user-owned material and existing managed-block edits.
3. Distinguish safe missing-file restoration from conflicting overwritten content. **Repair only when the actual project-scoped authorization covers the affected paths**, source and action. Ordinary feature permission does not authorize Core writes.
4. Use the real installer or exact supported project mechanism; preview in a safe copy when no dry-run exists, without claiming tool capabilities that were not observed. Do not manually reconstruct undocumented installer state.
5. Check affected paths after each authorized operation: exact lock and source pin; Bootstrap identity; `AGENTS.md` managed block and unrelated text; accepted policy choices. Do not assert transactionality or automatic rollback. If something fails, preserve observed state and provide a narrow recovery decision; restore only known managed data when safe and authorized.
6. Resume the original project goal where possible. Record separately `SETUP/REPAIR VERIFIED`, `PRIMARY TASK COMPLETE/INCOMPLETE` and unobserved runtime levels.

## Reporting

A useful recovery note is short: **observed parts**, exact pin or uncertainty, **conflict/missing element**, smallest safe next action with permission boundary, and **primary-task continuation**. Do not enumerate unrelated project files, create a global registry or force a separate setup ceremony before useful work.
