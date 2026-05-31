# Status Transition Protocol

This document defines packet status ownership and transition rules.

## Core Rule

Packet status is owned by the role that owns the packet.

Downstream roles must not rewrite upstream packet manifests. The Orchestrator must not rewrite role packet manifests. The user approves transitions, but the owning role performs the packet status update while the packet is still mutable.

## Manifest Status Values

Valid `handoff.manifest.json` packet statuses:

- `draft`: owning role is still working.
- `blocked`: owning role cannot proceed without user input.
- `ready_for_next_role`: owning role has user approval to hand off this packet.
- `superseded`: this packet has been replaced by a newer packet version.

`accepted` is not a valid upstream packet manifest status for new packets. Downstream acceptance is recorded as `accepted_as_input`.

## Downstream Consumption Status

Downstream consumption is recorded in the downstream packet `input_packets` entry and in the Orchestrator state.

Example:

```json
{
  "role": "researcher",
  "milestone": "example-milestone",
  "packet_version": "packet-v001",
  "manifest": "docs/workflow/roles/researcher/reports/example-milestone/packet-v001/handoff.manifest.json",
  "status_at_consumption": "ready_for_next_role",
  "consumption_status": "accepted_as_input"
}
```

This avoids mutating the upstream packet after it becomes immutable.

## Transition Matrix

| From | To | Allowed By | Writer | Notes |
| --- | --- | --- | --- | --- |
| `draft` | `blocked` | owning role when input is missing | owning role | Record blocker in manifest. |
| `blocked` | `draft` | user provides missing input | owning role | Packet remains mutable. |
| `draft` | `ready_for_next_role` | explicit user confirmation | owning role | Generate or update `packet.lock.json` before handoff. |
| `ready_for_next_role` | `superseded` | explicit user confirmation and new packet exists | owning role or Orchestrator record plus owning role update if needed | Do not edit content files. |
| `ready_for_next_role` | `accepted_as_input` | downstream role consumes packet | downstream packet and Orchestrator state | Do not write this into upstream manifest. |

## Immutability Boundary

- `draft` and `blocked` packets may be edited by the owning role.
- `ready_for_next_role` packets are immutable.
- `superseded` packets are immutable.
- Downstream `accepted_as_input` does not mutate the upstream packet.
- Any content change after `ready_for_next_role` requires a new packet version.

## Required Transition Checklist

Before `draft -> ready_for_next_role`:

- all manifest `documents` exist
- `blocked=false`
- required confirmations are resolved or explicitly carried forward
- source log or evidence map is present when repo facts are cited
- `packet.lock.json` records file hashes for the packet
- Orchestrator records the transition decision

Before downstream consumption:

- upstream status is `ready_for_next_role`, or draft consumption is explicitly approved
- downstream packet records `status_at_consumption`
- downstream packet records `consumption_status`
- downstream packet locks exact upstream manifest path and packet version

## User Confirmation Boundary

The user confirms:

- chain type
- draft consumption exception
- `draft -> ready_for_next_role`
- role skip
- Implementer start
- P1 risk acceptance
- milestone closeout

The Orchestrator recommends and records. It does not approve.

