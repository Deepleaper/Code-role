# PM Assignment -> Independent Evaluation / 项目经理任务书 -> 独立评估

assignment_id: json-export-evaluation-001
milestone: deterministic-json-export
delivery_stage: independent_evaluation
role_prompt_path: code-role/roles/independent-evaluation.md
milestone_objective: Users can export a report as stable JSON without changing the existing text-output contract.
milestone_okr_path: milestone-board.md#milestone-key-results--里程碑关键结果
product_okr_path: 02-product-contract.md
engineering_artifact_path: 05-engineering-delivery.md
candidate_artifact_path: dist/reporter-cli-candidate
candidate_ready_for_independent_evaluation: 1
evaluation_scope: complete_mkr_and_pkr_contract
authoritative_inputs:
- path: milestone-board.md
- path: 02-product-contract.md
- path: 05-engineering-delivery.md
evaluation_inputs:
- path_or_environment: fixtures/evaluation and Python 3.12 clean environment
acceptance_checks:
| check_id | complete independent observation | required evidence |
| --- | --- | --- |
| SOP-RECORDED | executable SOP is derived from accepted MKR/PKR thresholds before candidate results are inspected | SOP section in evaluation artifact |
| FULL-RUN | all CLI, JSON, determinism, and text checks run | evaluator-owned raw evidence |
| MKR-RESULTS | MKR-1 and MKR-2 receive binary results | per-MKR evidence matrix |
| CLAIM-BOUNDARY | conclusion stays inside accepted product claims | explicit allowed and forbidden claims |
required_artifact_path: 08-independent-evaluation-report.md
irreversible_actions: none
