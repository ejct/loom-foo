# Artifact-aware design QA

Quality assurance is proportional to the medium, user's required outcome and available tools. Avoid a global pass/fail score. **A written checklist is not evidence that a file passed it.**

## Every material deliverable

- **Content fidelity:** all required text, names, numbers, logos, source facts, languages and legal copy match the authoritative input. No invented data, testimonials, UI screenshots or unsupported claims.
- **Communication and craft:** intended audience and task are served; visual hierarchy, legibility, semantic imagery, composition and consistency make sense at actual use size.
- **Artifact integrity:** requested type really exists (editable, interactive, vector, print-ready, playable, etc.); files/links open; dimensions, export settings and source assets verified where possible.
- **Safety and ownership:** no unapproved publication, payment, licence bypass, use of third-party artwork as original, or undisclosed submission of user sources to outside services.
- **Evidence label:** differentiate `OBSERVED` (opened/rendered/tested), `STATIC_CHECK` (parsed/linted), `AUTHOR_CLAIM` (vendor docs), `UNVERIFIED` (not checked). A static check does not prove rendering or end-user quality.

## By medium

### Static graphic / poster / editorial layout
Inspect the actual render at full size and thumbnail. Check hierarchy, contrast, alignment, whitespace, cropping, legible exact copy, color consistency. For multi-page assets verify every relevant page, consistency and text flow. Match export dimensions and requested editability.

### Identity / logo / icon / type
Check vector/source availability, pixel appearance at realistic sizes, monochrome/reverse and background contexts when appropriate, clear space, visual consistency of sets, actual glyph support for user languages, font licensing. An automated SVG validator can flag technical defects but cannot prove distinctiveness, taste or trademark availability.

### Information / scientific figures
Ground all values, labels, units, ratios and scales in sources; verify transformations and graph geometry with the responsible numerical tool. Avoid image-model fabricated text or chart data. Check whether a five-second reading yields the intended takeaway. Preserve data provenance and editable chart definitions when requested.

### UX/UI and interactive prototypes
Use real browser/native preview when available; inspect target viewports, text overflow, focus/keyboard/screen-reader semantics where supported, responsive/adaptive behavior, empty/loading/error/permission/recovery states, interaction paths and feedback. A screenshot review cannot prove functionality or accessibility; label such claims accordingly.

### Print, packaging and physical graphics
Confirm printer/fabricator constraints rather than guessing. Check final trim size, bleed/safe areas, folding/dielines, source effective image resolution, embedded/outlined font strategy, overprint, spot/process color, color profiles/output intent, ink limits and requested PDF/X standard as relevant. PDF/X-4 can retain profiled RGB and transparency when the printer agrees; do not declare blanket 'CMYK only'. Without actual preflight or printer specification, report `PENDING_PRODUCTION_VERIFICATION`. Wayfinding also needs viewing distance, context, location and legibility checks.

### Motion / GIF / video
Inspect representative start/mid/end frames and transition timings; test playback, duration, resolution, safe areas, captions, font loading and audio sync where applicable. A storyboard/spritesheet is not proof of a playable output. Prefer deterministic seeded rendering for data or repeated assets.

### 3D / procedural
Inspect real views/renders and source geometry when available: scale, topology, normals, UV, materials, lighting, asset references, target poly limits and export settings. A beauty render alone does not certify production-ready mesh or editable scene.

## Reporting

Deliver actual file(s) or clearly scoped critique. State only material findings, corrections performed and **remaining specific checks**; use `CONCEPT`, `DRAFT`, `SOURCE_READY`, `PROTOTYPE`, `PRODUCTION_CANDIDATE`, `VERIFIED_OUTPUT` only as descriptive labels supported by corresponding evidence, never status decoration.
