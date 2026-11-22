# Conversational, voice and multimodal UX content

Read only when the product interaction meaningfully uses spoken output, conversational turns, audio + visual responses, spatial orientation, interrupts or modality switching. This concerns **content** rather than control architecture, speech synthesis implementation or HMI safety certification. For changing turn-taking, focus/gesture mechanics, spatial reference frames and system transitions, `loom-foo-experience-design` owns the behavior.

## Start with the user's next decision

For each message identify: intent/goal, what the system has understood or not understood, actual result/state, whether an action has occurred, whether confirmation is required, what is available on each output channel, and how the user can correct or exit. Avoid exposing model internals unless they resolve a real decision. Do not claim the agent remembers, sees, hears, monitors or continuously listens unless the implementation actually does.

## Spoken and screen content are not identical

- **Voice-only:** make the essential outcome audible with short, complete utterances; name the object/action when necessary; make ambiguity and uncertainty explicit. Avoid long menus, reference-only pointers such as “as shown above” and labels that depend on screen position.
- **Screen + voice:** preserve one semantic claim across channels while dividing detail appropriately; voice may state outcome and next choice while the screen holds lists, exact values, citations, limits, warnings and persistent controls. Never put a critical consequence solely in one channel when the product relies on the other for completion.
- **Voice command text:** anticipate speech recognition ambiguity, deictic requests (“that one”), changed context and interruption. Ask a minimal disambiguating question instead of choosing a target silently when consequences matter.
- **Streaming and progressive responses:** distinguish provisional text, generated suggestions and committed actions. Avoid narrating “finished” before completion; a partial spoken utterance must not imply an unconfirmed commitment.
- **Interruptibility / read-back:** if the product supports repeat, slow, stop, cancel, correction or switching to screen, label/announce that mechanism. If it does not, report a design dependency instead of advertising nonexistent controls.

## Safety, privacy and consent

When content includes private names, records, prices, directions or account information, confirm that the chosen channel is appropriate for the user's environment. Avoid reading sensitive details aloud without an actual permission/context model. A spoken “yes” may not establish approval of an exact recipient, payment amount, destructive scope or edited payload; specify the review and confirmation boundary supplied by the product.

## Example (illustrative)

- State: AI drafted a message, no send call completed. **Voice:** “I prepared a draft. Review the recipient and message before sending.” **Screen:** heading “Draft ready”; button “Review draft”; recipient shown, approval action separate.
- State: weather forecast and uncertainty available. **Voice:** give concise forecast and relevant recommendation; **Screen:** show temperatures, detailed conditions and data provenance. Do not invent measurements or claim real-time observation from a model-generated summary.

## Checks

Is the same important fact preserved between modalities? Can a screen-free user recover? Are attention, context and interruption limits acknowledged? Does spoken wording reveal more private information or grant broader authorization than the visible interface? Can the user identify the difference between suggested and executed actions?

Source inspiration: https://pair.withgoogle.com/guidebook-v2/chapter/mental-models/ ; https://pair.withgoogle.com/guidebook-v2/chapter/errors-failing/ ; https://www.w3.org/WAI/WCAG22/Understanding/ . Adaptation to multimodal voice UI is a design inference; it is not a claimed user-tested standard.
