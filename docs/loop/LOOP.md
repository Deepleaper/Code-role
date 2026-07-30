# Goal Loop Contract / 目标闭环协议

## 1. One Authority / 唯一权威

`code-role/milestone-board.md` is the only active control record.

`code-role/milestone-board.md` 是唯一活跃控制记录。

Chat summaries, role self-reports, old packets, manifests, indexes, and scores cannot update milestone status by themselves.

聊天摘要、角色自报、旧 packet、manifest、索引和分数都不能自行改变里程碑状态。

## 2. Binary Completion / 二值完成

- Every accepted KR is `0` or `1`.
- A KR remains `0` until every frozen pass condition has independent evidence.
- There is no `partial_pass`, `pass_with_residual_risk`, or equivalent milestone status.
- A residual item is either a new accepted KR, an explicit non-goal, or an unresolved `KR=0`.
- Only Project Manager updates KR and milestone status.

- 每个已确认 KR 只能是 `0` 或 `1`。
- 冻结通过条件没有全部获得独立证据前，KR 始终为 `0`。
- 不使用 `partial_pass`、`pass_with_residual_risk` 或同义里程碑状态。
- 残余事项必须成为新 KR、明确非目标，或保持为未解决的 `KR=0`。
- 只有项目经理更新 KR 和 milestone 状态。

## 3. One KR Per Iteration / 每轮一个 KR

Each assignment targets exactly one accepted `KR=0`. The assignment may require regression checks for other KRs, but it cannot quietly add a second delivery target.

每份任务书只针对一个已确认的 `KR=0`。任务可以要求回归其他 KR，但不能暗中增加第二个交付目标。

## 4. Dynamic Routing / 动态路由

Project Manager routes from evidence, not from a fixed role chain:

项目经理依据证据动态路由，而不是执行固定角色链：

1. If user value, product behavior, scope, threshold, or claim boundary is unclear, route to Product Strategy.
2. If the evaluation mechanism or baseline is not frozen, route to Independent Evaluation in `baseline_freeze` mode.
3. If the problem is actionable and candidate evidence is missing, route to Engineering.
4. If Engineering supplies candidate evidence, route to Independent Evaluation in `full_evaluation` mode.
5. If evaluation fails with an actionable engineering defect, return to Engineering.
6. If evaluation exposes ambiguous product meaning, return to Product Strategy.
7. If the task or grader is invalid, keep the KR at `0` and repair the definition before more implementation.

1. 用户价值、产品行为、范围、阈值或 claim boundary 不清晰，进入产品策略。
2. 评估机制或基线未冻结，进入独立评估的 `baseline_freeze` 模式。
3. 问题已经可执行但缺少候选证据，进入工程。
4. 工程提交候选证据后，进入独立评估的 `full_evaluation` 模式。
5. 评估发现可执行工程缺陷，返回工程。
6. 评估发现产品含义不清，返回产品策略。
7. 任务或 grader 无效，KR 保持 `0`，先修复定义再继续实现。

## 5. Valid Assignment Starts Work / 有效任务直接开始

A workstation starts immediately after receiving a complete `PM Assignment`. It must not ask the user to reply `开始`.

工位收到完整的 `PM Assignment` 后直接开始工作，不再要求用户回复“开始”。

This version uses manual transport between separate role conversations. Project Manager prints the copy-ready assignment; the user pastes it into the selected role conversation. The role prints its fixed return; the user pastes that return to Project Manager. No prompt may claim automatic dispatch unless an actual dispatch tool was called successfully.

本版本使用独立角色对话之间的手动传递。项目经理输出可复制任务书，用户把它贴入对应角色对话；角色输出固定回报，用户再贴回项目经理。没有真实成功调用调度工具时，任何提示词都不得声称已经自动派发。

## 6. Fixed Transport, Flexible Attachments / 固定流转，灵活附件

- Project Manager uses only `templates/assignment.md` to assign professional work.
- Each workstation uses only its role-specific return template.
- Detailed professional work lives in attachments under `code-role/work/<milestone>/`.
- Project Manager references accepted professional attachments; it does not rewrite their professional content.

- 项目经理只使用 `templates/assignment.md` 下发专业任务。
- 每个工位只使用自己唯一的回报模板。
- 详细专业工作写入 `code-role/work/<milestone>/` 附件。
- 项目经理引用已接受的专业附件，不重写其中的专业内容。

## 7. Evaluation Before Pass / 通过前独立评估

- Evaluation criteria, datasets, graders, commands, environment, and thresholds are frozen before Engineering optimizes against them.
- Independent Evaluation assesses the complete required milestone SOP, not only the latest diff.
- Targeted capability checks and regression checks are both required.
- Required checks that were not run are `0`.
- Engineering cannot self-pass a KR.
- Prefer deterministic graders. Use model-based graders only where needed, and calibrate them against human judgment or reference cases.

- 工程针对评估优化前，必须冻结评估条件、数据集、grader、命令、环境和阈值。
- 独立评估检查完整的 milestone 必需 SOP，不只检查最新 diff。
- 目标能力检查和回归检查都必须执行。
- 必需检查未运行即为 `0`。
- 工程不能自行把 KR 判为通过。
- 优先使用确定性 grader；只有必要时使用模型 grader，并用人工判断或参考案例校准。

## 8. Iteration Budget And Stop Rule / 迭代预算与停止条件

Default maximum: three failed Engineering-to-Evaluation attempts for the same KR.

默认上限：同一 KR 最多进行三次失败的“工程到独立评估”尝试。

After the limit, Project Manager must stop implementation and choose one action:

达到上限后，项目经理必须停止继续实现并选择：

- revise the product definition;
- repair the evaluation task or grader;
- split the KR;
- request a user scope decision;
- explicitly increase the iteration budget.

## 9. Human Gates / 人工闸门

Human confirmation is required for:

- accepting or changing Objective or KR definitions;
- changing frozen evaluation thresholds or claim boundaries;
- exceeding the iteration or cost budget;
- irreversible external actions such as merge, deploy, publish, delete, charge, or production mutation.

Routine role routing, local code edits, local tests, and ordinary evidence collection do not require an extra workflow confirmation once the assignment is valid. Git follows the target project's normal process; Code-role does not create a second Git approval system.

任务有效后，常规角色路由、本地代码修改、本地测试和普通证据采集不需要额外流程确认。Git 使用目标项目原有流程；Code-role 不再建立第二套 Git 审批系统。

## 10. Research And Data Boundary / 研究与数据边界

Every workstation may use public internet sources relevant to its assignment. It must separate:

- repository evidence;
- external evidence;
- professional judgment;
- unknown.

Private code, credentials, customer data, and unreleased artifacts must not be sent to external services unless the user explicitly authorizes it.
