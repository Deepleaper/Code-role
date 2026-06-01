# Code-role PRD

## 1. Product Summary

Code-role is a local role-configuration project for controlling Codex so it can deliver higher-quality programming results.

It does this by separating one broad coding conversation into explicit roles, document packets, handoff manifests, status gates, and validation checks. The product treats chat as an interaction layer, not as the source of truth. Durable workflow state lives in local files.

The current product form is a reusable template that can be copied into a target codebase. Its first job is to make AI-assisted engineering work more controlled, auditable, and repeatable.

Code-role is discussion-first, not automation-first. Every role creates a documented artifact for user discussion before the workflow advances. Except for Implementer after explicit approval, roles produce documents rather than changing code.

Code-role is used through separate configured role instances. The workflow should not be run by switching roles inside one conversation.

## 2. Positioning

Code-role is not an IDE plugin, agent runtime, task tracker, or project management SaaS.

It is a local coordination layer for AI engineering work. It defines how separate Codex role instances should move from product understanding to implementation and review without losing context, skipping gates, or mixing incompatible responsibilities.

Core positioning:

- Role-based control system for Codex-assisted software delivery.
- Document-first workflow for requirements, architecture, code context, implementation, testing, and review.
- Local template that can be added to a target project without becoming product code by default.
- Quality gate system that prevents implementation from starting from chat-only instructions.
- Discussion-first handoff system where each role produces documents for the next role.
- Separate role-instance setup where each role has its own configured conversation.

## 3. Problem Statement

Codex can produce weak programming results when the work is underspecified, context is scattered across chat, or multiple responsibilities are collapsed into one interaction.

Common failure modes:

- Implementation starts before product scope is clear.
- Architecture assumptions are not recorded.
- Code context is guessed instead of mapped.
- Tests are treated as optional or added after the fact.
- Review only checks code diff, not the reasoning chain.
- Chat memory becomes the only record of decisions.
- A later role cannot tell which upstream input was authoritative.

Code-role addresses these failures by forcing explicit packets, manifests, state transitions, and role boundaries.

## 4. Target Users

Primary users:

- Solo builders using Codex for non-trivial software changes.
- Technical founders who need better control over AI coding output.
- Engineering leads experimenting with AI-assisted delivery workflows.
- Product-minded engineers who want PRD, architecture, implementation, test, and review handoffs to be explicit.

Secondary users:

- Teams that want a lightweight local protocol before adopting heavier workflow infrastructure.
- AI workflow designers building reusable Codex operating patterns.

## 5. User Goals

Users want to:

- Start a coding task with clear product intent and scope.
- Decide which workflow chain fits the risk level of the task.
- Keep role responsibilities separate.
- Preserve decisions in files instead of chat memory.
- Prevent implementation from starting without accepted upstream input.
- Audit what evidence, PRD, architecture, code context, tests, and review were used.
- Reuse the workflow template across different local projects.

## 6. Core Concepts

### Workflow Orchestrator

The control role. It selects the chain, tracks milestone state, identifies the authoritative packet, checks whether the next role can consume it, and records required user confirmations.

It does not write research, PRD, architecture, code, tests, or review findings.

### Execution Roles

Configured execution roles:

1. Researcher
2. Product / PRD
3. Architect
4. Code Context
5. Implementer
6. Test Evaluator
7. Reviewer

Each execution role owns its folder, reads approved upstream packet manifests, and writes versioned packets only under its own reports directory.

### Packet

A versioned output unit written by a role.

Example:

```text
docs/workflow/roles/product-prd/reports/<milestone>/packet-v001/
```

Packets contain role documents and a `handoff.manifest.json`.

### Handoff Manifest

The downstream contract for a packet. It records status, documents, input packets, source scopes, open questions, blockers, and required confirmations.

### Workflow Chain

A selected sequence of roles for a milestone.

Supported chains:

- `full-chain`
- `mini-chain`
- `patch-chain`
- `docs-only-chain`
- `research-only`

### Status Gate

A rule that prevents unsafe progression. For example, Implementer must not begin from chat-only instruction, while strict packet readiness is used only when the user requests audit-grade handoff.

## 7. MVP Scope

The MVP should make Code-role usable as a local template that can be copied into a target project and used immediately with Codex.

MVP includes:

- Complete eight-role workflow documentation.
- Role-instance setup documentation.
- Explicit prompt contracts for every role: purpose, inputs, outputs, boundaries, discussion gates, downstream handoff, and correction of unrelated requests.
- Clear startup routine for Orchestrator.
- Chain selection policy.
- Packet schema and handoff manifest rules.
- Source map for role read/write boundaries.
- Template packets for each role.
- Local packet validator.
- Tests that verify role configuration and workflow protocol consistency.
- Basic setup instructions for local use.

MVP should prioritize correctness, clarity, and repeatability over automation.

## 8. Functional Requirements

### FR1. Local Template Structure

The repository must provide a complete `docs/workflow/` template that can be copied into a target project.

Acceptance:

- All configured roles have `ROLE.md`, `templates/`, and `reports/`.
- Required workflow protocol documents exist.
- The folder boundary is clearly documented as local coordination infrastructure by default.

### FR2. Orchestrator Startup

The Orchestrator must support a file-based startup routine.

Acceptance:

- Startup command is documented.
- Startup routine reads workflow state files first.
- Startup routine does not infer current packet by scanning for newest files.
- Current milestone, chain, role, authoritative packet, packet status, blockers, and required confirmations are recoverable from state files.

### FR3. Role Boundary Enforcement

Each role must have explicit read/write scope and must-not rules.

Acceptance:

- Orchestrator cannot write execution packets.
- Researcher cannot write PRD or code.
- Product / PRD cannot modify implementation details.
- Architect cannot implement.
- Code Context cannot modify code.
- Implementer cannot start from chat-only instruction.
- Test Evaluator cannot modify code unless reassigned.
- Reviewer cannot implement fixes or rewrite packet history.

### FR4. Packet Handoff

Each execution role must produce a packet with a manifest.

Acceptance:

- Packet directory follows `reports/<milestone>/packet-vNNN/`.
- Manifest includes required schema fields.
- Manifest document paths are packet-relative.
- Downstream packets record exact upstream packet versions in `input_packets`.
- Downstream acceptance is recorded as `accepted_as_input` without mutating upstream manifests.

### FR5. Packet Status And Immutability

The workflow must protect handed-off packets from silent drift.

Acceptance:

- Valid packet statuses are documented.
- `ready_for_next_role` packets are immutable.
- If a handed-off packet needs changes, a new packet version must be created.
- `latest.json` is a pointer only.
- Lock generation is available through local validation tooling.

### FR6. Chain Selection

The workflow must define when to use each chain.

Acceptance:

- `full-chain`, `mini-chain`, `patch-chain`, `docs-only-chain`, and `research-only` are documented.
- High-risk work routes to `full-chain`.
- Narrow implementation fixes can use `patch-chain`.
- Documentation-only work can use `docs-only-chain` only when it does not change runtime behavior, schema, permission, release status, or user-facing capability.

### FR7. Local Validation

The template must include local validation tooling.

Acceptance:

- Validator checks manifest shape.
- Validator checks required document existence.
- Validator rejects draft packet consumption unless explicitly allowed.
- Validator can print a packet lock with file hashes.

### FR8. Test Coverage For Workflow Integrity

The repository must include tests that protect the workflow contract.

Acceptance:

- Tests verify required role files and templates.
- Tests verify orchestrator policy.
- Tests verify packet validation contract.
- Tests verify source map coverage.
- Tests verify status transition protocol.

## 9. Non-Goals

MVP non-goals:

- Building a Codex runtime.
- Building a multi-agent execution engine.
- Providing a hosted SaaS workflow system.
- Replacing GitHub Issues, Linear, Jira, or code review tools.
- Automating every role transition without user confirmation.
- Automatically executing the coding workflow end to end.
- Switching through multiple roles inside one conversation as the default workflow.
- Making chat memory authoritative.
- Allowing implementation from chat-only instruction.
- Supporting third-party plugins or network APIs.
- Enforcing all rules through code from day one.

## 10. Success Metrics

Initial success metrics:

- A user can copy the workflow template into a target project and understand how to start.
- A user can select the correct chain for a milestone without asking for hidden context.
- A role can consume an upstream packet using only the manifest and listed documents.
- Implementer start is blocked unless upstream scope is explicit.
- Reviewer can audit the packet chain, not only code changes.
- Local validation catches malformed manifests and strict-handoff violations.
- Existing tests pass in a documented local environment.

## 11. Product Quality Bar

Code-role should be evaluated by whether it improves real Codex delivery quality.

The workflow is useful only if it:

- Reduces skipped requirements.
- Reduces implementation outside approved scope.
- Makes handoffs inspectable.
- Makes review more rigorous.
- Keeps local project boundaries clear.
- Adds process control without excessive overhead for small tasks.

If the workflow becomes too heavy for patch-level changes, the chain policy must preserve a lightweight path.

## 12. Current Known Gaps

Observed from the current repository state:

- The local environment used during initial review did not have `pytest` installed; tests require installing the `test` optional dependency from `pyproject.toml`.
- The validator checks single-packet structure, but does not yet validate a full packet chain.
- No complete example milestone demonstrates a real end-to-end handoff.

## 13. Suggested Near-Term Iteration

Recommended next iteration:

1. Initialize the repository and push the baseline to GitHub.
2. Add full-chain validation to the local validator or a companion tool.
3. Add one example milestone with packet chain samples.
4. Add a practical usage guide for installing Code-role into a target project.
5. Tighten docs so every role's template, manifest, tests, and source-map entries stay aligned.

## 14. Open Decisions

Open product decisions:

- Should Code-role remain a local template only, or also become a packaged initializer?
- Should workflow files stay excluded from target product repos by default, or should teams be able to promote them into repo standards through a documented path?
- Should chain validation remain a Python script, or should it become part of a CLI?
- Should strict-handoff packet locks be generated manually by validator command, or automatically when a packet becomes `ready_for_next_role`?
- Should example milestones be synthetic demos or based on real coding tasks?
- Should role conversations be run manually by the user, or should there eventually be a launcher that generates the correct initialization prompt?
