# Package and runtime delivery contract

## Default package

```
skill-id/
  SKILL.md
  references/          # optional; load only when needed
  scripts/             # optional; deterministic/reusable
  assets/              # optional; templates/icons
  agents/openai.yaml   # optional; check target-specific fields
```

Keep the startup `description` small, concrete, and distinct from adjacent skills. Full `SKILL.md` loads after activation. Long references should be accessed only for the specific question.

## Behavioral Semantic Versioning (loom-foo)

Version the **skill** and the **bundle** independently. Version expresses the expected impact on agent activation, responsibility, decision procedure, output and authority—not the number of edits, affected lines or releases. Classify the strongest intended behavior change:

| Class | Meaning | Examples |
| --- | --- | --- |
| PATCH (`x.y.Z`) | Non-contract repair or clarification, preserving intended normal behavior | Broken link, typographic fix, correcting a local defect to match an accepted contract |
| MINOR (`x.Y.0`) | Compatible meaningful behavior expansion/change | New skill, additional challenge behavior, revised default workflow, new optional output |
| MAJOR (`X.0.0`) | Breaking established contract once 1.x is adopted | Removed/renamed skill, incompatible output, reassigned authority or breaking trigger change |

`0.x` is development-phase SemVer: use the next **MINOR** for a breaking change and mark it **BREAKING** explicitly in the release note. Do not pretend the change is backward compatible. This does not promise that all 0.x consumers will be compatible; pin exact subjects where necessary.

- For a bundle, take the **highest impact** of all changes in one authorized release: new skills and semantic interaction/routing changes can require MINOR even if no existing skill file was edited. One bundle bump per release, not one per changed skill.
- For an individual skill, bump only its own changed contract; do not synchronize all skill versions with the bundle. A bundled dependency/copy can be retained unchanged. A material semantic change may warrant MINOR even if only one sentence changed.
- Keep the version in YAML metadata, manifests and optional compatibility overlay synchronized; preserve existing public identity, default prompts, assets, bindings, privacy and audience.
- A concise release note is sufficient: `version; ADDED/CHANGED/FIXED; BREAKING if applicable; affected skill versions; observed installation and discovery status`. Do not add registries, release committees, status promotion stages or a new skill.
- Never rewrite earlier published versions. Do not force 1.0.0 by elapsed time or release count. Historical Git/source revisions, bundle release_id and host runtime loaded copy are independently identified.
- If a consumer pins exact versions or a real incompatible integration is known, keep that boundary; do not silently overwrite it. Release readback establishes saved bytes, not automatic routing or field utility.

## Use-first delivery

After bounded technical integrity/security/authority checks, publish an already-authorized update **in the same task episode** and read it back. Observe behavior on real work and revise from actual defects. Do not require separate evaluation campaigns, blind holdout tests, two clean audit passes, or repeated owner approvals as ordinary preconditions. Stronger preflight remains warranted when a consequential change could destroy data, leak secrets, break accepted downstream contracts or misrepresent irreversible external actions.

## Separate identities

- **Source**: exact upstream file or Git commit, plus selected functional version.
- **Artifact**: specific packaged bytes, hash and file inventory.
- **Install**: package copied to a particular host-native location or plugin release.
- **Discovery**: host lists the skill as selectable/available.
- **Routing**: intended task caused it to load; unrelated task did not.
- **Behavior**: task output obeyed its contract.
- **Utility**: beneficial end-user outcome, if observed.

Do not treat successive layers as equivalent.

## Codex

Repository-local `.agents/skills/<skill-id>/SKILL.md` or supported user-level skill locations. Confirm the actual runtime setup and detection rules in current official docs. Protect previously pinned consumers; refuse silent overwrites. An existing project-native installer can copy one portable skill into the consumer path and should refuse silently replacing different bytes; verify the actual installer contract before use.

## ChatGPT

Skill discovery in Chat/Work may be provided by a connected skill-bearing plugin. A source Markdown file or published package is insufficient. Confirm connected plugin, skill inventory, version when exposed, and actual routing. Public or team sharing is not implicit.

## Compatibility and authority

A standalone skill request does not automatically authorize a new plugin, upload, deployment, public release, changes to repository history, or canonical authority transfer. Request/use only the missing approval for the specific external effect. Do not create multiple redundant registries or invent a universal skill router.

Source: https://learn.chatgpt.com/docs/build-skills

## Authoring overlap / platform creator

When available, use the built-in `skill-creator` for scaffolding, examples and package generation instead of shadow-copying it. Keep the skill engineering contract responsible for whether the skill should exist, how it fits the portfolio, targeted regression and final runtime-scoped evidence. The creator's existence does not prove it is callable from this conversation.

A change made to local package bytes without an installed ChatGPT plugin or Codex project does not change either runtime's active skills.
