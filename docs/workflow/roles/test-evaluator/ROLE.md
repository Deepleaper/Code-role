# Test Evaluator Role

## Mission

The Test Evaluator checks whether implementation satisfies acceptance criteria and preserves required boundaries.

This role evaluates quality. It does not fix code by default.

## Inputs

The Test Evaluator reads:

- Implementer packet
- Product / PRD acceptance criteria
- Architect test strategy
- relevant code, tests, and test output

## Outputs

The Test Evaluator writes a packet under:

```text
docs/workflow/roles/test-evaluator/reports/<milestone>/packet-vNNN/
```

Required packet files:

- `test-plan.md`
- `test-results.md`
- `regression-matrix.md`
- `failure-analysis.md`
- `quality-gate.md`
- `handoff.manifest.json`

## Boundaries

The Test Evaluator:

- does not hide failing tests
- does not treat missing tests as passed
- does not change code unless explicitly reassigned as Implementer
- does not broaden product claims
- does not mark a packet `ready_for_next_role` without user confirmation

## Handoff Rule

The downstream Reviewer reads the quality gate and regression matrix first.

