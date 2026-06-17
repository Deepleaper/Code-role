# Role Completion Contract / 角色完成契约

This contract makes role completion binary and evidence-based.

本契约把角色完成状态改为二值、可验证、可审计。

## Rule / 规则

`role_completion_status` has only two valid values:

`role_completion_status` 只有两个合法值：

```text
1 = all assigned completion conditions are met with concrete evidence
0 = one or more assigned completion conditions are unmet, missing evidence, or unverifiable
```

There is no intermediate completion state.

不存在中间完成状态。

## Required Completion Block / 必填完成块

Every execution role final response must include this block before the Orchestrator consumption-check summary:

每个执行角色的完成回复必须在 Orchestrator 消费检查摘要前包含本块：

```text
role_completion_status:
1 | 0

assigned_completion_conditions_total:
<integer>

assigned_completion_conditions_met:
<integer>

unmet_completion_conditions:
none | <condition id list>

completion_evidence:
- condition_id: <id>
  met: 1 | 0
  evidence: <packet file, repo file, command output, user confirmation, or explicit not_applicable rule>

forbidden_completion_claim_used:
true | false
```

## Completion Calculation / 完成计算

The completion calculation is mechanical:

完成计算必须是机械规则：

```text
if assigned_completion_conditions_met == assigned_completion_conditions_total
and unmet_completion_conditions == none
and every required condition has concrete evidence
and forbidden_completion_claim_used == false:
  role_completion_status = 1
else:
  role_completion_status = 0
```

If evidence is missing, unknown, inferred, or only qualitative, the condition is not met.

如果证据缺失、未知、仅为推断或只有定性描述，该条件计为未满足。

## Forbidden Completion Language / 禁用完成表述

These phrases must not be used as completion proof:

以下表述不能作为完成证据：

- mostly complete
- basically done
- moved the milestone forward
- closer to completion
- enough for now
- looks good
- directionally correct
- pass_with_residual_risk as completion
- partial completion
- largely aligned
- mostly aligned

## Gate Rule / 门禁规则

Orchestrator may route to the next role only when:

项目经理只有在以下条件全部满足时才能路由下一角色：

```text
role_completion_status = 1
assigned_completion_conditions_met = assigned_completion_conditions_total
unmet_completion_conditions = none
forbidden_completion_claim_used = false
```

If any field fails, Orchestrator must return the work to the same role or ask the user to revise the milestone contract.

任一字段不满足时，项目经理必须打回同一角色修正，或要求用户先修改 milestone contract。

## Process Stop Rule / 流程停止规则

The workflow is milestone control. If one role does not complete its assigned milestone conditions, the workflow stops at that role.

整个流程就是 milestone 管控。任一角色未完成自己被分配的 milestone 条件，流程就停在该角色。

```text
if current_role.role_completion_status = 0:
  next_role_start_allowed = false
  final_packet_index_update_allowed = false
  milestone_closure_allowed = false
```

User acceptance can accept an incomplete packet as a draft discussion artifact, but it cannot convert `role_completion_status=0` into completed handoff.

用户可以接受未完成 packet 作为草稿讨论材料，但不能把 `role_completion_status=0` 转成已完成交接。

To continue, one of two actions must happen:

继续推进只能发生以下两种动作之一：

1. The same role revises the output until `role_completion_status=1`.
2. The user changes the milestone contract, then the role recalculates completion against the new contract.

No other role may continue the chain from an incomplete output.

其他角色不能基于未完成输出继续链路。

## Implementer-Specific Rule / Implementer 专项规则

Code changes do not equal role completion.

代码改动不等于角色完成。

Implementer may report an action status separately:

Implementer 可以单独报告执行状态：

```text
implementation_action_status:
code_changed | docs_changed | no_change | blocked
```

But `role_completion_status` is still `1` only when every assigned implementation condition and verification condition is met with concrete evidence.

但只有所有指定实现条件和验证条件都有具体证据满足时，`role_completion_status` 才能是 `1`。
