# Evaluation Baseline / 评估基线

## Evaluation Objective / 评估目标

- objective / 目标: <what this evaluation must decide> [user_approved_eval_mechanism]
- milestone / 里程碑: <milestone> [original_milestone_anchor]
- original business goal / 原始业务目标: <business goal> [original_milestone_anchor]
- original delivery goal / 原始交付目标: <delivery goal> [original_milestone_anchor]
- success criteria / 成功标准: <success criteria> [original_milestone_anchor]
- non-goals / 明确不做: <non-goals> [original_milestone_anchor]
- milestone_alignment / milestone 对齐: <how this evaluation serves the milestone> [user_approved_eval_mechanism]
- possible drift / 可能的目标漂移: none / minor / major / unknown [evaluator_judgment]
- baseline_confirmed / 基线已确认: 0 | 1 [user_approved_eval_mechanism]

## Active SOP Mapping / 当前 SOP 映射

- active_sop_path / 当前 SOP 路径: code-role/workflow/evaluation/evaluation-sop.md [evaluation_sop]
- active_sop_confirmed / 当前 SOP 已确认: 0 | 1 [evaluation_sop]
- baseline_extends_sop / 本基线是否扩展 SOP: false | true [sop_calibration]
- if_extends_sop / 如扩展 SOP: record proposed changes in sop-calibration.md before Reviewer handoff [sop_calibration]

## Evaluation Mechanism / 评估机制

| Mechanism / 机制 | Purpose / 用途 | Source Label / 来源标签 | Confirmed (0/1) |
| --- | --- | --- | --- |
| <mechanism name> | <what it evaluates> | user_approved_eval_mechanism / evaluation_baseline / unknown | 0 |

## Industry Or Common-Consensus References / 行业或通用共识参考

| Reference / 参考 | Type / 类型 | Why Relevant / 相关性 | Source Label / 来源标签 | Permission Status / 权限状态 |
| --- | --- | --- | --- | --- |
| <template, benchmark, dataset, metric convention, or unknown> | evaluation_template / benchmark_dataset / metric_convention / engineering_practice / unknown | <reason> | industry_evaluation_reference / benchmark_dataset_reference / metric_definition / unknown | user_provided / public_network_research / not_found / unknown |

Public-source network research is allowed by default when relevant to the evaluation baseline. If no industry consensus source was found, mark it as `unknown` or `not_found`.

如未批准外部研究，不得声称已找到行业共识来源；应标记为 `unknown` 或请求用户批准。

## Benchmark Data And Baselines / Benchmark 数据与基线

| Baseline Or Dataset / 基线或数据集 | Metric / 指标 | Threshold / 阈值 | Source Label / 来源标签 | Confirmed (0/1) |
| --- | --- | --- | --- | --- |
| <baseline or dataset> | <metric> | <pass/fail threshold> | evaluation_baseline / benchmark_dataset_reference / metric_definition / unknown | 0 |

## Project Acceptance Mapping / 项目验收映射

| Project Acceptance Criterion / 项目验收项 | Evaluation Metric / 评估指标 | Planned Evidence / 计划证据 | Mapped (0/1) |
| --- | --- | --- | --- |
| <criterion> [acceptance_criteria_evidence] | <metric> [metric_definition] | <command, inspection, or dataset> [evaluation_baseline] | 0 |

## Baseline Open Questions / 基线开放问题

| Question / 问题 | Impact / 影响 | Required Confirmation / 需要确认 |
| --- | --- | --- |
| <question or none> [unknown] | <impact> [evaluator_judgment] | <confirmation> [user_approved_eval_mechanism] |
