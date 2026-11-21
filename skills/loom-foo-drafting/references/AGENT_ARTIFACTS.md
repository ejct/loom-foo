# Drafting instructions for other agents · v0.1

**Boundary:** Formatting or localizing agent-facing instructions is drafting work only after the authorized task semantics have been established by their actual owner (e.g. `loom-foo-agent-task-design`, `loom-foo-specification-design`, repository instructions). This reference does not grant authority to create or modify project policies, executor roles, acceptance gates or tool permissions.

## Language fields and invariants

Preserve separately:
- language used to talk to the current user;
- language of the artifact being processed;
- language of instructions for the executor;
- target response/output language;
- original quoted identifiers, commands, filenames and schema fields.

There is no universal superiority claim for English agent prompts. Choose target instruction language based on explicit consumer/runtime constraints or actual evidence. Never translate shell commands, APIs, IDs or quoted technical strings as prose; avoid literal translation that changes their meaning.

## Semantic parity check for any rewrite/translation

Compare before/after for: actor/action, scope, positive and negative obligations, authorization and approval boundaries, tool use, file destinations, source provenance, stop conditions, acceptance criteria, protected data, privacy, timing, numerical limits, error behavior and requested response language. Terms like MUST, SHOULD, MAY, forbidden vs unsupported, draft vs execute, observed vs proposed must retain their force. If parity is uncertain, flag exact divergence rather than declaring the new draft equivalent.

## Examples (synthetic)

Incorrect change: original "Do not merge without approval" → translated "Merge after review". This removes the approval gate.

Correct equivalent: retain the explicit separate authorization requirement, or quote it unchanged if the target runtime requires that exact wording.

For a user-facing instruction summary, choose readable natural prose and cite the controlling spec when it is available; never invent policy authority from a retrieved document.
