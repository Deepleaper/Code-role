# Project Practices / 项目实践

This document records engineering practices Code-role borrows from mature software projects.

本文记录 Code-role 从成熟软件项目中吸收的工程实践。

It does not add a heavy process layer. It defines the quality controls that keep role-based Codex work clear, reviewable, and aligned with the milestone.

它不是新增重流程，而是定义角色化 Codex 工作中必须保留的质量控制点，避免目标漂移和无证据结论。

## Practice 1: ADR / RFC Style Decisions

Architecture and product decisions should explain why a path was chosen, what alternatives were rejected, and what would trigger revision.

架构和产品决策要说明为什么选这个方案、为什么不选其他方案，以及什么条件会触发修正。

Apply this to:

- Product / PRD scope decisions
- Architect tradeoffs and contracts
- Code Context implementation constraints
- Implementer scope changes
- Reviewer correction routing

Minimum fields:

- decision
- alternatives considered
- rationale
- affected scope
- rollback or revision trigger
- source label

## Practice 2: Definition Of Done

Every role output needs a concrete completion standard.

每个角色产物都需要明确完成标准。

For Code-role, "done" means:

- the output serves the current milestone
- the packet or document path is explicit
- required evidence is present or marked unknown
- open questions and risks are visible
- downstream role can consume the output without guessing
- the completion response includes the copy-ready Orchestrator summary

If a role cannot meet these conditions, it should mark the packet as draft or blocked and explain the gap.

如果角色无法满足这些条件，就应保持 draft 或 blocked，并说明缺口。

## Practice 3: Claim Ledger

Strong claims need traceable evidence.

强结论必须有可追溯证据。

Every important claim should be labeled as one of:

- `repo_evidence`: directly supported by local project files or command output
- `upstream_packet`: inherited from an accepted upstream packet
- `external_source`: supported by public-source network research
- `user_input`: supplied by the user
- `role_judgment`: current role's professional judgment
- `unknown`: not yet supported

External research must not be presented as project fact. Papers, public docs, benchmarks, and industry practices can inform judgment, but they do not prove local project behavior.

外部研究不能当作当前项目事实。论文、公开文档、benchmark 和行业实践可以辅助判断，但不能证明本地项目已经具备某个行为。

## Practice 4: Golden Path Example

A workflow template is easier to adopt when one small example shows the complete path.

如果有一个最小完整示例，工作流模板会更容易被理解和采用。

Code-role should keep at least one example milestone that shows:

- Orchestrator milestone setup
- Researcher packet
- Product / PRD packet
- Architect packet
- Code Context packet
- Implementer packet
- Test Evaluator packet
- Reviewer packet
- Orchestrator closeout or residual-risk decision

The example should be small and synthetic enough to publish safely.

示例应足够小、足够安全，避免包含真实业务数据或私有项目记忆。

## Practice 5: Migration / Upgrade Policy

Template updates must not rewrite project memory.

模板升级不能重写项目记忆。

Safe to update:

- `code-role/README.md`
- `code-role/project-config.md`
- `code-role/role-instance-prompts/*.md`
- missing Orchestrator helper files such as `final-packet-index.md`

Do not overwrite by default:

- `code-role/workflow/orchestrator/workflow-state.md`
- `code-role/workflow/orchestrator/milestone-registry.md`
- `code-role/workflow/orchestrator/decision-log.md`
- `code-role/workflow/roles/**`
- `code-role/state-index/**`

If a new policy supersedes old state, append a dated override note to Orchestrator state files. Do not rewrite historical packets.

如果新策略覆盖旧状态，应在 Orchestrator 状态文件中追加带日期的 override 说明，不要批量改写历史 packet。

## Practice 6: Policy As Tests

Workflow rules should be tested like product behavior.

工作流规则也应像产品行为一样被测试。

Examples:

- Orchestrator must check milestone alignment before routing.
- Orchestrator must paste a copy-ready next-role startup message when routing forward.
- Execution roles must append a copy-ready Orchestrator summary.
- Daily workflow must not require `ready_for_next_role` or `packet.lock.json`.
- Public-source network research is allowed by default, while provider APIs and private resources require separate approval.
- Target-project `code-role/` remains local workflow assistance, not product release content.

Policy tests should protect the workflow from drifting back into heavy process or unsafe automation.

策略测试的目标是防止流程退回到重门禁，或变成不受控自动化。

## Practice 7: Release Boundary

What is excluded from release is as important as what is shipped.

哪些内容不发布，和发布什么同样重要。

In target projects:

- `code-role/` is local workflow assistance
- `code-role/` is not product runtime content
- `code-role/` is not a customer delivery bundle
- `code-role/` is not a release artifact
- `code-role/` should stay in `.git/info/exclude` unless the team explicitly promotes it into repo standards

In the Code-role repository itself, these workflow files are the product.

在 Code-role 仓库本身，这些 workflow 文件就是产品；在目标项目里，它们默认只是本地辅助。

## Practice 8: Network Research Boundary

Every role may use public-source network research when it helps the milestone.

每个角色都可以在有助于 milestone 时使用公开来源联网研究。

Required behavior:

- state the network purpose in the first response
- state likely public source types
- cite or record sources in the packet
- separate external practice from local project fact

Separate approval is still required for:

- real provider APIs
- authenticated or private resources
- downloading or executing remote content
- sending secrets or project-private data externally

## Practices Not Adopted

Code-role intentionally does not copy:

- heavy Jira or Scrum ceremony
- automatic full-chain agent execution
- mandatory strict handoff for every role
- broad historical packet migration
- process gates for normal Git operations

这些实践会增加流程负担，削弱 Code-role 的核心目标：讨论优先、角色清晰、用户控制。

## Default Bar

The default Code-role bar is:

```text
clear milestone
clear role boundary
clear upstream packet
clear claim evidence
clear downstream handoff
clear residual risk
```

中文默认标准：

```text
milestone 清晰
角色边界清晰
上游 packet 清晰
结论证据清晰
下游交接清晰
残余风险清晰
```
