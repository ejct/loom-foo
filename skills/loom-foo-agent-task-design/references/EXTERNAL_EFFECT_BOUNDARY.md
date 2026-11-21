# External-effect boundary — conditional execution guidance

Read when a task authorizes or proposes a consequential externally visible action, especially a message, publication, data disclosure, repository write, purchase, permission change, durable mutation or batch of cross-system actions. This is **task-level instruction**, not a host policy engine or proof of runtime enforcement. Use native permission/approval controls when available.

## Call-time scope check; not per-call reauthorization

Identify **existing authorization** first. A request to prepare a task authorizes drafting; whether it also includes *saving the prepared artifact* depends on the established project destination and intended downstream consumer, not the verb alone. A chat-only draft does not mandate a remote upload. Separate executor dispatch, publication, sharing and project acceptance remain separate effects. Do not carry forward a compiler's narrow preparation-only limit as a prohibition on a later, actually authorized executor. An authorized task may include ordinary delivery of its expected artifacts to a designated private or appropriately scoped project-native destination.

Compare actual effect against the approved bounds:
- actor and intended tool/operation; target object/record and account;
- destination/recipient, effective audience or visibility (including `PUBLIC`);
- bounded payload, attachments and permitted data classes; approved variation can include filenames/counts;
- side effect, durable state transition, batch membership and critical preconditions.

Immediately before a consequential call, compare the actual arguments, target/current state and expected effect **after** composition, templating, enrichment, fallback and retries. If the action remains in the authorized bounds, `PROCEED` — no second approval ritual. A material destination/recipient, audience, data-class, payload-scope, target or effect change **outside** those bounds requires new exact authorization. Missing, stale, conflicting, merely inferred, model-authored, or unverified transferred approval is not approval. Existing folder access, technical capability or a previous unrelated upload alone is not authorization.

If the current runtime cannot provide actual call arguments or enforce a check, label it `NOT_ENFORCED` and obey required native confirmation instead of asserting that the Task Brief supplies a tool interceptor. Do not repeat a denied effect through an alternate tool or silent retry. Do not add a model-authored gate to normal in-scope delivery merely because the tool itself is write-capable.

## Aggregate effect / cross-system disclosure

For a multi-step chain, assess the *combined* effect and information provenance of derived content:
- an authorized private read does not authorize public disclosure;
- an authorized write to a public destination does not authorize copying private read results into it;
- summarizing, paraphrasing, encoding or attaching private content does not remove source restrictions;
- multiple authorized writes can create an unapproved cumulative change or disclosure.

Unknown or lost provenance on consequential outbound content is an unresolved boundary, not proof that content is public. Use a verified public-only source or obtain required authorization; do not fabricate provenance tags.

Before the outbound step ask whether the end-to-end information flow and aggregate state transition are within the actual authorization, including source, data class, recipient, audience and destination. If so, proceed without repetitive owner confirmation. If not, produce a draft or request specific *additional* consent; perform no unauthorized external effect.

For a legitimate public-only payload, do not block because an unrelated private record was read elsewhere in the task; use provenance relevant to the actual outgoing content. A separately approved, accurately scoped disclosure may proceed after exact call-time recheck.

## Evidence and owner boundary

A Task Brief can encode required preflight but cannot install host call interception. For material claims, `loom-foo-change-review` owns open-ended defect analysis and `loom-foo-change-verification` owns exact property checks on the actual target route. A mocked adapter test establishes only its simulated route. Never label it proof that Gmail, GitHub, browser, Plugin Creator or another live connector applies these checks.
