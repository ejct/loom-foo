# Source attribution and third-party license inventory

**Status:** attribution inventory for the private `loom-foo` 0.41.1 generic candidate. This is not a comprehensive legal opinion or a clearance of future binaries.

## Project source license

The repository's [`LICENSE`](LICENSE) is MIT and **retains the historical copyright notice**:

> Copyright (c) 2026 LoomLoom contributors

That notice was already present in the older `LoomLoom` and separate `foo-loom` sources. It is not silently replaced by a single maintainer name or by the GitHub account handle. The MIT notice and permission text must accompany copies/substantial portions of covered source. A prospective new copyright line should only be added when its actual rights holder and scope are confirmed.

## Lucide / Feather icon licenses — conditional, not bundled

The private development source contains the Lucide ISC license text and associated Feather MIT attribution. The current generic distribution source contains **no checked-in vector/raster icon images or fonts**. This file therefore does **not** claim that Lucide or Feather icon files are bundled, nor that their license text can be omitted if such files are added later.

Before distributing any copied/derived Lucide or Feather graphics, identify the exact included artwork and carry the applicable original copyright notices and license permissions in the release artifact.

Upstream license reference: https://lucide.dev/license

## Tools and external references

Some optional source validators import third-party Python modules such as PyYAML, but those dependencies are **not vendored as source files in this generic candidate**. Users and host environments remain responsible for obtaining and licensing external dependencies under their own terms.

Skills also link to outside projects and public publications as methodological references. Merely linking to them does not redistribute their code or confer a right to republish their examples, diagrams, text, fonts or assets. If material is copied into a later build, its provenance/license must be reviewed separately.

## Original project brand assets — unresolved

The manifest references `assets/loom-foo-mark-v3.png` as a required logo and composer icon; the original v2/v3 image binaries have not been recovered into this generic source. The release builder must reject the incomplete package. Before adding the assets, verify their actual file hashes, author/origin and redistribution rights. Do not classify a generated replacement as an original.

## Final attribution check before release

Confirm all included source files and their ownership/provenance, all actual bundled assets and copied third-party text, MIT notice continuity, the exact final release-file inventory, public publisher identity, and private reporting routes. **No owner-approved public release is implied by this inventory.**
