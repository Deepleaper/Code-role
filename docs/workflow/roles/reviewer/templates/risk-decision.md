# Risk Decision

## Decision Summary / 决策摘要

- gate_status / 门禁状态: approve | pass_with_residual_risk | request_changes | blocked [reviewer_judgment]
- final_acceptance / 最终验收建议: true | false [reviewer_judgment]
- milestone_closure_recommendation / milestone 关闭建议: close | do_not_close | user_decision_required [reviewer_judgment]

## Risk Decisions / 风险决策

| Risk / 风险 | Severity / 严重级别 | Decision / 决策 | Source Label / 来源标签 | Reason / 理由 | Owner / 归属 |
| --- | --- | --- | --- | --- | --- |
| {{risk}} | P0 / P1 / P2 / P3 | accept / user_confirmation_required / return_upstream / blocks_closure | evaluation_baseline_evidence / industry_evaluation_reference / benchmark_dataset_reference / metric_definition / implementer_evidence / test_evaluator_evidence / packet_chain_evidence / reviewer_judgment / unknown | {{reason}} | user / orchestrator / test-evaluator / implementer / product-prd |

## Residual Risks Accepted For Handoff / 可交给用户决策的残余风险

| Residual Risk / 残余风险 | Acceptance Condition / 接受条件 | User Confirmation Needed / 是否需用户确认 |
| --- | --- | --- |
| {{residual_risk}} [reviewer_judgment] | {{condition}} [reviewer_judgment] | yes / no [user_confirmation_needed] |

## Risks Requiring Return / 需要回流的风险

| Risk / 风险 | Return Role / 回流角色 | Required Correction / 必要修正 |
| --- | --- | --- |
| {{risk}} [reviewer_judgment] | product-prd / architect / code-context / implementer / test-evaluator | {{correction}} [reviewer_judgment] |

## Evaluation Baseline Risks / 评估基线风险

| Baseline Risk / 基线风险 | Decision / 决策 | Required Correction / 必要修正 |
| --- | --- | --- |
| unconfirmed mechanism / missing benchmark / unsupported industry reference / unclear metric threshold / unknown | accept_as_residual_risk / user_confirmation_required / return_to_test_evaluator / blocks_closure [reviewer_judgment] | {{correction}} [reviewer_judgment] |
