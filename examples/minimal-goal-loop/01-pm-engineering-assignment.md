# PM Assignment -> Engineering / 项目经理任务书 -> 工程

assignment_id: json-export-eng-001
milestone: deterministic-json-export
objective: Users can export a report as stable JSON without changing the existing text-output contract.
target_kr: KR-1
current_kr_state: 0
role_prompt_path: code-role/role-instance-prompts/engineering.md
current_failed_evidence: JSON mode does not exist; therefore no fixture can produce schema-valid deterministic JSON. The 12 existing text-output regression tests pass.
role_deliverable: A runnable JSON-export candidate plus reproducible candidate evidence for every KR-1 check.
authoritative_inputs:
- path: milestone-board.md
acceptance_checks:
| check_id | runnable behavior/result | required evidence |
| --- | --- | --- |
| JSON-1 | Fixtures A, B, and C exit 0 and emit exactly `report_id`, `generated_at`, and `rows` as schema-valid JSON. | Command log, three output artifacts, and schema-validation output. |
| JSON-2 | Two runs against each fixture are byte-identical after applying the frozen `generated_at` fixture value. | SHA-256 comparison for two runs per fixture. |
| REG-1 | All 12 existing text-output regression tests pass without snapshot changes. | Fresh test command, 12/12 result, and empty snapshot diff. |
required_regressions:
- check_id: REG-1
task_specific_exclusions: YAML, XML, streaming, plugin APIs, unrelated refactors, and changes to existing text snapshots
required_artifact_path: attachments/engineering-candidate-evidence.md
irreversible_actions: none
