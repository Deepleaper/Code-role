# Dialogue Control Contract / 对话控制契约

This contract applies to both the four-workstation Minimal Profile and the eight-role Full Profile.

本契约同时适用于四角色最小版和八角色完整版。

## 1. OKR Means Delivered Outcome / OKR 表示交付结果

Both profiles follow [One Project OKR Standard](okr-standard.md). `KR` is the only outcome namespace. `STEP` is a separate Engineering execution namespace and is not another OKR.

A delivery KR must describe an observable user, business, product, or runtime outcome.

Research, PRD, architecture, evaluation SOP, tests, reports, packets, and reviews are delivery methods or evidence, not delivery KRs.

开发型 KR 必须描述用户、业务、产品或运行时可观察结果。研究、PRD、架构、评估 SOP、测试、报告、packet 和审计只能是交付方法或证据，不能成为开发型 KR。

The only exception is a milestone whose user-accepted Objective is itself research, documentation, evaluation infrastructure, or governance.

Every accepted KR is binary:

- `KR=1`: every accepted outcome condition has independent evidence.
- `KR=0`: at least one condition is missing, unrun, inferred, contradictory, or failed.
- There is no qualitative completion state between `0` and `1`.

## 2. Complete Contracts, Engineering Decomposition / 完整契约与工程分解

Project Manager and Product Strategy are global roles:

- Project Manager defines one complete Project OKR with `KR-1...KR-N`.
- Product Strategy completes one Product Contract under the existing `KR-1...KR-N`; it creates no second Objective or KR set.
- Neither role repeatedly routes or designs one isolated KR at a time.

Engineering is the decomposition owner. It consumes the accepted Project OKR and Product Contract, then defines `STEP-1...STEP-N` for ordered implementation phases. STEP completion is candidate evidence only; it never passes a KR.

Independent Evaluation consumes the complete runnable candidate and evaluates the full accepted KR scope. It does not evaluate an unfinished implementation, one STEP, or the latest diff.

项目经理和产品策略负责完整全局契约，只有工程负责按实际依赖拆分执行 STEP。任何 STEP 完成均不等于产品或里程碑通过。

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
delivery_stage
work_unit_pass: 0 | 1
check_results: <check id -> 0|1>
artifact_path
evidence_paths
blocking_check_ids
return_to: project-manager | workflow-orchestrator
```

Product additionally reports whether the complete Product Contract covers every KR. Engineering reports STEP status and whether the complete runnable candidate is ready. Evaluation reports whether the complete evaluation ran, every KR result, and whether the milestone was independently observed as `0|1`.

The role does not choose or recommend the next role.

## 7. Project Manager Decision / 项目经理决策

After reading the artifact and evidence, Project Manager emits one decision:

```text
accepted_deliverable: 0 | 1
delivery_stage
project_okr_accepted: 0 | 1
product_contract_accepted: 0 | 1
candidate_ready: 0 | 1
evaluation_executed: 0 | 1
milestone_observed_pass: 0 | 1
accepted_evidence_path
route
next_assignment_or_user_decision
```

For software delivery, routing order is mandatory: complete Project OKR, complete Product Contract, Engineering candidate, Independent Evaluation, then closure. Only independent evidence can change a KR from `0` to `1`. Research, product decisions, architecture, implementation, STEP self-tests, reports, packet status, and review prose cannot change it by themselves.

Project Manager must complete assignment preflight internally. If user input is required, ask once for the complete decision set.

## 8. Evaluation Integrity / 评估完整性

- Evaluation design is an acceptance mechanism, not a delivery KR.
- Independent Evaluation starts only after Engineering provides a complete runnable candidate and `candidate_ready_for_independent_evaluation=1`.
- The evaluator derives the executable SOP from the accepted Project KRs and Product Contract, records it before inspecting candidate results, then runs the full evaluation.
- Product acceptance thresholds and claim boundaries are frozen before Engineering; the evaluator cannot invent or loosen them.
- Required checks that are not run are `0`.
- Evaluation and review gates are binary: `0|1`.
- Any SOP change after candidate results requires explicit user approval, a new SOP version, and rerun of affected evidence.
- Full evaluation checks every accepted KR, not one STEP, the latest diff, or the Implementer's report.

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
- one assignment and one return per professional delivery stage;
- format-only rework: `0`;
- one required primary professional artifact per role work unit;
- optional evidence annexes only when the result needs them.

Professional artifacts may be detailed. Their contents must not be duplicated into chat.

## 11. Historical Regression Cases / 历史回放用例

Both profiles must pass these cases:

1. A delivery milestone proposes “research completed” or “SOP frozen” as a KR: reject it and rewrite it as an observable delivered outcome.
2. A role receives a complete assignment: start work with no acknowledgement turn.
3. A role narrates routine research, reads, edits, or tests: suppress narration and continue to the artifact.
4. An artifact satisfies checks but the return summary is incomplete: inspect and accept the artifact; do not request format repair.
5. An evaluator artifact proves failure but its chat fields are incomplete: accept the failure evidence and route the substantive blocker owner.
6. Project Manager omitted prerequisites: ask once for the complete decision set.
7. Project Manager or Product Strategy attempts to route one isolated KR: reject the slice and complete the global contract.
8. Engineering provides only analysis, a plan, or documents: keep candidate readiness at `0`.
9. Independent Evaluation is assigned before a runnable candidate exists: reject the assignment and route Engineering.
10. An evaluator changes SOP after seeing candidate results: invalidate affected evidence until the user approves a versioned SOP change and rerun.
11. A Project Manager consumption check needs several internal reads: emit one final decision, not narrated progress checkpoints.
