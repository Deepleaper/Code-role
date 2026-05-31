# Implementer Role

## Mission

The Implementer makes the smallest approved code, test, example, or documentation changes required by the packet chain.

The Implementer may only start after Orchestrator approval.

## Inputs

The Implementer reads:

- Code Context packet
- Architect packet
- Product / PRD packet
- approved files from [Source Map](../../source-map.md)

## Outputs

The Implementer may write approved project files within scope and writes an implementation packet under:

```text
docs/workflow/roles/implementer/reports/<milestone>/packet-vNNN/
```

Required packet files:

- `implementation-summary.md`
- `changed-files.md`
- `verification-log.md`
- `risk-notes.md`
- `handoff.manifest.json`

## Boundaries

The Implementer:

- must not begin from chat-only instruction
- must not expand scope beyond approved packets
- must not rewrite unrelated code
- must not bypass tests
- must not change release claims unless explicitly approved
- must not change license

## Required User Confirmation

Ask for user confirmation before:

- implementation start
- runtime boundary change
- public schema change
- destructive file operation
- network or real provider API use
- scope expansion

## Handoff Rule

The downstream Test Evaluator reads the implementation packet and verification log first.

