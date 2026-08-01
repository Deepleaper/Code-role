# Workflow Validation

This document defines local validation checks for the document workflow.

The validator is local by default. It is not part of product CI unless the team explicitly promotes this workflow into a repository standard.

## Local Validator

Reference local tool:

```text
docs/workflow/tools/validate_workflow_packet.py
```

The tool is stored under `docs/workflow/`, so it is covered by the local workflow exclude policy.

## Required Checks

### Packet Structure

- `handoff.manifest.json` exists.
- manifest is valid JSON.
- required manifest fields exist.
- every document listed in `documents` exists.
- document paths are relative to the packet directory.

### Consumption

- lightweight downstream consumption requires Project Manager acceptance of the upstream professional artifact against the frozen assignment checks.
- upstream status may remain `draft` in lightweight mode.
- Orchestrator records artifact acceptance and the evidence-based route.
- downstream `input_packets` must record exact upstream role, milestone, packet version, manifest path, and status at consumption.
- strict downstream consumption requires `ready_for_next_role` and `packet.lock.json`.

### Status Transition

- only the owning role writes its own packet manifest.
- upstream packet manifest is not rewritten for downstream acceptance.
- downstream acceptance is recorded as `accepted_as_input`.
- `ready_for_next_role` packets are immutable.
- post-ready changes require a new packet version.

### Packet Lock

When strict handoff is requested and a packet is marked `ready_for_next_role`, create:

```text
packet.lock.json
```

The lock records hashes for packet files. A future validator can compare current hashes against the lock to detect drift.

### Implementer Gate

Before implementation:

- the Implementer assignment is complete;
- objective, authoritative inputs, writable modules or directories, required checks, and stop condition are present;
- product or architecture decisions needed by the change are accepted;
- task-specific exclusions are explicit when needed.

A valid assignment authorizes ordinary local implementation. No second startup confirmation is required.

### Chain-Specific Checks

- named chains are planning hints, not fixed predecessor/successor gates;
- every selected role must answer one explicit evidence gap;
- every professional role returns to Workflow Orchestrator;
- `docs-only-chain` assignments must not request code changes;
- implementation evidence cannot pass a KR without required independent evaluation.

## Privacy / Repo Boundary

Validation must not:

- call provider APIs
- mutate runtime
- write product code
- write release docs
- include local workflow files in GitHub commits by default

Public-source network research is allowed for role work when relevant to the milestone, but validation itself remains local by default unless a specific network-dependent validator is explicitly introduced.
