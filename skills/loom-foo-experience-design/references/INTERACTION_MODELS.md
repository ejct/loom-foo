# Interaction models: decisions that matter

## Object-action-state analysis

Identify objects users manipulate, their availability and lifetime, permissible actions, states, feedback and errors. Use state tables, transition diagrams or annotated flows only when the task needs them. Include events from other users, background jobs, network failure and permissions where material.

Model user expectations, system reality, visibility and reversibility: Can the user tell what changed? What is undoable? Does delayed processing preserve intent? Can focus/selection and user data survive interruption? Don't treat a confirmation modal as the universal solution.

## Information architecture

Organize around user concepts and retrieval tasks. Distinguish object ownership, location, grouping, navigation, search, filtering, disclosure and cross-linking. Test against real terms, entities, confusing overlaps and exceptional tasks. A proposed IA isn't proven by visual neatness.

## Alternative generation

Choose alternatives that change interaction **mechanism** (e.g. direct manipulation versus command-based, progressive disclosure versus separate navigation) rather than palette. Evaluate cognitive effort, error recovery, access, frequency of use, source constraints and operational complexity. Avoid frictionless claims without measurement.

## Conversational/spatial contexts

For conversational UI: model uncertainty, clarification, consent for external actions, recoverable history and distinction between suggestion and execution. For spatial HMI/XR: consider reference frames, sensor latency, physical safety, hand/eye load and mode errors; do not claim hardware tests not performed.
