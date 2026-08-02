# Milestone Contract / 里程碑合同

Workflow Orchestrator maintains one accepted milestone contract. This contract defines the result to deliver; it does not prescribe a fixed role chain.

项目经理维护一份已确认的里程碑合同。它定义要交付的结果，不规定固定的角色链。

```text
milestone:
objective:
objective_accepted: 0 | 1

key_results:
| KR | Observable user/business/product/runtime outcome | Numeric threshold | Required independent evidence | Pass (0/1) |
| --- | --- | --- | --- | ---: |

non_goals:
- item:

claim_boundary:
- allowed:
- forbidden:

iteration_limit_per_kr: 3
accepted_time_or_cost_budget:
```

## Outcome Rule / 结果规则

**A delivery KR must describe an observable user, business, product, or runtime outcome.**

**Research, PRD, architecture, evaluation SOP, tests, reports, packets, and reviews are delivery methods or evidence, not delivery KRs.**

交付 KR 必须描述可观测的用户、业务、产品或运行时结果。调研、PRD、架构、评估 SOP、测试、报告、packet 和 review 只是达成结果的方法或证据，不是交付 KR。

Only one exception exists: an artifact may be a KR when the user explicitly accepts that artifact itself as the milestone's external deliverable.

唯一例外：用户明确确认某份文档或工件本身就是里程碑对外交付物。

## Binary Rules / 二值规则

- Objective, KR definitions, thresholds, datasets, graders, and claim boundaries require user acceptance.
- Every KR remains `0` until every required observation is independently evidenced.
- Missing, unrun, inferred, stale, or qualitative required evidence is `0`.
- A role work unit can pass while the target KR remains `0`; work-unit completion never substitutes for outcome evidence.
- Residual work becomes a new accepted KR, an explicit non-goal, or remains failed. There is no partial KR state.

## Work Unit Assignment / 工作单元任务

Workflow Orchestrator routes the owner of one exact failed or missing evidence item. The assignment contains only:

项目经理只路由一个精确的失败或缺失证据项，任务书只包含：

```text
objective
target_kr
current_failed_evidence
role_deliverable
acceptance_checks
authoritative_inputs
required_artifact_path
```

- `current_failed_evidence` must identify one observed failure, not a broad topic.
- `role_deliverable` describes what this role must produce to repair or decide that failure.
- `acceptance_checks` are binary and observable.
- `required_artifact_path` names one primary professional artifact. Annexes are optional.
- A complete assignment starts the role immediately. Routine startup acknowledgements and permission loops are invalid.

## Acceptance / 接受与路由

Workflow Orchestrator reads the primary artifact and its evidence, then makes one decision:

```text
accept
return_to_same_role
route_failed_evidence_owner
request_user_decision
```

Formatting, packet metadata, manifest status, lock files, or a short chat-summary defect cannot overturn substantively sufficient evidence. They may be corrected in place without starting another role loop.

## Drift Check / 漂移检查

For every submitted artifact:

- Does it address the accepted Objective and exact `target_kr`?
- Does it repair or decide `current_failed_evidence`?
- Does it satisfy every binary `acceptance_check` with cited evidence?
- Does it preserve non-goals and claim boundaries?
- Does it distinguish observed evidence, professional judgment, inference, and unknown?
- If the KR remains `0`, does the next failed evidence item identify a concrete owner?

## Closure / 关闭

Milestone pass is `1` only when every accepted KR is `1`, all required independent outcome evidence exists, any required final audit passes, and irreversible release actions follow the target project's normal human approval process.

里程碑只在所有已确认 KR 都为 `1`、必需的独立结果证据齐全、必需的最终审计通过，且不可逆发布动作遵守目标项目原有人工审批流程时才为 `1`。
