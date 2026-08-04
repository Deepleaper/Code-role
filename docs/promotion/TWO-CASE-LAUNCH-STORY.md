# Two Real Projects Taught Me That AI Coding Needs Milestone Control

# 两个真实项目告诉我：AI 编程最缺的不是更多 Agent，而是里程碑控制

## 中文版

我最初以为，AI 编程项目的问题是角色不够专业。

于是我们配置了研究员、产品经理、架构师、上下文工程师、实现工程师、评估师和审计角色。每个角色都能写出专业文档，但项目仍然会出现一个更隐蔽的问题：

**每个环节看起来都完成了，最开始的里程碑却没有完成。**

Code-role 不是从一张理想化流程图里设计出来的。它是在 DeepBrain 和 Leaper Agent 两个真实项目里，被一次次错误完成判断逼出来的。

### 案例一：DeepBrain 的数据很好看，但里程碑仍然是 0

DeepBrain 是一个 AI Agent 记忆运行时项目。

在一次业务记忆产品化评估中，我们已经拿到了大量正面证据：

- 1,750 项单元测试通过；
- 142 项前端与运行时测试通过；
- S50 为 50/50；
- Smoke20 为 20/20；
- LongMemEval-S 为 499/500；
- 100 个业务案例都有记忆决策记录；
- 100/100 的答案片段都能关联到选中的来源证据。

如果只看这些数字，很容易写出一句：“DeepBrain 的记忆能力已经完成产品化。”

独立评估没有这么做。

它把产品目标拆成九类验收要求，最终只确认前四项通过。公平 Hermes 对比、无冲突裁决、可修复失败诊断、原始基准独立复跑和干净环境复现仍然没有闭合。生产成本、SLO、runtime learning、真实 L2 capture 和 storage mutation 也没有证据。

所以即使综合评分达到 73/100，最终决定仍然是：

- milestone complete = 0；
- Reviewer allowed = 0；
- production ready = 0；
- benchmark ready = 0。

Code-role 在这个案例里的价值，不是让结果更好看，而是阻止团队把局部高分包装成完整产品结论。

### 案例二：Leaper Agent 的评估文档很专业，但根本不能执行

Leaper Agent 的目标更直接：在完全相同的模型、provider、工具、预算、环境和评分条件下，证明企业任务效果和重复稳定性优于 Hermes。

项目经理先确认了五个互不补偿的硬 KR：业务结果、可靠性与效率、企业治理、审计修复闭环、独立复现。

评估工位提交的第一版基线看起来非常专业：有任务规则、holdout、grader、same-condition、manifest 和统计方法。

但项目经理没有检查“写得专业不专业”，而是检查“下一个工位能不能不猜就执行”。

结果发现：

- 引用的冻结任务文件不存在；
- 任务和 reserve 里还有占位数据；
- holdout 正文能被实现工位看到；
- grader 只是角色代号；
- model/provider/backend 仍是占位符；
- hash 没有对应独立的权威 artifact。

项目经理直接打回，KR 保持 0，评估 SOP 保持 0，工程工位不得启动。

修正版随后真正产出了 60 个主任务、24 个 reserve、物理隔离的 20% holdout、Engineering 公开包、grader calibration、具体运行条件、198 个完整性索引文件和泄露扫描。

但即使评估工位自报 `evaluation_sop_frozen=1`，项目经理没有验收前，作战板仍保持 0。

这个边界很重要：专业角色可以给出专业结论，但不能修改项目控制状态。

### 两个项目暴露的是同一个问题

DeepBrain 的问题发生在工程和证据已经很多之后：**不能把局部证据扩大成里程碑完成。**

Leaper Agent 的问题发生在工程开始之前：**不能把一份专业方案当成可执行输入。**

这两个问题最终让 Code-role 收敛成四个最小工位：

1. 项目经理：定义 Objective 和二值 KR，对最终结果负责。
2. 产品策略：把价值、行为、范围和阈值定义清楚。
3. 工程：研究、设计、实现、测试并提交候选证据。
4. 独立评估：冻结评估机制，并独立运行完整验收。

每次只处理一个 `KR=0`。工程不能自我验收。没有完整独立证据，状态就是 0。

这听起来比“让多个 Agent 自动协作”慢一点，但它换来的是更重要的东西：**你知道项目到底完成了没有。**

### v0.4.0：把控制做硬，把流程做轻

真实使用也暴露了另一类问题：如果每个角色都要先确认启动、转换 readiness、维护 packet lock、解释路由状态，角色就会把精力花在流程上，而不是修复让 KR 保持为 0 的真实证据缺口。

因此 v0.4.0 保留二值 KR、独立评估和项目经理最终责任，同时删除默认流程中的启动确认、readiness-only 回合和强制 packet 元数据。现在每份任务只指向一个明确的失败证据，每个角色只强制交付一份主专业产物。流程更短，但完成标准没有放松。

Code-role: https://github.com/Deepleaper/Code-role

完整案例：

- https://github.com/Deepleaper/Code-role/blob/main/docs/case-studies/deepbrain.md
- https://github.com/Deepleaper/Code-role/blob/main/docs/case-studies/leaper-agent.md

## English Version

I originally thought AI coding projects failed because the roles were not specialized enough.

We added research, product, architecture, context, implementation, evaluation, and review roles. Every role could produce professional-looking work, yet the original milestone still drifted between handoffs.

Code-role emerged from two private projects.

In DeepBrain, the evidence looked excellent: 1,750 unit tests, 142 frontend/runtime tests, S50 at 50/50, LongMemEval-S at 499/500, and 100/100 grounded business source joins. Independent Evaluation still held the milestone at `0` because the fair comparator, representative raw benchmark reruns, repair proof, clean reproducibility, and production cost/SLO evidence were incomplete.

In Leaper Agent, a historical pre-code evaluation baseline looked rigorous but referenced missing task artifacts, exposed holdout content, used placeholder runtime conditions, and did not commit an executable grader mechanism. The Project Manager rejected it. The correction replaced declarations with 60 primary tasks, 24 reserve tasks, a physically separated holdout, a visible-only Engineering extract, concrete runtime conditions, calibration artifacts, and an integrity index. That run also revealed that evaluation ownership had been placed too early; the current model keeps these acceptance requirements in Product, then routes Engineering, then post-candidate Evaluation.

The two projects exposed the same control problem at different times:

- DeepBrain: strong partial evidence must not become a complete product claim.
- Leaper Agent: a professional plan must not become executable work until its inputs are real.

That is why the minimal Code-role profile has four workstations: Project Manager, Product Strategy, Engineering, and Independent Evaluation. Project Manager and user define one Project Objective and KR set, Product Strategy completes the Product Contract under those same KRs, Engineering alone decomposes STEP stages and builds the candidate, and Independent Evaluation runs only after candidate readiness. Engineering cannot approve itself. Missing independent evidence remains `0`.

It is less theatrical than autonomous multi-agent orchestration, but it answers the question that matters: **is the software milestone actually complete?**

### v0.4.0: harder control, lighter process

Real use exposed a second failure mode: when every role must acknowledge startup, convert readiness, maintain packet locks, and narrate routing state, the workflow itself displaces the failed evidence keeping the KR at `0`.

The current workflow keeps binary KRs, independent evaluation, and Project Manager accountability while removing startup acknowledgements, readiness-only turns, and mandatory packet metadata from the default path. Global KR contracts remain complete; only Engineering decomposes execution into STEP stages. Each role owes one primary professional artifact, so the loop stays short without weakening completion.

Code-role: https://github.com/Deepleaper/Code-role
