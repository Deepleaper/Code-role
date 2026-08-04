# PM Assignment -> Engineering / 项目经理任务书 -> 工程

assignment_id:
milestone:
delivery_stage: engineering_delivery
role_prompt_path:
milestone_objective:
milestone_okr_path:
product_okr_path:
product_okr_accepted: 1
engineering_objective: produce_the_complete_runnable_candidate
authoritative_inputs:
- path:
acceptance_checks:
| check_id | complete engineering result | required evidence |
| --- | --- | --- |
| EKR-PLAN | `EKR-1...EKR-N` covers the complete Product OKR | EKR-to-PKR traceability and dependency order |
| IMPLEMENTED | all required PKR behavior exists in the integrated candidate | runnable candidate and implementation evidence |
| VERIFIED | every required EKR, integration check, and regression passes | commands, exit codes, and observed outputs |
| REPRODUCIBLE | Independent Evaluation can reproduce the candidate | candidate artifact, environment, and run instructions |
required_regressions:
- check_id:
task_specific_exclusions: none
required_artifact_path:
irreversible_actions: none
