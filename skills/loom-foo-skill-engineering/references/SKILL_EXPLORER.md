# Skill Explorer

Use this procedure only when the user wants to find, compare, or choose an existing skill for a task. It is a discovery aid, not a global router or installer.

## Resolve the catalog source

Use the exact current package manifest, installed skill list, or runtime catalog visible to this execution. Prefer the installed package when it can be identified. If only a partial runtime list is visible, describe it as partial. Do not create or maintain a second skill database.

Report a package version, release ID, or source hash only when it was actually read from an authoritative manifest or release record. Otherwise say that the runtime-visible catalog's exact version is unverified.

## Find and compare candidates

1. Match the user's goal to each candidate's trigger, primary output, and explicit exclusions.
2. Compare only the closest relevant candidates. Read their exact `SKILL.md` files and the smallest relevant reference sections when available.
3. Check runtime fit and required sources/tools. Mark unsupported capabilities `UNAVAILABLE`; do not invent a substitute or a skill that is absent from the catalog.
4. If no existing skill fits, say so. Route a question about whether a reusable skill should be created to `ASSESS`; do not recommend a new skill merely to make the catalog appear complete.

## Return

Give the best fit or small set of fits, why each applies, what it produces, important limits, runtime availability, and relevant catalog identity. Explain differences when the user asked to compare. End with a short prompt the user can use to request the selected workflow.

A saved export, Git tree, prior release, or starter prompt is not current runtime availability. Report only skills present in the exact catalog inspected. Choosing a skill does not prove that the runtime loaded or routed to it; claim activation only with direct execution evidence. This procedure does not change skill descriptions, automatic routing, installation, permissions, or project files.
