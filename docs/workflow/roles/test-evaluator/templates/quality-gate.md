# Quality Gate / 质量门禁

- evaluation_executed: 0 | 1
- product_contract_pass: 0 | 1
- milestone_observed_pass: 0 | 1
- kr_results: <KR id -> 0|1>
- required_checks_total:
- required_checks_passed:
- failed_check_ids:
- open_p0:
- open_p1:
- open_p2:
- evidence_basis:
- evaluation_sop_status: confirmed / unconfirmed / changed / blocked
- evaluation_baseline_status: confirmed / unconfirmed / blocked
- failed_check_owner: product-prd / architect / code-context / implementer / test-evaluator / workflow-orchestrator / user / none

`evaluation_executed=1` requires a valid runnable-candidate gate and the complete KR evaluation to run with evaluator-owned evidence. `milestone_observed_pass=1` is allowed only when every accepted KR passes. Any required unrun, missing, inferred, contradictory, or unsupported check keeps the relevant value at `0`.
