# Short Role Return / 角色短回报

Use the selected role's `templates/return.md`. Common transport fields are:

```text
assignment_id:
delivery_stage:
work_unit_pass: 0 | 1
check_results: <check_id -> 0|1>
artifact_path:
evidence_paths:
blocking_check_ids: none | <check ids>
return_to: workflow-orchestrator
```

Product / PRD additionally reports complete KR coverage. Implementer reports STEP status and candidate readiness. Test Evaluator reports `evaluation_executed`, per-KR results, `product_contract_pass`, and `milestone_observed_pass`. Reviewer reports `review_executed` and `review_gate_pass`.

This return is a pointer. Workflow Orchestrator reads the primary artifact and evidence before deciding.

Missing transport fields or field order do not justify revision when the artifact contains enough evidence. Do not include a next-role recommendation, readiness request, packet-lock request, or repeated professional summary.
