# Independent Evaluation Return / 独立评估回报

assignment_id:
delivery_stage: independent_evaluation
candidate_gate_valid: 0 | 1
evaluation_executed: 0 | 1
product_contract_pass: 0 | 1
milestone_observed_pass: 0 | 1
mkr_results:
| mkr_id | pass (0/1) | observed | evidence |
| --- | ---: | --- | --- |
check_results:
| check_id | pass (0/1) | observed | evidence |
| --- | ---: | --- | --- |
artifact_path:
evidence_paths:
failure_reason_code: none | product_contract_invalid | candidate_not_ready | engineering_defect | evaluation_execution_invalid | environment_invalid | evidence_missing
failed_contract_owner: none | product-strategy | engineering | independent-evaluation | project-manager
blocking_check_ids: none | <check ids>
return_to: project-manager
