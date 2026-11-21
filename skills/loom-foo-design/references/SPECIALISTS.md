# External specialist candidates — evidence catalog

**As of 2026-11-12. None of these candidate packages is bundled, installed or verified as runnable by this skill.** URLs are evidence and discovery pointers, not installation instructions or grants of access. Verify the current upstream revision, license (including assets and fonts), security of scripts and dependencies, costs and actual target runtime before using. Reuse design methods selectively; never copy external executable code or reference assets without a scoped review.

| Specialist/source | Applicable task | Mechanism worth considering | Limits / status |
|---|---|---|---|
| `anthropics/skills/skills/canvas-design` — https://github.com/anthropics/skills/tree/main/skills/canvas-design | Posters, artistic graphics | Separate visual philosophy and canvas composition | Minimal-text/style bias; `REFERENCE_ONLY` |
| `fatihaydost/brand-identity-skill` — https://github.com/fatihaydost/brand-identity-skill | Identity systems | Bundled logo/type/color decisions, script-based audits of contrast/glyph/license and site preview | Heavy runtime, Python/Chromium/fonts/network, author-reported high cost; `CANDIDATE` |
| `kaankiziltug/logo-design-skill` — https://github.com/kaankiziltug/logo-design-skill | Logos/marks | SVG audit, 16/32 px render and test sheets, monochrome and lockups | Library trademarks not reusable as new marks; author evals not comparative proof; `CANDIDATE` |
| `mkottaichamy/UX_Skills/agent-skills/illustration` — https://github.com/mkottaichamy/UX_Skills/tree/main/agent-skills/illustration | Consistent vector illustration | Per-style SVG grammars, example comparison, lint + render/zoom | Fixed styles may constrain art direction; Node/Chromium needed for some tools; `CANDIDATE` |
| `aosoficial/agent-infographic-skill` — https://github.com/aosoficial/agent-infographic-skill | Editorial infographic | Evidence -> takeaway -> information topology -> composition -> anti-slop review | Limited demonstrated automatic testing; `REFERENCE_ONLY` |
| `K-Dense-AI/scientific-agent-skills` — https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-visualization | Scientific diagrams/figures | Palette audits, reproducible export and source fidelity | Scientific context; `REFERENCE_ONLY` |
| `iart-ai/motion-design-skills` — https://github.com/iart-ai/motion-design-skills | Motion graphics | Motion art direction, frame snapshots, Remotion checks | Requires runtime/video tools; `CANDIDATE` |
| `EL4CTEO/blender-skills` — https://github.com/EL4CTEO/blender-skills | Blender scenes/assets | Domain-specific modeling, QA, exporting | Requires compatible Blender runtime; `CANDIDATE` |
| `anthropics/skills/skills/algorithmic-art` — https://github.com/anthropics/skills/tree/main/skills/algorithmic-art | Generative art | Seeded p5.js procedural work | Anthropic-branded fixed example template; adapt ideas, not fixed UI; `REFERENCE_ONLY` |
| `SkillMedev/skills/skills/print-layout` — https://github.com/SkillMedev/skills/tree/main/skills/print-layout | Print production | Prepress checks, color management, PDF/X distinctions | Text instructions alone not a validated preflight; `REFERENCE_ONLY` |
| `mblode/agent-skills`, `bmad-code-org/BMAD-METHOD`, `anthropics/skills/skills/frontend-design` — https://github.com/mblode/agent-skills ; https://github.com/bmad-code-org/BMAD-METHOD ; https://github.com/anthropics/skills/tree/main/skills/frontend-design | Product/UX/frontend | Interaction/behavior contracts, UX specification, visual interface craft | Varying scope and host requirements; `REFERENCE_ONLY` |

Prefer host-native tools when already available and competent: image editing/generation for static rendered images, Figma for editable native designs, browser/runtime for real UI, document and presentation tools for their native sources, verified Python/SVG/PDF/Blender/Remotion tools for deterministic outputs. Match the **requested medium** before selecting a tool. A capability mentioned here may not exist in a given ChatGPT or Codex session.

## Negative knowledge

- No global ranking of these specialists has been empirically established for our user tasks.
- The presence of `SKILL.md`, a test directory or advertised successes does not prove runtime compatibility or design utility.
- Branding, typography, art direction, data correctness and production verification are related but distinct responsibilities.
- External references may change; date and commit-pin when actually adopting anything, do not rely on this catalog's as-of date as current truth.
