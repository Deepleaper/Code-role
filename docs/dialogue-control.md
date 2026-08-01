# Dialogue Control Contract / 对话控制契约

This contract applies to both the four-workstation Minimal Profile and the eight-role Full Profile.

本契约同时适用于四角色最小版和八角色完整版。

## 1. Control The Result / 控制结果

The workflow controls the accepted milestone and its observable evidence. It does not control progress by requiring more chat, more status files, or perfect transport formatting.

工作流控制的是已确认 milestone 及其可观察证据，不通过增加聊天、状态文件或完美流转格式制造进度。

- Every accepted KR is `0` or `1`.
- Missing, unrun, inferred, or qualitative evidence is `0` for a required check.
- A role's self-report never changes a KR by itself.
- Only the Project Manager updates milestone state from accepted evidence.
- Implementation evidence is candidate evidence until independently evaluated.

## 2. Three Information Layers / 三层信息

Each role conversation has only three active layers:

1. **Stable role contract:** read when the conversation is configured or refreshed.
2. **Current assignment:** variable milestone work issued by Project Manager.
3. **Professional artifact plus short return:** detailed work lives in files; chat carries only the result pointer.

Do not repeat stable role rules, the complete milestone history, or professional attachment content in every assignment and return.

不得在每份任务书和回报中重复稳定角色规则、完整 milestone 历史或专业附件正文。

## 3. Valid Assignment Starts Work / 有效任务直接启动

A complete assignment contains:

- assignment ID;
- milestone and one primary target KR or one full-milestone audit objective;
- role objective and one professional question;
- authoritative input paths;
- frozen required checks and evidence expectations;
- required output path;
- stop condition.

The role starts immediately when these fields are present. It does not send a startup acknowledgement, recite read/write boundaries, or ask the user to reply `开始`.

这些字段齐全时角色立即开始，不发送启动确认，不复述读取/写入边界，也不要求用户回复“开始”。

If a genuine task decision is missing, the role asks one consolidated blocker question. It must not reveal missing requirements one at a time across several turns.

## 4. Artifact-First Acceptance / 专业附件优先

Project Manager judges the professional artifact and evidence against the frozen checks.

- A missing or imperfect chat return is not a substantive blocker when the artifact contains enough evidence.
- Project Manager may extract a transport summary from an artifact but may not invent a professional conclusion.
- Return the work only for a failed or missing substantive check, not for wording, field order, packet status, lock status, or summary format.
- A role correction updates the current artifact. Create a new version only when a professional decision or evidence baseline changes.

项目经理必须审阅专业附件本身。格式缺失不能覆盖专业事实，也不能成为无效往返的理由。

## 5. Role Return / 角色回报

The short return contains only:

```text
assignment_id
assignment_pass: 0 | 1
check_results: <check id -> 0|1>
artifact_paths
evidence_paths
substantive_blockers
return_to: project-manager | workflow-orchestrator
```

The role does not choose or recommend the next role. Routing belongs to Project Manager.

角色不得选择或建议下一角色，路由只属于项目经理。

## 6. Project Manager Decision / 项目经理决策

After reading the artifact, Project Manager emits one decision:

```text
accepted_artifact
target_kr_before: 0 | 1
target_kr_after: 0 | 1
evidence_basis
failed_check_ids
blocker_owner
route
next_assignment_or_user_decision
```

Project Manager must complete assignment preflight internally before issuing work. If user input is required, ask once for the complete decision set. Requirements discovered after assignment start are a Project Manager definition defect, not a role failure.

## 7. Evaluation Freeze / 评估冻结

- Freeze datasets, graders, commands, environment, thresholds, positive cases, negative cases, regression scope, and claim boundaries before candidate optimization.
- Required checks that are not run are `0`.
- Evaluation gate and Reviewer gate are binary: `0` or `1`.
- Diagnostic risks and blocker codes may be recorded, but they do not create a third completion state.
- Any SOP change after candidate results requires explicit user approval, a new SOP version, and rerun of affected evidence.

## 8. Human Gates / 人工闸门

Human confirmation is required only for:

- accepting or changing Objective, KR, threshold, dataset, grader, or claim boundary;
- exceeding accepted iteration, time, or cost budget;
- irreversible external actions such as merge, deploy, publish, delete, charge, or production mutation;
- sending private code, credentials, customer data, or unreleased artifacts to an external service.

Routine routing, local file reads, ordinary implementation, local tests, public-source research, and artifact writing do not require another workflow confirmation once covered by a valid assignment.

## 9. Conversation Budget / 对话预算

- startup acknowledgement messages: `0`;
- process-narration messages: `0`, unless a blocker or user decision occurs;
- PM assignment: at most 20 body lines, excluding path and check tables;
- role return: at most 12 body lines, excluding the check table;
- PM decision: at most 12 body lines, followed by one copy-ready assignment only when routing;
- format-only rework: `0`;
- manual transports per role iteration: one assignment and one return.

Professional artifacts may be as detailed as the work requires. Their contents must not be duplicated into chat.

## 10. Historical Regression Cases / 历史回放用例

Both profiles must pass these cases:

1. An artifact satisfies checks but the return summary is incomplete: inspect and accept the artifact; do not request format repair.
2. An evaluator artifact proves failure but its chat fields are incomplete: accept the failure evidence and route the substantive blocker owner.
3. Project Manager omitted evaluation prerequisites: stop before assignment or ask one consolidated decision set; do not discover requirements over multiple role revisions.
4. A role receives a complete assignment: start work with no acknowledgement turn.
5. An evaluator changes SOP after seeing candidate results: invalidate affected evidence until the user approves a versioned SOP change and rerun.
6. A Project Manager consumption check needs several internal reads: emit one final decision, not narrated progress checkpoints.
