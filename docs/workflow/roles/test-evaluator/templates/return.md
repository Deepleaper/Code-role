# Test Evaluator Return / 测试评估师回报

assignment_id:
delivery_stage: independent_evaluation
candidate_gate_valid: 0 | 1
evaluation_executed: 0 | 1
product_contract_pass: 0 | 1
milestone_observed_pass: 0 | 1
mkr_results:
| mkr_id | pass (0/1) | observed | evidence |
| --- | ---: | --- | --- |
check_results: <check_id -> 0|1>
artifact_path:
evidence_paths:
failed_contract_owner: none | product-prd | architect | code-context | implementer | test-evaluator | workflow-orchestrator
blocking_check_ids: none | <check ids>
return_to: workflow-orchestrator
