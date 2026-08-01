# Source Map / 读写边界

This file defines stable role ownership. Task-specific input paths, writable modules, exclusions, and evidence belong in the current role assignment. Historical packet scopes never accumulate into permanent restrictions.

本文件只定义稳定角色边界。任务级输入路径、可写模块、特殊排除项和证据要求写在当前任务书中；历史 packet 的范围不得累积成永久限制。

## Shared Read Rule / 通用读取规则

Every role may read the active dialogue contract, milestone contract, workflow state, its own role contract and output standard, assignment-named artifacts, and repository files reasonably necessary to answer its professional question.

角色不需要为普通本地读取逐文件申请许可。若任务缺少会改变产品目标、评估基线、成本预算或不可逆动作的用户决策，才集中提出 blocker。

## Workflow Orchestrator / 项目经理

May read all accepted professional artifacts and their referenced evidence.

May write only:

```text
code-role/workflow/orchestrator/workflow-state.md
code-role/workflow/orchestrator/milestone-contract.md
code-role/workflow/orchestrator/final-packet-index.md
code-role/workflow/evaluation/evaluation-sop.md
```

Must not write professional role conclusions, target-project code, tests, or execution-role packets.

## Researcher / 研究员

May read repository files and public sources needed to answer the assigned research question.

Writes only:

```text
docs/workflow/roles/researcher/reports/<milestone>/packet-vNNN/
```

Must not write PRD commitments, architecture commitments, code, tests, evaluation verdicts, or Orchestrator state.

## Product / PRD / 产品经理

May read assignment-named evidence, relevant product documents, repository behavior evidence, and public market or industry sources.

Writes only:

```text
docs/workflow/roles/product-prd/reports/<milestone>/packet-vNNN/
```

Must not write architecture implementation, code, tests, evaluation verdicts, or Orchestrator state.

## Architect / 架构师

May read accepted product/research artifacts and repository files needed to verify current architecture facts.

Writes only:

```text
docs/workflow/roles/architect/reports/<milestone>/packet-vNNN/
```

Must not implement code, change tests, make product commitments, or issue evaluation verdicts.

## Code Context / 上下文工程师

May inspect any repository file, function, test, dependency, configuration, or generated artifact reasonably necessary to map the assigned implementation seam and impact.

Writes only:

```text
docs/workflow/roles/code-context/reports/<milestone>/packet-vNNN/
```

Must not implement fixes, change tests, or convert a writable candidate into authorization.

## Implementer / 实现工程师

May read and modify target-project files inside the modules or directories authorized by a complete Implementer assignment. The assignment lists task-specific exclusions only when needed; it does not need to predict every changed file.

May also write its own packet under:

```text
docs/workflow/roles/implementer/reports/<milestone>/packet-vNNN/
```

Must not change Objective, KR, frozen evaluation inputs, public claim boundaries, task-specific exclusions, or upstream packets.

## Test Evaluator / 测试评估师

May read and execute everything required by the frozen evaluation SOP, including repository code, tests, datasets, candidate artifacts, and runtime outputs.

Writes only:

```text
docs/workflow/roles/test-evaluator/reports/<milestone>/packet-vNNN/
```

Must not repair the candidate, alter the frozen SOP after seeing results, or turn Implementer self-report into independent evidence.

## Reviewer / 复核审计

May read the original milestone anchor, Workflow Orchestrator outputs, every accepted final role artifact, frozen evaluation SOP, evaluator evidence, relevant source/test evidence, and Git diff needed for the assigned full-flow audit.

Writes only:

```text
docs/workflow/roles/reviewer/reports/<milestone>/packet-vNNN/
```

Must not implement fixes, rerun itself as Test Evaluator, rewrite upstream artifacts, route directly to another role, or close the milestone.

## Network And External Actions / 联网与外部动作

Public-source research is allowed when relevant and must be labeled in the professional artifact. Explicit user approval is required for authenticated/private resources, paid provider work outside the accepted budget, remote code execution, private-data external transfer, or irreversible external actions.
