# PM Assignment -> Engineering / 项目经理任务书 -> 工程

assignment_id:
milestone:
delivery_stage: engineering_delivery
role_prompt_path:
milestone_objective:
project_okr_path:
product_contract_path:
product_contract_accepted: 1
engineering_objective: produce_the_complete_runnable_candidate
authoritative_inputs:
- path:
acceptance_checks:
| check_id | complete engineering result | required evidence |
| --- | --- | --- |
| STEP-PLAN | `STEP-1...STEP-N` covers every accepted KR through the Product Contract | STEP-to-KR traceability and dependency order |
| IMPLEMENTED | all required KR behavior exists in the integrated candidate | runnable candidate and implementation evidence |
| VERIFIED | every required STEP, integration check, and regression passes | commands, exit codes, and observed outputs |
| REPRODUCIBLE | Independent Evaluation can reproduce the candidate | candidate artifact, environment, and run instructions |
required_regressions:
- check_id:
task_specific_exclusions: none
required_artifact_path:
irreversible_actions: none
