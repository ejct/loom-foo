# Project Integration v0.5.0 — bounded expected outcomes (NOT runtime routing proof)

| Case | Input evidence | Expected behavior |
| --- | --- | --- |
| P1 | Multi-session Codex project; asks whether to adopt Core | Project Integration assesses existing setup and usefulness; proposes only if justified |
| P2 | Explicitly connect repository to foo-loom | Inspect immutable source, existing instructions, project write authorization before setup |
| P3 | Multi-session continuation with verified exact lock and complete Bootstrap | `EXISTING_CORE`; no reinstall/upgrade |
| P4 | Local workspace unavailable to coordinator | `LOCAL_INSPECTION_NEEDED`; same-task read-only preflight, not speculative install |
| P5 | Lock exists, Bootstrap is missing after interruption | `PARTIAL_SETUP`; bounded preview; no unconditional installer rerun |
| P6 | Managed AGENTS block differs from expected saved hash | `PARTIAL_SETUP` conflict; preserve edits, do not overwrite |
| P7 | Old `.loomloom/loomloom.lock` conflicts with proposed modern pin | Conflict/authority boundary; no silent migration |
| P8 | Exact source + file permissions + clean preview approved | `SETUP_AUTHORIZED`; readback and original-task continuation required |
| P9 | Partial setup authorized for repair only, feature not complete | Verify repair separately; continue feature, do not close work early |
| P10 | Source missing but workspace inspectable | `SETUP_PROPOSED` or `PARTIAL_SETUP`; no latest-main substitution |
| N1 | Fix a CSS button, no durable infrastructure need | Task Design owns; `NO_SETUP` as needed, no ceremony |
| N2 | What does foo-loom mean? | Concept explanation only, not setup |
| N3 | Platform disables Project Integration Skill | Host-level behavior unknown; do not implement fallback within Task Design |
| N4 | Feature-only write authorization, no managed-file approval | No Core installation; safe primary task can proceed |
| N5 | Special agent profiles copied, host spawn unverified | `STAGED_FILES_ONLY`, never a runtime spawn PASS |
| N6 | Source is private and later public export considered | Separate distribution/privacy audit; no owner-private leakage |

Cases are intended behavior fixtures only. They do not prove runtime routing or actual project setup.
