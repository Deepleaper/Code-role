# PM Assignment -> Engineering / 项目经理任务书 -> 工程

assignment_id: json-export-engineering-001
milestone: deterministic-json-export
delivery_stage: engineering_delivery
role_prompt_path: code-role/roles/engineering.md
milestone_objective: Users can export a report as stable JSON without changing the existing text-output contract.
project_okr_path: milestone-board.md#milestone-key-results--里程碑关键结果
product_contract_path: 02-product-contract.md
product_contract_accepted: 1
engineering_objective: produce_the_complete_runnable_candidate
authoritative_inputs:
- path: milestone-board.md
- path: 02-product-contract.md
acceptance_checks:
| check_id | complete engineering result | required evidence |
| --- | --- | --- |
| STEP-PLAN | STEP stages cover KR-1 and KR-2 without creating new KRs | traceability and dependency order |
| IMPLEMENTED | integrated candidate contains all required behavior | runnable candidate and implementation evidence |
| VERIFIED | STEP checks and 12 text regressions pass | commands, exit codes, observed output |
| REPRODUCIBLE | evaluator can run the candidate independently | artifact path, environment, run instructions |
required_regressions:
- check_id: TEXT-12
task_specific_exclusions: none
required_artifact_path: 05-engineering-delivery.md
irreversible_actions: none
