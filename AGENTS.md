# loom-foo — repository development instructions

**Status: PRIVATE generic-only distribution preparation, not a public release.**

This repository distributes portable **loom-foo Agent Skills**. Core is separately distributed at `ejct/foo-loom`; private development source of both projects is `ejct/LoomDev`.

## Source, privacy and publication boundaries

- Current source import: `ejct/LoomDev@f2e0fe4e02e848ea06ce3e72028a7c58c5959f5b`. Preserve skill IDs/versions and exact provenance of subsequent changes.
- Never import `loom-foo/private/`, `reconciliation/`, `legacy-2026-11-01/`, owner-specific files, private incident history, unpublished user details or a mixed private plugin archive.
- Source files and passing CI do not equal a semantic privacy/legal approval, a public release, an installed plugin, or host runtime discovery.
- No repository visibility change, release/tag, marketplace publication, consumer-pin migration, update to installed private plugin or owner-approval index may be inferred from repo setup or CI success.
- Never fabricate `approved_by_owner: true` or self-approve file hashes. A release index must be separately reviewed and approved by the owner, tied to the exact final source bytes. Keep the review/approval record outside release artifacts.
- The original brand PNGs are not verified as recovered. Do not invent replacements and call them identical.

## Execution

Run `python3 scripts/validate_distribution.py` and `python3 -m unittest discover -s tests -v` after changes. Build a public package only from exact reviewed source through `scripts/build_public_release.py` with a real approved SHA-256 allowlist and current manifests/assets.

Use the selected skill for a real task when relevant; local source does not mandate Core, extra agent roles or paid/remote services. Do not treat CI checks as end-to-end skill routing evidence.
