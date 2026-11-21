# Trigger-to-oracle matrix (conditional reference)

The event trigger is a **cue**, not itself proof of error. Decide based on the exact claim and direct evidence; skip harmless cases.

| Event | Candidate oracle | Avoid claiming |
|---|---|---|
| `COMPLETION_CLAIM` local file | direct file readback, size/hash, expected exact location | success on remote service, correct content, agent skill activation |
| `COMPLETION_CLAIM` external mutation | authenticated tool success + readback when needed | a queued/draft state is a completed external effect |
| `SOURCE_COVERAGE` | page count/range, bytes retrieved versus model-visible emitted intervals, source identity, explicit truncation status | full source was read from one excerpt |
| `CONTRADICTION` | original user requirement and actual tool error/output | green status despite failed operation |
| `CHECKABLE_FACT` | authoritative dated source and scope | source snippet proves a different/stronger claim |
| `RISKY_PRECONDITION` | permissions plus source-specific preconditions | verification grants action authority |
| `GOAL_DRIFT` | compare accepted goal with short, feasible alternative | verification is necessarily the main deliverable |

## Local artifact probe

`scripts/check_local_artifact.py --root ROOT --path FILE [--sha256 EXPECTED]`:
- Performs **read-only** local filesystem existence, regular-file, size and optional SHA-256 comparison within ROOT.
- Exit 0: observed matching local artifact; exit 2: absent/mismatch/unsupported scope; exit 1: malformed CLI input.
- Outputs JSON with `status`, file size and digest when available; an output path that is outside `ROOT` (including via symlink) is rejected.
- This checks exactly the file's current local bytes, **not** that a model read them, that the intended content is correct, that an external API mutation succeeded or that a plugin was installed.
- Raw file paths and hashes may be private; do not publish logs outside their authorized context.
