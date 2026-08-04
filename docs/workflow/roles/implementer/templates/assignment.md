# Implementer Assignment / 实现工程师任务书

assignment_id:
milestone:
delivery_stage: engineering_delivery
project_okr_path:
product_contract_path:
architecture_artifact_path: none | <path>
code_context_artifact_path: none | <path>
product_contract_accepted: 1
engineering_objective: produce_the_complete_runnable_candidate
authoritative_inputs:
- path:
acceptance_checks:
| check_id | complete engineering result | required evidence |
| --- | --- | --- |
| STEP-PLAN | `STEP-1...STEP-N` covers the complete Product Contract | STEP-to-KR traceability and dependency order |
| IMPLEMENTED | all KR behavior exists in the integrated candidate | runnable candidate and implementation evidence |
| VERIFIED | every STEP, integration check, and regression passes | commands, exits, and observed outputs |
| REPRODUCIBLE | Test Evaluator can reproduce the candidate | candidate artifact, environment, and run instructions |
required_regressions:
- check_id:
task_specific_exclusions: none
required_artifact_path:
irreversible_actions: none
