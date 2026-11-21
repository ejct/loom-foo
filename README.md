# loom-foo

Reusable Agent Skills for design, research, product development, planning, writing, verification and agent workflows.

Use the relevant skill for the work at hand. Skills are independently versioned, support progressive disclosure and remain usable without the optional [foo-loom](https://github.com/ejct/foo-loom) project infrastructure.

## Source and distribution status

**Private release-preparation repository — not published.** This repository is being populated from a reviewed, generic-only projection of private development source `ejct/LoomDev`. Its content is not automatically approved for a public audience. No release tag, marketplace listing or runtime installation is implied.

- **Development authority:** private `ejct/LoomDev`, for Core and Skills source.
- **Distribution:** `ejct/loom-foo` for portable skills; `ejct/foo-loom` independently for optional Core infrastructure.
- **Baseline:** `loom-foo` 0.40.0 / 40 Skill IDs; individual Skills retain their own versions.
- **Known gap:** original brand assets `assets/loom-foo-mark-v2.png` and `assets/loom-foo-mark-v3.png` have not yet been verified as recovered.
- **Public release:** requires semantic privacy/license review, exact approved file hashes, verified platform assets, and explicit publication authorization.

## Structure

`skills/<skill-id>/SKILL.md` defines a portable skill; `references/`, `scripts/`, `agents/`, and `assets/` belong to individual skills where needed. Native manifests at the repository root describe supported hosts.

`scripts/build_public_release.py` is the fail-closed packager; it must never treat the private development source or a plugin's private installed archive as approved public input.

The current package must not contain private owner profiles, private development reconciliation material, historical incident transcripts or legacy development archives.

## Usage and validation

For a compatible agent host, select the skill that fits the task and follow its `SKILL.md`; installation/discovery behavior varies by host. Source presence and CI checks alone do not prove automatic routing or runtime behavior.

Publication and support details will be finalized before a public release.

[MIT License](LICENSE) · [Release status](RELEASE_STATUS.md)
