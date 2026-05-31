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

- official downstream consumption requires upstream status `ready_for_next_role`.
- `draft` consumption requires explicit user approval.
- draft-consumption approval must be recorded in Orchestrator `decision-log.md`.
- downstream `input_packets` must lock exact upstream role, milestone, packet version, manifest path, and status at consumption.

### Status Transition

- only the owning role writes its own packet manifest.
- upstream packet manifest is not rewritten for downstream acceptance.
- downstream acceptance is recorded as `accepted_as_input`.
- `ready_for_next_role` packets are immutable.
- post-ready changes require a new packet version.

### Packet Lock

When a packet is marked `ready_for_next_role`, create:

```text
packet.lock.json
```

The lock records hashes for packet files. A future validator can compare current hashes against the lock to detect drift.

### Implementer Gate

Before implementation:

- chain permits implementation
- Product/PRD or equivalent scope is accepted, unless the user explicitly chose patch-chain
- Code Context packet exists for non-trivial work
- user explicitly allows Implementer to start

### Chain-Specific Checks

- `full-chain`: all seven execution role packets must be present unless current stage is earlier in the chain.
- `mini-chain`: requires accepted product scope or explicit user override.
- `patch-chain`: must not touch runtime boundary, memory scope, permissions, schema, or release claims.
- `docs-only-chain`: must not include code or test changes.
- `research-only`: may stop after Researcher only if Orchestrator records why.

## Privacy / Repo Boundary

Validation must not:

- call network
- call provider APIs
- mutate runtime
- write product code
- write release docs
- include local workflow files in GitHub commits by default

