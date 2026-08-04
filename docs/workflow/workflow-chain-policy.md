# Workflow Stage Policy / 工作流阶段策略

Full Profile separates professional ownership while preserving one global delivery dependency order.

八角色完整版拆分专业责任，但不能颠倒完整产品、工程候选物和独立评估之间的依赖关系。

## Mandatory Stage Order / 强制阶段顺序

| Stage | Typical roles | Required global result |
| --- | --- | --- |
| Milestone definition | Workflow Orchestrator + user | complete Objective and `KR-1...KR-N` |
| Research and product definition | Researcher when needed, Product / PRD | complete Product Contract for every existing `KR-1...KR-N` |
| Architecture and repository context | Architect, Code Context | complete technical and repository contracts for the whole Product Contract |
| Engineering delivery | Implementer | `STEP-1...STEP-N`, integrated runnable candidate, regressions, reproducibility |
| Independent evaluation | Test Evaluator | complete KR evaluation after candidate readiness |
| Audit and closure | Reviewer when required, Workflow Orchestrator | full-chain audit and milestone decision |

Roles may be skipped only when a current accepted artifact already satisfies the complete stage contract. A downstream dependency cannot be skipped:

- Product / PRD must not work one KR at a time.
- Implementer is the only Full Profile role that owns STEP decomposition.
- Test Evaluator must not start before a complete runnable candidate exists.
- Reviewer must not start before independent evaluation.

## Named Profiles / 命名组合

Named profiles indicate which supporting roles are normally needed; they do not weaken stage gates:

| Profile | Typical path |
| --- | --- |
| `full-chain` | Researcher -> Product / PRD -> Architect -> Code Context -> Implementer -> Test Evaluator -> Reviewer |
| `mini-chain` | Product / PRD -> Architect or Code Context -> Implementer -> Test Evaluator -> optional Reviewer |
| `patch-chain` | Code Context when needed -> Implementer -> Test Evaluator -> optional Reviewer |
| `docs-only-chain` | Relevant document owner -> independent artifact check when required |
| `research-only` | Researcher -> Workflow Orchestrator decision; no software completion claim |

Every selected role returns to Workflow Orchestrator. The Orchestrator accepts or rejects the complete stage artifact and issues the next stage assignment.

## Evaluation And Review / 评估与审计

- Implementer cannot pass KRs or the milestone.
- Test Evaluator evaluates the full accepted KR contract, not STEP activity or the latest diff.
- Reviewer audits the complete current final chain against the original Project OKR.
- Required unrun evidence is `0`.
- Evaluation and review gates are binary.

## Iteration Stop / 迭代停止

After three failed Engineering-to-Evaluation attempts for the complete candidate contract, stop implementation and ask the user to revise the global product contract, change scope or budget, repair evaluation execution, or terminate the milestone.
