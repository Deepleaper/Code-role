# Milestone Contract / 里程碑合同

Workflow Orchestrator maintains one accepted milestone contract.

```text
milestone:
objective:
objective_accepted: 0 | 1

key_results:
| KR | Observable pass condition | Required independent evidence | Pass (0/1) |
| --- | --- | --- | ---: |

non_goals:
- item:

claim_boundary:
- allowed:
- forbidden:

evaluation_sop_required: 0 | 1
evaluation_sop_path:
iteration_limit_per_primary_kr: 3
accepted_time_or_cost_budget:
```

## Rules / 规则

- Objective, KR definitions, thresholds, datasets, graders, and claim boundaries require user acceptance.
- Every KR remains `0` until all pass conditions have independent evidence.
- A role assignment targets one primary `KR=0`, except full-milestone evaluation or audit.
- Role `assignment_pass` is scoped work evidence, not milestone status.
- Required missing, unrun, inferred, or qualitative evidence is `0`.
- Residual items become a new accepted KR, an explicit non-goal, or remain a failed check.

## Assignment Definition / 任务定义

Before routing a role, Workflow Orchestrator freezes:

```text
assignment_id
role_objective
professional_question
authoritative_inputs
required_checks with expected observations and evidence
required_output_path
stop_condition
```

Requirements discovered after assignment start are an Orchestrator definition defect and do not consume a role failure iteration.

## Drift Check / 漂移检查

For every accepted artifact:

- Does it answer the original Objective and selected KR?
- Does it preserve non-goals and claim boundaries?
- Does it distinguish evidence, professional judgment, inference, and unknown?
- Does it reduce a milestone uncertainty rather than only add process output?
- Does the proposed route point to the owner of the substantive failed check?

## Closure / 关闭

Milestone pass is `1` only when every accepted KR is `1`, required independent evaluation passes, required Reviewer audit passes, and any irreversible release action follows the target project's normal human approval process.
