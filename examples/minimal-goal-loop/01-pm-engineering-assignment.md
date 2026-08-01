# Engineering Assignment / 工程任务书

assignment_id: json-export-eng-001
milestone: deterministic-json-export
target_kr: KR-1
role_prompt_path: code-role/role-instance-prompts/engineering.md
role_objective: Implement deterministic schema-valid JSON export without changing existing text output.
observed_gap: JSON mode does not exist; 12 existing text-output regression tests pass.
authoritative_inputs:
- path: milestone-board.md
writable_scope:
- module_or_directory: src/reporter/
- module_or_directory: tests/
task_specific_exclusions: YAML, XML, streaming, plugin APIs, unrelated refactors, and existing text snapshots
required_checks:
| check_id | expected behavior | required evidence |
| --- | --- | --- |
| JSON-1 | Fixtures A, B, and C exit 0 and emit exactly `report_id`, `generated_at`, and `rows` as schema-valid JSON. | Command log, three output artifacts, and schema-validation output. |
| JSON-2 | Two runs against each fixture are byte-identical after applying the frozen `generated_at` fixture value. | SHA-256 comparison for two runs per fixture. |
| REG-1 | All 12 existing text-output regression tests pass without snapshot changes. | Fresh test command, 12/12 result, and empty snapshot diff. |
required_regressions:
- check_id: REG-1
required_output_attachment: attachments/engineering-candidate-evidence.md
stop_condition: Stop if the frozen JSON keys or existing text snapshots must change, or a required fixture/regression cannot run.
