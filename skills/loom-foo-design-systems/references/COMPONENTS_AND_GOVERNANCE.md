# Components, patterns, governance and change impact

## Component contract (when requested)

- Name, purpose, acceptable contexts, anatomy and semantics.
- State graph: default, hover/focus/pressed, selected, disabled, loading, invalid, empty, error and system interruptions *only when applicable*.
- Properties and variants: avoid exhaustive size × theme × state matrix when composable properties suffice; document combinations that are intentionally forbidden.
- Behavior: keyboard/focus, input handling, responsiveness, content length, icon/copy limits, internationalization and assistive technology behavior.
- Visual contract: token bindings, typography, spacing, elevation, contrast and platform-specific exceptions.
- Implementation mapping: Figma master/component ID, code component name/version, representative instances and fidelity limitations.

A **pattern** covers multi-component user intent and behavior; a **component** is reusable bounded anatomy/behavior. Do not turn every layout into a component to fill the catalog.

## System evolution

Identify consumers and expected impact before change. For a breaking rename/semantic shift, specify deprecation warnings, migrations, compatibility aliases, target versions and owner of old/new decisions. Allow legacy exceptions when documented; uniformity for its own sake can harm product usability.

Contributions need discoverable request, design rationale, implementation evidence, review criteria and compatibility note proportional to change risk. Don't demand a committee or multi-agent ceremony for a token typo.

## Tool-specific execution boundary

Native `figma-generate-library` plus `figma-use` owns real Figma construction, property bindings, variants and API context. Code editors/build tools own CSS/native implementation. A design-system document cannot certify those external tools ran or that source synchronization is complete. Use provider IDs and verified source paths, not guessed handles.

Reference: https://www.carbondesignsystem.com/getting-started/contributing/component-checklist (component design/code/testing/documentation coverage), inspected as external practice, not a mandatory universal policy.
