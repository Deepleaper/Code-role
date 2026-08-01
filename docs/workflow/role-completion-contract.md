# Full Profile Assignment Acceptance / 八角色任务验收契约

This contract applies the shared [Dialogue Control Contract](../dialogue-control.md) to Full Profile packets.

本契约把共享[对话控制契约](../dialogue-control.md)应用到八角色 packet 工作流。

## 1. Two Binary Results / 两个二值结果

```text
assignment_pass = 1
```

means every check assigned to the current role has concrete evidence.

```text
assignment_pass = 0
```

means at least one assigned check failed, was not run, is unknown, or lacks evidence.

`assignment_pass` does not update a milestone KR. A KR remains `0` until Project Manager accepts independent evidence for every frozen KR condition.

`assignment_pass` 不直接更新 milestone KR。冻结条件没有全部获得独立证据前，KR 始终为 `0`。

## 2. Artifact Is Authoritative / 附件是专业权威

The packet's professional documents and referenced evidence are authoritative for role work. `handoff.manifest.json` is a document index and provenance record. The short role return is a transport summary.

packet 中的专业文档和引用证据是角色工作的权威内容；`handoff.manifest.json` 是文档索引和来源记录；短回报只是流转摘要。

- Project Manager must inspect the professional documents.
- Missing return fields, field order, packet `draft` status, or absent lock do not invalidate otherwise sufficient professional evidence.
- Strict `ready_for_next_role` and `packet.lock.json` remain optional audit controls only when the user explicitly requests strict handoff.
- Project Manager may extract a summary from the packet but may not invent a professional conclusion.

## 3. Mechanical Check / 机械检查

For each assigned check:

```text
check_pass = 1 only when expected observation and required evidence are both present
check_pass = 0 otherwise

assignment_pass = 1 only when every required check_pass = 1
assignment_pass = 0 otherwise
```

Required `not_run`, `unknown`, inferred, or qualitative results are `0`. Diagnostic risk labels never create a third completion state.

## 4. Routing From Substance / 依据实质路由

Project Manager routes from the failed check and its owner:

- research evidence missing: Researcher;
- product meaning or acceptance ambiguous: Product / PRD;
- architecture contract ambiguous: Architect;
- repository seam or impact unknown: Code Context;
- implementation or candidate evidence missing: Implementer;
- evaluation mechanism invalid or independent evidence missing: Test Evaluator;
- final flow drift or acceptance gap audit missing: Reviewer;
- Objective, KR, threshold, claim boundary, budget, or irreversible action decision: user through Project Manager.

An incomplete assignment does not automatically return to the same role. It returns to the role that owns the substantive blocker.

未通过的任务不自动打回原角色，而是交给实质 blocker 的责任角色。

## 5. Short Return / 短回报

Every professional role uses its role-specific return template. It contains:

```text
assignment_id
assignment_pass: 0 | 1
check_results
artifact_paths
evidence_paths
substantive_blockers
return_to: workflow-orchestrator
```

The role must not recommend the next role. Project Manager owns routing.

## 6. Evaluation And Review / 评估与审计

- Test Evaluator reports `evaluation_pass: 0|1`.
- Reviewer reports `review_gate_pass: 0|1`.
- A required unrun check is `0`.
- `partial_pass`, `pass_with_residual_risk`, `mostly complete`, and similar phrases cannot be gate values.
- Risks remain explicit records linked to failed checks, new KRs, or accepted non-goals.

## 7. No Format-Only Rework / 禁止格式返工

Project Manager must not request a role revision solely to:

- restate read/write/forbidden scope;
- add a startup confirmation;
- reorder return fields;
- convert a packet from `draft` to `ready_for_next_role` in normal mode;
- create a packet lock;
- repeat evidence already present in the artifact;
- add a next-role recommendation.

Only missing or failed professional checks justify rework.
