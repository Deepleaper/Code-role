# Role Assignment Template / 分角色任务书模板

This is one KR-delivery work unit, not a workflow tutorial. Workflow Orchestrator fills the selected role's exact `templates/assignment.md` from accepted evidence.

Do not issue a generic workflow essay. Do not restate stable role rules.

## Required Content / 必填内容

```text
assignment_id:
milestone:
objective:
target_kr: <one exact outcome KR=0 or full-milestone audit>
current_kr_state: 0
current_failed_evidence:
role_deliverable:
authoritative_inputs:
- path:
acceptance_checks:
| check_id | observable result | required evidence |
| --- | --- | --- |
required_artifact_path:
irreversible_actions: none
```

Use the role-specific template:

- `roles/researcher/templates/assignment.md`
- `roles/product-prd/templates/assignment.md`
- `roles/architect/templates/assignment.md`
- `roles/code-context/templates/assignment.md`
- `roles/implementer/templates/assignment.md`
- `roles/test-evaluator/templates/assignment.md`
- `roles/reviewer/templates/assignment.md`

## Rules / 规则

- Copy the exact Objective, KR, failed evidence, and accepted upstream fields.
- Assign one role-owned deliverable that removes the named failed evidence.
- Freeze acceptance checks before work starts.
- Require one primary professional artifact; optional annexes exist only for necessary evidence.
- Include task-specific exclusions only when genuinely necessary.
- A complete assignment starts immediately.
- Do not ask for startup acknowledgement, `开始`, readiness conversion, packet lock, or next-role recommendation.

If the target KR, current failed evidence, deliverable, inputs, acceptance checks, or artifact path is missing, do not issue the assignment. Ask once for the complete missing user-decision set.
