# PM Assignment -> Engineering / 项目经理任务书 -> 工程

assignment_id: json-export-engineering-001
milestone: deterministic-json-export
delivery_stage: engineering_delivery
role_prompt_path: code-role/roles/engineering.md
milestone_objective: Users can export a report as stable JSON without changing the existing text-output contract.
milestone_okr_path: milestone-board.md#milestone-key-results--里程碑关键结果
product_okr_path: 02-product-contract.md
product_okr_accepted: 1
engineering_objective: produce_the_complete_runnable_candidate
authoritative_inputs:
- path: milestone-board.md
- path: 02-product-contract.md
acceptance_checks:
| check_id | complete engineering result | required evidence |
| --- | --- | --- |
| EKR-PLAN | EKR stages cover PKR-1 through PKR-3 | traceability and dependency order |
| IMPLEMENTED | integrated candidate contains all required behavior | runnable candidate and implementation evidence |
| VERIFIED | EKR checks and 12 text regressions pass | commands, exit codes, observed output |
| REPRODUCIBLE | evaluator can run the candidate independently | artifact path, environment, run instructions |
required_regressions:
- check_id: TEXT-12
task_specific_exclusions: none
required_artifact_path: 05-engineering-delivery.md
irreversible_actions: none
