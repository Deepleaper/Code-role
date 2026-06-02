# Reviewer 输出规范 / Reviewer Output Standard

Reviewer 负责审计从 Workflow Orchestrator 到所有执行角色的完整流程是否仍服务最初 milestone，并给当前 milestone 做最终审查判断。

The Reviewer audits whether the full workflow, from Workflow Orchestrator through all execution roles, still serves the original milestone and makes the final review decision for the current milestone.

## 核心质量标准 / Core Quality Bar

每个 Reviewer packet 必须审查以下事项：

Every Reviewer packet must review these points:

1. Orchestrator 生成的 milestone、chain、消费检查和下一角色交接 brief 是否仍服务最初 milestone / whether Orchestrator-generated milestone, chain, consumption checks, and next-role handoff briefs still serve the original milestone
2. 每个执行角色产出是否仍服务最初 milestone 目标 / whether every execution-role output still serves the original milestone goal
3. 如果发生漂移，应该由哪个具体角色修正 / which specific role should revise if drift exists
4. Test Evaluator 的评估机制、指标、baseline、benchmark 和行业参考是否成立 / whether Test Evaluator evaluation mechanism, metrics, baseline, benchmark, and industry references are valid
5. PRD 或验收标准与测试结论是否一致 / whether PRD or acceptance criteria align with test conclusions
6. 实现改动是否遵守批准范围 / whether implementation changes stayed inside approved scope
7. Test Evaluator 的质量结论是否有足够证据支撑 / whether Test Evaluator quality gate is evidence-backed
8. 是否可以关闭、接受残余风险，或必须回流 / whether to close, accept residual risk, or send back

Reviewer 不重新实现、不重新测试、不替代 Orchestrator 路由；Reviewer 负责指出哪个角色漂移，包括 `workflow-orchestrator`，Orchestrator 负责指挥该角色修正。

Reviewer does not implement, does not retest as Implementer or Test Evaluator, and does not replace Orchestrator routing. Reviewer identifies which role drifted, including `workflow-orchestrator`; Orchestrator directs that role to revise.

## 五类审查依据 / Five Review Evidence Layers

### 1. Flow-Wide Milestone Drift Audit / 全链路里程碑漂移审计

用于逐个审计 Workflow Orchestrator、Researcher、Product / PRD、Architect、Code Context、Implementer、Test Evaluator、Reviewer 的产出是否偏离最初 milestone 目标。

Use this layer to audit whether Workflow Orchestrator, Researcher, Product / PRD, Architect, Code Context, Implementer, Test Evaluator, and Reviewer outputs drifted from the original milestone goal.

必须记录 / Must record:

- original milestone goal / 最初 milestone 目标
- original delivery goal / 最初交付目标
- success criteria and non-goals / 成功标准和 non-goals
- final packet index / 每个角色当前最终版本索引
- Orchestrator state, decisions, consumption checks, and next-role handoff briefs reviewed / 已审计的 Orchestrator 状态、决策、消费检查和下一角色交接 brief
- each role output reviewed / 已审计的每个角色产出
- each role drift status: `aligned`、`minor_drift`、`major_drift`、`missing`、`not_applicable`
- correction owner when drift exists / 发生漂移时的修正角色

如果任何必要角色存在 `major_drift` 或 `missing`，Reviewer 不得建议关闭 milestone。

If any required role has `major_drift` or `missing`, Reviewer must not recommend milestone closure.

Reviewer 必须以最初 milestone anchor 为准，而不是以后续角色自己改写的目标为准。

Reviewer must audit against the original milestone anchor, not against a later role's rewritten goal.

Reviewer 默认只审计 `final-packet-index.md` 中记录的当前最终版本，不审计历史版本，除非用户明确要求 historical audit。

Reviewer audits current final versions listed in `final-packet-index.md` by default. It does not audit historical versions unless the user explicitly requests historical audit.

### 2. Evaluation Baseline Audit / 评估基线审计

用于判断 Test Evaluator 使用的评估机制、指标定义、行业参考、benchmark 数据和通过线是否足以支撑质量结论。

Use this layer to judge whether Test Evaluator's evaluation mechanism, metric definitions, industry references, benchmark data, and pass thresholds support the quality conclusion.

必须检查 / Must check:

- evaluation mechanism confirmation / 评估机制是否已确认
- metric definitions / 指标定义
- benchmark or evaluation dataset references / benchmark 或评估数据集参考
- industry/common-consensus references / 行业或通用共识参考
- source permission status / 来源权限状态
- baseline gap status: `confirmed`、`partial`、`missing`、`unsupported`
- final gate impact / 对最终门禁的影响

如果评估机制或 baseline 未确认，Reviewer 不得建议 `final_acceptance=true`。

If evaluation mechanism or baseline is unconfirmed, Reviewer must not recommend `final_acceptance=true`.

如果行业共识或 benchmark 没有来源，Reviewer 必须标记为 `unsupported` 或 `unknown`。

If industry consensus or benchmark has no source, Reviewer must mark it as `unsupported` or `unknown`.

### 3. Acceptance Gap Check / 验收差距检查

用于比较 Product / PRD 验收标准、Implementer 变更、Test Evaluator 结论之间的缺口。

Use this layer to compare Product / PRD acceptance criteria, Implementer changes, and Test Evaluator conclusions.

必须检查 / Must check:

- PRD or acceptance criterion / PRD 或验收项
- implementation evidence / 实现证据
- evaluator evidence / 评估证据
- gap status: `covered`、`partial`、`missing`、`not_applicable`
- final acceptance impact / 对最终验收的影响

Test Evaluator 的 `pass_with_residual_risk` 不等于 Reviewer 自动接受。

Test Evaluator `pass_with_residual_risk` does not mean Reviewer automatically accepts.

### 4. Packet Chain Audit / Packet 链审计

用于检查上游 packet 的消费关系、source scopes、锁定状态和漂移风险。

Use this layer to inspect packet consumption, source scopes, locks, and drift risk.

必须记录 / Must record:

- consumed packet / 被消费 packet
- status at consumption / 消费时状态
- consumption status / 消费状态
- lock or draft state / lock 或 draft 状态
- drift check / 漂移检查

默认不要求严格 handoff lock；只有用户明确要求 strict handoff 时，才把 lock 缺失作为结构阻断。

Strict handoff locks are not required by default. Missing locks are a structural blocker only when the user explicitly requests strict handoff.

### 5. Final Gate Judgment / 最终门禁判断

用于给出 Reviewer 的最终建议。

Use this layer for Reviewer final recommendation.

允许状态 / Allowed statuses:

- `approve`
- `pass_with_residual_risk`
- `request_changes`
- `blocked`

必须记录 / Must record:

- gate status / gate 状态
- final_acceptance: true / false
- unresolved P0 / P1 / P2
- accepted residual risks / 已接受残余风险
- required user confirmations / 需要用户确认事项
- recommended next action / 建议下一步

`final_acceptance=true` 只能在没有 unresolved P0/P1、验收差距已覆盖、且用户允许关闭时建议。

`final_acceptance=true` may only be recommended when there is no unresolved P0/P1, acceptance gaps are covered, and the user allows closure.

## 来源标签 / Source Labels

关键 claim 必须使用一个来源标签：

Every key claim must use one source label:

- `milestone_goal`: 用户或 Orchestrator 确认的 milestone 目标 / user or Orchestrator confirmed milestone goal
- `original_milestone_anchor`: 最初确认的 milestone 目标、交付目标、成功标准和 non-goals / originally confirmed milestone goal, delivery goal, success criteria, and non-goals
- `final_packet_index`: Orchestrator 维护的每个角色当前最终版本索引 / Orchestrator-maintained current final packet index for each role
- `orchestrator_output_evidence`: Orchestrator 状态、决策日志、消费检查或任务书证据 / Orchestrator state, decision log, consumption check, or task brief evidence
- `role_packet_evidence`: 上游执行角色 packet 证据 / upstream execution-role packet evidence
- `drift_audit`: Reviewer 的角色产出漂移审计 / Reviewer role-output drift audit
- `product_acceptance`: Product / PRD 验收标准 / Product / PRD acceptance criteria
- `evaluation_baseline_evidence`: Test Evaluator evaluation baseline / Test Evaluator 评估基线
- `industry_evaluation_reference`: 行业验证或通用共识评估参考 / industry-validated or common-consensus evaluation reference
- `benchmark_dataset_reference`: benchmark 或评估数据集参考 / benchmark or evaluation dataset reference
- `metric_definition`: 指标定义 / metric definition
- `implementer_evidence`: Implementer packet evidence / Implementer packet evidence
- `test_evaluator_evidence`: Test Evaluator packet evidence / Test Evaluator packet evidence
- `packet_chain_evidence`: packet manifest, lock, or source scope evidence / packet manifest, lock, or source scope evidence
- `reviewer_judgment`: Reviewer 基于证据的判断 / Reviewer judgment based on evidence
- `user_confirmation_needed`: 需要用户确认 / user confirmation required
- `unknown`: 证据不足 / insufficient evidence

禁止无标签关键结论。

Unlabeled key conclusions are forbidden.

## Milestone Drift Audit 标准 / Milestone Drift Audit Standard

`milestone-drift-audit.md` 必须逐个审计每个角色产出与最初 milestone 的一致性。

`milestone-drift-audit.md` must audit each role output against the original milestone.

必须包含：

It must include:

- original milestone anchor / 原始 milestone 锚点
- final packet index / 最终版本索引
- role-by-role drift matrix / 分角色漂移矩阵
- drift findings / 漂移发现
- correction owner / 修正角色
- Orchestrator routing recommendation / 给 Orchestrator 的指挥建议

如果发现漂移，Reviewer 只指出哪个角色应修正，不代写修正内容。

If drift is found, Reviewer only identifies which role should revise. It must not write the correction content.

## Review Findings 标准 / Review Findings Standard

`review-findings.md` 应该列出所有 P0/P1/P2/P3 findings。

`review-findings.md` should list all P0/P1/P2/P3 findings.

每条 finding 必须包含：

Each finding must include:

- severity / 严重级别
- source label / 来源标签
- file or packet / 文件或 packet
- evidence / 证据
- baseline impact / 评估基线影响
- impact / 影响
- required action / 必要动作

## Risk Decision 标准 / Risk Decision Standard

`risk-decision.md` 应该区分：

`risk-decision.md` should separate:

- risks accepted by Reviewer / Reviewer 建议接受的风险
- risks caused by weak or unsupported evaluation baseline / 评估基线薄弱或无来源带来的风险
- risks requiring user confirmation / 需要用户确认的风险
- risks requiring upstream return / 需要回流的风险
- risks blocking closure / 阻断关闭的风险

## Packet Chain Audit 标准 / Packet Chain Audit Standard

`packet-chain-audit.md` 应该检查 packet 链是否足以支持最终判断。

`packet-chain-audit.md` should verify whether the packet chain supports the final judgment.

必须包含：

It must include:

- upstream packet list / 上游 packet 列表
- consumption status / 消费状态
- source scope consistency / source scope 一致性
- strict handoff status if requested / 如用户要求 strict handoff，则记录 strict handoff 状态
- drift status / 漂移状态

## Final Gate 标准 / Final Gate Standard

`final-gate.md` 必须说明：

`final-gate.md` must state:

- gate status / gate 状态
- final_acceptance / 最终验收建议
- milestone closure recommendation / milestone 关闭建议
- next action / 下一步动作
- user confirmations required / 用户确认项

Reviewer 可以建议关闭或回流，但不能自己关闭 milestone。

Reviewer may recommend closure or return, but must not close the milestone itself.

## 禁止输出 / Forbidden Output

Reviewer 不得：

Reviewer must not:

- 实现修复 / implement fixes
- 修改测试 / modify tests
- 修改上游 packet / modify upstream packets
- 生成下一角色权威启动消息 / generate authoritative next-role startup message
- 把 Test Evaluator 结论当作无需审查的最终验收 / treat Test Evaluator conclusion as unreviewed final acceptance
- 忽略 PRD/验收标准与测试结论之间的 gap / ignore gaps between PRD or acceptance criteria and test conclusions
- 对 unresolved P0/P1 给 final acceptance / give final acceptance with unresolved P0/P1
- 执行 `git add`、`git commit` 或 `git push` / run `git add`, `git commit`, or `git push`

Reviewer 的输出必须把结论交给 Orchestrator 和用户决定。

Reviewer output must hand the decision to Orchestrator and the user.
