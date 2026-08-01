# Final Gate / 最终门禁

- review_gate_pass: 0 | 1 [reviewer_judgment]
- required_checks_total: [reviewer_judgment]
- required_checks_passed: [reviewer_judgment]
- failed_check_ids: none | <check ids> [reviewer_judgment]
- correction_owner: none | workflow-orchestrator | researcher | product-prd | architect | code-context | implementer | test-evaluator | user [drift_audit]
- original_milestone_anchor_verified: 0 | 1 [milestone_contract]
- orchestrator_audited: 0 | 1 [orchestrator_output_evidence]
- all_required_role_outputs_audited: 0 | 1 [drift_audit]
- evaluation_sop_followed: 0 | 1 [evaluation_sop]
- acceptance_evidence_complete: 0 | 1 [test_evaluator_evidence]
- unsupported_claims_rejected: 0 | 1 [reviewer_judgment]

`review_gate_pass=1` requires every field above to be `1` and `failed_check_ids=none`. Reviewer returns this evidence to Orchestrator; Reviewer does not close the milestone.
