# Evaluation SOP Consumption / 评估 SOP 消费记录

## Active SOP / 当前 SOP

- sop_path / SOP 路径: code-role/workflow/evaluation/evaluation-sop.md [evaluation_sop]
- sop_status / SOP 状态: confirmed | draft | partial | missing | blocked [evaluation_sop]
- milestone / 里程碑: {{milestone}} [original_milestone_anchor]
- evaluation_subject / 评估对象: {{subject}} [evaluation_sop]
- evaluation_objective / 评估目标: {{objective}} [evaluation_sop]

## Required Layers / 必需评估层

| SOP Layer / SOP 层 | Required / 是否必需 | Planned Packet Evidence / packet 证据 | Status / 状态 |
| --- | --- | --- | --- |
| evaluation_baseline | true | evaluation-baseline.md [evaluation_baseline] | planned / partial / not_run / blocked |
| evidence_integrity | true | test-results.md / packet-chain evidence [evaluator_observed_result] | planned / partial / not_run / blocked |
| acceptance_mapping | true | test-plan.md / regression-matrix.md [acceptance_criteria_evidence] | planned / partial / not_run / blocked |
| independent_evaluation | true | test-results.md [evaluator_observed_result] | planned / partial / not_run / blocked |
| regression_and_risk | true | regression-matrix.md / failure-analysis.md [regression_evidence] | planned / partial / not_run / blocked |
| claim_boundary | true | quality-gate.md [evaluator_judgment] | planned / partial / not_run / blocked |
| final_quality_gate | true | quality-gate.md [evaluator_judgment] | planned / partial / not_run / blocked |
| sop_calibration | true | sop-calibration.md [sop_calibration] | planned / partial / not_run / blocked |

## Not-Run Policy / 未运行项处理规则

- required_not_run_blocks_unconditional_pass / 必需项未运行阻断无条件通过: true [evaluation_sop]
- optional_not_run_handling / 可选项未运行处理: residual_risk | not_applicable [evaluation_sop]
- implementer_verification_is_input_only / Implementer 验证只作为输入: true [evaluation_sop]

## Claim Boundary / 结论边界

- allowed_claims / 允许结论: {{allowed_claims}} [evaluation_sop]
- forbidden_claims / 禁止结论: {{forbidden_claims}} [evaluation_sop]
- unknown_claims / 未知结论: {{unknown_claims}} [evaluation_sop]

## SOP Use Decision / SOP 使用判断

- sop_use / SOP 使用方式: followed | narrowed | proposed_change | blocked [sop_calibration]
- reason / 原因: {{reason}} [sop_calibration]
- reviewer_attention / 需要 Reviewer 注意: {{attention_or_none}} [sop_calibration]
