# Complete Minimal Goal Loop / 四工位完整闭环示例

This worked example shows one small milestone moving from `KR=0` to independently verified `KR=1`.

本示例展示一个小型 milestone 如何从 `KR=0` 走到经过独立评估的 `KR=1`。

## Scenario / 场景

An existing command-line report tool only emits text. The accepted milestone is to add deterministic JSON output without changing the existing text behavior.

一个现有的命令行报告工具只能输出文本。本轮已确认的 milestone 是增加确定性 JSON 输出，同时不改变原有文本行为。

This is an illustrative, internally consistent packet set. Its command observations demonstrate the contract; they are not test results from the Code-role repository itself.

这是一组用于说明机制、内部一致的示例文档。其中命令结果用于展示契约，并不是 Code-role 仓库自身的测试结果。

## Read In This Order / 阅读顺序

1. [`milestone-board.md`](milestone-board.md): the accepted Objective, binary KR, and final control state.
2. [`01-pm-engineering-assignment.md`](01-pm-engineering-assignment.md): the exact missing evidence assigned to Engineering.
3. [`02-engineering-return.md`](02-engineering-return.md): candidate implementation evidence, not self-acceptance.
4. [`03-pm-evaluation-assignment.md`](03-pm-evaluation-assignment.md): the frozen full-evaluation task issued by Project Manager.
5. [`04-independent-evaluation-return.md`](04-independent-evaluation-return.md): a fresh, independent run of every frozen check.
6. [`05-pm-decision.md`](05-pm-decision.md): the only document that changes the KR from `0` to `1`.

## What This Demonstrates / 这个示例证明什么

- The assignment targets one accepted `KR=0`.
- Engineering can report a candidate but cannot close the milestone.
- Independent Evaluation runs the complete frozen scope rather than checking only changed files.
- The Project Manager accepts evidence and owns the final status update.
- Every completion claim can be traced to a check, observation, and evidence path.
