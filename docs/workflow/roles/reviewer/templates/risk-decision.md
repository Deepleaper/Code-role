# Risk Decision / 风险决策

- risk_gate_pass: 0 | 1 [reviewer_judgment]
- blocking_risk_ids: none | <risk ids> [reviewer_judgment]

| Risk ID | Severity | Evidence | Accepted Non-Goal Or KR | Pass (0/1) | Correction Owner |
| --- | --- | --- | --- | ---: | --- |
| {{risk_id}} | P0 / P1 / P2 / P3 | {{evidence}} | {{non_goal_or_kr}} | 0 | workflow-orchestrator / researcher / product-prd / architect / code-context / implementer / test-evaluator / user |

A risk does not create a gray gate. It is covered by an accepted non-goal or KR and passes, or it remains a failed check.
