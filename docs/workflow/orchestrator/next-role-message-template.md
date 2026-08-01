# Role Assignment Template / 分角色任务书模板

This is a professional assignment, not a workflow tutorial. Workflow Orchestrator fills the selected role's exact `templates/assignment.md` from accepted upstream artifacts.

Do not issue a generic workflow essay. The assignment must contain the selected role's professional question and frozen checks.

这是专业任务书，不是工作流教程。项目经理必须根据已接受上游附件填写目标角色自己的 `templates/assignment.md`。

## Required Content / 必填内容

```text
assignment_id:
milestone:
target_kr: <one primary KR=0 or one full-milestone audit objective>
role_objective:
professional_question:
authoritative_inputs:
- path:
required_checks:
| check_id | expected | required evidence |
| --- | --- | --- |
required_packet_path:
stop_condition:
```

Use the role-specific additions from:

- `roles/researcher/templates/assignment.md`
- `roles/product-prd/templates/assignment.md`
- `roles/architect/templates/assignment.md`
- `roles/code-context/templates/assignment.md`
- `roles/implementer/templates/assignment.md`
- `roles/test-evaluator/templates/assignment.md`
- `roles/reviewer/templates/assignment.md`

## Assignment Rules / 任务规则

- Copy exact professional fields and evidence paths from accepted upstream artifacts; do not rewrite their conclusions.
- The Orchestrator must state the professional question. Do not make the next role infer its task from a manifest or milestone history.
- Freeze the complete required-check set before assignment.
- Include task-specific exclusions only when genuinely necessary.
- A complete assignment starts work immediately.
- Do not ask for startup acknowledgement, read/write recitation, a separate `开始`, readiness conversion, packet lock, or next-role recommendation.
- Keep the assignment body within 20 lines excluding paths and the check table.

## Invalid Assignment / 无效任务

If the professional question, authoritative inputs, required checks, evidence expectations, output path, or stop condition is missing, do not issue the assignment. Ask once for the complete missing user-decision set.
