# Full Profile Work Unit Acceptance / 八角色工作单元验收契约

This contract applies the shared [Dialogue Control Contract](../dialogue-control.md) to Full Profile professional work.

## 1. Work Unit And KR Are Separate / 工作单元与 KR 分离

```text
work_unit_pass = 1
```

means every check assigned to the current role has concrete evidence.

```text
work_unit_pass = 0
```

means at least one assigned check failed, was not run, is unknown, or lacks evidence.

A work unit pass never changes a delivery KR by itself. A KR remains `0` until every accepted outcome condition has independent evidence.

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

## 4. Routing From Failed Evidence / 依据失败证据路由

Project Manager routes the exact failed evidence:

- research evidence: Researcher;
- product meaning or acceptance: Product / PRD;
- architecture contract: Architect;
- repository seam: Code Context;
- runnable candidate or engineering defect: Implementer;
- evaluation mechanism or independent evidence: Test Evaluator;
- required final flow audit: Reviewer;
- Objective, KR, threshold, claim, budget, or irreversible action: user decision.

An incomplete assignment does not automatically return to the same role. It returns to the substantive blocker owner.

## 5. Evaluation And Review / 评估与审计

- Test Evaluator reports `evaluation_executed: 0|1` and `kr_observed_pass: 0|1`.
- Reviewer reports `review_executed: 0|1` and `review_gate_pass: 0|1`.
- Required unrun checks are `0`.
- `partial_pass`, `pass_with_residual_risk`, and “mostly complete” cannot be gate values.

## 6. No Format-Only Rework / 禁止格式返工

Only missing or failed professional checks justify rework. Do not request revision solely to add startup confirmation, reorder fields, change packet readiness, create a lock, repeat evidence, or add a next-role recommendation.
