# PM Assignment -> Product Strategy / 项目经理任务书 -> 产品策略

assignment_id: json-export-product-001
milestone: deterministic-json-export
delivery_stage: product_definition
role_prompt_path: code-role/roles/product-strategy.md
milestone_objective: Users can export a report as stable JSON without changing the existing text-output contract.
milestone_okr_path: milestone-board.md#milestone-key-results--里程碑关键结果
milestone_okr_scope: all_accepted_mkrs
role_deliverable: complete_product_okr_and_product_contract
authoritative_inputs:
- path: milestone-board.md
acceptance_checks:
| check_id | complete product-contract result | required evidence |
| --- | --- | --- |
| PRODUCT-OKR | `PKR-1...PKR-N` defines the complete product result | complete PKR table |
| MKR-COVERAGE | MKR-1 and MKR-2 each map to product behavior | MKR-to-PKR matrix |
| ENGINEERING-READY | no product behavior must be invented by Engineering | CLI, JSON, error, and compatibility contracts |
| EVALUATION-READY | every PKR has observable evidence | product acceptance matrix |
required_artifact_path: 02-product-contract.md
irreversible_actions: none
