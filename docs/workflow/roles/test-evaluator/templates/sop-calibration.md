# SOP Calibration / SOP 校准

## Calibration Result / 校准结果

- sop_adherence_status / SOP 遵守状态: followed | narrowed | changed | blocked [sop_calibration]
- sop_remains_valid / SOP 是否仍有效: true | false | unknown [sop_calibration]
- final_gate_impact / 对最终门禁影响: none | residual_risk | request_changes | blocked [sop_calibration]
- reviewer_can_audit_using_sop / Reviewer 是否可基于该 SOP 审计: true | false | unknown [sop_calibration]

## Required Layer Coverage / 必需层覆盖

| SOP Layer / SOP 层 | Coverage / 覆盖状态 | Evidence / 证据 | Gate Impact / 门禁影响 |
| --- | --- | --- | --- |
| evaluation_baseline | covered / partial / not_run / blocked | {{evidence}} [evaluation_baseline] | none / residual_risk / blocked |
| evidence_integrity | covered / partial / not_run / blocked | {{evidence}} [evaluator_observed_result] | none / residual_risk / blocked |
| acceptance_mapping | covered / partial / not_run / blocked | {{evidence}} [acceptance_criteria_evidence] | none / residual_risk / blocked |
| independent_evaluation | covered / partial / not_run / blocked | {{evidence}} [evaluator_observed_result] | none / residual_risk / blocked |
| regression_and_risk | covered / partial / not_run / blocked | {{evidence}} [regression_evidence] | none / residual_risk / blocked |
| claim_boundary | covered / partial / not_run / blocked | {{evidence}} [evaluator_judgment] | none / residual_risk / blocked |
| final_quality_gate | covered / partial / not_run / blocked | {{evidence}} [evaluator_judgment] | none / residual_risk / blocked |

## SOP Change Log / SOP 变更记录

| Proposed Change / 建议变更 | Reason / 原因 | Source Label / 来源标签 | Requires User Confirmation / 需要用户确认 |
| --- | --- | --- | --- |
| {{change_or_none}} | {{reason}} | sop_calibration / evaluator_judgment / unknown | true / false |

## Reviewer Handoff / Reviewer 交接

- sop_risk_summary / SOP 风险摘要: {{summary}} [sop_calibration]
- reviewer_check_required / Reviewer 必查项: {{required_check}} [sop_calibration]
- downstream_warning / 下游警告: Do not treat a changed or unconfirmed SOP as final acceptance evidence. [sop_calibration]
