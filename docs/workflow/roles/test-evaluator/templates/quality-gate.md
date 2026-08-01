# Quality Gate / 质量门

- evaluation_pass: 0 | 1
- sop_confirmed: 0 | 1
- baseline_confirmed: 0 | 1
- required_checks_total:
- required_checks_passed:
- failed_check_ids: none | <check ids>
- failed_check_owner: none | researcher | product-prd | architect | code-context | implementer | test-evaluator | workflow-orchestrator
- evidence_basis:
- unsupported_claims_rejected:

`evaluation_pass=1` requires every required check to pass with evaluator-observed evidence. Any required unrun, missing, inferred, or unsupported check makes it `0`.

## Evidence Summary / 证据摘要

| Claim | Source Label | Evidence | Check Pass (0/1) |
| --- | --- | --- | ---: |
| <claim> | evaluator_observed_result / test_command_output / regression_evidence / unknown | <source> | 0 |
