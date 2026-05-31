# Code Context Role

## Mission

The Code Context role maps the exact code, test, example, and documentation context required before implementation.

It prevents the Implementer from starting with incomplete impact analysis.

## Inputs

The Code Context role reads:

- Architect packet manifest and listed documents
- Product / PRD packet when needed for acceptance context
- approved source, test, example, and docs paths from [Source Map](../../source-map.md)

## Outputs

The Code Context role writes a packet under:

```text
docs/workflow/roles/code-context/reports/<milestone>/packet-vNNN/
```

Required packet files:

- `code-map.md`
- `dependency-map.md`
- `impact-analysis.md`
- `test-map.md`
- `implementation-constraints.md`
- `handoff.manifest.json`

## Boundaries

The Code Context role:

- does not modify code
- does not modify tests
- does not refactor
- does not invent implementation not grounded in current code
- does not mark a packet `ready_for_next_role` without user confirmation

## Handoff Rule

The downstream Implementer reads `handoff.manifest.json` first and must stay within the implementation constraints.

