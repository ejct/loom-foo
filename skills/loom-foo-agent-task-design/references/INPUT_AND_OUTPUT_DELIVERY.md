# Input/output delivery

Read for cross-runtime input delivery, staging or durable result materialization. Detailed transport rules originated in v0.1.6; apply **Routine Authorized Operations** using the actual task, project conventions, optional verified user-specific instructions and host-enforced restrictions; do not assume any provider-specific standing grant.

## Input delivery resolution

Source reachability is not the same as source delivery. For each material execution input not already trivially available in the target workspace, resolve the narrowest viable delivery path before finalizing runtime projection.

Prefer, in order when authorized and reliable:

1. **workspace-local** — the material already exists in the target workspace or runtime-native project context;
2. **target-retrievable** — the target runtime can retrieve the authoritative source directly through an established connector, tool, repository path or durable source;
3. **coordinator-stageable** — an authorized coordinator/compiler can retrieve the exact material and stage only the required surface;
4. **exact-slice-inline** — direct/staged retrieval is unavailable or disproportionate, but a small exact authoritative slice can be safely inlined with provenance;
5. **human-transfer-required** — no authorized machine path exists and a bounded exact slice is not sufficient.

This is an internal compilation control, not a mandatory visible taxonomy. Do not make the user manually download, attach, re-upload, copy or relay an artifact when an authorized reliable machine-readable path already exists. An explicit user preference for manual transfer may override this default.

Compiler/coordinator access and executor access are distinct capabilities. This skill determines and represents the delivery contract; actual retrieval, staging, worker creation and connector invocation belong to the coordinator/runtime. If proposed delivery depends on an unestablished runtime capability, preserve that uncertainty rather than assuming access.

Coordinator staging must preserve authority/disclosure boundaries. Ability to read a source does not itself authorize disclosure to a new executor/audience. For exact subject identity, use a proportionate immutable commit/ref, provider revision/version, artifact identity plus hash or exact bounded content; a mutable locator alone is insufficient for a frozen treatment. When isolated workers or experimental conditions have different visibility, express allowed/forbidden inputs per worker. Never stage treatment content into a control context merely because the coordinator has it.

## Consumer-ready output — semantic completeness before transport

Before deciding *where* to deliver, verify *what* the real next consumer must receive. Apply the Next-Step Readiness Check in `PD_TASK_CONSTRUCTION.md`: next actor/decision, minimum usable artifact/data and evidence, exact candidate or revision identity where material, negative findings/limits and authorized retrieval surface. A successful save or readable URL demonstrates location/access, **not** the semantic sufficiency of its contents for downstream action. Conversely, an adequate local report does not prove external delivery. Carry both through the Task Brief without a mandatory attachment manifest or redundant report.

For a root/worker boundary, request from each worker only the data the root actually needs to reconcile/integrate the accepted work. Worker-local PASS, an inaccessible file path, a summary that omits measurements needed for a decision, or a patch without material reproducibility evidence may leave the next action blocked. Specify a concise truthful **return status plus the missing/blocked input** if real capability or authority prevents durable delivery; do not fabricate the output or invent approval. The user should not become a manual courier when an authorized reliable machine path exists.

## Required downstream delivery is terminal acceptance

Resolve this **before authoring the brief**, not after the executor returns. Recover verified applicable standing owner/project instructions and the current controlling storage/authority convention, including explicit current overrides. Use the canonical project folder/repository/knowledge surface with an exact stable locator; verify ownership, effective audience and permitted data class. Do not create a parallel scratch folder because the canonical destination was not searched. If no authoritative location is established, resolve it under project conventions or state the genuine unresolved destination; never guess a private or shared audience. A private grant applies only to the bounded task and destination; do not broaden it into universal provider permission or bypass host denials.

Identify all material authorized downstream consumers and the actual next operations. If even one required consumer cannot retrieve executor-local output, local-only completion is insufficient. Separate input reachability, required result materialization, semantic sufficiency and consumer retrieval. For a cross-runtime handoff, the executable brief must carry:

- The exact material inputs, their identities, and a verified feasible retrieval or staging route (or explicitly unresolved capability).
- The minimum output inventory and exact destination for each artifact class, with existing source authority, allowed data/audience and bounded write permissions.
- An available executor transport or authorized coordinator fallback with responsibility assigned explicitly; no assumption that runtimes share connectors or a filesystem.
- Required write/destination/audience checks, proportional readback and exact identity/hash where material, plus stable return references and any unverified consumer access.

**Counterexample gate:** assume implementation and all domain tests pass, but the executor returns only inaccessible local paths. If a required consumer is stranded, the brief is not `TASK_READY`. Put actual delivery into the delegated acceptance and stop criteria, not merely a return suggestion or coordinator-only note. Require the executor to continue within its authorized span through delivery and verification; do not end at a local commit, test report or artifact creation. For a coordinator-owned transfer, the coordinator must own and complete its part before declaring the overall handoff complete; the worker may report its bounded implementation complete without implying the overall delivery is done.

Terminal status: `COMPLETE` requires both the delegated substantive outcome and its required delivery postconditions; preserve separate implementation/verification/delivery statuses. If delivery cannot proceed after reasonable authorized alternatives (host denial, unavailable write/transport, unresolved authority or destination), preserve completed artifacts and report `DELIVERY_BLOCKED` with exact missing property, retrievable evidence if available, and the smallest resume action. Do not restart implementation solely to deliver existing artifacts. Remote save/readback and actual target-consumer retrieval remain distinct; where retrieval cannot be exercised, mark it unverified and do not claim that property passed. If actual consumer retrieval is a material acceptance condition, keep the handoff open; a genuine exhausted verification blocker yields `DELIVERY_BLOCKED`, not `COMPLETE`. An explicit no-write, new audience, or local-only/chat-only outcome must not be turned into a remote-write requirement. These are conditional acceptance clauses, not a universal manifest or a mandatory extra task.

## Output materialization resolution

Input delivery and output deliverability are symmetric concerns. For each output, ask whether another agent, chat, reviewer, workflow or later execution must consume it outside the producing runtime. If no downstream consumer exists, local-only may suffice. If downstream consumption is required, resolve a **project-authorized** durable path before claiming delivery complete.

Use the narrowest applicable internal disposition:

- **local-ephemeral** — no downstream consumer requires the artifact;
- **workspace-durable** — artifact exists on a shared workspace surface accessible to its next consumer;
- **repository-owned** — artifact belongs to repository state, to be written there when authorized;
- **project-knowledge** — artifact belongs to the project's native knowledge surface;
- **delivery-pending-authority** — a genuinely new external action, audience, disclosure class or sharing boundary is not covered by the owner's instructions or project rules; **ordinary project-native delivery within an existing authorized task is not reauthorized per file or per preparation step**;
- **delivery-blocked** — downstream-consumable durable output is required but the host denies the action or no reliable authorized machine path is available.

A local path is not sufficient handoff identity if the intended consumer cannot resolve it. Prefer, when authorized and reliable:

`natural project-native owner → direct executor delivery → coordinator materialization → bounded machine staging → human transfer only if genuinely unavoidable or explicitly preferred`.

If a project already has an artifact-delivery, repository-boundary, documentation-ownership or equivalent profile, use that as controlling transport policy rather than inventing a competing Drive/GitHub mapping.

**Routine authorized project delivery (provider-neutral).** An explicit task and its established project conventions may cover necessary in-scope read/create/edit/save to the intended private or appropriately scoped project destination. When the durable output has a known downstream consumer and destination, an ordinary private save can be part of *preparing* the artifact, without a new per-file approval. Equally, a chat-only draft, optional scratch file, accessible folder, connected account or ambiguous "my storage" claim does not automatically authorize external writes. Check the exact destination, effective inherited sharing/audience, source/data sensitivity, task scope and connector's actual write capability. Ordinary filename/count/hash changes within the same authorized output class require no new model-created approval; material audience/disclosure, destructive scope or separate external effects do. Respect real native confirmations, OAuth/ACL errors and host denials. For a read-only connector (e.g. a Dropbox interface without write actions), do not pretend to save: offer a suitable accessible result/fallback. No personal profile is required for task-based authorization, and no provider-specific universal standing permission is asserted.

Distinguish producing bytes, materializing them externally, and accepting/canonicalizing them. Authorization to privately deliver a report is not authority for merge, public publication, release, permission changes or acceptance. Capability to write to other systems does not create unrelated authority. When external materialization truly lacks authorization, preserve local output and intended destination and report the precise missing condition, without requiring the user to act as a manual courier.

**Readback content sufficiency (P3).** A successful provider write, resolved path, byte-identical copy or remote re-read establishes that particular storage property; an accurately copied but **incomplete** artifact may still be unusable by its intended consumer. Where downstream acceptance depends on material sections, source identities, acceptance criteria or machine fields, check those properties against the saved/read-back body and report `SAVED_CONTENT_INCOMPLETE` if absent. If the content's semantic sufficiency was not checked, claim storage/retrievability only. No readback ceremony for ordinary chat output or duplicate check where current evidence already covers the property.

**Closure evidence is property-specific.** A generated Task Brief or local file is not proof of Drive delivery. Before reporting a required project-native result as delivered, inspect the actual write result and stable provider ID; check the destination folder and visibility; perform a proportional remote readback, including exact-byte hash where needed. Target-runtime access (for example Codex retrieving a Drive file) is a separate property: verify it if feasible, otherwise mark `NOT_VERIFIED`. A static check that the brief *mentions* Drive is not delivery verification. Report partial/mismatched/unavailable remote results precisely rather than claiming success.

When exact output identity matters, preserve stable provider ID/revision, commit/ref or hash. For experimental/audit raw outputs, preserve the raw artifact before delivery; delivery must not silently rewrite or contaminate raw data, and derived summaries are separate.
