# Milestone Drift Audit / 里程碑目标漂移审计

Reviewer 必须以最开始确认的 milestone 目标为锚点，审计从 Workflow Orchestrator 到所有执行角色的完整流程产出是否发生目标漂移。

Reviewer must use the originally confirmed milestone goal as the anchor and audit whether Workflow Orchestrator and each execution-role output drifted from that goal.

## Original Milestone Anchor / 原始里程碑锚点

- milestone_name / milestone 名称: {{milestone_name}} [original_milestone_anchor]
- original_business_goal / 原始业务目标: {{business_goal}} [original_milestone_anchor]
- original_delivery_goal / 原始交付目标: {{delivery_goal}} [original_milestone_anchor]
- success_criteria / 成功标准: {{success_criteria}} [original_milestone_anchor]
- non_goals / 明确不做: {{non_goals}} [original_milestone_anchor]
- milestone_contract_path / milestone 合约路径: code-role/workflow/orchestrator/milestone-contract.md [milestone_contract]
- milestone_contract_status / milestone 合约状态: confirmed | draft | missing | blocked [milestone_contract]
- anchor_source / 锚点来源: user_input / orchestrator_state / packet_chain_evidence / unknown [original_milestone_anchor]
- possible_drift_summary / 可能的目标漂移摘要: none / minor / major / blocked_missing_milestone_anchor [drift_audit]

If the original milestone anchor or active milestone contract is missing or unclear, Reviewer must mark final gate as `blocked` or `request_changes`.

如果原始 milestone 锚点或当前 milestone contract 缺失或不清晰，Reviewer 必须把最终 gate 标为 `blocked` 或 `request_changes`。

## Final Packet Index / 最终版本索引

- final_packet_index_path / 最终版本索引路径: {{final_packet_index_path}} [final_packet_index]
- historical_audit_requested / 是否审计历史版本: true | false [user_confirmation_needed]
- audit_scope / 审计范围: current_final_versions_only | historical_versions [reviewer_judgment]

Reviewer 默认只审计 final packet index 中列出的当前最终版本。

Reviewer audits current final versions listed in the final packet index by default.

## Role-By-Role Drift Matrix / 分角色漂移矩阵

| Role / 角色 | Expected Contribution To Milestone / 应服务的 milestone 贡献 | Actual Output Reviewed / 实际审计产出 | Drift Status / 漂移状态 | Drift Point / 漂移点 | Correction Owner / 修正角色 |
| --- | --- | --- | --- | --- | --- |
| workflow-orchestrator | preserve original milestone, choose chain, run consumption checks, and generate next-role handoff briefs without changing the goal | {{orchestrator_state_decision_log_and_handoff_briefs_from_final_index}} [final_packet_index / orchestrator_output_evidence] | aligned / minor_drift / major_drift / missing / not_applicable [reviewer_judgment] | {{drift_point_or_none}} [reviewer_judgment] | none / workflow-orchestrator |
| researcher | answer the milestone research question and evidence map | {{researcher_final_packet_from_index_or_na}} [final_packet_index / role_packet_evidence] | aligned / minor_drift / major_drift / missing / not_applicable [reviewer_judgment] | {{drift_point_or_none}} [reviewer_judgment] | none / researcher |
| product-prd | translate milestone goal into product scope, acceptance criteria, and non-goals | {{product_final_packet_from_index_or_na}} [final_packet_index / role_packet_evidence] | aligned / minor_drift / major_drift / missing / not_applicable [reviewer_judgment] | {{drift_point_or_none}} [reviewer_judgment] | none / product-prd |
| architect | define architecture that serves accepted product scope without expanding it | {{architect_final_packet_from_index_or_na}} [final_packet_index / role_packet_evidence] | aligned / minor_drift / major_drift / missing / not_applicable [reviewer_judgment] | {{drift_point_or_none}} [reviewer_judgment] | none / architect |
| code-context | map architecture intent to current project files, dependencies, impact, and implementation constraints | {{code_context_final_packet_from_index_or_na}} [final_packet_index / role_packet_evidence] | aligned / minor_drift / major_drift / missing / not_applicable [reviewer_judgment] | {{drift_point_or_none}} [reviewer_judgment] | none / code-context |
| implementer | produce the runnable candidate, preserve accepted contracts, and avoid unrelated changes | {{implementer_final_packet_from_index_or_na}} [final_packet_index / role_packet_evidence] | aligned / minor_drift / major_drift / missing / not_applicable [reviewer_judgment] | {{drift_point_or_none}} [reviewer_judgment] | none / implementer |
| test-evaluator | confirm evaluation baseline and judge implementation against milestone acceptance | {{test_evaluator_final_packet_from_index_or_na}} [final_packet_index / role_packet_evidence] | aligned / minor_drift / major_drift / missing / not_applicable [reviewer_judgment] | {{drift_point_or_none}} [reviewer_judgment] | none / test-evaluator |
| reviewer | produce final chain audit and gate decision against original milestone | current reviewer packet [reviewer_judgment] | aligned / minor_drift / major_drift [reviewer_judgment] | {{drift_point_or_none}} [reviewer_judgment] | none / reviewer |

## Drift Findings / 漂移发现

| Finding / 发现 | Severity / 严重级别 | Role / 角色 | Evidence / 证据 | Impact On Milestone / 对 milestone 的影响 | Required Correction / 必要修正 |
| --- | --- | --- | --- | --- | --- |
| {{finding_or_none}} | P0 / P1 / P2 / P3 / none | workflow-orchestrator / researcher / product-prd / architect / code-context / implementer / test-evaluator / reviewer | {{evidence}} [orchestrator_output_evidence / role_packet_evidence] | {{impact}} [reviewer_judgment] | {{correction}} [reviewer_judgment] |

## Correction Routing Recommendation / 修正路由建议

- correction_required / 是否需要修正: true | false [reviewer_judgment]
- correction_owner / 修正角色: none | workflow-orchestrator | researcher | product-prd | architect | code-context | implementer | test-evaluator | reviewer | user [reviewer_judgment]
- correction_reason / 修正原因: {{reason}} [reviewer_judgment]
- orchestrator_instruction / 给 Orchestrator 的指挥建议: route_forward | ask_user | route_revision_to_specific_role | block_until_milestone_anchor_confirmed [reviewer_judgment]

Reviewer 只能建议 Orchestrator 指挥对应角色修正，不能自己代写修正内容。

Reviewer may recommend that Orchestrator directs a specific role to revise, but must not write the correction content itself.
