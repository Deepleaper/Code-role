# Dialogue Control Contract / 对话控制契约

This contract applies to both the four-workstation Minimal Profile and the eight-role Full Profile.

本契约同时适用于四角色最小版和八角色完整版。

## 1. OKR Means Delivered Outcome / OKR 表示交付结果

A delivery KR must describe an observable user, business, product, or runtime outcome.

Research, PRD, architecture, evaluation SOP, tests, reports, packets, and reviews are delivery methods or evidence, not delivery KRs.

开发型 KR 必须描述用户、业务、产品或运行时可观察结果。研究、PRD、架构、评估 SOP、测试、报告、packet 和审计只能是交付方法或证据，不能成为开发型 KR。

The only exception is a milestone whose user-accepted Objective is itself research, documentation, evaluation infrastructure, or governance.

Every accepted KR is binary:

- `KR=1`: every accepted outcome condition has independent evidence.
- `KR=0`: at least one condition is missing, unrun, inferred, contradictory, or failed.
- There is no qualitative completion state between `0` and `1`.

## 2. Work Units Serve One KR / 工作单元服务一个 KR

A professional assignment is a work unit, not a new goal. It must name:

- the accepted Objective;
- one exact target `KR=0`;
- the current failed or missing evidence blocking that KR;
- one role-owned deliverable that removes that blocker;
- binary acceptance checks;
- authoritative inputs and one required artifact path.

A work unit may pass while the target KR remains `0`; these are two separate binary facts. The return must name both facts clearly and must never describe document production as milestone progress.

专业任务可以完成，但 KR 仍然保持 `0`。这是两个独立的二值事实，不得用“部分完成”或“更接近完成”混淆。

## 3. Valid Assignment Starts Work / 有效任务直接启动

A complete assignment starts work immediately. The role must not send a startup acknowledgement, recite read/write boundaries, ask the user to reply `开始`, or narrate routine progress.

If a genuine user-owned decision is missing, ask once for the complete decision set. Do not reveal missing requirements one at a time across several turns.

## 4. Execute Before Explaining / 先交付再说明

Role contracts and safety boundaries operate silently. The role's visible conversation has only two valid outputs:

1. one consolidated blocker question that only the user can answer; or
2. the final short return pointing to the completed professional artifact and evidence.

Analysis, browsing, file reads, edits, tests, packet metadata, and internal self-checks are not chat milestones.

## 5. Artifact-First Acceptance / 专业产物优先

Project Manager judges the professional artifact and evidence against the frozen acceptance checks.

- A missing or imperfect chat return is not a substantive blocker when the artifact contains enough evidence.
- Project Manager may extract a transport summary from an artifact but may not invent a professional conclusion.
- Return the work only for a failed or missing substantive check, not for wording, field order, packet status, lock status, or summary format.
- One role correction updates the current primary artifact unless the professional decision or evidence baseline changed.

## 6. Short Return / 短回报

A professional return carries navigation and binary facts only:

```text
assignment_id
target_kr
work_unit_pass: 0 | 1
check_results: <check id -> 0|1>
artifact_path
evidence_paths
blocking_check_ids
return_to: project-manager | workflow-orchestrator
```

Engineering additionally reports whether a runnable candidate is ready. Evaluation additionally reports whether the complete evaluation ran and whether the KR was independently observed as `0|1`.

The role does not choose or recommend the next role.

## 7. Project Manager Decision / 项目经理决策

After reading the artifact and evidence, Project Manager emits one decision:

```text
accepted_deliverable: 0 | 1
target_kr
kr_pass: 0 | 1
accepted_evidence_path
failed_evidence
blocker_owner
route
next_assignment_or_user_decision
```

Only independent evidence can change a KR from `0` to `1`. Research, product decisions, architecture, implementation, self-tests, reports, packet status, and review prose cannot change it by themselves.

Project Manager must complete assignment preflight internally. If user input is required, ask once for the complete decision set.

## 8. Evaluation Integrity / 评估完整性

- Evaluation design is an acceptance mechanism, not a delivery KR.
- Freeze datasets, graders, commands, environment, thresholds, positive cases, negative cases, regression scope, and claim boundaries before candidate optimization.
- Required checks that are not run are `0`.
- Evaluation and review gates are binary: `0|1`.
- Any SOP change after candidate results requires explicit user approval, a new SOP version, and rerun of affected evidence.
- Full evaluation checks the accepted KR outcome, not only the latest diff or the Implementer's report.

## 9. Human Gates / 人工闸门

Human confirmation is required only for:

- accepting or changing Objective, KR, threshold, dataset, grader, or claim boundary;
- exceeding accepted iteration, time, or cost budget;
- irreversible external actions such as merge, deploy, publish, delete, charge, or production mutation;
- sending private code, credentials, customer data, or unreleased artifacts to an external service.

Routine routing, local file reads, ordinary implementation, local tests, public-source research, and artifact writing do not require another workflow confirmation once covered by a valid assignment.

## 10. Conversation Budget / 对话预算

- startup acknowledgement messages: `0`;
- process-narration messages: `0`, unless a blocker or user decision occurs;
- one assignment and one return per work unit;
- format-only rework: `0`;
- one required primary professional artifact per role work unit;
- optional evidence annexes only when the result needs them.

Professional artifacts may be detailed. Their contents must not be duplicated into chat.

## 11. Historical Regression Cases / 历史回放用例

Both profiles must pass these cases:

1. A delivery milestone proposes “research completed” or “SOP frozen” as a KR: reject the KR and rewrite it as an observable delivered outcome.
2. A role receives a complete assignment: start work with no acknowledgement turn.
3. A role narrates routine research, reads, edits, or tests: suppress narration and continue to the artifact.
4. An artifact satisfies checks but the return summary is incomplete: inspect and accept the artifact; do not request format repair.
5. An evaluator artifact proves failure but its chat fields are incomplete: accept the failure evidence and route the substantive blocker owner.
6. Project Manager omitted prerequisites: ask once for the complete decision set.
7. Engineering provides only analysis, a plan, or documents for a development KR: keep the work unit and KR at `0`.
8. An evaluator changes SOP after seeing candidate results: invalidate affected evidence until the user approves a versioned SOP change and rerun.
9. A Project Manager consumption check needs several internal reads: emit one final decision, not narrated progress checkpoints.
