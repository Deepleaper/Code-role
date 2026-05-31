# Document Workflow

This folder defines the document-based role workflow for the target project.

The workflow separates responsibilities into roles. Each role reads approved document packets from upstream roles and writes a new versioned document packet for downstream roles. Roles do not pass state through chat memory as the source of truth.

The workflow has eight configured role slots. The [Workflow Orchestrator](orchestrator/ROLE.md) is the control role; the other seven roles are execution roles.

## Current Scope

Currently materialized role files:

- [Workflow Orchestrator](orchestrator/ROLE.md)
- [Researcher](roles/researcher/ROLE.md)
- [Product / PRD](roles/product-prd/ROLE.md)
- [Architect](roles/architect/ROLE.md)
- [Code Context](roles/code-context/ROLE.md)
- [Implementer](roles/implementer/ROLE.md)
- [Test Evaluator](roles/test-evaluator/ROLE.md)
- [Reviewer](roles/reviewer/ROLE.md)

The [Role Configuration Guide](role-configuration-guide.md) defines the operating model and role responsibilities for the full workflow.

## Core Rules

- Every role owns its own folder under `docs/workflow/roles/<role>/`.
- Every role writes reports only under `docs/workflow/roles/<role>/reports/`.
- Every milestone output is a versioned packet: `packet-v001`, `packet-v002`, and so on.
- Packet content is immutable once marked `ready_for_next_role`.
- `latest.json` is only a pointer to the latest packet.
- Downstream roles must read `handoff.manifest.json`, not guess which files matter.
- Downstream roles must lock the exact upstream packet version they consumed.
- Implementer must not start from chat-only instruction.
- Draft packet consumption requires explicit user approval.

## Protocol Documents

- [Role Configuration Guide](role-configuration-guide.md)
- [Workflow Bootstrap](bootstrap.md)
- [Workflow Chain Policy](workflow-chain-policy.md)
- [Status Transition Protocol](status-transition-protocol.md)
- [Workflow Validation](workflow-validation.md)
- [Orchestrator Startup Routine](orchestrator/STARTUP.md)
- [Handoff Protocol](handoff-protocol.md)
- [Packet Schema](packet-schema.md)
- [Source Map](source-map.md)
