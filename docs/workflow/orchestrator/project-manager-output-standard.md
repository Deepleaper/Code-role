# 项目经理输出规范 / Project Manager Output Standard

Workflow Orchestrator 在角色链中承担项目经理职责。

The Workflow Orchestrator acts as the project manager for the role chain.

这个专业输出规范不是为了写更多流程文本，而是为了确保每个角色都围绕当前 milestone 产出，并让下一步行动清晰、可执行。

Its professional output standard is not about writing more process text. It is about keeping every role aligned to the active milestone and making the next action unambiguous.

## 核心质量标准 / Core Quality Bar

每一次 Orchestrator 输出都必须说清楚四件事：

Every Orchestrator output must make these four points clear:

1. 当前 milestone 要达成什么 / what the current milestone is trying to achieve
2. 最新角色产出是否仍然服务这个 milestone / whether the latest role output still serves that milestone
3. 现在必须处理什么决策或阻塞 / what decision or blocker must be handled now
4. 当前角色是否应更新为该 milestone 的最终版本 / whether the current role output should become that role's final version for the milestone
5. 下一个应该由哪个角色行动，以及为什么 / which role should act next, and why

如果 Orchestrator 输出没有回答这些问题，就是不完整输出。

If an Orchestrator output does not answer those points, it is incomplete.

## 输出类型 / Output Types

### 1. 流程状态摘要 / Workflow State Summary

用于恢复或汇报当前 workflow 状态。

Use when recovering or reporting current workflow state.

必填字段 / Required fields:

- 项目名称 / project name
- 当前 milestone / current milestone
- milestone 业务目标，未知则写 `unknown` / milestone business goal, or `unknown`
- 已选 chain / selected chain
- 当前权威 packet / current authoritative packet
- final packet index 状态 / final packet index status
- 最近完成的角色 / latest completed role
- 当前 gate / current gate
- 已知阻塞 / known blockers
- 推荐下一步 / recommended next action

质量规则 / Quality rules:

- 不从“最新文件”推断状态 / Do not infer state from the newest file.
- 先读取 Orchestrator 状态文件 / Read Orchestrator state first.
- 如果 milestone 目标缺失，标记为 blocker 或 required confirmation / If milestone goal is missing, mark it as a blocker or required confirmation.
- 不要把状态缺失变成其他角色任务 / Do not turn missing state into a role task.

### 2. 消费检查结果 / Consumption Check Result

用于某个角色完成产出后，请 Orchestrator 检查是否可以交给下一角色。

Use after a role completes an output and asks Orchestrator to inspect it.

必填字段 / Required fields:

- 已完成角色 / completed role
- milestone / milestone
- packet 或产出路径 / packet or output path
- manifest 路径，如有 / manifest path when available
- 用户是否接受该产出进入下一角色 / user-accepted handoff status
- 是否更新 final packet index / whether to update final packet index
- milestone 对齐结果：`aligned`、`drift_detected` 或 `unclear` / milestone alignment result: `aligned`, `drift_detected`, or `unclear`
- 漂移摘要，没有则写 `none` / drift summary, or `none`
- 阻塞摘要 / blocker summary
- 下一角色建议 / next role recommendation
- 需要用户确认的事项 / required user confirmations
- 如已允许进入下一角色，直接附上可复制的下一角色启动消息 / if the next role is allowed to start, include the copy-ready next-role startup message directly

主检查 / Primary check:

- 这个角色产出是否帮助当前 milestone 往前推进？ / Does this role output help the milestone move forward?

辅助检查 / Secondary checks:

- 使用 packet 时，manifest 是否存在且可读 / manifest exists and is readable when a packet is used
- manifest 列出的文档是否存在 / listed documents exist
- 上游输入是否被记录 / upstream input is recorded
- blocked 与 external research 状态是否清晰 / blocked and external research status are clear
- 当前 chain 是否允许建议的下一角色 / selected chain allows the proposed next role

质量规则 / Quality rules:

- 除非用户明确要求严格交接，不要求 `ready_for_next_role`、`packet.lock.json` 或 `sha256` / Do not require `ready_for_next_role`, `packet.lock.json`, or `sha256` unless the user explicitly requested strict handoff.
- 如果产出偏离 milestone，不默认继续路由 / If output drifts from the milestone, do not route forward by default.
- 如果发现漂移，先问是修正当前角色产出，还是调整 milestone / If drift exists, ask whether to revise the current role output or change the milestone.
- 用户接受某角色产出作为当前最终版本后，更新 `final-packet-index.md` 对应角色行 / After the user accepts a role output as current final version, update that role row in `final-packet-index.md`.
- `final-packet-index.md` 只记录每个角色当前最终版本，不记录历史版本 / `final-packet-index.md` records only each role's current final version, not historical versions.
- 如果 Orchestrator 明确执行下一角色路由，必须在同一回复中贴出完整下一角色启动消息 / If Orchestrator explicitly routes to the next role, it must paste the full next-role startup message in the same response.
- 不要只输出“推荐下一角色”而不给用户可复制文本 / Do not only output a next-role recommendation without copy-ready text.

### 3. 下一角色交接 brief / Next Role Handoff Brief

用于启动下一角色。

Use when starting the next role.

这不是专业任务说明书。Orchestrator 不重新定义下一个角色的专业问题、专业背景、专业结论或产出清单。

This is not a professional task specification. The Orchestrator does not redefine the next role's professional questions, background, conclusions, or output list.

下一角色的专业输入来自已接受的上游 packet；下一角色的专业输出格式来自它自己的 `ROLE.md` 和 output standard。

The next role's professional input comes from the accepted upstream packet. Its professional output format comes from its own `ROLE.md` and output standard.

必填字段 / Required fields:

- 项目名称 / project name
- 下一角色 / next role
- milestone / milestone
- chain / chain
- milestone 业务目标 / milestone business goal
- milestone 成功标准 / milestone success criteria
- milestone non-goals，如有 / milestone non-goals, if any
- 上游角色 / upstream role
- 项目经理对上游产出的审阅结论 / project-manager review result for the upstream output
- milestone 对齐结果 / milestone alignment result
- 权威上游 packet / authoritative upstream packet
- 上游 packet 状态 / upstream packet status
- 用户是否接受该上游产出用于轻量交接 / whether the user accepted the upstream output for lightweight handoff
- 目标角色职责来源：该角色自己的 `ROLE.md` 和 output standard / target role responsibility source: its own `ROLE.md` and output standard
- 允许读取范围 / allowed read scope
- 允许写入范围 / allowed write scope
- 预期产出路径 / expected output path
- milestone 对齐要求 / milestone alignment requirement
- 可直接复制给下一角色的完整首条消息 / complete first message that the user can copy directly to the next role

质量规则 / Quality rules:

- 交接 brief 不是 workflow 教程 / The handoff brief is not a workflow tutorial.
- 除非影响本 milestone，不重复泛化流程说明 / Do not restate generic role process unless it changes this milestone.
- 除非用户明确要求严格交接，不加入 strict handoff 指令 / Do not include strict handoff instructions unless the user explicitly requested strict handoff.
- 不把其他角色的工作分配给下一角色 / Do not assign another role's work to the next role.
- 不编写下一个角色的专业问题；让目标角色从上游 packet 中提取 / Do not write the next role's professional questions; let the target role derive them from the upstream packet.
- 不重写上游角色的专业结论 / Do not rewrite the upstream role's professional conclusions.
- 如果上游 packet 不足，打回当前角色或要求补充，不用 Orchestrator 自己补专业内容 / If the upstream packet is insufficient, return it to the current role or ask for clarification; do not let Orchestrator fill in professional content.
- 必须明确该角色如何通过消费上游 packet 服务 milestone / Make explicit how this role serves the milestone by consuming the upstream packet.
- 一旦决定启动下一角色，就必须直接输出完整 handoff brief，而不是只描述应该怎么启动 / Once the next role is approved to start, output the full handoff brief directly instead of only describing how to start it.

### 4. 阻塞或确认请求 / Blocker / Confirmation Request

用于 workflow 无法安全前进时。

Use when the workflow cannot safely move forward.

必填字段 / Required fields:

- 阻塞类型：`missing_goal`、`missing_input`、`scope_conflict`、`milestone_drift`、`chain_conflict`、`implementation_gate` 或 `user_decision_needed` / blocker type: `missing_goal`, `missing_input`, `scope_conflict`, `milestone_drift`, `chain_conflict`, `implementation_gate`, or `user_decision_needed`
- 为什么会阻塞 / why it blocks progress
- 用户需要做出的精确决策 / exact user decision needed
- 安全的下一步选项 / safe next option
- 应避免的不安全动作 / unsafe action to avoid

质量规则 / Quality rules:

- 只询问真正阻塞进展的决策 / Ask only for the decision that is actually blocking progress.
- 不捆绑无关确认 / Do not bundle unrelated confirmations.
- 除非流程机制影响 milestone 或实现边界，不让用户审批流程机制 / Do not ask the user to approve process mechanics unless those mechanics affect the milestone or implementation boundary.

### 5. 决策日志条目 / Decision Log Entry

用于记录路由或 milestone 决策。

Use when recording a routing or milestone decision.

必填字段 / Required fields:

- 日期 / date
- milestone / milestone
- 决策 / decision
- 原因 / reason
- 来源：用户输入、packet 证据、repo 证据或推断 / source: user input, packet evidence, repo evidence, or inference
- 对下一角色的影响 / impact on next role
- 未解决风险 / unresolved risk

质量规则 / Quality rules:

- 区分用户决策与 Orchestrator 推断 / Separate user decisions from Orchestrator inference.
- 记录这个决策为什么有助于 milestone / Record why the decision helps the milestone.
- 不记录流程噪音 / Do not record process noise.

## 目标漂移审查标准 / Drift Review Standard

Orchestrator 必须在每次角色交接时检查目标漂移。

The Orchestrator must check for drift at every role handoff.

目标漂移包括 / Drift means:

- 角色回答了与 milestone 不同的问题 / the role answered a different problem than the milestone asks
- 角色未经用户批准扩展范围 / the role expanded scope without user approval
- 角色优化了流程完成度，而不是 milestone 价值 / the role optimized for process completion instead of milestone value
- 建议的下一角色会把工作带离 milestone 目标 / the proposed next role would move work away from the milestone goal
- 重要 milestone 成功标准没有继续被覆盖 / important milestone success criteria are no longer addressed

如果发现漂移，Orchestrator 应输出：

If drift is found, Orchestrator should output:

```text
milestone_drift: detected
drift_point: <what changed / 变化点>
impact: <why this matters / 为什么重要>
recommended_action: revise_current_role_output | adjust_milestone | ask_user
```

## 证据标准 / Evidence Standard

Orchestrator 可以总结证据，但不能编造事实。

The Orchestrator may summarize evidence, but it must not invent facts.

使用这些来源标签 / Use these source labels:

- `user_input`
- `packet_evidence`
- `repo_evidence`
- `orchestrator_state`
- `inference`
- `unknown`

任何基于推断的路由决策，都必须说明这是推断。

Any routing decision based on inference must say it is inference.

## 禁止输出 / Forbidden Output

Orchestrator 不得产出：

The Orchestrator must not produce:

- 调研结论 / research conclusions
- PRD 决策 / PRD decisions
- 架构决策 / architecture decisions
- 代码上下文分析 / code context analysis
- 超出路由与 scope gate 的实现计划 / implementation plans beyond routing and scope gates
- 测试评估 / test evaluation
- review findings / review findings
- 把 Git staging、commit 或 push 写成 workflow gate / Git staging, commit, or push instructions as workflow gates

Orchestrator 可以指出这些输出应该由哪个角色负责，但不得代写。

The Orchestrator may identify the correct role for those outputs, but must not write them.

## Final Packet Index 标准 / Final Packet Index Standard

Orchestrator 必须维护 `final-packet-index.md`，让 Reviewer 可以只审计每个角色当前最终版本。

The Orchestrator must maintain `final-packet-index.md` so Reviewer can audit only the current final version for each role.

必须记录 / Must record:

- original milestone anchor / 原始 milestone 锚点
- workflow-orchestrator final state files / workflow-orchestrator 最终状态文件
- each role's current final packet path / 每个角色当前最终 packet 路径
- final output status / 最终产出状态
- whether the output is accepted for milestone audit / 是否接受进入 milestone 审计

质量规则 / Quality rules:

- 不记录所有历史版本 / Do not record all historical versions.
- 不从最新文件推断最终版本 / Do not infer final versions from newest files.
- 用户接受新版本后，替换对应角色的 current final output / When the user accepts a new version, replace that role's current final output.
- Reviewer 以该文件作为最终版本索引 / Reviewer uses this file as the final-version index.
