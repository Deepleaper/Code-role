# Final Gate

## Gate Decision / 门禁决策

- gate_status / 门禁状态: approve | pass_with_residual_risk | request_changes | blocked [reviewer_judgment]
- final_acceptance / 最终验收建议: true | false [reviewer_judgment]
- milestone_closure_recommendation / milestone 关闭建议: close | do_not_close | user_decision_required [reviewer_judgment]
- recommended_next_action / 建议下一步: {{next_action}} [reviewer_judgment]

## Decision Basis / 决策依据

- flow_wide_milestone_drift / 全链路 milestone 漂移: aligned | minor_drift | major_drift | blocked_missing_milestone_anchor [drift_audit]
- correction_owner / 修正角色: none | workflow-orchestrator | researcher | product-prd | architect | code-context | implementer | test-evaluator | reviewer | user [drift_audit]
- milestone_contract_status / milestone 合约状态: confirmed | draft | missing | blocked [milestone_contract]
- evaluation_sop_status / 评估 SOP 状态: confirmed | draft | partial | missing | blocked [evaluation_sop]
- sop_calibration_status / SOP 校准状态: followed | narrowed | changed | blocked | unknown [sop_calibration]
- evaluation_baseline_status / 评估基线状态: confirmed | partial | missing | unsupported | unknown [reviewer_judgment]
- industry_reference_status / 行业参考状态: sourced | user_provided | not_found | unsupported | unknown [reviewer_judgment]
- benchmark_dataset_status / benchmark 数据状态: confirmed | partial | missing | not_applicable | unknown [reviewer_judgment]
- acceptance_gap_status / 验收差距状态: covered | partial | missing | unknown [reviewer_judgment]
- implementation_scope_status / 实现范围状态: within_scope | scope_risk | scope_violation | unknown [reviewer_judgment]
- test_evidence_status / 测试证据状态: sufficient | partial | insufficient | blocked [reviewer_judgment]
- packet_chain_status / packet 链状态: supports_review | partial | blocked [reviewer_judgment]

## Blocking Items / 阻断项

| Blocking Item / 阻断项 | Severity / 严重级别 | Source Label / 来源标签 | Required Resolution / 必要解决 |
| --- | --- | --- | --- |
| {{blocking_item_or_none}} | P0 / P1 / P2 / none | milestone_contract / product_acceptance / evaluation_sop / sop_calibration / evaluation_baseline_evidence / industry_evaluation_reference / benchmark_dataset_reference / metric_definition / implementer_evidence / test_evaluator_evidence / packet_chain_evidence / reviewer_judgment / unknown | {{resolution}} |

## User Confirmations / 用户确认项

| Confirmation / 确认项 | Required For / 用途 | Default If Not Confirmed / 未确认默认处理 |
| --- | --- | --- |
| {{confirmation}} [user_confirmation_needed] | milestone closure / residual risk acceptance / upstream return / no further action | do_not_close / request_changes / blocked |

## Next Step / 下一步

- if_approved / 如通过: Orchestrator may ask user whether to close the milestone. [reviewer_judgment]
- if_residual_risk / 如有残余风险: Orchestrator must ask whether user accepts residual risk. [reviewer_judgment]
- if_changes_required / 如需修改: Orchestrator should route to the correct upstream role with a milestone-focused task brief. [reviewer_judgment]
- if_role_output_drift_detected / 如发现角色产出目标漂移: Orchestrator should direct the named correction owner to revise against the original milestone anchor. [drift_audit]
- if_milestone_contract_missing / 如 milestone contract 缺失: Orchestrator should return to milestone contract confirmation before downstream routing. [milestone_contract]
- if_evaluation_sop_missing / 如 evaluation SOP 缺失: Orchestrator should return to Test Evaluator to confirm SOP before final acceptance. [evaluation_sop]
- if_evaluation_baseline_missing / 如评估基线缺失: Orchestrator should return to Test Evaluator to confirm mechanism, metrics, benchmark data, and industry references. [reviewer_judgment]
- git_boundary / Git 边界: Reviewer does not run `git add`, `git commit`, or `git push`; target-project Git follows normal project process. [reviewer_judgment]
