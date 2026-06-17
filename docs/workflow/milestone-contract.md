# Milestone Contract / 里程碑契约

The Milestone Contract is the hard goal anchor for a workflow milestone.

里程碑契约是一个 milestone 的硬目标锚点。

It exists because milestone alignment cannot rely on repeated chat reminders. Orchestrator, every execution role, Test Evaluator, and Reviewer must use the same confirmed contract when judging whether work has drifted.

它存在的原因是：目标对齐不能依赖反复聊天提醒。项目经理、每个执行角色、评估师和审计评审都必须使用同一份已确认契约判断工作是否漂移。

## Authority / 权威性

In a target project, the active contract lives at:

```text
code-role/workflow/orchestrator/milestone-contract.md
```

在目标项目中，当前有效契约位于：

```text
code-role/workflow/orchestrator/milestone-contract.md
```

Orchestrator owns this file. The user must confirm a milestone contract before Orchestrator routes the first execution role for that milestone.

该文件由项目经理维护。项目经理在路由第一个执行角色前，必须先让用户确认当前 milestone contract。

## Required Fields / 必填字段

```text
milestone_name:
business_goal:
delivery_goal:
success_criteria:
role_completion_conditions:
non_goals:
in_scope:
out_of_scope:
hard_prohibitions:
required_roles:
allowed_chain:
evidence_requirements:
drift_detection_questions:
correction_policy:
closure_rule:
```

## Hard Rules / 硬规则

- If `milestone-contract.md` is missing or unconfirmed, Orchestrator must not route the first execution role.
- Orchestrator checks this contract before packet structure, packet status, or routing convenience.
- Every role completion summary must include a binary `role_completion_status`.
- `role_completion_status=1` is allowed only when all assigned completion conditions are met with concrete evidence.
- If any assigned condition is missing, unverifiable, or only qualitatively described, `role_completion_status` must be `0`.
- If a role output changes the business goal, delivery goal, scope, or closure rule, Orchestrator must stop routing and ask whether the milestone contract should change.
- Reviewer audits against the original confirmed contract, not against a later role's rewritten goal.

- 如果 `milestone-contract.md` 缺失或未确认，项目经理不得路由第一个执行角色。
- 项目经理先检查本契约，再检查 packet 结构、packet 状态或路由便利性。
- 每个角色完成摘要必须包含二值 `role_completion_status`。
- 只有所有指定完成条件都有具体证据满足时，`role_completion_status=1` 才成立。
- 任一指定条件缺失、不可验证或只有定性描述时，`role_completion_status` 必须是 `0`。
- 如果角色产出改变业务目标、交付目标、范围或关闭规则，项目经理必须停止路由并询问是否调整 milestone contract。
- Reviewer 以最初确认的契约审计，不以后续角色改写后的目标审计。

## Template / 模板

```text
# Milestone Contract

status: draft | confirmed | superseded
confirmed_by: user | unknown
confirmed_at: YYYY-MM-DD | unknown

milestone_name:
<short stable milestone id>

business_goal:
<what business or project outcome this milestone must achieve>

delivery_goal:
<what concrete deliverable must exist when this milestone is done>

success_criteria:
- <criterion 1>
- <criterion 2>
- <criterion 3>

role_completion_conditions:
- id: <role-condition-1>
  role: <role id>
  required: true
  condition: <binary condition that must be met>
  evidence_required: <packet file, repo file, command output, user confirmation, or external citation>
- id: <role-condition-2>
  role: <role id>
  required: true
  condition: <binary condition that must be met>
  evidence_required: <packet file, repo file, command output, user confirmation, or external citation>

non_goals:
- <explicitly excluded outcome or task>
- <explicitly excluded claim>

in_scope:
- <allowed work area>
- <allowed evidence area>

out_of_scope:
- <excluded work area>
- <excluded evidence area>

hard_prohibitions:
- <action or claim that blocks routing if touched>

required_roles:
- workflow-orchestrator
- researcher | not_applicable
- product-prd | not_applicable
- architect | not_applicable
- code-context | not_applicable
- implementer | not_applicable
- test-evaluator | not_applicable
- reviewer | not_applicable

allowed_chain:
full-chain | mini-chain | patch-chain | docs-only-chain | research-only

evidence_requirements:
- <required packet evidence, repo evidence, command evidence, external reference, or user decision>

drift_detection_questions:
- Does this output answer the milestone business goal?
- Are all assigned role completion conditions met with concrete evidence?
- Is `role_completion_status` exactly `1` or `0`?
- Is `assigned_completion_conditions_met` equal to `assigned_completion_conditions_total`?
- Is `unmet_completion_conditions` equal to `none`?
- Did it introduce any out-of-scope claim?
- Did it touch any hard prohibition?
- Did it use forbidden completion language such as "mostly complete", "closer to completion", or "pass_with_residual_risk" as completion?

correction_policy:
- If role output drifts: return to the same role for revision.
- If the milestone itself should change: ask user to revise this contract first.
- If evidence is missing: return to the role responsible for that evidence.
- If scope is unclear: hold routing.

closure_rule:
<what must be true before Reviewer may recommend milestone closure>
```
