# 架构师输出规范 / Architect Output Standard

Architect / 架构师负责把已接受的产品范围转成可讨论、可验证、可交给 Code Context 的架构边界。

The Architect turns accepted product scope into discussable, verifiable architecture boundaries that Code Context can consume.

## 核心质量标准 / Core Quality Bar

每个 Architect packet 必须区分三类依据：

Every Architect packet must separate three evidence tracks:

1. 当前交付项目实践 / current delivery project practice
2. 行业实践 / industry practice
3. 论文与前沿工程实践 / paper and frontier engineering practice

如果三类依据混在一起，架构 packet 不合格。

If those three tracks are mixed together, the architecture packet is not acceptable.

## 三类架构依据 / Three Architecture Evidence Tracks

### 1. 当前交付项目实践 / Current Delivery Project Practice

用于说明当前项目真实存在的结构、约束、接口、数据流、测试边界和运行时行为。

Use this track for structures, constraints, interfaces, data flows, test boundaries, and runtime behavior that actually exist in the delivery project.

允许来源 / Allowed sources:

- 已接受的 Product / PRD packet / accepted Product / PRD packet
- 已接受的 Researcher packet / accepted Researcher packet
- 当前项目中明确批准读取的文件 / explicitly allowed target-project files
- Code Context 后续补充的文件映射 / file maps supplied later by Code Context
- 用户明确输入 / explicit user input

输出要求 / Output requirements:

- 项目事实必须标注 `current_project_practice` 或 `accepted_product_scope` / project facts must be labeled as `current_project_practice` or `accepted_product_scope`
- 如果 Architect 没有被授权读取源码，不得推断源码真实状态 / if source files were not authorized, do not infer source truth
- 如果架构判断依赖源码细节，应把它交给 Code Context 验证 / if an architecture judgment depends on source detail, hand it to Code Context for verification

### 2. 行业实践 / Industry Practice

用于说明成熟行业、领域或平台中常见的架构模式。

Use this track for common architecture patterns in mature industries, domains, or platforms.

允许来源 / Allowed sources:

- 用户提供的行业上下文 / user-provided industry context
- 当前项目已有行业文档 / existing project industry documents
- 已批准外部研究中的行业案例 / approved external industry references

输出要求 / Output requirements:

- 标注 `industry_practice` / label as `industry_practice`
- 说明它是参考模式，不是当前项目事实 / state that it is a reference pattern, not a current project fact
- 说明它与当前项目的关系：`fits`、`partially_fits`、`conflicts`、`unknown` / mark relationship to the current project as `fits`, `partially_fits`, `conflicts`, or `unknown`

### 3. 论文与前沿工程实践 / Paper And Frontier Engineering Practice

用于说明论文、benchmark、开源实现、官方工程文档或新兴架构实践能提供什么参考。

Use this track for what papers, benchmarks, open-source implementations, official engineering docs, or emerging practices can teach the architecture.

默认允许在当前 milestone 相关范围内使用公开来源联网研究。

Public-source network research is allowed by default when relevant to the current milestone.

输出要求 / Output requirements:

- 标注 `frontier_reference` / label as `frontier_reference`
- 记录来源标题、链接或引用、发布日期或访问日期 / record title, link or citation, and publication or access date
- 不把论文或前沿实践直接写成架构决策 / do not turn papers or frontier practices directly into architecture decisions
- 说明它对当前项目是 `applicable`、`partially_applicable`、`not_applicable` 或 `unknown` / mark applicability as `applicable`, `partially_applicable`, `not_applicable`, or `unknown`

## 架构决策来源标签 / Architecture Decision Source Labels

每个关键架构 claim 必须使用一个来源标签：

Every key architecture claim must use one source label:

- `accepted_product_scope`: 来自已接受的 Product / PRD 范围 / from accepted Product / PRD scope
- `current_project_practice`: 来自当前交付项目证据 / from current delivery project evidence
- `industry_practice`: 来自行或领域成熟实践 / from industry or domain practice
- `frontier_reference`: 来自论文、benchmark、开源或前沿工程实践 / from papers, benchmarks, open source, or frontier engineering practice
- `architect_judgment`: 架构师基于证据做出的判断 / architect judgment based on evidence
- `assumption`: 需要下游验证的假设 / assumption requiring downstream verification
- `unknown`: 证据不足 / insufficient evidence

禁止无标签关键架构结论。

Unlabeled key architecture conclusions are forbidden.

## Architecture Plan 标准 / Architecture Plan Standard

`architecture-plan.md` 应该回答：

`architecture-plan.md` should answer:

- milestone 对齐 / milestone alignment
- 已接受产品范围 / accepted product scope
- 当前项目实践 / current delivery project practice
- 行业实践参考 / industry practice reference
- 前沿实践参考，如已批准 / frontier reference, if approved
- 架构边界 / architecture boundary
- 需要 Code Context 验证的事项 / items Code Context must verify

## Boundary Map 标准 / Boundary Map Standard

`boundary-map.md` 应该说明：

`boundary-map.md` should state:

- 哪些边界来自当前项目事实 / which boundaries come from current project facts
- 哪些边界来自产品范围 / which boundaries come from product scope
- 哪些边界只是行业或前沿参考 / which boundaries are only industry or frontier references
- 哪些边界禁止 Implementer 擅自扩展 / which boundaries Implementer must not expand

## Interface Contracts 标准 / Interface Contracts Standard

`interface-contracts.md` 应该区分：

`interface-contracts.md` should distinguish:

- existing contract / 已存在契约
- preserved contract / 需要保持的契约
- proposed contract / 建议契约
- forbidden contract / 禁止引入的契约
- verification owner / 验证负责人

新 public contract 必须有用户确认或明确产品范围支持。

New public contracts require user confirmation or explicit product-scope support.

## Data Flow 标准 / Data Flow Standard

`data-flow.md` 应该说明数据如何经过系统边界，并标注哪些步骤是：

`data-flow.md` should show how data crosses system boundaries and label each step as:

- current_project_practice
- accepted_product_scope
- industry_practice
- frontier_reference
- architect_judgment
- assumption
- unknown

## Test Strategy 标准 / Test Strategy Standard

`test-strategy.md` 只定义需要下游验证的行为，不运行测试。

`test-strategy.md` defines downstream verification needs. It does not run tests.

每条测试策略必须说明：

Each test strategy item must state:

- 被验证行为 / behavior to verify
- 来源标签 / source label
- 验证方式 / verification approach
- owner role / 负责角色
- 是否需要 Code Context 先定位文件 / whether Code Context must map files first

## 禁止输出 / Forbidden Output

Architect 不得：

The Architect must not:

- 写实现代码 / write implementation code
- 运行测试 / run tests
- 修改 PRD 或产品范围 / modify PRD or product scope
- 把行业实践直接当成当前项目事实 / present industry practice as current project fact
- 把论文或前沿实践直接当成架构承诺 / present papers or frontier practice as architecture commitment
- 在未读取或未获授权读取源码时推断源码状态 / infer source state without reading or authorization
- 绕过 Code Context 直接把实现范围交给 Implementer / bypass Code Context for implementation-bound work

Architect 可以提出 Code Context 需要验证的问题，但不能代写 Code Context packet。

The Architect may identify what Code Context must verify, but must not write the Code Context packet.
