# Implementer Assignment / 实现工程师任务书

assignment_id:
milestone:
delivery_stage: engineering_delivery
milestone_okr_path:
product_okr_path:
architecture_artifact_path: none | <path>
code_context_artifact_path: none | <path>
product_okr_accepted: 1
engineering_objective: produce_the_complete_runnable_candidate
authoritative_inputs:
- path:
acceptance_checks:
| check_id | complete engineering result | required evidence |
| --- | --- | --- |
| EKR-PLAN | `EKR-1...EKR-N` covers the complete Product OKR | EKR-to-PKR traceability and dependency order |
| IMPLEMENTED | all PKR behavior exists in the integrated candidate | runnable candidate and implementation evidence |
| VERIFIED | every EKR, integration check, and regression passes | commands, exits, and observed outputs |
| REPRODUCIBLE | Test Evaluator can reproduce the candidate | candidate artifact, environment, and run instructions |
required_regressions:
- check_id:
task_specific_exclusions: none
required_artifact_path:
irreversible_actions: none
