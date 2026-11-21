# Discipline and artifact selection

Use when a request spans disciplines, is ambiguous, or demands a particular production pipeline. Treat disciplines as *composable competencies*, not rigid silos or fixed workflow steps.

## Three independent axes

1. **Intent / task mode:** communicate, identify, explain, persuade, guide, enable interaction, evoke; CREATE / REDESIGN / CRITIQUE / SPECIFY / PRODUCTION_CHECK.
2. **Discipline:** what knowledge is needed to make a sound decision?
3. **Medium / artifact contract:** what must actually exist and what must remain editable, interactive, measurable, publishable or printable?

| Competency | Typical problems | Critical handoff/verification |
|---|---|---|
| Product, service and UX | Value, audience, journey, information architecture, user flows, research-led decisions | Scope and user goals; error/empty/loading/edge cases; research evidence |
| UI, interaction, HMI, spatial UX | Controls, navigation, responsive and adaptive states, behavior, feedback | Working interactions vs screenshot; keyboard/accessibility; system constraints |
| Graphic communication, posters, campaign | Attention, concept, hierarchy, memorability across formats | Required copy correct; actual size/crop and channels; coherent art direction |
| Brand, identity, logo | Distinctiveness, recognition, brand system, marks, lockups | Optical sizes, mono/reverse, font/glyph rights, SVG variants; no unsupported uniqueness claim |
| Typography, lettering, type design | Reading, visual voice, glyph construction, alignment, systems | Exact copy/diacritics, fonts and licensing, legibility; type design needs font-source formats |
| Editorial, books, reports, presentation | Long-form reading, information hierarchy, pacing, narrative structure | Content completeness, pages/spreads, grids, typographic density, editing source |
| Infographics, data storytelling, scientific diagram | Explain, prove, compare, map or show process | Evidence and exact numbers; correct scales; labels and provenance |
| Illustration, iconography, comics | Style, narrative, metaphors, consistent sets and pictograms | Consistent visual grammar, size/optical tests, vector/raster needs |
| Photography, retouch, collage | Image truth, composition, exposure, retouch quality, manipulation | Source provenance, no inadvertent object/fact fabrication, format and export |
| Motion, kinetic type, video | Timing, hierarchy across frames, transitions, pacing, narrative | Keyframes, playback, audio sync if needed, codec/duration/export |
| 3D, CGI, procedural art | Geometry, materials, camera, lighting, parametrization | Actual scene/source when required, mesh QA and target export |
| Packaging, print, environmental graphic / wayfinding | Physical scale, substrate, legibility, technical constraints and context | Printer/fabricator spec, dieline, trim/bleed, color/ICC, spatial viewing conditions |

## Choose the smallest sufficient artifact route

| Requested outcome | Suitable route | Do NOT substitute |
|---|---|---|
| Visual reference / concept art | Image generation, raster/vector drawing | An implementation/prototype claim |
| Editable logo, icon set | SVG/vector source and renders | Raster logo pretending to be vector |
| Editable product UI | Figma or equivalent native design file; or clearly accepted code-based editable representation | Screenshot or HTML mock unless user accepts it |
| Working UI / prototype | Actual executable interaction plus visual rendering | A design specification or dead mock |
| Precise infographic | Deterministic data/text/chart layer plus designed layout | Image model's invented numbers or fake chart |
| Presentation / publication | Source slides/layout document plus requested export | Beautiful cover without editable content |
| Motion / animation | Timeline or code source plus playable GIF/video if required | Static storyboard labeled as video |
| 3D asset | Real scene/mesh, materials/exports as requested | Render alone when scene editability is required |
| Print / packaging | Printer-appropriate production files and actual preflight | Ordinary PDF labeled production-ready |

When user-supplied text, logos, fonts, imagery, numbers or layout are authoritative, preserve them. When style or visual reference is asked for, inspect it and transfer the relevant creative mechanisms without copying third-party work.

## Independent specialist primary owners (when installed)

| Primary requested outcome | Prefer |
| --- | --- |
| Cross-disciplinary art direction, integrated end-to-end visual work | `loom-foo-design` |
| Type roles, font pairing, typesetting, glyphs | `loom-foo-typography` |
| Poster, campaign, editorial graphic, communication layout | `loom-foo-graphic-design` |
| Infographic, explanatory diagram, information topology | `loom-foo-information-design` |
| UI glyphs, app icons, pictogram systems | `loom-foo-icon-design` |
| UX flows, user-facing behavior, IA, interaction model | `loom-foo-experience-design` |
| Cross-platform token/component architecture and system evolution | `loom-foo-design-systems` |
| Brand mark and coherent identity system | `loom-foo-identity-design` |
| Standalone visual/interaction critique, audit, comparison | `loom-foo-design-review` |

These are **entrypoints**, not a required hierarchy. The requested principal artifact and user action decide the owner. A long multidisciplinary task can apply multiple methods without pretending separate skills automatically loaded.

## Adjacent ownership

- Pure numeric analysis and chart accuracy belong to Data specialists; design contributes communication, hierarchy, accessible visual choices and layout.
- Skill, application or system architecture belongs to relevant loom-foo architecture/skill specialists.
- Named Figma, presentation, document or image-editing tool workflows obey their native host/tool skill prerequisites.
- If no suitable tool is available, provide the best supported artifact, explicitly state gaps, and do not claim production completion.
