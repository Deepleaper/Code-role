# Optional Packet Schema / 可选 Packet Schema

Full Profile requires one assignment-named primary professional artifact. Packet metadata is optional provenance support and must not become a routine delivery gate.

## Current Output Pointer / 当前产物指针

Use Orchestrator `workflow-state.md` for the current target KR, failed evidence, owner, and accepted primary artifact. The compatibility file `final-packet-index.md` may point to each role's current accepted artifact.

Daily workflow does not require `latest.json`, `handoff.manifest.json`, readiness conversion, or a lock.

## `handoff.manifest.json`

When versioned provenance is useful, a packet may include this manifest:

```json
{
  "schema_version": "0.1",
  "role": "researcher",
  "milestone": "example-milestone",
  "packet_version": "packet-v001",
  "status": "draft",
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD",
  "summary": "Short artifact summary.",
  "artifact_policy": {
    "primary_artifact_from_assignment": true,
    "required_primary_artifact_count": 1,
    "documents_are_optional_annexes": true
  },
  "documents": [],
  "input_packets": [],
  "source_scopes": [],
  "return_to": "workflow-orchestrator",
  "open_questions": [],
  "blocked": false,
  "required_confirmations": []
}
```

Manifest status describes provenance metadata, not work-unit acceptance. Valid values are `draft`, `blocked`, `ready_for_next_role`, and `superseded`. Workflow Orchestrator accepts the primary artifact from substantive evidence, not manifest status.

## `input_packets`

When provenance is recorded, `input_packets` names exact assignment-relevant upstream artifact versions actually consumed. It never prescribes a fixed predecessor or successor.

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

Downstream recording must not mutate an upstream manifest.

## `packet.lock.json` Strict Audit Mode

Only when the user explicitly requests immutable audit handoff, a `ready_for_next_role` packet may include:

```json
{
  "schema_version": "0.1",
  "role": "researcher",
  "milestone": "example-milestone",
  "packet_version": "packet-v001",
  "status": "ready_for_next_role",
  "files": [
    {"path": "handoff.manifest.json", "sha256": "..."}
  ]
}
```

A locked packet is immutable; changes require `packet-v002`. Strict packet checks remain audit operations and cannot change a delivery KR without substantive outcome evidence.

## Compatibility / 兼容

- New manifest fields are additive.
- Unknown fields are ignored unless strict validation is requested.
- Document paths are relative to the packet directory.
- Legacy `latest.json` and packet status may be read for history but never override current Orchestrator state or an accepted primary artifact.
