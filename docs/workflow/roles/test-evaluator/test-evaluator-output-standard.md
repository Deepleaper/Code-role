# Test Evaluator 输出规范 / Test Evaluator Output Standard

## One Primary Artifact / 一个主专业产物

Every assignment requires one primary professional artifact. The sections and legacy templates below are content guidance or optional evidence annexes, not a mandatory multi-file packet checklist. Create an annex only when it materially improves traceability or reproducibility.

每次任务只强制一个主专业产物。下列章节和历史模板是内容规范或可选证据附录，不是必须逐文件生成的 packet 清单。

Test Evaluator 负责先确认评估机制与评估基线，再评估实现是否满足验收标准、架构边界和回归要求。

The Test Evaluator first confirms evaluation mechanism and baseline, then evaluates whether implementation satisfies acceptance criteria, architecture boundaries, and regression requirements.

## 核心质量标准 / Core Quality Bar

在 `full_evaluation` 模式中，每份 Test Evaluator 主交付物必须先消费已冻结的 evaluation SOP，再区分六类证据。在 `baseline_freeze` 模式中，该交付物负责定义和校准 SOP，不得声明 KR 通过。

In `full_evaluation`, every Test Evaluator primary artifact must consume the frozen evaluation SOP and separate six evidence layers. In `baseline_freeze`, the artifact defines and calibrates that SOP and cannot claim the KR passed:

1. 当前 milestone 评估 SOP / active milestone evaluation SOP
2. 用户确认的评估机制与 packet-local 基线 / user-confirmed evaluation mechanism and packet-local baseline
3. 行业内得到验证或通用共识的评估模板、评估数据和指标口径 / industry-validated or common-consensus evaluation templates, evaluation data, and metric conventions
4. Implementer 已报告验证 / implementer-reported verification
5. Test Evaluator 实际评估证据 / evaluator-observed evidence
6. Test Evaluator 质量判断与 SOP 校准 / evaluator quality judgment and SOP calibration

如果把 Implementer 的验证日志直接当成最终质量结论，packet 不合格。

If Implementer verification logs are treated as final quality conclusions, the packet is not acceptable.

如果没有确认当前 `evaluation-sop.md`、评估机制与基线，packet 不得给出无条件通过结论。

If the active `evaluation-sop.md`, evaluation mechanism, and baseline are not confirmed, the packet must not give an unconditional pass.

## 六类评估依据 / Six Evaluation Evidence Layers

### 1. 当前 Milestone Evaluation SOP / Active Milestone Evaluation SOP

用于固定本 milestone 的评估机制，防止评估师每轮临时换口径。

Use this layer to fix the milestone-level evaluation mechanism and prevent the Test Evaluator from changing standards ad hoc in each packet.

必须读取 / Must read:

- `code-role/workflow/evaluation/evaluation-sop.md`

必须记录 / Must record:

- SOP confirmation: `sop_confirmed=0|1`
- required layers / 必需评估层
- not-run policy / 未运行项处理规则
- claim boundary / 允许和禁止的质量结论
- final acceptance rule / 最终验收规则
- whether this packet follows or proposes changes to the SOP / 本 packet 是遵守还是建议修改 SOP

如果 SOP 缺失、草稿、过期或未确认，`quality-gate.md` 不得写成 `pass`。

If the SOP is missing, draft, stale, or unconfirmed, `quality-gate.md` must not be `pass`.

### 2. 用户确认的评估机制与基线 / User-Confirmed Evaluation Mechanism And Baseline

用于记录本轮评估采用什么机制、什么指标、什么数据、什么通过线。

Use this layer to record the mechanism, metrics, data, and pass threshold used for this evaluation.

必须记录 / Must record:

- evaluation objective / 评估目标
- evaluation mechanism / 评估机制
- metric definitions / 指标定义
- baseline data or baseline expectation / 基线数据或基线期望
- benchmark datasets if any / benchmark 数据集，如有
- pass/fail threshold / 通过或失败阈值
- user confirmation status / 用户确认状态

完整任务书已经包含这些决定时，Test Evaluator 直接开始。只有任务书缺少用户专属决定时，才一次性列出全部缺项。

When the complete assignment already contains these decisions, Test Evaluator starts immediately. Ask once for the complete missing decision set only when a user-owned decision is absent.

### 3. 行业共识评估参考 / Industry Or Common-Consensus Evaluation References

用于记录行业内得到验证、常用或有共识的评估模板、评估数据、benchmark、指标口径和工程实践。

Use this layer for industry-validated, common, or consensus evaluation templates, evaluation data, benchmarks, metric conventions, and engineering practices.

允许来源 / Allowed sources:

- user-provided industry references / 用户提供的行业参考
- public-source network research / 公开来源联网研究
- current project documentation that explicitly names an evaluation standard / 当前项目文档中明确命名的评估标准

输出要求 / Output requirements:

- 标注 `industry_evaluation_reference`、`benchmark_dataset_reference` 或 `metric_definition`
- 区分 industry/common-consensus reference 与当前项目已确认 baseline
- 未获准外部研究时，不得声称“已找到行业共识”；只能记录 `unknown` 或请求确认

### 4. Implementer 已报告验证 / Implementer-Reported Verification

用于记录 Implementer packet 中声称执行过的验证、改动和风险。

Use this layer for verification, changes, and risks reported by the Implementer packet.

输出要求 / Output requirements:

- 标注 `implementer_reported_verification` 或 `implementer_reported_change`
- 不能把 reported result 写成 evaluator-observed result
- 如果 Implementer 未运行某项验证，必须保持 `not_run` 或 `unknown`

### 5. Test Evaluator 实际评估证据 / Evaluator-Observed Evidence

用于记录 Test Evaluator 实际读取、运行、检查或观察到的结果。

Use this layer for results actually read, run, inspected, or observed by Test Evaluator.

允许来源 / Allowed sources:

- Implementer packet
- evaluation baseline confirmed by user
- approved industry/common-consensus evaluation references
- Product / PRD acceptance criteria
- Architect test strategy
- Code Context test map
- explicitly allowed code and test files
- user-approved test command output

输出要求 / Output requirements:

- 标注 `evaluator_observed_result`、`acceptance_criteria_evidence`、`regression_evidence` 或 `test_command_output`
- 每个实际运行命令必须记录命令、范围、结果和状态
- 未运行的测试不得标记为 pass
- Test Evaluator 不修改代码或测试

### 6. Test Evaluator 质量判断与 SOP 校准 / Evaluator Quality Judgment And SOP Calibration

用于给出二值质量门结论、回归风险和实质 blocker owner。

Use this layer for the binary quality gate, regression risk, and substantive blocker ownership.

输出要求 / Output requirements:

- 标注 `evaluator_judgment`
- 分开记录 `evaluation_executed=0|1` 和 `kr_observed_pass=0|1`
- 任何必需检查失败、未运行或证据不足，`kr_observed_pass=0`
- 如果评估基线未确认，`full_evaluation` 不得开始，`evaluation_executed=0`
- 如果证据不足，必须说明缺口和下一步
- 必须说明 SOP 是否继续有效、是否需要修订、是否阻断 Reviewer

## 来源标签 / Source Labels

关键 claim 必须使用一个来源标签：

Every key claim must use one source label:

- `implementer_reported_verification`: 来自 Implementer verification-log / from Implementer verification log
- `implementer_reported_change`: 来自 Implementer changed-files 或 summary / from Implementer changed files or summary
- `evaluation_sop`: 当前 milestone evaluation SOP / active milestone evaluation SOP
- `sop_calibration`: Test Evaluator 对 SOP 是否继续有效的校准判断 / Test Evaluator calibration judgment on SOP validity
- `user_approved_eval_mechanism`: 用户确认的评估机制 / user-approved evaluation mechanism
- `evaluation_baseline`: 用户确认的评估基线 / confirmed evaluation baseline
- `industry_evaluation_reference`: 行业验证或通用共识评估模板 / industry-validated or common-consensus evaluation template
- `benchmark_dataset_reference`: benchmark 或评估数据集参考 / benchmark or evaluation dataset reference
- `metric_definition`: 指标定义 / metric definition
- `acceptance_criteria_evidence`: 来自 Product / PRD 验收标准 / from Product / PRD acceptance criteria
- `architecture_test_strategy`: 来自 Architect test strategy / from Architect test strategy
- `code_context_test_map`: 来自 Code Context test map / from Code Context test map
- `evaluator_observed_result`: Test Evaluator 实际观察结果 / evaluator-observed result
- `test_command_output`: 实际测试命令输出 / actual test command output
- `regression_evidence`: 回归覆盖证据 / regression coverage evidence
- `evaluator_judgment`: Test Evaluator 基于证据的判断 / Test Evaluator judgment based on evidence
- `assumption`: 需要 Reviewer 或用户确认的假设 / assumption requiring Reviewer or user confirmation
- `unknown`: 证据不足 / insufficient evidence

禁止无标签关键结论。

Unlabeled key conclusions are forbidden.

## Evaluation Baseline 标准 / Evaluation Baseline Standard

`evaluation-sop.md` 应该记录本 packet 对当前 milestone SOP 的消费状态。

`evaluation-sop.md` should record how this packet consumed the active milestone SOP.

必须记录：

It must record:

- active SOP path / 当前 SOP 路径
- SOP status / SOP 状态
- required layers / 必需评估层
- not-run policy / 未运行项处理规则
- claim boundary / 结论边界
- whether the packet follows, narrows, or proposes changes to the SOP / 是否遵守、收窄或建议修改 SOP

`evaluation-baseline.md` 应该基于 SOP 定义本轮怎么评估，而不是重新发明评估机制。

`evaluation-baseline.md` should define this packet's evaluation baseline based on the SOP, not reinvent the evaluation mechanism.

`evaluation-baseline.md` should define how this round will be evaluated.

必须记录：

It must record:

- evaluation objective / 评估目标
- user-approved evaluation mechanism / 用户确认的评估机制
- industry/common-consensus references considered / 已考虑的行业或通用共识参考
- benchmark or evaluation dataset baseline / benchmark 或评估数据基线
- metric definitions and thresholds / 指标定义与阈值
- project-specific acceptance mapping / 项目验收映射
- network research purpose and source boundary / 联网研究目的与来源边界
- mapping to active SOP required layers / 到当前 SOP 必需评估层的映射
- unresolved baseline questions / 未解决的基线问题

如果用户尚未确认 SOP 或评估机制，`quality-gate.md` 不得写成 `pass`。

If the user has not confirmed the SOP or evaluation mechanism, `quality-gate.md` must not be `pass`.

## Test Plan 标准 / Test Plan Standard

`test-plan.md` 应该把评估基线、验收标准、架构测试策略和 Code Context test map 映射到实际检查。

`test-plan.md` should map evaluation baseline, acceptance criteria, architecture test strategy, and Code Context test map to concrete checks.

必须记录：

It must record:

- acceptance criterion or behavior / 验收项或行为
- evaluation baseline or metric / 评估基线或指标
- source label / 来源标签
- planned command or check / 计划命令或检查
- required or optional / 必需或可选
- run permission status / 执行许可状态

## Test Results 标准 / Test Results Standard

`test-results.md` 应该记录实际运行或检查的结果。

`test-results.md` should record results actually run or inspected.

状态必须是：

Status must be:

- `pass`
- `fail`
- `not_run`
- `blocked`

不得把 `not_run` 写成 `pass`。

Do not convert `not_run` into `pass`.

## Regression Matrix 标准 / Regression Matrix Standard

`regression-matrix.md` 应该说明哪些区域被覆盖、未覆盖和仍有风险。

`regression-matrix.md` should state which areas are covered, uncovered, and still risky.

## Failure Analysis 标准 / Failure Analysis Standard

`failure-analysis.md` 应该分析失败、未运行、阻塞和证据不足。

`failure-analysis.md` should analyze failures, unrun checks, blockers, and evidence gaps.

## Quality Gate 标准 / Quality Gate Standard

`quality-gate.md` 必须给出清晰 gate。

`quality-gate.md` must provide a clear gate.

必须分开记录 / Required separate facts:

- `evaluation_executed: 0 | 1`
- `kr_observed_pass: 0 | 1`

必须记录：

It must record:

- evaluation executed / 评估已完整执行: `0 | 1`
- KR observed pass / KR 结果已观测通过: `0 | 1`
- required checks total / 必需检查总数
- required checks passed / 必需检查通过数
- failed check IDs / 失败检查项
- open P0 / open P1 / open P2
- evidence basis / 证据基础
- evaluation SOP status / 评估 SOP 状态
- evaluation baseline status / 评估基线状态
- failed check owner / 失败检查责任人

只有 `full_evaluation` 中 SOP 已确认、全部必需检查完整执行且证据充分时，`evaluation_executed=1`。只有全部目标 KR 检查通过时，`kr_observed_pass=1`。

In `full_evaluation`, `evaluation_executed=1` is allowed only when the SOP is confirmed and every required check was run with sufficient evidence. `kr_observed_pass=1` is allowed only when every target-KR check passed.

如果 SOP、评估机制或 baseline 未确认，`full_evaluation` 的 `evaluation_executed=0`、`kr_observed_pass=0`，并记录 blocker code。

If the SOP, evaluation mechanism, or baseline is unconfirmed, set both `evaluation_executed=0` and `kr_observed_pass=0` for `full_evaluation` and record the blocker code.

## SOP Calibration 标准 / SOP Calibration Standard

`sop-calibration.md` 必须在评估结束后回答：当前 SOP 是否仍然适合这个 milestone。

`sop-calibration.md` must answer whether the active SOP remains suitable for this milestone after evaluation.

必须记录：

It must record:

- SOP adherence status / SOP 遵守状态: followed / narrowed / changed / blocked
- required layer coverage / 必需层覆盖情况
- not-run items and final gate impact / 未运行项及其门禁影响
- proposed SOP amendments, if any / 如有，建议修订项
- whether Reviewer can audit using this SOP / Reviewer 是否可基于该 SOP 审计

SOP 不得在 packet 内静默变化。候选结果出现后的任何变更都必须获得用户明确批准、创建新版本，并重跑受影响证据。

The SOP must not drift silently. Any change after candidate results requires explicit user approval, a new version, and rerun of affected evidence.

## 禁止输出 / Forbidden Output

Test Evaluator 不得：

Test Evaluator must not:

- 修改代码或测试 / modify code or tests
- 实现修复 / implement fixes
- 未经用户确认直接选定评估机制 / select an evaluation mechanism without user confirmation
- 静默替换或绕过 `evaluation-sop.md` / silently replace or bypass `evaluation-sop.md`
- 未经批准声称行业共识或 benchmark 数据 / claim industry consensus or benchmark data without approved sources
- 把 Implementer 的 reported verification 当作 evaluator-observed result / treat Implementer reported verification as evaluator-observed result
- 把未运行测试写成通过 / present unrun tests as passed
- 对未覆盖范围给 final acceptance / give final acceptance for uncovered scope
- 修改上游 packet / modify upstream packets
- 执行 `git add`、`git commit` 或 `git push` / run `git add`, `git commit`, or `git push`

Test Evaluator 可以建议回流 Implementer，但不能自己修复。

Test Evaluator may recommend returning to Implementer, but must not fix implementation itself.
