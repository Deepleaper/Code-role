# OKR Delivery Loop / OKR 交付闭环

This profile follows [Dialogue Control Contract](../dialogue-control.md) and [One Project OKR Standard](../okr-standard.md). If an older prompt, chat instruction, packet, or memory conflicts, the current local contracts win.

本配置遵守[对话控制契约](../dialogue-control.md)和[单一项目 OKR 规范](../okr-standard.md)。旧提示词、旧对话、packet 或记忆与其冲突时，以当前本地规范为准。

## 1. One Authority / 唯一权威

`code-role/milestone-board.md` is the only active control record. It contains the complete Project OKR, current delivery stage, accepted global artifact paths, candidate status, and independent evidence.

Chat summaries, role self-reports, old packets, manifests, indexes, STEP status, scores, and process history cannot update KR or milestone status by themselves.

## 2. One Project OKR / 一套项目 OKR

1. **Project OKR (`KR`)**: Project Manager and user define the complete delivered result once.
2. **Product Contract**: Product Strategy completes product behavior and acceptance detail under those same KR IDs.
3. **Engineering Execution Steps (`STEP`)**: Engineering decomposes the accepted product contract into implementation phases mapped to the existing KRs.

Project Manager and Product Strategy are global roles. They do not work one KR at a time. Engineering is the only role allowed to split execution into staged STEP items.

KRs require independent outcome evidence. A STEP is internal candidate evidence and cannot pass the milestone.

## 3. Mandatory Delivery Stages / 强制交付阶段

For software delivery, the order is fixed:

```text
milestone_definition
    -> product_definition
    -> engineering_delivery
    -> independent_evaluation
    -> closure
```

Stage gates:

| Stage | Owner | Required result | Next-stage gate |
| --- | --- | --- | --- |
| `milestone_definition` | Project Manager + user | Complete Objective and `KR-1...KR-N` | `project_okr_accepted=1` |
| `product_definition` | Product Strategy | Complete Product Contract for every existing KR | `product_contract_accepted=1` |
| `engineering_delivery` | Engineering | STEP decomposition, implementation, integration, self-verification | `candidate_ready_for_independent_evaluation=1` |
| `independent_evaluation` | Independent Evaluation | Full KR evaluation with evaluator-owned evidence | `evaluation_executed=1` |
| `closure` | Project Manager | Accept all independent results or return the failed contract owner | every KR is `1` |

Independent Evaluation must not start before a complete runnable candidate exists. Reviewer is not part of the Minimal Profile.

## 4. Complete Project OKR / 完整项目 OKR

Project Manager defines one Objective and two to five KRs with the user. Every KR must name:

- observable outcome, subject, and scenario;
- exact binary threshold and measurement conditions;
- independent evidence;
- claim boundary.

Research, PRD, architecture, code activity, tests written, evaluation SOPs, reports, and reviews are methods or evidence, not KRs.

Project Manager hands the complete accepted Project OKR to Product Strategy once. It does not issue separate Product assignments for individual KRs.

## 5. Complete Product Contract / 完整产品契约

Product Strategy consumes all accepted KRs and produces one complete Product Contract:

- one product-definition section for every existing `KR-1...KR-N`;
- user flows and state transitions;
- input, output, error, timeout, permission, and recovery behavior;
- binary product acceptance;
- KR product-coverage with no uncovered KR;
- scope, non-goals, and claim boundaries;
- exact fields Engineering and Independent Evaluation must consume.

Product Strategy does not split work by one KR, select implementation stages, or send work to Evaluation. After the complete product contract is accepted, Project Manager routes Engineering.

## 6. Engineering Execution Loop / 工程执行闭环

Engineering receives the accepted Project OKR and Product Contract, inspects the actual repository, and creates `STEP-1...STEP-N` according to technical dependencies and delivery phases.

Engineering owns the full candidate:

- repository research and root-cause analysis;
- architecture and context mapping when needed;
- STEP sequencing and dependency management;
- code, configuration, migration, fixtures, and tests;
- integration and relevant regression verification;
- reproducible candidate evidence.

Engineering may update STEP structure when code facts require it, but may not change the Project Objective, any KR, or Product Contract meaning. Analysis, plans, architecture, documents, partial STEP completion, or self-tests alone cannot make the candidate ready.

`candidate_ready_for_independent_evaluation=1` only when every required STEP is `1`, the integrated product is runnable, required regressions pass, and Independent Evaluation can reproduce it from named artifacts and commands.

## 7. Independent Evaluation / 独立评估

Independent Evaluation receives the complete runnable candidate only after Engineering readiness equals `1`.

Before inspecting candidate results, the evaluator records the executable SOP derived from the accepted Project KRs and Product Contract: datasets, graders, commands, environment, thresholds, positive and negative cases, regressions, budgets, and claim boundaries. It then runs the complete evaluation.

The evaluator reports:

- `evaluation_executed: 0|1`;
- each `KR-1...KR-N: 0|1`;
- `product_contract_pass: 0|1`;
- `milestone_observed_pass: 0|1`.

It does not evaluate one STEP, one diff, or Engineering's self-report. Any required missing or unrun check is `0`.

There is no `partial_pass` or qualitative completion state. Each required result is `0` or `1`.

## 8. Project Manager Decision / 项目经理决策

After each global stage, Project Manager reads the primary artifact and evidence, then either accepts the stage or returns the owning role.

- Product defect or ambiguity: return the complete Product Contract to Product Strategy, then rerun affected Engineering work.
- Engineering defect: return the complete candidate assignment to Engineering, which revises affected STEP items.
- Invalid evaluation execution: return Independent Evaluation without changing product thresholds.
- Objective, KR, Product Contract scope, threshold, claim, budget, or irreversible action: user decision.

Project Manager does not micromanage STEP items. It updates KRs only from complete independent evidence.

## 9. One Professional Artifact Per Stage / 每阶段一个主专业产物

Each professional stage has one required primary artifact under `code-role/work/<milestone>/`:

- Product Strategy: complete Product Contract organized by the existing KRs;
- Engineering: STEP plan, implementation record, integrated candidate, and reproducibility evidence;
- Independent Evaluation: complete evaluation report and evidence pointers.

Optional annexes exist only when needed for reproduction. Return formatting, packet status, readiness conversion, and locks are not completion gates.

## 10. Iteration Budget / 迭代预算

Default maximum: three failed Engineering-to-Evaluation attempts for one complete candidate contract.

After the limit, Project Manager stops implementation and asks the user to choose one: revise the global product contract, change milestone scope or budget, repair the evaluation method, or terminate the milestone.

## 11. Human Gates / 人工闸门

Human confirmation is required for Objective, KR definition, threshold or claim changes, accepted budget expansion, private-data external transfer, and irreversible external actions.

Routine Product-to-Engineering routing, Engineering STEP decomposition, local implementation, tests, public research, artifact writing, and post-candidate Evaluation do not require another workflow confirmation.
