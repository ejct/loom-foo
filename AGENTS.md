# loom-foo — distribution source policy

**Status: private, unapproved release candidate.**

This repository contains the portable generic Agent Skills distribution. Optional Core integration is a separate product.

## Privacy and authority

- Do not import private owner profiles, internal project records, historical incident logs, unpublished user details, private repository identifiers or private plugin release IDs.
- Keep source provenance and any private approval/review evidence in the protected development environment, not in public-bound package files.
- Existing Git history may contain private development provenance: **never change this repository to PUBLIC as-is**. Publication requires a separately inspected clean-history export and an explicit owner decision.
- Do not infer publication approval from source presence, CI, tests or a generated `approved_by_owner` flag. The real file-hash review/approval record must be independently authorized.
- Do not import previously installed project artwork into the generic distribution. Icons are deferred until a separate approved pass; do not invent icon files or claim brand asset parity.
- Do not install/update an existing private plugin or migrate pinned consumers merely by preparing this repository.

## Validation

```sh
python3 scripts/validate_distribution.py
python3 -m unittest discover -s tests -v
```

The fail-closed `scripts/build_public_release.py` packages **only** exact reviewed source bytes. Native public submission also requires separately reviewed verified logo and composer-icon files. Static validation is not proof of runtime discovery, selection or output quality.
