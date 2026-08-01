# Implementer 输出规范 / Implementer Output Standard

Implementer 是唯一可依据项目经理下发的有效任务书修改目标项目文件的执行角色。

The Implementer is the only execution role that may modify target-project files under a valid Project Manager assignment.

## 核心质量标准 / Core Quality Bar

每个 Implementer packet 必须证明四件事：

Every Implementer packet must prove four points:

1. 实现任务书完整有效 / implementation assignment was complete and valid
2. 写入范围足以完成目标且没有越界 / writable scope was sufficient and respected
3. 每个改动都服务当前 milestone / every change serves the current milestone
4. 验证证据足以支持交给 Test Evaluator / verification evidence is sufficient for Test Evaluator handoff

有效任务书本身即是启动授权，不再要求单独的“开始”确认。任务书必须给出目标、权威输入、允许修改的模块或目录、任务特定禁止项、必需检查和停止条件；不要求项目经理预先枚举实现过程中可能触及的每个文件。

A valid assignment is the start authorization; no separate `start` confirmation is required. It must define the objective, authoritative inputs, writable modules or directories, task-specific exclusions, required checks, and stop condition. Project Manager does not need to predict every file the implementation may touch.

## 三类实现依据 / Three Implementation Evidence Layers

### 1. 已批准实现范围 / Approved Implementation Scope

用于记录项目经理任务书确定的实现目标、可写模块或目录、任务特定禁止项和验证要求。

Use this layer for the implementation objective, writable modules or directories, task-specific exclusions, and verification requirements fixed by the Project Manager assignment.

必须记录 / Must record:

- implementation objective / 实现目标
- writable scope / 可写模块或目录
- forbidden scope / 禁止范围
- dirty-file handling rule / 已有脏文件处理规则
- verification commands / 验证命令
- assignment validity / 任务书有效性

### 2. 当前项目实际改动 / Actual Project Changes

用于记录实际修改的文件、改动类型和理由。

Use this layer for actual changed files, change type, and reason.

输出要求 / Output requirements:

- 每个 changed file 必须在任务书允许的模块或目录内 / every changed file must be inside an assignment-authorized module or directory
- 每个改动必须说明对应的有效任务书检查项或已接受上游约束 / every change must cite a valid-assignment check or accepted upstream constraint
- 不得修改未批准文件 / unapproved files must not be modified
- 不得修改上游 packet / upstream packets must not be modified

### 3. 验证证据与残余风险 / Verification Evidence And Residual Risk

用于记录验证命令、结果、失败、未执行原因和剩余风险。

Use this layer for verification commands, results, failures, skipped checks, and risks mapped to binary required checks.

输出要求 / Output requirements:

- 记录实际运行的每个命令 / record every command actually run
- 如果没有运行某个建议验证，必须说明原因 / if a suggested verification was not run, explain why
- 区分 pass、fail、not_run、blocked / separate pass, fail, not_run, and blocked
- 不能把未运行测试写成通过 / do not mark unrun tests as passed

## 来源标签 / Source Labels

关键 claim 必须使用一个来源标签：

Every key claim must use one source label:

- `valid_assignment`: 项目经理下发的完整有效任务书 / complete valid Project Manager assignment
- `approved_writable_scope`: 任务书允许的模块或目录 / assignment-authorized module or directory
- `code_context_constraint`: 来自 Code Context 的实现约束 / from Code Context implementation constraints
- `accepted_upstream_scope`: 来自已接受上游范围 / from accepted upstream scope
- `actual_file_change`: 实际文件改动 / actual file change
- `verification_evidence`: 实际验证输出 / actual verification output
- `implementer_judgment`: Implementer 基于证据的判断 / Implementer judgment based on evidence
- `assumption`: 需要下游验证的假设 / assumption requiring downstream verification
- `unknown`: 证据不足 / insufficient evidence

禁止无标签关键结论。

Unlabeled key conclusions are forbidden.

## Implementation Summary 标准 / Implementation Summary Standard

`implementation-summary.md` 应该说明：

`implementation-summary.md` should state:

- milestone 对齐 / milestone alignment
- assignment validity / 任务书有效性
- approved objective / 已批准目标
- actual change summary / 实际改动摘要
- what was intentionally not changed / 明确未改什么
- downstream Test Evaluator focus / 下游 Test Evaluator 重点

## Changed Files 标准 / Changed Files Standard

`changed-files.md` 应该列出：

`changed-files.md` should list:

- path / 路径
- approved writable scope status / 是否在已批准可写范围内
- change type / 改动类型
- source label / 来源标签
- reason / 理由
- verification link / 验证关联

## Verification Log 标准 / Verification Log Standard

`verification-log.md` 应该记录：

`verification-log.md` should record:

- command or check / 命令或检查
- source label / 来源标签
- expected result / 预期结果
- actual result / 实际结果
- status: pass、fail、not_run、blocked
- notes / 说明

## Risk Notes 标准 / Risk Notes Standard

`risk-notes.md` 应该记录：

`risk-notes.md` should record:

- 残余实现风险 / residual implementation risk
- 未执行验证风险 / unrun verification risk
- 脏文件或未跟踪文件风险 / dirty or untracked file risk
- 下游测试风险 / downstream test risk
- 是否阻塞 Test Evaluator / whether it blocks Test Evaluator

## 禁止输出 / Forbidden Output

Implementer 不得：

The Implementer must not:

- 从缺少目标、必需检查或写入边界的不完整任务开始实现 / start from an incomplete assignment missing objective, required checks, or write boundary
- 把 Code Context 的 `writable_candidate` 当成已批准写入范围 / treat Code Context `writable_candidate` as approved writable scope
- 修改未批准文件 / modify unapproved files
- 扩展产品范围或架构边界 / expand product scope or architecture boundary
- 修改上游 packet / modify upstream packets
- 未经单独批准运行真实 provider API、访问私有认证资源、下载执行远程内容或外传项目私有数据 / run real provider APIs, access authenticated/private resources, download/execute remote content, or externally transmit project-private data without separate approval
- 执行 `git add`、`git commit` 或 `git push` / run `git add`, `git commit`, or `git push`
- 把未运行的测试写成通过 / present unrun tests as passed

Implementer 可以报告 Git 状态，但项目 Git 发布仍按目标项目自己的正常流程执行。

Implementer may report Git status, but target-project Git publishing follows the target project's normal Git process.
