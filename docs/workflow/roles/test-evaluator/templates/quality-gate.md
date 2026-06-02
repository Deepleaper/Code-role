# Quality Gate / 质量门

## Gate Decision / Gate 结论

- gate status / gate 状态: pass | pass_with_residual_risk | fail | blocked
- final_acceptance / 最终验收建议: true | false
- evaluation baseline status / 评估基线状态: confirmed | partial | missing | blocked
- evidence basis / 证据基础:
- reviewer handoff recommendation / Reviewer 交接建议:

If evaluation mechanism or baseline is not confirmed, `gate status` must not be `pass`.

如果评估机制或评估基线尚未确认，`gate status` 不得为 `pass`。

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

`final_acceptance=true` is allowed only when evidence is sufficient and no unresolved P0/P1 remains.

只有证据充分且无未解决 P0/P1 时，才允许建议 `final_acceptance=true`。
