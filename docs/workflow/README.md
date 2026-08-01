# Full Profile: Eight-Role Workflow / 八角色完整版

Use the Full Profile when a milestone benefits from separate research, product, architecture, code-context, implementation, independent-evaluation, and final-audit ownership.

当复杂或高风险 milestone 需要独立的研究、产品、架构、上下文、实现、评估和最终审计责任时，使用八角色完整版。

The Full Profile follows the shared [Dialogue Control Contract](../dialogue-control.md). It keeps professional packet depth without making packet formatting the delivery goal.

八角色遵守共享[对话控制契约](../dialogue-control.md)：保留专业 packet 深度，但不把 packet 格式当成交付目标。

## Eight Roles / 八个角色

| Role | Professional ownership |
| --- | --- |
| Workflow Orchestrator / 项目经理 | Objective, binary KRs, artifact acceptance, blocker ownership, routing, closure |
| Researcher / 研究员 | Current-project evidence, frontier research, evidence map, risks, unknowns |
| Product / PRD / 产品经理 | User value, behavior, scope, non-goals, binary acceptance, claim boundary |
| Architect / 架构师 | Contracts, boundaries, interfaces, data/state flow, test strategy, architecture risks |
| Code Context / 上下文工程师 | Exact file/function/field/test/artifact seams and implementation constraints |
| Implementer / 实现工程师 | Project changes, tests, verification, candidate evidence |
| Test Evaluator / 测试评估师 | Frozen evaluation baseline and complete independent evaluation |
| Reviewer / 复核审计 | Orchestrator and role-by-role drift audit against the original milestone |

Each role uses a separate configured conversation. Every professional role returns to Workflow Orchestrator. There is no role-to-role self-routing.

每个角色使用独立对话；所有专业角色都回到项目经理；角色之间不能自行路由。

All non-Implementer roles produce governance or professional documents only. Implementer is the only role that changes target-project code under a valid assignment.

## Active Control / 活跃控制

- `milestone-contract.md` anchors Objective, KRs, evidence, non-goals, and claim boundaries.
- Orchestrator state records the current target, accepted artifact pointers, and blocker owner.
- Professional packet documents are the substantive handoff.
- `handoff.manifest.json` is packet index and provenance metadata, not a completion gate.
- `ready_for_next_role` and `packet.lock.json` are optional strict-audit controls only when explicitly requested.
- Chat summaries, role self-reports, packet status, and locks do not update a KR by themselves.

## Operating Loop / 运行闭环

```mermaid
flowchart LR
    U["User accepts Objective and KRs"] --> PM["Workflow Orchestrator"]
    PM --> R["Selected professional role"]
    R --> PM
    PM --> D{"Substantive evidence gap"}
    D --> R
    PM --> X["All KRs = 1 and required audit = 1"]
```

Workflow Orchestrator chooses the blocker owner from evidence. A complete role-specific assignment starts immediately. The role writes its packet, sends one short return, and does not choose the next role.

## Binary Rules / 二值规则

- Every accepted KR is `0` or `1`.
- Required unrun, missing, inferred, or qualitative evidence is `0`.
- `assignment_pass=1` means the current role's assigned checks passed; it does not pass the KR.
- `evaluation_pass=1` requires every frozen required check to pass independently.
- `review_gate_pass=1` requires every assigned final-audit check to pass.
- `partial_pass`, `pass_with_residual_risk`, and similar gate states are invalid.

## Assignment And Return / 任务与回报

Each professional role owns exactly one `templates/assignment.md` and one `templates/return.md`. Detailed professional outputs remain in that role's packet templates.

每个专业角色只有一份任务书模板和一份短回报模板；详细专业产出继续使用本角色 packet 模板。

- [Researcher](roles/researcher/ROLE.md)
- [Product / PRD](roles/product-prd/ROLE.md)
- [Architect](roles/architect/ROLE.md)
- [Code Context](roles/code-context/ROLE.md)
- [Implementer](roles/implementer/ROLE.md)
- [Test Evaluator](roles/test-evaluator/ROLE.md)
- [Reviewer](roles/reviewer/ROLE.md)
- [Workflow Orchestrator](orchestrator/ROLE.md)

## Human Gates / 人工闸门

Human confirmation is limited to Objective/KR/threshold/dataset/grader/claim changes, budget expansion, private-data external transfer, and irreversible external actions. Routine routing, local work, packet writing, public research, and normal project Git practice do not require another Code-role approval.

## Initialize / 初始化

```bash
python scripts/init_project_workflow.py \
  --target "/absolute/path/to/project" \
  --project-name "Project Name" \
  --initial-milestone workflow-bootstrap \
  --initial-chain full-chain \
  --write
```

See [Project Bootstrap](project-bootstrap.md) and [Role Configuration Guide](role-configuration-guide.md).

## Protocols / 协议

- [Dialogue Control](../dialogue-control.md)
- [Discussion-First Protocol](discussion-first-protocol.md)
- [Role Completion Contract](role-completion-contract.md)
- [Milestone Contract](milestone-contract.md)
- [Evaluation SOP](evaluation-sop.md)
- [Handoff Protocol](handoff-protocol.md)
- [Workflow Chain Policy](workflow-chain-policy.md)
- [Role Instance Setup](role-instance-setup.md)
- [Project Bootstrap](project-bootstrap.md)
- [State Index](state-index.md), optional non-authoritative navigation
- [Project Practices](project-practices.md)
- [Git Operation Policy](git-operation-policy.md)
- [Packet Schema](packet-schema.md), optional strict-audit metadata
- [Status Transition Protocol](status-transition-protocol.md), optional strict handoff
