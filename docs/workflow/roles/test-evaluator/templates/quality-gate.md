# Quality Gate / 质量门禁

- evaluation_executed: 0 | 1
- kr_observed_pass: 0 | 1
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

`evaluation_executed=1` requires the complete assigned evaluation mode to run with evaluator-owned evidence. `kr_observed_pass=1` is allowed only in `full_evaluation` when every frozen target-KR check passes. Any required unrun, missing, inferred, or unsupported check keeps the relevant value at `0`.
