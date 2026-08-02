# Code Context 输出规范 / Code Context Output Standard

## One Primary Artifact / 一个主专业产物

Every assignment requires one primary professional artifact. The sections and legacy templates below are content guidance or optional evidence annexes, not a mandatory multi-file packet checklist. Create an annex only when it materially improves traceability or reproducibility.

每次任务只强制一个主专业产物。下列章节和历史模板是内容规范或可选证据附录，不是必须逐文件生成的 packet 清单。

Code Context / Context Engineer 负责把 Architect packet 转成当前项目可执行上下文。

Code Context / Context Engineer turns the Architect packet into implementation-ready context grounded in the current project.

## 核心质量标准 / Core Quality Bar

每份 Code Context 主交付物必须区分三类内容：

Every Code Context primary artifact must separate three layers:

1. 架构意图 / architecture intent
2. 当前项目代码证据 / current project code evidence
3. Context Engineer 判断或待验证假设 / Context Engineer judgment or assumptions

如果把 Architect 的意图直接写成当前代码事实，packet 不合格。

If Architect intent is presented as current code fact, the packet is not acceptable.

## 三类上下文 / Three Context Layers

### 1. 架构意图 / Architecture Intent

用于记录 Architect 要求下游理解的边界、接口、数据流、测试策略和风险。

Use this layer for boundaries, interfaces, data flows, test strategy, and risks that Architect asks downstream roles to understand.

允许来源 / Allowed sources:

- Architect packet manifest and listed documents
- Product / PRD packet when accepted for traceability
- Researcher packet when accepted for traceability
- user input

输出要求 / Output requirements:

- 标注 `architecture_intent` 或 `accepted_upstream_scope` / label as `architecture_intent` or `accepted_upstream_scope`
- 不把架构意图写成当前代码事实 / do not present architecture intent as current code fact
- 需要代码验证的地方必须写入 verification need / record verification needs when code facts are required

### 2. 当前项目代码证据 / Current Project Code Evidence

用于记录当前项目中真实存在的文件、依赖、测试、示例、文档和配置。

Use this layer for files, dependencies, tests, examples, docs, and configuration that actually exist in the current project.

允许来源 / Allowed sources:

- explicitly allowed source files
- explicitly allowed test files
- explicitly allowed examples and docs
- read-only command output approved by scope

输出要求 / Output requirements:

- 标注 `current_code_evidence`、`current_test_evidence`、`current_dependency_evidence` 或 `current_doc_evidence`
- 每个文件 claim 必须有路径 / every file claim must include a path
- 没有读取的文件不得被写成事实 / files not read must not be stated as facts
- 不做代码修改、不写测试、不格式化文件 / do not modify code, write tests, or format files

### 3. Context Engineer 判断或待验证假设 / Context Engineer Judgment Or Assumptions

用于说明基于上游和代码证据得出的影响面、实现约束和下游风险。

Use this layer for impact, implementation constraints, and downstream risk inferred from upstream and code evidence.

输出要求 / Output requirements:

- 标注 `context_engineer_judgment`、`assumption` 或 `unknown`
- 判断必须说明依据 / judgment must state its basis
- 假设必须交给 Implementer 或 Test Evaluator 验证 / assumptions must be handed to Implementer or Test Evaluator for verification
- 不把建议写成授权 / do not present recommendations as authorization

## 来源标签 / Source Labels

关键 claim 必须使用一个来源标签：

Every key claim must use one source label:

- `architecture_intent`: 来自 Architect packet / from Architect packet
- `accepted_upstream_scope`: 来自已接受上游范围 / from accepted upstream scope
- `current_code_evidence`: 来自当前代码文件 / from current code files
- `current_test_evidence`: 来自当前测试文件或测试配置 / from current tests or test config
- `current_dependency_evidence`: 来自依赖、配置或 lock 文件 / from dependency, config, or lock files
- `current_doc_evidence`: 来自当前项目文档 / from current project docs
- `context_engineer_judgment`: Context Engineer 基于证据的判断 / Context Engineer judgment based on evidence
- `assumption`: 需要下游验证的假设 / assumption requiring downstream verification
- `unknown`: 证据不足 / insufficient evidence

禁止无标签关键结论。

Unlabeled key conclusions are forbidden.

## Code Map 标准 / Code Map Standard

`code-map.md` 应该列出：

`code-map.md` should list:

- 文件路径 / file path
- 文件是否已读取 / whether the file was read
- 文件在变更中的角色 / role in change
- 建议访问方式：`read_only`、`writable_candidate`、`do_not_touch` / recommended access mode
- 来源标签 / source label
- 依据 / evidence basis

`writable_candidate` 是实现入口判断，不是永久可写白名单。有效 Implementer 任务书授权为完成交付所合理必需的文件改动，只应列出真正必要的任务特定排除项。

`writable_candidate` is not write authorization. Project Manager must authorize writable modules or directories and task-specific exclusions in the Implementer assignment; an exhaustive per-file list is not required.

## Dependency Map 标准 / Dependency Map Standard

`dependency-map.md` 应该说明：

`dependency-map.md` should state:

- 依赖名称或关系 / dependency name or relation
- 方向：imports、calls、configures、generates、reads、writes / direction
- 当前项目证据 / current project evidence
- 风险 / risk
- 下游验证责任 / downstream verification owner

## Impact Analysis 标准 / Impact Analysis Standard

`impact-analysis.md` 应该区分：

`impact-analysis.md` should separate:

- Architect 预期影响 / Architect expected impact
- 当前代码证据支持的影响 / impact supported by current code evidence
- 未读或未知区域 / unread or unknown areas
- 不应触碰的区域 / areas that should not be touched
- 目标漂移风险 / milestone drift risk

## Test Map 标准 / Test Map Standard

`test-map.md` 应该记录：

`test-map.md` should record:

- 需要验证的行为 / behavior to verify
- 已存在测试或测试配置 / existing tests or test config
- 缺失测试 / missing tests
- 测试 owner role / owner role
- 是否允许 Test Evaluator 执行 / whether Test Evaluator may run it

Code Context 不运行测试。

Code Context does not run tests.

## Implementation Constraints 标准 / Implementation Constraints Standard

`implementation-constraints.md` 应该给 Implementer 一个窄范围上下文，但不得授权实现。

`implementation-constraints.md` should give Implementer narrow implementation context, but must not authorize implementation.

必须区分：

It must distinguish:

- recommended writable candidates / 建议写入候选
- read-only support files / 只读辅助文件
- do-not-touch files / 禁止触碰文件
- required user confirmation / 需要用户确认
- required verification commands / 建议验证命令

## 禁止输出 / Forbidden Output

Code Context 不得：

Code Context must not:

- 修改代码、测试、示例或文档 / modify code, tests, examples, or docs
- 写实现计划作为承诺 / write implementation plans as commitments
- 运行测试 / run tests
- 做产品或架构决策 / make product or architecture decisions
- 把 Architect 意图写成当前代码事实 / present Architect intent as current code fact
- 把 writable candidate 写成永久可写白名单 / present writable candidates as a permanent writable whitelist
- 直接启动 Implementer / start Implementer directly

Code Context 可以建议 Implementer 需要的文件范围，但最终实现启动必须由用户和 Orchestrator 确认。

Code Context may recommend file scope for Implementer. Project Manager authorizes implementation by issuing a complete Implementer assignment; no second startup confirmation is required.
