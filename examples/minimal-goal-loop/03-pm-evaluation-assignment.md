# Independent Evaluation Assignment / 独立评估任务书

assignment_id: json-export-eval-001
milestone: deterministic-json-export
target_kr: KR-1
role_prompt_path: code-role/role-instance-prompts/independent-evaluation.md
assignment_mode: full_evaluation
role_objective: Independently reproduce every frozen KR-1 check in a clean environment.
authoritative_inputs:
- path: milestone-board.md
- path: attachments/engineering-candidate-evidence.md
frozen_sop_path: 01-pm-engineering-assignment.md#required_checks
required_checks:
| check_id | expected | required evidence |
| --- | --- | --- |
| JSON-1 | 3/3 fixtures exit 0 and match the exact frozen JSON schema. | Fresh commands and evaluator-owned JSON/schema artifacts. |
| JSON-2 | 3/3 repeated fixture pairs are byte-identical. | Evaluator-owned SHA-256 output. |
| REG-1 | 12/12 existing text regressions pass with no snapshot diff. | Fresh regression output and empty diff. |
required_output_attachment: attachments/independent-evaluation-report.md
stop_condition: Stop with `evaluation_pass=0` if any required check cannot run or lacks evaluator-observed evidence.
