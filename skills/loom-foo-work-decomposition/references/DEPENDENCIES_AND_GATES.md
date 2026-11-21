# Dependencies and Gates

Dependencies should explain why work cannot start/finish safely or correctly yet.

Useful semantic concepts:
- requires artifact;
- requires decision;
- requires evidence;
- requires acceptance;
- integrates after;
- can run in parallel.

Do not freeze these as a universal ontology.

## Gates

A gate can be:
- owner decision/acceptance;
- evidence result;
- architecture/specification decision;
- credential/permission availability;
- compatibility/integration result.

A gate is not automatically a task.

## Integration

Parallel units may still require an integration point. Create an integration Work Unit only for real executable integration work; otherwise preserve the boundary as review/acceptance/reconciliation gate.
