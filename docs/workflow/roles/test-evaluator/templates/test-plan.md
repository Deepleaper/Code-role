# Test Plan / 测试计划

## Baseline Mapping / 基线映射

- evaluation_mechanism_status / 评估机制状态: confirmed / pending / blocked [user_approved_eval_mechanism]
- benchmark_status / benchmark 状态: confirmed / pending / not_applicable / unknown [evaluation_baseline]
- industry_reference_status / 行业参考状态: user_provided / external_research_approved / not_approved / unknown [industry_evaluation_reference / unknown]

## Planned Checks / 计划检查

| Acceptance Criterion Or Behavior / 验收项或行为 | Evaluation Baseline Or Metric / 评估基线或指标 | Source Label / 来源标签 | Planned Command Or Check / 计划命令或检查 | Required / 是否必需 | Run Permission Status / 执行许可状态 |
| --- | --- | --- | --- | --- | --- |
| <criterion or behavior> | <baseline, benchmark, metric, or unknown> | user_approved_eval_mechanism / evaluation_baseline / industry_evaluation_reference / benchmark_dataset_reference / metric_definition / acceptance_criteria_evidence / architecture_test_strategy / code_context_test_map / implementer_reported_verification / evaluator_judgment / unknown | <command or inspection> | yes / no | approved / not_requested / denied / blocked |

Test Evaluator may only run commands inside user-approved scope.

Test Evaluator 只能在用户批准的范围内运行命令。
