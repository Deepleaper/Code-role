# PM Assignment / 项目经理任务书

assignment_id: json-export-001
milestone: deterministic-json-export
objective: Users can export a report as stable JSON without changing the existing text-output contract.
current_kr: KR-1
current_kr_status: 0
iteration: 1/3
assigned_workstation: engineering
assignment_mode: engineering_delivery
role_prompt_path: code-role/role-instance-prompts/engineering.md

professional_question: What is the smallest implementation that produces deterministic schema-valid JSON for fixtures A, B, and C while preserving all existing text output?
current_baseline: JSON mode does not exist; 12 existing text-output regression tests pass.
accepted_upstream_attachments: none
required_output_attachment: attachments/engineering-candidate-evidence.md

frozen_pass_conditions:
- check_id: JSON-1
  expected: Each of fixtures A, B, and C exits 0 and emits valid JSON with exactly the frozen keys report_id, generated_at, and rows.
  required_evidence: Command log, three output artifacts, and schema-validation output.
- check_id: JSON-2
  expected: Two runs against the same fixture produce byte-identical JSON after the frozen generated_at fixture value is applied.
  required_evidence: SHA-256 comparison for two runs per fixture.
- check_id: REG-1
  expected: All 12 pre-existing text-output regression tests pass without snapshot changes.
  required_evidence: Fresh test command and observed 12/12 pass result.

required_regression_checks:
- check_id: REG-1

out_of_scope:
- item: YAML, XML, streaming, plugin APIs, and unrelated refactors.

stop_conditions:
- condition: The frozen JSON keys must change.
- condition: Passing requires changing an existing text snapshot.
- condition: A required fixture or regression test cannot run.

return_template: code-role/templates/engineering-return.md
