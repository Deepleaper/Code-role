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

role_completion_summary:
{ROLE_COMPLETION_SUMMARY}

milestone_alignment:
{HOW_THIS_OUTPUT_SERVES_THE_MILESTONE}

success_criteria_covered:
{SUCCESS_CRITERIA_COVERED_OR_UNKNOWN}

non_goals_or_hard_prohibitions_touched:
{NON_GOALS_OR_HARD_PROHIBITIONS_TOUCHED_OR_NONE}

possible_drift:
{ANY_TASK_GOAL_DRIFT_OR_NONE}

recommended_routing:
{RECOMMENDED_NEXT_ROLE_OR_NONE}

请优先检查：
1. `milestone-contract.md` 是否存在且已确认。
2. 该产出是否仍服务当前 milestone contract。
3. 该产出覆盖了哪些 success criteria。
4. 是否触碰 non-goals 或 hard prohibitions。
5. 如有漂移，是打回当前角色，还是需要用户调整 milestone contract。
6. manifest 是否可读，documents 是否存在。
7. 用户是否接受该产出作为本角色当前最终版本，并允许进入下一角色。
8. 如果允许进入下一角色，请更新 final-packet-index，并生成只做审阅和路由的 next-role handoff brief。

边界：
- 只更新 Orchestrator 状态文件。
- 不修改当前角色 packet。
- 不创建下游 packet。
- 不执行 git add / git commit / git push。
- 不修改业务文件。
- 不检查 ready_for_next_role / packet.lock.json / sha256，除非用户明确要求 strict handoff。
```

## Role Boundary

The current role may recommend a downstream role in its packet or summary, but it must not generate the authoritative next-role startup message.

Orchestrator owns milestone alignment check, consumable check, final-packet-index updates, routing, and next-role handoff brief generation.

When Orchestrator routes forward, it must paste the copy-ready next-role startup message in its response.
