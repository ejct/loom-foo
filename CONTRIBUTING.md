# Contributing to loom-foo

Thanks for helping improve the Agent Skills collection. You can suggest a change through a [GitHub Issue](https://github.com/ejct/loom-foo/issues) or open a pull request (PR). A separate issue is not required for a small, self-contained fix.

## Before you change anything

- Check the [README](README.md), [Ukrainian README](README.uk.md), and [skill inventory](SKILL_INVENTORY.json) to locate the relevant skill and its current contract.
- Keep one understandable concern per PR. For unrelated changes, use separate PRs.
- This is a **public source preview**, not a tagged marketplace release. A merged PR does not install or publish a plugin.
- **Never include** personal profiles, internal project details, private documents, credentials, private source/release identifiers, unlicensed assets, or confidential issue details. For sensitive concerns, consult [SECURITY.md](SECURITY.md) and [SUPPORT.md](SUPPORT.md); public Issues are not a secure reporting channel.

## Make a change

1. Work on a branch and submit a PR against `main`. Explain the problem, the affected behavior, and the intended result.
2. Change the smallest relevant files. Preserve the skill's purpose, selection boundaries, permissions, and supported host differences.
3. Update related references, tests, and documentation when the change affects them. If the change affects shared README content, keep both language versions aligned.
4. Run the applicable checks and report **which checks actually ran**. Document material risks, missing tests, and any behavior that remains unverified.
5. Wait for the PR to be reviewed and merged by a maintainer. GitHub Actions checks run on PRs; a green source check does not prove runtime discovery or skill effectiveness.

## Versioning and checks

| Change | Expected maintenance |
| --- | --- |
| Typo, broken link, documentation-only improvement | Update affected Markdown and links; normally no skill or bundle version bump |
| Skill behavior, activation, output, or authority contract | Update `SKILL.md`, conditional references if needed, relevant regression cases, the individual skill version, `SKILL_INVENTORY.json`, and `CHANGELOG.md` |
| Skill added, removed, or renamed | Update the inventory, affected discovery/neighboring-skill contracts, manifests/bundle version, tests, and changelog; flag compatibility effects |
| Bundle/package metadata | Reconcile all affected host manifests and package version; check source, privacy, license and links |
| Public distribution or runtime installation | **Separate maintainer-authorized operation** with its own exact artifact, permissions, validation and readback |

Use behavioral versioning: PATCH for compatible corrections; MINOR for new normal behavior; during the current `0.x` series, explicitly mark breaking changes and advance the MINOR version. Individual skill versions and bundle version are separate. See [CHANGELOG.md](CHANGELOG.md) for current source history.

For local checks, use Python 3.12 and install PyYAML 6.0.2 if it is not available:

```sh
python3 scripts/validate_distribution.py
python3 -m unittest discover -s tests -v
```

These are static/source and deterministic checks only. If claiming automatic skill selection, host-specific installation, or improved agent performance, provide actual host observations; do not infer them from CI.

## PR information

The [PR template](.github/PULL_REQUEST_TEMPLATE.md) covers scope, change class, relevant tests, risks, version updates, and delivery state. Use the parts relevant to the change; do not generate speculative test results or fill an administrative checklist merely to satisfy a format.

**Public contributions do not authorize a release**, private-plugin update, consumer migration, force push, or changes to another repository. Such actions have separate maintainer-controlled procedures.
