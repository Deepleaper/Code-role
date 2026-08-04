# PM Assignment -> Product Strategy / 项目经理任务书 -> 产品策略

assignment_id: json-export-product-001
milestone: deterministic-json-export
delivery_stage: product_definition
role_prompt_path: code-role/roles/product-strategy.md
milestone_objective: Users can export a report as stable JSON without changing the existing text-output contract.
project_okr_path: milestone-board.md#milestone-key-results--里程碑关键结果
project_okr_scope: all_accepted_krs
role_deliverable: complete_product_contract_for_existing_krs
authoritative_inputs:
- path: milestone-board.md
acceptance_checks:
| check_id | complete product-contract result | required evidence |
| --- | --- | --- |
| PRODUCT-CONTRACT | KR-1 and KR-2 each have complete product behavior and acceptance detail | Product Contract organized by unchanged KR IDs |
| KR-COVERAGE | KR-1 and KR-2 are both fully specified | KR product-coverage matrix |
| ENGINEERING-READY | no product behavior must be invented by Engineering | CLI, JSON, error, and compatibility contracts |
| EVALUATION-READY | every KR has observable evidence | product acceptance matrix |
required_artifact_path: 02-product-contract.md
irreversible_actions: none
