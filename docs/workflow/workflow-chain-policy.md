# Workflow Selection Policy / 工作流选择策略

Full Profile separates professional ownership but does not impose a fixed chain. Workflow Orchestrator routes to the owner of the current evidence gap.

八角色拆分专业责任，但不强制每次依次走完八个角色。

## Named Profiles / 命名组合

Named chains are planning presets, not routing authority:

| Chain | Typical roles |
| --- | --- |
| `full-chain` | Researcher, Product / PRD, Architect, Code Context, Implementer, Test Evaluator, Reviewer as needed |
| `mini-chain` | Product / PRD or Architect, Code Context, Implementer, Test Evaluator, optional Reviewer |
| `patch-chain` | Code Context when needed, Implementer, Test Evaluator, optional Reviewer |
| `docs-only-chain` | Relevant document owner, optional Reviewer |
| `research-only` | Researcher, then Orchestrator decision |

## Evidence Routing / 证据路由

- evidence or frontier uncertainty: Researcher;
- product ambiguity: Product / PRD;
- architecture ambiguity: Architect;
- repository-context ambiguity: Code Context;
- implementation gap: Implementer;
- evaluation baseline or independent evidence gap: Test Evaluator;
- final flow-wide drift audit: Reviewer.

Every selected role returns to Workflow Orchestrator. Architecture usually benefits from Code Context before implementation, but the Orchestrator may skip roles whose professional uncertainty is already resolved by accepted evidence.

## Routing Gate / 路由门禁

Route when:

```text
assignment is complete
target evidence gap is explicit
authoritative inputs are named
role deliverable and binary acceptance checks are frozen
one required primary artifact path is defined
```

Do not route based on packet readiness, a role recommendation, or a fixed next-role table.

## Evaluation And Review / 评估与审计

- Implementer cannot pass its own KR.
- Test Evaluator evaluates the complete frozen required scope, not only the latest diff.
- Reviewer, when required, audits Workflow Orchestrator and all accepted final role outputs against the original milestone.
- Required unrun evidence is `0`.
- Evaluation and review gates are binary.

## Iteration Stop / 迭代停止

After three failed implementation-to-evaluation attempts for the same primary KR, stop implementation and choose one: repair product definition, repair evaluation, split the KR, change scope/budget with the user, or terminate the milestone.
