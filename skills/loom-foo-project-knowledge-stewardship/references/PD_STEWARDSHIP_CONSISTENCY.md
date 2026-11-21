# project-knowledge-stewardship — detailed conditional method (PD_STEWARDSHIP_CONSISTENCY.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 6. Preserve supersession and history

Prefer prospective supersession:
- keep old artifact inspectable;
- mark/link supersession when the project convention supports it;
- make the new current source explicit;
- preserve prior run/evidence references;
- do not retroactively alter historical claims/evidence to match current truth.

Follow project-native terminology and status conventions. Do not impose a universal status enum.

Read `references/AUTHORITY_AND_SUPERSESSION.md` when authority/supersession is non-trivial.
## 7. Distinguish stale derived state from authority conflict

If sources differ:
- apply explicit project precedence;
- do not choose by filename, recency, or location;
- if one authoritative source is clear and another surface is derived/stale, reconcile the derived surface;
- if controlling authority itself is contradictory, return `AUTHORITY_CONFLICT` and identify the smallest owner decision needed.

Do not adjudicate product/architecture truth inside this skill.
## 8. Apply authorized durable changes proportionately

For a small transition, sufficient work may be:
- link/mark an older artifact as superseded;
- point one current index to the new source;
- update compact PROJECT_STATE if continuation materially changed;
- verify material links/IDs;
- emit a compact delta.

For a larger transition, reconcile only the bounded affected current/index/status/registry surfaces.

No ongoing background gardening.
