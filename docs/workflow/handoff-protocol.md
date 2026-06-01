# Handoff Protocol

This protocol controls how roles exchange work through documents.

## Packet Location

Each role writes packets under:

```text
docs/workflow/roles/<role>/reports/<milestone>/packet-vNNN/
```

Example:

```text
docs/workflow/roles/researcher/reports/mvp-scope/packet-v001/
```

## Packet Lifecycle

Valid packet statuses:

- `draft`: work in progress.
- `ready_for_next_role`: approved for downstream consumption.
- `blocked`: missing required input or decision.
- `superseded`: replaced by a newer packet.

`accepted` is not written back to upstream packet manifests. Downstream acceptance is recorded as `accepted_as_input` in the downstream packet and in Orchestrator state.

Only packets with `ready_for_next_role` may be used as official downstream input.

A downstream role may consume `draft` only when the user explicitly approves draft consumption for exploration. Draft consumption must be recorded by the [Workflow Orchestrator](orchestrator/ROLE.md) and in the downstream packet `input_packets`.

## Versioning Rules

- Packet versions are append-only.
- Do not edit a packet after it is marked `ready_for_next_role`.
- If content must change, create the next packet version.
- `latest.json` may be updated to point to the newest packet.
- Downstream roles must lock the exact packet version they read in their own `handoff.manifest.json`.
- Downstream roles must not mutate upstream packet manifests.
- `accepted_as_input` is a downstream consumption record, not an upstream packet status.

## Required Packet Files

Every packet must include:

- `handoff.manifest.json`
- role-specific output documents
- a source log or evidence map when the role cites repo facts

The manifest is the contract. Downstream roles read the manifest first and then read only the files listed by the manifest unless explicitly instructed otherwise.

## Required User Confirmation

Ask for user confirmation before:

- creating a new milestone name when the requested milestone is ambiguous
- using external research or network access
- reading code paths outside the approved source map
- marking a packet `ready_for_next_role`
- superseding a packet that was already accepted
- changing this handoff protocol or the global source map
- allowing a downstream role to consume a `draft` packet
- allowing Implementer to start work

## Downstream Input Lock

When a downstream role consumes an upstream packet, it records:

- upstream role
- milestone
- packet version
- manifest path
- packet status at time of consumption
- consumption status, normally `accepted_as_input`

This prevents silent drift when upstream roles publish newer packets later.

## Orchestrator Consumption Check Request

Every execution role must include an Orchestrator consumption-check request block at the end of its completion response.

The block must include:

- current role
- milestone
- packet path
- handoff manifest path
- reported packet status
- reported `ready_for_next_role`
- concise role completion summary
- request for Orchestrator to check manifest validity, documents, input packets, blocked state, external research state, lock presence, consumability, and next route
- boundary reminder that Orchestrator must not modify the role packet, create downstream packets, run Git commands, or modify business files

Use [Orchestrator Consumption Check Request Template](orchestrator/consumption-check-request-template.md).

The current role may recommend a downstream role, but it must not generate the authoritative next-role startup message. Orchestrator owns consumable checks, chain routing, and next-role startup message generation.

## Status Transitions

See [Status Transition Protocol](status-transition-protocol.md).

## Implementer Gate

Implementer must not begin from chat-only instruction. Implementation requires an approved chain decision from the Orchestrator and explicit user permission to start.
