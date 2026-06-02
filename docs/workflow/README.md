# Document Workflow

This folder defines the document-based role workflow for Code-role role instances.

The workflow separates responsibilities into roles. Each role reads approved document packets from upstream roles and writes a new versioned document packet for downstream roles. Roles do not pass state through chat memory as the source of truth.

The workflow is discussion-first, not automation-first. Each role produces a documented output for user discussion. The default flow is lightweight: after the user accepts a role's completed output, Orchestrator may route the next role even when the packet remains `draft`.

The workflow has eight configured role slots. The [Workflow Orchestrator](orchestrator/ROLE.md) is the control role; the other seven roles are execution roles.

The recommended usage model is one configured Codex role instance per role. Do not run the full workflow by switching roles inside one conversation.

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
- Every role conversation must point to that role's explicit output.
- Every role should be configured and used as a separate role instance.
- Unrelated requests must be corrected and routed to the proper role.
- Every non-Implementer role produces documents only and does not change code.
- Implementer is the only role that may change approved project files, and only after user-confirmed implementation start.
- Every milestone output is a versioned packet: `packet-v001`, `packet-v002`, and so on.
- Packet content is immutable only in strict handoff mode after it is marked `ready_for_next_role`.
- `latest.json` is deprecated for daily workflow. Use Orchestrator state and `final-packet-index.md` to identify current outputs.
- Downstream roles must read `handoff.manifest.json`, not guess which files matter.
- Downstream roles must record the exact upstream packet version they consumed.
- Strict `ready_for_next_role` plus `packet.lock.json` handoff is advanced optional mode. Daily lightweight workflow should not require it.
- Implementer must not start from chat-only instruction.
- Each role must stop for discussion when scope, tradeoffs, evidence, risks, or handoff readiness are not settled.
- Advancing to the next role requires user acceptance of the completed role output.
- Upstream packet manifests must be passed explicitly between role instances.

## Protocol Documents

- [Role Configuration Guide](role-configuration-guide.md)
- [Workflow Bootstrap](bootstrap.md)
- [Project Bootstrap](project-bootstrap.md)
- [Role Instance Setup](role-instance-setup.md)
- [State Index](state-index.md) optional navigation
- [Git Operation Policy](git-operation-policy.md)
- [Workflow Chain Policy](workflow-chain-policy.md)
- [Discussion-First Protocol](discussion-first-protocol.md)
- [Status Transition Protocol](status-transition-protocol.md)
- [Workflow Validation](workflow-validation.md)
- [Orchestrator Startup Routine](orchestrator/STARTUP.md)
- [Orchestrator Consumption Check Request Template](orchestrator/consumption-check-request-template.md)
- [Handoff Protocol](handoff-protocol.md)
- [Packet Schema](packet-schema.md)
- [Source Map](source-map.md)
