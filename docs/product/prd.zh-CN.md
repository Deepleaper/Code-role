# Code-role 产品需求对齐稿 v0.1

## 1. 一句话定义

Code-role 是一个用来控制 Codex 编程交付质量的本地角色配置项目。

它不是让 Codex “更会聊天”，而是让 Codex 在做复杂编程任务时，按固定角色、固定文档、固定交接规则推进，减少需求不清、架构没想清、代码乱改、测试缺失、 review 只看表面的情况。

它的核心目标不是让 Codex 自动化执行代码，而是让每个环节都先形成可讨论的文档。用户和 Codex 对文档讨论确认后，才进入下一个环节。除了 Implementer 在被批准后写代码之外，其他角色都只产出文档。

实际使用时，不是在一个对话里连续扮演所有角色，而是在 Code-role 项目里为每个角色分别配置一个独立角色实例。

## 2. 我们要解决的问题

现在直接让 Codex 做复杂编程任务，常见问题是：

- 需求还没对齐，就开始写代码。
- 产品目标、架构假设、代码范围、测试标准都混在聊天记录里。
- 一轮对话里同时做产品、架构、实现、测试和 review，职责不清。
- Codex 经常根据“看起来合理”的假设动手，而不是根据已经确认的输入。
- 后续 review 很难追溯：为什么这么做、依据是什么、哪些风险被接受了。
- 用户想让 Codex 交付稳定结果，但缺少一套可复制的控制流程。

Code-role 要解决的核心问题是：

> 把 Codex 的编程过程从“聊天驱动”变成“角色 + 文档 + 状态门禁驱动”。

更具体地说，是从“让 Codex 自动往下做”变成“每个专业角色先交付文档，再和用户讨论，确认后再交给下一个专业角色”。

## 3. 产品定位

Code-role 是一个本地角色配置项目和 workflow 模板。

它的推荐使用方式是：

```text
Code-role 项目 = 存放角色配置、workflow 协议、角色输出文档
原有业务项目 = 实际被分析、讨论或修改的代码项目
```

用户在 Code-role 项目里为每个角色建立独立对话。每个角色读取自己的 `ROLE.md` 和上游 packet，只产出自己的文档。业务代码项目只在被明确指定路径后作为目标项目被读取或修改。

默认定位：

- 本地使用。
- 文档驱动。
- 不依赖云服务。
- 不默认进入产品仓库发布包。
- 不替代 GitHub、Jira、Linear 或 IDE。
- 不直接做多 Agent 自动执行。
- 不要求在同一个对话里切换多个角色。

它的价值不是“自动化一切”，而是提高复杂编程交付的确定性。

## 4. 目标用户

第一类用户是个人开发者或技术创始人。

他们经常让 Codex 做较复杂的功能开发、重构、修 bug、补测试，但发现纯聊天方式不稳定，需要一套更可控的流程。

第二类用户是小团队技术负责人。

他们希望 AI 参与工程交付，但又不希望 AI 直接跳过需求、架构、测试和 review。

第三类用户是 AI 工作流设计者。

他们关心如何把 Codex 的工作拆成多个角色，并让每个角色有明确输入、输出和边界。

## 5. 核心设计原则

### 5.1 聊天不是事实源

聊天可以用来沟通，但不能作为最终依据。

真正的事实源应该是文件：

- 产品文档
- 研究文档
- 架构文档
- 代码上下文文档
- 实现记录
- 测试结果
- review 结论
- handoff manifest

### 5.2 角色必须分工

Code-role 不希望一个 Codex 会话同时承担所有职责。

每个角色应该是一个单独配置的角色实例。角色实例之间通过 packet 和 `handoff.manifest.json` 交接，不通过聊天记忆交接。

它把复杂编程任务拆成这些角色：

1. 项目经理 / Workflow Orchestrator
2. Researcher
3. Product / PRD
4. Architect
5. Code Context
6. Implementer
7. Test Evaluator
8. Reviewer

每个角色只做自己的事。

每个角色都必须写清楚自己的提示工程协议：

- 这个角色做什么。
- 这个角色读什么输入。
- 输入来自哪个上游角色的哪个文档 packet。
- 这个角色输出什么文档。
- 输出给下一个角色消费什么。
- 哪些情况必须停下来和用户讨论。
- 是否允许改代码。
- 如果用户沟通内容偏离当前角色产出，如何提醒并纠正。

默认规则是：除 Implementer 外，其他角色都不改代码，只产出文档。

### 5.3 实现不能从聊天直接开始

这是最重要的质量门禁。

Implementer 不能只根据用户一句话就开始改代码。它必须有上游明确输入，例如：

- 已确认的 PRD
- 已确认的架构方案
- 已确认的代码影响范围
- 已确认的验收标准

小修小补可以走轻量链路，但也要有明确边界。

即使是轻量链路，也不能变成“用户一句话，Codex 自动写到底”。轻量链路只是减少中间文档数量，不取消讨论和确认。

### 5.4 每次交付都要能追溯

后续 review 时，必须能回答：

- 这个需求来自哪里？
- 架构依据是什么？
- 实现范围是谁批准的？
- 测试覆盖了什么？
- 哪些风险被接受？
- 当前版本消费了哪个上游 packet？

## 6. 核心对象

### 6.1 Orchestrator / 项目经理

项目经理是流程总控。

它负责判断：

- 当前 milestone 是什么。
- 应该走哪条 chain。
- 当前权威输入 packet 是哪个。
- 下一个角色是谁。
- 是否允许下游角色消费当前 packet。
- 是否需要用户确认。

它不写 PRD、不写架构、不写代码、不写测试、不做 review。

### 6.2 Role / 角色

角色是一次工作中的职责身份。

例如：

- Researcher 只做调研和事实整理。
- Product / PRD 只做需求和验收标准。
- Architect 只做架构方案。
- Code Context 只做代码影响范围分析。
- Implementer 只做被批准范围内的实现。
- Test Evaluator 只做测试计划和测试结果判断。
- Reviewer 只做最终 review 和链路审计。

### 6.3 Packet / 工作包

Packet 是角色输出的版本化文件夹。

例如：

```text
docs/workflow/roles/product-prd/reports/<milestone>/packet-v001/
```

一个 packet 里包含这个角色的输出文档，以及一个 `handoff.manifest.json`。

### 6.4 Handoff Manifest / 交接清单

`handoff.manifest.json` 是下游角色读取上游成果的入口。

它记录：

- 当前 packet 属于哪个角色。
- 当前 milestone 是什么。
- packet 版本是什么。
- packet 状态是什么。
- 包含哪些文档。
- 消费了哪些上游 packet。
- 还有哪些开放问题。
- 是否阻塞。
- 需要哪些用户确认。

下游角色不应该靠猜文件名来找输入，而应该读 manifest。

### 6.5 Chain / 工作链路

不同风险级别的任务，走不同链路。

当前支持：

- `full-chain`：完整链路，适合新功能、复杂重构、权限/运行时/安全相关变更。
- `mini-chain`：中等链路，适合范围清楚但仍需要架构和代码上下文的任务。
- `patch-chain`：轻量链路，适合小 bug、小测试、小范围修复。
- `docs-only-chain`：只改文档的链路。
- `research-only`：只做调研，不进入实现。

## 7. MVP 要做什么

第一版 MVP 的目标不是做自动化平台，而是把本地工作流模板打磨到可用。

MVP 必须包含：

- 完整的 8 个角色说明。
- 独立角色实例的配置说明。
- 每个角色明确的提示工程协议：输入、输出、边界、讨论点、下游交接、偏题纠正。
- 项目经理启动流程。
- chain 选择规则。
- packet schema。
- handoff manifest 规则。
- 每个角色的读写边界。
- 非 Implementer 角色只产出文档的约束。
- Implementer 写代码前必须获得用户确认的约束。
- 每个角色的模板文件。
- 本地 packet 校验工具。
- 本地测试，确保模板结构和协议不漂移。
- 清楚的安装/复制说明。

MVP 的判断标准是：

> 一个用户把 Code-role 放进目标项目后，能按照它控制 Codex 做一次更稳定的编程交付。

## 8. MVP 不做什么

第一版明确不做：

- 不做云端 SaaS。
- 不做 IDE 插件。
- 不做完整多 Agent 自动运行时。
- 不做自动连续执行的代码流水线。
- 不做一个对话内的多角色自动切换。
- 不做任务管理系统。
- 不替代 GitHub PR review。
- 不自动批准状态流转。
- 不让 Codex 绕过用户确认。
- 不允许 Implementer 从聊天直接开工。
- 不接第三方网络 API。

这些以后可以讨论，但不是第一版重点。

## 9. 典型使用流程

### 9.0 配置角色实例

用户新建或拉取 Code-role 项目。

在 Code-role 项目中分别配置这些角色实例：

```text
workflow-orchestrator
researcher
product-prd
architect
code-context
implementer
test-evaluator
reviewer
```

每个角色实例都读取自己的 `ROLE.md`。角色之间不靠同一个对话切换身份，而是显式传递上游 `handoff.manifest.json` 和对应文档。

### 9.1 启动

用户在目标项目中放入 Code-role 模板。

然后对 Codex 说：

```text
项目经理，执行 startup routine，恢复当前状态
```

Orchestrator 读取 workflow state，确认当前状态。

### 9.2 选择链路

用户提出一个任务。

Orchestrator 判断任务类型：

- 如果是新能力，走 `full-chain`。
- 如果产品范围已定，但架构和代码范围还要明确，走 `mini-chain`。
- 如果是小修复，走 `patch-chain`。
- 如果只是文档，走 `docs-only-chain`。
- 如果只是调研，走 `research-only`。

### 9.3 上游角色产出 packet

例如 Product / PRD 角色产出：

- `product-brief.md`
- `prd.md`
- `acceptance-criteria.md`
- `non-goals.md`
- `decision-log.md`
- `handoff.manifest.json`

默认轻量流程里，用户接受该角色产出后，Orchestrator 可以把当前 packet 交给下一角色，即使它仍是 `draft`。只有用户明确要求严格交接、审计、不可变证据或发布级留档时，packet 才需要进入 `ready_for_next_role`。

### 9.4 下游角色消费 packet

Architect 不直接读聊天记录，而是读取 Product / PRD 的 manifest 和文档。

Architect 输出自己的 architecture packet。

后续 Code Context、Implementer、Test Evaluator、Reviewer 依次消费上游 packet。

### 9.5 最终 review

Reviewer 不只看代码 diff。

Reviewer 要检查：

- `milestone-contract.md` 是否是已确认的原始目标锚点。
- 每个角色最终版本是否有 `role_completion_status=1`。
- Test Evaluator 是否遵守 `evaluation-sop.md`。
- packet 链路是否完整。
- Implementer 是否越权。
- 测试是否覆盖验收标准。
- 是否有未解决 P0 风险。
- P1 风险是否被明确接受。

## 10. 当前项目现状

当前 `/Users/wangran/Documents/Code-role` 里已经有比较完整的基础：

- `docs/workflow/` 已存在。
- 8 个角色中的 Orchestrator 和 7 个执行角色目录都已存在。
- 每个执行角色有 `ROLE.md`、`templates/`、`reports/`。
- 已有 packet schema、chain policy、source map、status transition、handoff protocol。
- 已有本地 packet validator。
- 已有一批 pytest 测试文件。

当前明显缺口：

- 项目不是 git 仓库。
- 当前环境没有安装 `pytest`，测试需要先按 `pyproject.toml` 安装依赖后运行。
- validator 现在主要校验单个 packet，还不能完整校验 packet chain。
- 缺少一个完整示例 milestone，展示从需求到 review 的完整交接。

## 11. 第一阶段迭代方向

我建议第一阶段不要继续加新角色，也不要先做复杂自动化。

第一阶段目标应该是：

> 把 Code-role 从“文档集合”变成“可复制、可验证、可演示的本地工作流模板”。

建议按这个顺序做：

1. 初始化 git 仓库并推送到 GitHub。
2. 补一个 `examples/` 或 `docs/examples/`，放完整示例 milestone。
3. 增强 validator，让它能校验 packet chain。
4. 给用户写一份“怎么在目标项目里使用 Code-role”的中文指南。
5. 根据示例 milestone 反向修正角色模板中不清晰的地方。

## 12. 后续可选方向

这些不是第一阶段必做，但后续可以评估：

- 做一个初始化脚本，把 workflow 模板复制到目标项目。
- 做一个 CLI，例如 `code-role init`、`code-role validate`、`code-role new-packet`。
- 自动生成角色启动 prompt。
- 按需生成 strict packet lock。
- 自动检查 chain 是否完整。
- 支持把 workflow 从本地模板升级为团队 repo 标准。

## 13. 我们现在需要确认的问题

为了继续推进，我们需要先确认这几个产品决策：

1. Code-role 第一版是否只做本地模板，不做 CLI？
2. `docs/workflow/` 默认是否继续作为本地协调层，不进入目标项目 git？
3. 我们是否把 8 角色系统作为当前确定版本，不再继续拆新角色？
4. 第一阶段是否优先补示例 milestone、chain validator 和中文使用指南？
5. 中文文档是否作为主文档，英文文档作为参考？

我建议当前先确认以上五点，再进入下一轮修改。
