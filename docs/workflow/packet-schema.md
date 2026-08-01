# Packet Schema

This document defines the stable fields for workflow packet pointers and handoff manifests.

## Current Output Pointer

Daily workflow does not require `latest.json`.

Use Orchestrator `workflow-state.md` for the current authoritative packet and `final-packet-index.md` for each role's current final output in a milestone.

Legacy projects may still contain `latest.json`, but downstream roles must not treat it as authoritative when Orchestrator state or `final-packet-index.md` exists.

## `handoff.manifest.json`

Each packet must include a manifest with this shape:

```json
{
  "schema_version": "0.1",
  "role": "researcher",
  "milestone": "example-milestone",
  "packet_version": "packet-v001",
  "status": "draft",
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD",
  "summary": "Short packet summary.",
  "documents": [
    {
      "path": "research-brief.md",
      "type": "research_brief",
      "required": true,
      "description": "Main research output."
    }
  ],
  "input_packets": [],
  "source_scopes": [],
  "return_to": "workflow-orchestrator",
  "open_questions": [],
  "blocked": false,
  "required_confirmations": []
}
```

Valid packet manifest statuses:

- `draft`
- `blocked`
- `ready_for_next_role`
- `superseded`

`accepted` is not a packet manifest status for new packets. Downstream acceptance is recorded in downstream `input_packets` as `accepted_as_input`.

## `input_packets`

Downstream packets must record exact assignment-named upstream packet versions actually consumed. Manifests do not prescribe a fixed predecessor or successor; every professional role returns to Workflow Orchestrator. In lightweight flow the upstream packet may still be `draft`; strict handoff may add `ready_for_next_role` and `packet.lock.json`.

```json
{
  "role": "researcher",
  "milestone": "example-milestone",
  "packet_version": "packet-v001",
  "manifest": "docs/workflow/roles/researcher/reports/example-milestone/packet-v001/handoff.manifest.json",
  "status_at_consumption": "draft",
  "consumption_status": "accepted_as_input"
}
```

Rules:

- `status_at_consumption` records the upstream manifest status when read.
- `consumption_status` records the downstream role's action.
- downstream acceptance must not mutate the upstream manifest.

## `packet.lock.json` Advanced Optional Mode

When strict handoff is requested and a packet becomes `ready_for_next_role`, create a lock file:

```json
{
  "schema_version": "0.1",
  "role": "researcher",
  "milestone": "example-milestone",
  "packet_version": "packet-v001",
  "status": "ready_for_next_role",
  "files": [
    {
      "path": "handoff.manifest.json",
      "sha256": "..."
    }
  ]
}
```

The lock detects drift after handoff.

## Packet Immutability Rules

Packet immutability is required only for strict downstream audit.

- `packet-v001` may be edited only while its manifest status is `draft`.
- Once a packet status becomes `ready_for_next_role`, do not edit files inside that packet.
- If content must change after `ready_for_next_role`, create the next version, for example `packet-v002`.
- Orchestrator state and `final-packet-index.md` should move to the accepted current output.
- Historical strict-handoff packets must remain immutable so downstream `input_packets` records do not drift.

## Compatibility Rules

- New manifest fields must be additive.
- Unknown fields should be ignored by downstream roles unless strict validation is requested.
- Status semantics cannot change without updating [Handoff Protocol](handoff-protocol.md).
- Document paths in the manifest are relative to the packet directory.
