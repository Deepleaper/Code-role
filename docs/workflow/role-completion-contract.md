# Full Profile Work Unit Acceptance / 八角色工作单元验收契约

This contract applies the shared [Dialogue Control Contract](../dialogue-control.md) to Full Profile professional work.

## 1. Stage Work And The Project OKR Are Separate / 阶段工作与项目 OKR 分离

```text
work_unit_pass = 1
```

means every check assigned to the current role has concrete evidence.

```text
work_unit_pass = 0
```

means at least one assigned check failed, was not run, is unknown, or lacks evidence.

A stage work-unit pass never changes a Project KR by itself. A `KR-*` remains `0` until every accepted outcome condition has independent evidence. An Engineering `STEP-*` pass proves only that execution stage.

## 2. Primary Artifact Is Authoritative / 主专业产物是权威

One primary professional artifact and its referenced evidence are authoritative. A manifest is optional provenance metadata; the short return is transport only.

- Project Manager inspects the primary artifact.
- Missing return fields, field order, draft status, or absent optional lock do not invalidate sufficient evidence.
- Strict readiness and locks are optional audit controls only when explicitly requested.
- Project Manager may summarize but may not invent a professional conclusion.

## 3. Mechanical Check / 机械检查

```text
check_pass = 1 only when expected observation and required evidence are present
check_pass = 0 otherwise
work_unit_pass = 1 only when every acceptance check_pass = 1
work_unit_pass = 0 otherwise
```

Missing, unrun, unknown, inferred, contradictory, or qualitative evidence is `0`.

## 4. Global Stage Routing / 全局阶段路由

Project Manager routes the complete current stage contract in mandatory dependency order:

- complete milestone research evidence, when needed: Researcher;
- complete product meaning and acceptance across every KR: Product / PRD;
- complete product architecture contract, when needed: Architect;
- complete repository implementation map, when needed: Code Context;
- Engineering STEP decomposition and complete runnable candidate: Implementer;
- complete KR independent evidence after candidate readiness: Test Evaluator;
- required final flow audit after evaluation: Reviewer;
- Objective, KR, threshold, claim, budget, or irreversible action: user decision.

Product, Architecture, and Code Context are global contracts, not one-KR work slices. Implementer alone decomposes delivery into `STEP-1...STEP-N`. Test Evaluator must reject any assignment issued before `candidate_ready_for_independent_evaluation=1` or without a runnable candidate artifact.

An incomplete stage returns to the substantive contract owner. Dependency order cannot be reversed.

## 5. Evaluation And Review / 评估与审计

- Test Evaluator reports `evaluation_executed: 0|1`, one binary result for every `KR-*`, `product_contract_pass: 0|1`, and `milestone_observed_pass: 0|1`.
- Reviewer reports `review_executed: 0|1` and `review_gate_pass: 0|1`.
- Required unrun checks are `0`.
- `partial_pass`, `pass_with_residual_risk`, and “mostly complete” cannot be gate values.

## 6. No Format-Only Rework / 禁止格式返工

Only missing or failed professional checks justify rework. Do not request revision solely to add startup confirmation, reorder fields, change packet readiness, create a lock, repeat evidence, or add a next-role recommendation.
