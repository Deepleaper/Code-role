# PM Assignment -> Independent Evaluation / 项目经理任务书 -> 独立评估

assignment_id: json-export-eval-001
milestone: deterministic-json-export
objective: Users can export a report as stable JSON without changing the existing text-output contract.
target_kr: KR-1
current_kr_state: 0
role_prompt_path: code-role/role-instance-prompts/independent-evaluation.md
assignment_mode: full_evaluation
current_failed_evidence: Engineering candidate evidence exists, but no evaluator-owned run has yet observed the complete KR-1 outcome.
role_deliverable: One fresh independent evaluation artifact covering every KR-1 capability and regression check.
authoritative_inputs:
- path: milestone-board.md
- path: attachments/engineering-candidate-evidence.md
frozen_sop_path: 01-pm-engineering-assignment.md#acceptance_checks
acceptance_checks:
| check_id | expected independent observation | required evidence |
| --- | --- | --- |
| JSON-1 | 3/3 fixtures exit 0 and match the exact frozen JSON schema. | Fresh commands and evaluator-owned JSON/schema artifacts. |
| JSON-2 | 3/3 repeated fixture pairs are byte-identical. | Evaluator-owned SHA-256 output. |
| REG-1 | 12/12 existing text regressions pass with no snapshot diff. | Fresh regression output and empty diff. |
required_artifact_path: attachments/independent-evaluation-report.md
irreversible_actions: none
