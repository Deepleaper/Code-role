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

Default handoff is lightweight:

- The user may accept a role's completed output for the next role without forcing a `ready_for_next_role` status transition.
- The Orchestrator records that acceptance and generates the next-role startup message.
- The downstream packet records the upstream manifest path and the actual upstream status at consumption, even if that status is `draft`.

Strict handoff is optional:

- Use `ready_for_next_role` and `packet.lock.json` only when the user explicitly asks for strict handoff, auditability, immutability, or release-grade evidence.
- Do not ask the owning role to do a readiness conversion by default.

## Versioning Rules

- Packet versions are append-only.
- Do not edit a packet after it is marked `ready_for_next_role`.
- If content must change, create the next packet version.
- `latest.json` may be updated to point to the newest packet.
- Downstream roles must record the exact upstream packet version they read in their own `handoff.manifest.json`.
- Strict handoff may also lock packet hashes with `packet.lock.json`.
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
- advancing to the next role after accepting a completed role output
- allowing Implementer to start work

## Downstream Input Lock

When a downstream role consumes an upstream packet, it records:

- upstream role
- milestone
- packet version
- manifest path
- packet status at time of consumption
- consumption status, normally `accepted_as_input`

This prevents silent drift when upstream roles publish newer packets later. In lightweight mode, the record is a navigation and accountability link. In strict mode, `packet.lock.json` adds hash-level immutability.

## Orchestrator Consumption Check Request

Every execution role must include an Orchestrator consumption-check request block at the end of its completion response.

The block must include:

- current role
- milestone
- packet path
- handoff manifest path
- reported packet status
- whether strict handoff was requested
- concise role completion summary
- request for Orchestrator to check manifest validity, documents, input packets, blocked state, external research state, user acceptance, handoff mode, and next route
- boundary reminder that Orchestrator must not modify the role packet, create downstream packets, run Git commands, or modify business files

Use [Orchestrator Consumption Check Request Template](orchestrator/consumption-check-request-template.md).

The current role may recommend a downstream role, but it must not generate the authoritative next-role startup message. Orchestrator owns consumable checks, chain routing, and next-role startup message generation.

## Status Transitions

See [Status Transition Protocol](status-transition-protocol.md).

## Implementer Gate

Implementer must not begin from chat-only instruction. Implementation requires an approved chain decision from the Orchestrator and explicit user permission to start.
