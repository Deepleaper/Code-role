# Complete Minimal Goal Loop / 四工位完整闭环示例

This worked example shows one small milestone moving through one Project OKR, a Product Contract attached to the same KRs, Engineering-owned execution steps, a runnable candidate, and independent verification.

本示例展示一个小型 milestone 如何围绕同一套项目 OKR，依次完成产品契约、工程执行步骤、可运行候选物和独立验证。

## Scenario / 场景

An existing command-line report tool only emits text. The accepted milestone is to add deterministic JSON output without changing the existing text behavior.

一个现有的命令行报告工具只能输出文本。本轮已确认的 milestone 是增加确定性 JSON 输出，同时不改变原有文本行为。

This is an illustrative, internally consistent artifact set. Its command observations demonstrate the contract; they are not test results from the Code-role repository itself.

这是一组用于说明机制、内部一致的示例交付物。其中命令结果用于展示契约，并不是 Code-role 仓库自身的测试结果。

## Read In This Order / 阅读顺序

1. [`milestone-board.md`](milestone-board.md): the accepted complete KR set and final control state.
2. [`01-pm-product-assignment.md`](01-pm-product-assignment.md): Project Manager assigns the complete milestone to Product Strategy.
3. [`02-product-contract.md`](02-product-contract.md): the complete Product Contract and KR product-coverage contract.
4. [`03-product-return.md`](03-product-return.md): Product Strategy returns the accepted artifact pointer.
5. [`04-pm-engineering-assignment.md`](04-pm-engineering-assignment.md): Project Manager hands the accepted Project OKR and Product Contract to Engineering.
6. [`05-engineering-delivery.md`](05-engineering-delivery.md): Engineering defines STEP stages and records the complete candidate evidence.
7. [`06-engineering-return.md`](06-engineering-return.md): Engineering reports candidate readiness without self-passing KRs.
8. [`07-pm-evaluation-assignment.md`](07-pm-evaluation-assignment.md): evaluation starts only after the candidate gate passes.
9. [`08-independent-evaluation-report.md`](08-independent-evaluation-report.md): a fresh independent run of every KR check.
10. [`09-independent-evaluation-return.md`](09-independent-evaluation-return.md): the evaluator returns binary observed results.
11. [`10-pm-decision.md`](10-pm-decision.md): Project Manager makes the final milestone decision.

## What This Demonstrates / 这个示例证明什么

- Project Manager defines the complete `KR-*` outcome set rather than dispatching one KR at a time.
- Product Strategy completes the Product Contract under the existing `KR-*` IDs without creating another Objective or KR set.
- Engineering alone decomposes work into `STEP-*` stages and can report a candidate but cannot pass KRs.
- Independent Evaluation starts only after the complete candidate gate and evaluates every KR rather than only changed files.
- The Project Manager accepts evidence and owns the final status update.
- Every completion claim can be traced to a check, observation, and evidence path.
