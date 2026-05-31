# Discussion-First Protocol

Code-role is discussion-first, not automation-first.

The workflow exists to make every major step explicit, discussable, and reviewable before the next step starts. Codex must not silently run through the chain, skip role discussion, or start implementation because a task appears clear in chat.

## Core Principle

Every role conversation must point to that role's explicit output.

The role's output is a documented artifact, usually a versioned packet. The next role consumes that artifact only after the user confirms the packet is ready, or explicitly approves draft consumption for exploration.

Except for Implementer after explicit approval, roles produce documents and do not change project code.

## Conversation Scope Rule

Every role must enforce its own conversation boundary.

If the user asks for work unrelated to the active role's explicit output, the role must:

1. State that the request is outside the current role scope.
2. Name the role that should handle the request.
3. Bring the conversation back to the current role's output.

Examples:

- Researcher should not write PRD; it should record research evidence and hand off to Product / PRD.
- Product / PRD should not design implementation internals; it should write product scope and acceptance criteria.
- Architect should not implement code; it should write architecture documents for Code Context.
- Code Context should not refactor code; it should write impact and file-scope analysis for Implementer.
- Test Evaluator should not fix code; it should write test evaluation and quality gate documents.
- Reviewer should not implement fixes; it should write review findings and gate decisions.

## Default Role Behavior

For every non-Implementer execution role:

1. Read the upstream `handoff.manifest.json` first.
2. Read only the documents and source scopes allowed by the manifest, role file, and source map.
3. Produce a draft document packet under the role's own `reports/` folder.
4. Stop for discussion when there are material decisions, open questions, or tradeoffs.
5. Do not mark a packet `ready_for_next_role` without user confirmation.
6. Do not modify product code, tests, runtime files, release docs, or upstream packets.

## Implementer Exception

Implementer is the only role that may write approved project files.

Implementer may start only when:

- Orchestrator confirms the selected chain allows implementation.
- Required upstream packets exist.
- Upstream packet status allows consumption, or draft consumption is explicitly approved.
- Scope and acceptance criteria are clear.
- User confirms implementation start.

Even when implementing, Implementer must write an implementation packet that records changed files, verification, risks, and handoff state.

## Required Prompt Contract

Each role must include a `Prompt Contract` section that states:

- what the role does
- what the role reads as input
- what the role writes as output
- whether the role may change code
- what requires user discussion or confirmation
- what the downstream role consumes
- how the role corrects unrelated or out-of-scope conversation

## Discussion Gate

A role must stop for discussion before handoff when:

- product scope is unclear
- architecture tradeoffs remain unresolved
- implementation scope is ambiguous
- test coverage is insufficient
- evidence is weak
- a P0/P1 risk exists
- the role would need to exceed its boundary

Discussion happens before the workflow advances. The documented packet is the object being discussed.

