# Discussion-First Protocol / 先决策后执行协议

Code-role is discussion-first because important product, architecture, evaluation, budget, and irreversible-action decisions are explicit before execution. It is not confirmation-first.

Code-role 强调重要决策先明确，不代表每个角色都要先发送确认、等待“开始”。

## Complete Assignment / 完整任务

A complete Project Manager assignment contains the fields required by [Dialogue Control Contract](../dialogue-control.md) and the selected role's assignment template.

When complete:

- the role starts immediately;
- no startup acknowledgement is sent;
- no read/write/forbidden-scope recital is sent;
- no extra `开始` confirmation is requested;
- routine progress is not narrated;
- the role writes the assignment's one primary professional artifact and sends one short return.

## Incomplete Assignment / 不完整任务

If a substantive decision is missing, the role sends one consolidated blocker request containing:

```text
assignment_valid: 0
missing_decisions: <complete list>
why_each_decision_blocks: <short reason>
owner: project-manager | user
```

Do not ask for missing fields one at a time. Do not create the primary artifact until the blocker is resolved.

## Conversation Scope / 对话范围

Each role keeps its professional boundary. An unrelated request is returned to Project Manager with a one-line scope conflict; the role does not choose the next role or write another role's output.

Non-Implementer roles write documents only. Implementer may modify project files reasonably necessary for a valid assignment. Task-specific exclusions belong in the assignment only when genuinely required; old packet scopes do not accumulate into permanent restrictions.

## Network Boundary / 联网边界

Every role may use public internet sources relevant to its assignment and must label external evidence. Separate approval is required only for authenticated/private resources, paid provider execution outside the accepted budget, remote code execution, or external transmission of private project data.

## Human Discussion Gates / 人工讨论闸门

Stop for user decision only when changing:

- Objective or KR;
- accepted product behavior, threshold, dataset, grader, or claim boundary;
- public contract, security boundary, privacy boundary, or production mutation;
- accepted iteration, time, or cost budget;
- an irreversible external action.

Routine role routing, packet writing, local implementation, local tests, public research, and normal project Git practice do not require another Code-role confirmation after a valid assignment is issued.

## Artifact-First Handoff / 交付物优先交接

The assignment-named primary professional artifact is the handoff object. Optional packet documents may provide provenance or evidence annexes. The short return points to the primary artifact. Project Manager reads that artifact and judges the frozen checks even when the short return is imperfect.

Default handoff does not require `ready_for_next_role`, `packet.lock.json`, or a separate readiness conversation. Strict handoff remains optional for explicitly requested audit scenarios.
