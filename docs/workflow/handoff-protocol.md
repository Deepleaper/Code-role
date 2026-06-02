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
- `ready_for_next_role`: approved for strict immutable downstream consumption.
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
- Orchestrator state records the current authoritative packet. `final-packet-index.md` records each role's accepted current final output.
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

## Orchestrator Consumption Check Summary

Every execution role must include a short Orchestrator consumption-check summary at the end of its completion response.

This summary is the copy-ready message the user sends back to Workflow Orchestrator / Project Manager. It must appear in the same conversation response as the role's completion report, not in a separate hidden file.

The summary must include:

- current role
- milestone
- packet path
- handoff manifest path
- reported packet status
- concise role completion summary
- milestone alignment
- possible drift
- recommended routing, if any
- request for Orchestrator to check milestone alignment, manifest readability, user acceptance, and next route
- boundary reminder that Orchestrator must not modify the role packet, create downstream packets, run Git commands, or modify business files

Use [Orchestrator Consumption Check Request Template](orchestrator/consumption-check-request-template.md).

The current role may recommend a downstream role, but it must not generate the authoritative next-role startup message. Orchestrator owns consumable checks, chain routing, and next-role startup message generation.

When Orchestrator accepts the output and decides to start the next role, it must paste a copy-ready next-role startup message in its response. It should not only say "start the next role" or only list the role name.

## Status Transitions

See [Status Transition Protocol](status-transition-protocol.md).

## Implementer Gate

Implementer must not begin from chat-only instruction. Implementation requires an approved chain decision from the Orchestrator and explicit user permission to start.
