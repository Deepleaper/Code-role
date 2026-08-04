# Code-role Launch Kit / 发布素材包

Use these as starting points. Adapt each post to the community and answer technical questions directly. Do not publish the same copy everywhere or ask for empty engagement.

以下内容可直接作为初稿，但应按社区语境调整，并认真回答技术问题。不要在所有平台复制同一段文字，也不要索取无意义互动。

## One-Line Positioning / 一句话定位

**English:** Code-role keeps AI coding focused on one accepted software milestone through explicit ownership, binary evidence, and independent evaluation.

**中文：** Code-role 用明确责任、二值证据和独立评估，让 AI 编程始终围绕一个已确认的软件里程碑交付。

## 30-Second Description / 30 秒介绍

**English**

AI coding agents are good at producing activity, but activity is not delivery. Code-role is a local, open-source role-control system built around one Project OKR. Project Manager and user define one Objective and KR set, Product completes the Product Contract under those same KRs, and Engineering alone decomposes execution steps and builds the candidate. Independent Evaluation starts only after the complete runnable candidate exists. Use the four-workstation Minimal Profile for normal work or the eight-role Full Profile when research, architecture, and audit need separate ownership.

**中文**

AI 编程 Agent 很擅长“做很多事”，但活动量不等于交付。Code-role 是一套围绕单一项目 OKR 的本地开源角色控制机制：项目经理与用户定义一个 Objective 和一组 KR，产品只在同一组 KR 下补全 Product Contract，只有工程可以拆分执行 STEP 并交付可运行候选物。完整候选物产生后才进入独立评估。普通任务使用四工位最小版；研究、架构和审计需要独立负责时，使用八角色完整版。

## Current Release Post / 当前发布文案

**English**

Code-role gives AI coding a global OKR contract without turning the Project Manager into an engineering task scheduler.

- Project Manager defines the complete `KR-*` milestone outcome set.
- Product completes the Product Contract under the same `KR-*` IDs and creates no second OKR.
- Engineering alone decomposes `STEP-*` implementation stages and produces the runnable candidate.
- Independent Evaluation cannot start before candidate readiness and evaluates the complete Project OKR.
- A complete assignment starts the role immediately; no startup acknowledgement or readiness-only turn.
- Every role owes one primary professional artifact; packet metadata is optional.

The result is a smaller loop with clear authority: global goals stay global, execution detail stays with Engineering, and no implementation approves itself.

Repository: https://github.com/Deepleaper/Code-role

**中文**

Code-role 用全局 OKR 契约控制 AI 编程，同时不把项目经理变成工程任务调度器：

- 项目经理定义完整 `KR-*` 里程碑结果；
- 产品在同一组 `KR-*` 下补全 Product Contract，不创建第二套 OKR；
- 只有工程可以拆分 `STEP-*` 实现阶段并产出可运行候选物；
- 候选物门禁通过后才能独立评估，且评估必须覆盖完整 KR；
- 完整任务书直接启动角色，不再等待启动确认或 readiness 回合；
- 每个角色只强制交付一份主专业产物，packet 元数据降为可选；

结果是一套权责更清楚的闭环：全局目标保持全局，执行细节归工程，任何实现都不能自我验收。

项目地址：https://github.com/Deepleaper/Code-role

## Show HN

**Title**

`Show HN: Code-role – milestone control for Codex with independent evaluation`

**Body**

I built Code-role after repeatedly seeing coding agents produce plausible documents and large diffs while the actual milestone remained unproven.

The core idea is intentionally small:

- one Project Manager owns the complete milestone Objective and binary KRs;
- Product completes one Product Contract under the same Project KRs;
- Engineering alone decomposes STEP stages and produces candidate evidence but cannot approve itself;
- an independent evaluator starts after candidate readiness and runs the complete KR checks;
- only the Project Manager updates milestone state.

There are two profiles: a four-workstation goal loop for normal delivery and an eight-role packet workflow for higher-risk work. It is local-first, bilingual, MIT licensed, and it does not try to auto-run an entire project.

Repository: https://github.com/Deepleaper/Code-role

The part I most want challenged is the boundary between useful control and process overhead. A complete worked example is in the repo.

## Product Hunt

**Tagline**

`Keep AI coding aligned to one software milestone`

**Short description**

Code-role is an open-source local workflow for controlling Codex-assisted delivery with PM-owned objectives, binary evidence, and independent evaluation. Choose a four-workstation minimal loop or an eight-role auditable workflow.

**First comment**

I built Code-role because my coding-agent workflows kept confusing motion with completion. The difficult part was not generating code; it was keeping every role aligned to the same milestone and preventing implementation from approving itself.

Code-role now has two operating profiles. The Minimal Profile is the default: Project Manager, Product Strategy, Engineering, and Independent Evaluation. The Full Profile separates eight professional roles when the milestone genuinely needs deeper research or audit.

This is not an autonomous coding runner. It is a local control layer for human-discussed, evidence-driven delivery. I would especially value feedback from people running multi-agent or multi-conversation coding workflows.

The workflow came from two private projects. In DeepBrain, Independent Evaluation kept a strong `73/100` partial result from becoming an unsupported production claim. In Leaper Agent, a historical pre-code evaluation route exposed missing task data, holdout isolation, grader mechanics, and runtime conditions. That case helped establish the current Product -> Engineering -> post-candidate Evaluation order.

## X / Twitter

**English**

AI coding agents often confuse activity with delivery.

I open-sourced Code-role: a local milestone-control workflow for Codex with:

- one PM-and-user-owned Project Objective and KR set
- one Product Contract attached to the same KRs
- Engineering-owned STEP stages
- post-candidate evaluation
- independent evaluation
- 4-role minimal and 8-role full profiles

https://github.com/Deepleaper/Code-role

**中文**

AI 编程最常见的问题，不是不会写代码，而是把“做了很多”当成“里程碑完成”。

我开源了 Code-role：

- 项目经理与用户负责唯一的项目 Objective 和 KR
- 产品在同一组 KR 下补全 Product Contract
- 工程负责分阶段执行 STEP
- 完整候选物后再独立评估
- 实现不能自我验收
- 四工位最小版 + 八角色完整版

https://github.com/Deepleaper/Code-role

## LinkedIn / 公众号技术文章开头

**Title / 标题**

`Why AI coding needs milestone control, not more autonomous roles`

`AI 编程真正缺的不是更多角色，而是里程碑控制`

**Opening / 开头**

The failure mode I kept seeing was subtle: every AI role could produce a professional-looking answer, yet the project goal drifted between handoffs. The solution was not another agent. It was a stable control loop that made ownership, required evidence, and acceptance authority explicit.

我反复遇到一种很隐蔽的失败：每个 AI 角色都能写出看起来专业的内容，但项目目标却在一次次交接中漂移。解决办法不是再增加一个 Agent，而是建立稳定的控制闭环，把责任、完成证据和验收权写清楚。

Continue with one real before/after milestone and link directly to the worked example.

Ready-to-publish source article:

- [Two real projects taught me that AI coding needs milestone control](TWO-CASE-LAUNCH-STORY.md)

## Reddit Or Forum Post

**Title**

`I built a local role-control workflow to stop coding agents from self-declaring completion`

**Body**

I am looking for technical feedback on a workflow problem: when several coding-agent roles collaborate, each handoff can look locally correct while the original milestone drifts.

Code-role uses a PM-owned Objective, binary KRs, fixed assignment/return contracts, and independent evaluation. The default profile has only four workstations; an eight-role profile is available for higher-risk work.

I included a complete example from `KR=0` to independent `KR=1`. I would like critique on where this adds useful control and where it still creates avoidable process.

Repository: https://github.com/Deepleaper/Code-role

Before posting, verify that the community allows project links and self-promotion.

## Direct Outreach To Design Partners / 定向邀请

你好，我在测试一套开源的 AI 编程里程碑控制机制 Code-role。它不自动执行整个项目，而是用项目经理、固定任务书、二值 KR 和独立评估，避免 Agent 提前宣布完成。

我想邀请你拿一个范围明确、1-3 天能完成的软件任务试一次四工位最小版。我不需要泛泛评价，只想知道三件事：

1. 哪个字段真正减少了角色猜测；
2. 哪一步仍然造成了流程负担；
3. 独立评估是否阻止了一次错误完成判断。

项目地址：https://github.com/Deepleaper/Code-role

## Maintainer Launch Checklist / 维护者发布检查

- [ ] README social image and 60-second start render correctly.
- [ ] The worked example is internally consistent.
- [ ] Tests pass on the release commit.
- [ ] GitHub description and topics match the current two-profile product.
- [ ] Discussions are enabled and Issue forms work.
- [ ] The current release contains honest, scoped release notes.
- [ ] One real user has completed initialization before broad launch.
- [ ] Every channel post links to evidence, not only the repository homepage.
- [ ] Maintainer availability is reserved for launch-day replies.
- [ ] No purchased stars, reciprocal-star requests, or automated engagement.
