# Orchestrator 轻量消费检查摘要 / Lightweight Consumption Check Summary

执行角色完成 packet 后，必须在同一条完成回复的末尾追加这个短摘要，供用户直接复制给 Workflow Orchestrator / 项目经理。

After an execution role finishes a packet, it must append this short summary at the end of the same completion response so the user can copy it to Workflow Orchestrator / Project Manager.

这个摘要不授权 Orchestrator 修改角色 packet、创建下游 packet、执行 Git 命令或修改业务文件。

This summary does not authorize the Orchestrator to modify the role packet, create downstream packets, run Git commands, or change business files.

```text
请执行 Orchestrator 轻量消费检查。
Please run the Orchestrator lightweight consumption check.

completed_role:
{CURRENT_ROLE}

milestone:
{MILESTONE}

milestone_contract:
{MILESTONE_CONTRACT_PATH}

packet:
{CURRENT_PACKET_PATH}

handoff_manifest:
{CURRENT_MANIFEST_PATH}

handoff manifest path:
same as handoff_manifest above

packet_status:
{PACKET_STATUS}

role_completion_status:
1 | 0

assigned_completion_conditions_total:
{TOTAL_REQUIRED_CONDITIONS_INTEGER}

assigned_completion_conditions_met:
{MET_REQUIRED_CONDITIONS_INTEGER}

unmet_completion_conditions:
none | {UNMET_CONDITION_IDS}

completion_evidence:
- condition_id: {CONDITION_ID}
  met: 1 | 0
  evidence: {PACKET_FILE_OR_REPO_FILE_OR_COMMAND_OR_USER_CONFIRMATION}

forbidden_completion_claim_used:
true | false

milestone_alignment:
aligned | drift_detected | unclear

success_criteria_covered:
{SUCCESS_CRITERIA_IDS_OR_NONE}

non_goals_or_hard_prohibitions_touched:
{NON_GOALS_OR_HARD_PROHIBITIONS_TOUCHED_OR_NONE}

possible_drift:
{ANY_TASK_GOAL_DRIFT_OR_NONE}

recommended_routing:
{RECOMMENDED_NEXT_ROLE_OR_NONE}

请优先检查：
1. `milestone-contract.md` 是否存在且已确认。
2. `role_completion_status` 是否等于 `1`。
3. `assigned_completion_conditions_met` 是否等于 `assigned_completion_conditions_total`。
4. `unmet_completion_conditions` 是否为 `none`。
5. 每个完成条件是否有具体证据；缺失、unknown、inference-only 或定性描述一律计为未完成。
6. `forbidden_completion_claim_used` 是否为 `false`。
7. 该产出是否仍服务当前 milestone contract。
8. 是否触碰 non-goals 或 hard prohibitions。
9. manifest 是否可读，documents 是否存在。
10. 如果且仅如果二值完成检查通过、milestone 对齐、用户接受该产出，才更新 final-packet-index 并生成下一角色启动消息。

边界：
- 只更新 Orchestrator 状态文件。
- 不修改当前角色 packet。
- 不创建下游 packet。
- 不执行 git add / git commit / git push。
- 不修改业务文件。
- 不检查 ready_for_next_role / packet.lock.json / sha256，除非用户明确要求 strict handoff。
- 不允许用 `pass_with_residual_risk`、`partial`、`closer to completion` 或类似定性词作为完成状态。
```

## Role Boundary

The current role may recommend a downstream role in its packet or summary, but it must not generate the authoritative next-role startup message.

Orchestrator owns milestone alignment check, consumable check, final-packet-index updates, routing, and next-role handoff brief generation.

When Orchestrator routes forward, it must paste the copy-ready next-role startup message in its response.
