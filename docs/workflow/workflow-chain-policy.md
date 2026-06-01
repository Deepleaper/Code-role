# Workflow Chain Policy

This document defines when to use each workflow chain and which packet statuses may be consumed.

## Chain Type Matrix

| Chain | Roles | Use When |
| --- | --- | --- |
| `full-chain` | `researcher -> product-prd -> architect -> code-context -> implementer -> test-evaluator -> reviewer` | User value, product scope, architecture, runtime, permission, schema, or security risk is unclear. |
| `mini-chain` | `architect -> code-context -> implementer -> test-evaluator -> reviewer` | Product scope is already accepted, but architecture and implementation still need controlled handoff. |
| `patch-chain` | `code-context -> implementer -> test-evaluator -> reviewer` | A narrow fix has accepted scope and does not touch runtime boundary, permission, memory, schema, or release claims. |
| `docs-only-chain` | `product-prd or architect -> reviewer` | Documentation-only work that does not change runtime behavior, schema, permission, release status, or user-facing capability. |
| `research-only` | `researcher -> product-prd or stop` | A question needs research before product commitment, or the workflow intentionally stops after research. |

The Workflow Orchestrator selects a chain and records the decision. The Orchestrator cannot approve state transitions for the user.

Architect must not hand off directly to Test Evaluator in implementation-bound work. Architecture packets first go to Code Context / Context Engineer so downstream roles receive a stable file, dependency, impact, test, and implementation-constraint map.

## Chain Details

### `full-chain`

Use for high-impact work:

```text
researcher -> product-prd -> architect -> code-context -> implementer -> test-evaluator -> reviewer
```

Required for:

- new product capability
- runtime, memory, permission, schema, or security work
- release positioning changes
- unclear user value
- work with P0/P1 risk

Architect handoff rule:

- after `architect`, route to `code-context`
- do not route directly to `test-evaluator`

### `mini-chain`

Use for medium-impact work:

```text
architect -> code-context -> implementer -> test-evaluator -> reviewer
```

Allowed for:

- bounded implementation with already accepted product scope
- architecture-sensitive docs or examples
- moderate refactor with clear scope

Architect handoff rule:

- after `architect`, route to `code-context`
- do not route directly to `test-evaluator`

### `patch-chain`

Use for narrow fixes:

```text
code-context -> implementer -> test-evaluator -> reviewer
```

Allowed for:

- small bug fix
- small test fix
- narrow follow-up with accepted scope

Not allowed for:

- permission model changes
- memory scope changes
- runtime boundary changes
- release claims

### `docs-only-chain`

Use for documentation-only work:

```text
product-prd or architect -> reviewer
```

Allowed for:

- wording cleanup
- role configuration docs
- protocol documentation updates

Not allowed for:

- changes that alter product claim, runtime behavior, schema, permission, release status, or user-facing capability.

### `research-only`

Use for research or discovery work:

```text
researcher -> product-prd or stop
```

Allowed for:

- user-value investigation
- technology or concept validation
- deciding whether a product packet is needed

If the workflow stops after Researcher, record the reason in the Orchestrator decision log.

## Packet Consumption Policy

Default rule:

- Downstream roles consume only `ready_for_next_role` or `accepted` packets.

Exception:

- A downstream role may consume `draft` only when the user explicitly approves draft consumption for exploration.
- Draft consumption must be recorded in `docs/workflow/orchestrator/decision-log.md`.
- Draft consumption must be recorded in the downstream packet `input_packets`.
- Orchestrator must output `consumable_check=fail` when a packet is `draft` and no explicit draft-consumption approval exists.

## Implementer Gate

The Implementer must not begin work from chat-only instruction.

Before implementation starts, the Orchestrator must confirm:

- selected chain permits implementation
- required upstream packets exist
- upstream packet status is `ready_for_next_role` or `accepted`, unless draft consumption is explicitly approved
- scope is clear
- required acceptance criteria exist, unless the user explicitly chooses patch-chain for a narrow fix

If any check fails, Implementer remains blocked.

## Reviewer Gate

The Reviewer must audit the packet chain, not only the code.

Reviewer checks:

- required upstream packets exist
- packet versions are locked
- draft consumption, if any, was explicitly approved
- Implementer stayed within approved scope
- Test Evaluator covered acceptance criteria when applicable
- no unresolved P0
- P1 risks are explicitly accepted or sent back

## User Confirmation Points

User confirmation is required for:

- creating ambiguous milestone names
- selecting or changing chain type
- consuming draft as official input
- marking packet `ready_for_next_role`
- marking packet `accepted`
- allowing Implementer to start
- skipping a role in a chain
- accepting unresolved P1 risk
