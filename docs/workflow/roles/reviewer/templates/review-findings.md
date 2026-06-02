# Review Findings

## Milestone Alignment / 里程碑对齐

- milestone_goal / 里程碑目标: {{milestone_goal}} [milestone_goal]
- original_milestone_anchor / 原始 milestone 锚点: {{original_anchor}} [original_milestone_anchor]
- role_chain_audited / 已审计角色链: workflow-orchestrator / researcher / product-prd / architect / code-context / implementer / test-evaluator / reviewer [drift_audit]
- chain_drift_status / 全链路漂移状态: aligned | minor_drift | major_drift | blocked_missing_milestone_anchor [drift_audit]
- correction_owner / 修正角色: none | workflow-orchestrator | researcher | product-prd | architect | code-context | implementer | test-evaluator | reviewer | user [drift_audit]
- drift_reason / 漂移理由: {{drift_reason}} [reviewer_judgment]

## Evaluation Baseline Audit / 评估基线审计

| Baseline Item / 基线项 | Test Evaluator Claim / 评估师结论 | Source Label / 来源标签 | Audit Result / 审计结果 | Final Gate Impact / 门禁影响 |
| --- | --- | --- | --- | --- |
| evaluation mechanism / metric definition / industry reference / benchmark dataset / pass threshold | {{claim}} | evaluation_baseline_evidence / industry_evaluation_reference / benchmark_dataset_reference / metric_definition / test_evaluator_evidence / unknown | confirmed / partial / missing / unsupported / unknown [reviewer_judgment] | {{impact}} [reviewer_judgment] |

## Acceptance Gap Check / 验收差距检查

| Acceptance Criterion / 验收项 | Implementation Evidence / 实现证据 | Evaluator Evidence / 评估证据 | Gap Status / 缺口状态 | Final Acceptance Impact / 最终验收影响 |
| --- | --- | --- | --- | --- |
| {{criterion}} [product_acceptance] | {{implementation_evidence}} [implementer_evidence] | {{evaluator_evidence}} [test_evaluator_evidence] | covered / partial / missing / not_applicable [reviewer_judgment] | {{impact}} [reviewer_judgment] |

## Findings / 审查发现

| Finding / 发现 | Severity / 严重级别 | Source Label / 来源标签 | File or Packet / 文件或 Packet | Evidence / 证据 | Required Action / 必要动作 |
| --- | --- | --- | --- | --- | --- |
| {{finding}} | P0 / P1 / P2 / P3 | milestone_goal / product_acceptance / implementer_evidence / test_evaluator_evidence / packet_chain_evidence / reviewer_judgment / unknown | {{path_or_packet}} | {{evidence}} | {{required_action}} |

## Reviewer Judgment / Reviewer 判断

- reviewer_gate_basis / 门禁依据: {{gate_basis}} [reviewer_judgment]
- unresolved_p0 / 未解决 P0: {{count_or_none}} [reviewer_judgment]
- unresolved_p1 / 未解决 P1: {{count_or_none}} [reviewer_judgment]
- evaluation_baseline_gap_summary / 评估基线缺口摘要: {{baseline_gap_summary}} [reviewer_judgment]
- evidence_gap_summary / 证据缺口摘要: {{gap_summary}} [reviewer_judgment]
