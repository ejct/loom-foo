# Design system foundations and token semantics

## Determine the system's job

A system exists to share intentional decisions across products, teams or platforms. Ask what needs to stay consistent and what should vary: brand, modality, platform, density, accessibility, locale, responsive mode. If there is one small one-off view, prefer local components over a general system.

## Token model

- **Primitive:** raw palette/size/spacing value, not necessarily user-facing role.
- **Semantic:** meaning and role (e.g. `color.text.default`, `space.control.inline`) that can alias primitives across themes.
- **Component token:** deliberate specialized role only when reuse/migration justifies it; avoid one token for every arbitrary style value.
- Define naming namespaces and semantic boundaries, typed values, valid modes, override scope and fallback semantics. A theme is an explicit mapping, not simply a new palette screenshot.

DTCG **Format Module 2025.10**: https://www.designtokens.org/TR/2025.10/format/ — token data structure (`$value`, `$type`, groups, aliases/references, types, color/composite values). **Resolver Module 2025.10**: https://www.designtokens.org/TR/2025.10/resolver/ — token *sets, modifiers, contexts, resolution order*, and selecting effective token values across themes/modes. Both are **W3C Community Group Final Reports, not W3C Recommendations**. Check each module's actual applicability and supported subset; passing Format validation does **not** establish context resolution or Resolver conformance. Figma-specific variable *modes* are an implementation detail with mappings to source-token contexts — they are not proof of native DTCG Resolver support. The 2026 preview/drafts are not interchangeable with the stable 2025.10 reports.

## Source of truth and traceability

Resolve canonical owner *per property*: authored token source, Figma vars/styles, code variables, documentation and distribution build can differ. Record ID/name mappings, version, conversion rules, owner approvals, drift and exceptions. Do not replace authoritative code tokens because a library screenshot has a different shade. An automated equality test may be insufficient when conversion is intentionally lossy or platform-specific.

## Minimal checks

Detect missing semantic roles, unresolved references, cycles, unreachable tokens, inconsistent mode coverage, type/scale mismatches, inaccessible combinations where relevant, unused/duplicated terms, and changed meanings under unchanged names. Static parser PASS does not establish actual rendered consistency.
