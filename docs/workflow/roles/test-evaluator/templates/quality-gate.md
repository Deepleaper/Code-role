# Quality Gate / 质量门

## Gate Decision / Gate 结论

- gate status / gate 状态: pass | pass_with_residual_risk | fail | blocked
- final_acceptance / 最终验收建议: true | false
- evaluation SOP status / 评估 SOP 状态: confirmed | draft | partial | missing | blocked
- evaluation baseline status / 评估基线状态: confirmed | partial | missing | blocked
- required SOP layers / 必需 SOP 层: covered | partial | not_run | blocked
- evidence basis / 证据基础:
- reviewer handoff recommendation / Reviewer 交接建议:

If active SOP, evaluation mechanism, or baseline is not confirmed, `gate status` must not be `pass`.

如果当前 SOP、评估机制或评估基线尚未确认，`gate status` 不得为 `pass`。

## Evidence Summary / 证据摘要

| Claim / 结论 | Source Label / 来源标签 | Evidence / 证据 | Confidence / 置信度 |
| --- | --- | --- | --- |
| <quality claim> | user_approved_eval_mechanism / evaluation_baseline / industry_evaluation_reference / benchmark_dataset_reference / metric_definition / evaluator_observed_result / test_command_output / regression_evidence / evaluator_judgment / unknown | <source> | high / medium / low |

## Open P0 / 未解决 P0

- <P0 or none>

## Open P1 / 未解决 P1

- <P1 or none>

## Open P2 / 未解决 P2

- <P2 or none>

`final_acceptance=true` is allowed only when the active SOP is confirmed, required SOP layers are not `not_run`, evidence is sufficient, and no unresolved P0/P1 remains.

只有当前 SOP 已确认、必需 SOP 层没有 `not_run`、证据充分且无未解决 P0/P1 时，才允许建议 `final_acceptance=true`。

## SOP Calibration Summary / SOP 校准摘要

- sop_adherence_status / SOP 遵守状态: followed | narrowed | changed | blocked [sop_calibration]
- sop_remains_valid / SOP 是否仍有效: true | false | unknown [sop_calibration]
- reviewer_attention / Reviewer 注意事项: {{attention_or_none}} [sop_calibration]
