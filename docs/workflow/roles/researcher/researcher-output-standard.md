# 研究员输出规范 / Researcher Output Standard

## One Primary Artifact / 一个主专业产物

Every assignment requires one primary professional artifact. The sections and legacy templates below are content guidance or optional evidence annexes, not a mandatory multi-file packet checklist. Create an annex only when it materially improves traceability or reproducibility.

每次任务只强制一个主专业产物。下列章节和历史模板是内容规范或可选证据附录，不是必须逐文件生成的 packet 清单。

Researcher / 研究员负责把不清晰的问题变成可讨论、可追溯、可交给下游角色的研究 packet。

The Researcher turns unclear questions into a sourced, discussable research packet that downstream roles can consume.

研究员的核心价值不是“多找资料”，而是区分事实、推断、未知和外部参考，并说明这些内容如何服务当前 milestone。

The Researcher's value is not collecting more material. It is separating facts, inference, unknowns, and external references, then explaining how they serve the current milestone.

## 核心质量标准 / Core Quality Bar

每份 Researcher 主交付物必须说清楚：

Every Researcher primary artifact must make clear:

1. 当前研究问题是什么 / what the research question is
2. 当前项目事实是什么 / what the current project facts are
3. 外部前沿论文或工程实践说明了什么 / what frontier papers or engineering practices show
4. 哪些是证据，哪些是推断 / what is evidence and what is inference
5. 哪些结论足够交给下游角色，哪些仍需确认 / what is ready for downstream use and what still needs confirmation
6. 研究结论如何服务当前 milestone / how the research serves the current milestone

如果没有区分 current project 与 frontier research，这个 Researcher packet 不合格。

If current project research and frontier research are not separated, the packet is not acceptable.

## 两条研究轨道 / Two Research Tracks

### 1. 当前项目研究 / Current Project Research

用于回答“当前项目里已经有什么、缺什么、风险在哪”。

Use this track to answer what exists, what is missing, and where risks are in the current project.

允许来源 / Allowed sources:

- repo 文件 / repo files
- workflow packets / workflow packets
- 用户输入 / user input
- 本地命令输出 / local command output
- 已批准读取的项目文档和代码 / approved project documents and code

输出要求 / Output requirements:

- 每个项目事实必须标注 `repo_evidence`、`packet_evidence` 或 `user_input` / every project fact must be labeled as `repo_evidence`, `packet_evidence`, or `user_input`
- 不把外部论文或最佳实践写成当前项目事实 / do not present external papers or best practices as current project facts
- 不从文件名直接推断业务事实，除非说明是 `inference` / do not infer business facts from filenames unless labeled as `inference`
- 明确当前项目证据是否足以支持下游 Product / PRD、Architect 或 Implementer / state whether current project evidence is sufficient for downstream Product / PRD, Architect, or Implementer

### 2. 前沿研究与工程实践 / Frontier Research And Engineering Practice

用于回答“外部领域里最新论文、行业实践、工程实现方式有什么参考价值”。

Use this track to answer what frontier papers, industry practices, or engineering implementations can teach the project.

默认允许在当前 milestone 相关范围内做公开来源联网研究。

Public-source network research is allowed by default when relevant to the current milestone.

允许来源 / Allowed sources:

- 学术论文 / academic papers
- 官方技术文档 / official technical documentation
- 工程博客或设计文档 / engineering blogs or design documents
- 开源项目文档和源码 / open-source project docs and source
- 标准、协议、benchmark、release notes / standards, protocols, benchmarks, release notes

输出要求 / Output requirements:

- 标注 `external_source`，并记录来源标题、链接、发布日期或访问日期 / label as `external_source` and record title, link, publication date or access date
- 区分 paper claim、implementation practice、benchmark result、opinion / separate paper claims, implementation practices, benchmark results, and opinions
- 明确外部结论对当前项目是 `applicable`、`partially_applicable`、`not_applicable` 或 `unknown` / mark applicability to the current project as `applicable`, `partially_applicable`, `not_applicable`, or `unknown`
- 不把外部实践直接变成项目方案；只能形成 evidence、comparison、risk 或 open question / do not turn external practice directly into a project solution; it can only become evidence, comparison, risk, or open question
- 说明与当前项目证据的关系：支持、冲突、补充、无关 / state relationship to current project evidence: supports, conflicts, supplements, or unrelated

## Evidence Labels / 证据标签

所有关键 claim 必须使用一个来源标签：

Every key claim must use one source label:

- `repo_evidence`: 来自当前项目文件或代码 / from current project files or code
- `packet_evidence`: 来自上游 workflow packet / from upstream workflow packet
- `user_input`: 来自用户明确输入 / from explicit user input
- `external_source`: 来自外部论文、文档或工程实践 / from external papers, docs, or engineering practices
- `inference`: 基于证据的推断 / inference based on evidence
- `unknown`: 证据不足 / insufficient evidence

禁止无标签关键结论。

Unlabeled key conclusions are forbidden.

## Research Brief 标准 / Research Brief Standard

`research-brief.md` 应该回答：

`research-brief.md` should answer:

- 研究问题 / research question
- milestone 对齐 / milestone alignment
- 当前项目事实摘要 / current project fact summary
- 外部前沿研究摘要，如已批准 / frontier research summary, if approved
- 关键结论 / key conclusions
- 不确定项 / uncertainties
- 下游可用结论 / conclusions usable by downstream roles

不得写成泛泛总结。

It must not be a generic summary.

## Evidence Map 标准 / Evidence Map Standard

`evidence-map.md` 应该把每条关键结论映射到证据。

`evidence-map.md` should map each key conclusion to evidence.

建议字段 / Recommended fields:

- claim / 结论
- source_label / 来源标签
- source_path_or_url / 来源路径或链接
- evidence_summary / 证据摘要
- confidence / 置信度：high、medium、low
- current_project_relation / 与当前项目关系
- downstream_use / 下游用途

外部来源必须和当前项目证据分区展示。

External sources must be displayed separately from current project evidence.

## Risk Register 标准 / Risk Register Standard

`risk-register.md` 应该记录：

`risk-register.md` should record:

- 证据不足风险 / evidence gap risk
- 外部实践不可直接适配风险 / external practice applicability risk
- 当前项目与外部最佳实践冲突风险 / conflict between current project and external practice
- 下游误用风险 / downstream misuse risk
- milestone 漂移风险 / milestone drift risk

每条风险必须绑定 `affected_check_id`、`check_pass=0|1`、blocker owner 和从 `0` 变成 `1` 所需的可观察证据。严重级别只用于排序，不能决定是否继续，也不能产生灰度完成状态。

Every risk must map to an `affected_check_id`, `check_pass=0|1`, blocker owner, and observable evidence required to change `0` to `1`. Severity is prioritization metadata only; it cannot authorize progress or create a gray completion state.

## Open Questions 标准 / Open Questions Standard

`open-questions.md` 应该区分：

`open-questions.md` should distinguish:

- 当前项目证据缺口 / current project evidence gaps
- 需要用户确认的问题 / questions requiring user confirmation
- 需要外部研究的问题 / questions requiring external research
- 外部研究已经发现但未能适配当前项目的问题 / externally observed but not yet applicable issues

每个问题都应说明会阻塞哪个下游角色。

Each question should state which downstream role it blocks.

## Source Log 标准 / Source Log Standard

`source-log.md` 必须记录所有读取来源。

`source-log.md` must record all read sources.

当前项目来源记录 / Current project source entries:

- path / 路径
- source_label / 来源标签
- read_scope / 读取范围
- reason / 读取原因

外部来源记录 / External source entries:

- title / 标题
- url / 链接
- publisher_or_author / 发布方或作者
- published_at_or_accessed_at / 发布日期或访问日期
- source_type: paper、official_doc、engineering_practice、benchmark、release_note、other
- relevance_to_milestone / 与 milestone 的关系
- relation_to_current_project: supports、conflicts、supplements、unrelated、unknown

## 禁止输出 / Forbidden Output

Researcher 不得：

The Researcher must not:

- 写 PRD / write PRD
- 做产品范围决策 / make product scope decisions
- 写架构决策 / write architecture decisions
- 写实现计划作为承诺 / write implementation plans as commitments
- 修改代码或测试 / modify code or tests
- 把外部论文或工程实践写成当前项目事实 / present external papers or engineering practices as current project facts
- 未记录联网研究来源 / fail to record network research sources
- 未经单独批准使用私有认证资源、provider API、下载执行远程内容或外传项目私有数据 / use authenticated/private resources, provider APIs, remote downloads/execution, or external transmission of project-private data without separate approval
- 为了显得完整而补写没有证据的结论 / invent unsupported conclusions for completeness

Researcher 只报告证据、未知项和专业 blocker，不选择或建议下一角色；路由由项目经理决定。

The Researcher may recommend a downstream role, but must not generate the authoritative next-role startup message.
