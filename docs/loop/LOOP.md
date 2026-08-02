# OKR Delivery Loop / OKR 交付闭环

This profile follows [Dialogue Control Contract](../dialogue-control.md). If an older prompt, chat instruction, packet, or memory conflicts with that contract, the current local contract wins.

本配置遵守[对话控制契约](../dialogue-control.md)。旧提示词、旧对话指令、packet 或记忆与其冲突时，以当前本地契约为准。

## 1. One Authority / 唯一权威

`code-role/milestone-board.md` is the only active control record. It contains the current Objective, binary KRs, current failed evidence, current owner, and accepted evidence paths.

Chat summaries, role self-reports, old packets, manifests, indexes, scores, and process history cannot update milestone status by themselves.

## 2. Outcome KR Only / KR 只写结果

A delivery KR must be observable at a user, business, product, or runtime boundary.

Research, PRD, architecture, evaluation SOP, code written, tests written, reports, packets, and reviews cannot be KRs unless the accepted Objective explicitly makes that artifact the delivered product.

There is no `partial_pass`, `pass_with_residual_risk`, progress percentage, or “closer to completion”. A KR is `0` or `1`.

## 3. One Primary KR Per Iteration / 每轮一个主要 KR

Project Manager selects one decisive failed or missing evidence item keeping exactly one primary accepted KR at `0`.

Each assignment must remove that evidence blocker. It may include coherent supporting checks and regressions, but it cannot create a second product outcome or a parallel process objective.

## 4. Dynamic Workstations / 动态工位

Project Manager chooses the owner of the current failed evidence:

1. Product behavior, user value, scope, threshold, or claim ambiguity: Product Strategy.
2. Missing runnable product or technical defect: Engineering.
3. Missing evaluation contract before optimization: Independent Evaluation in `baseline_freeze`.
4. Runnable candidate awaiting independent evidence: Independent Evaluation in `full_evaluation`.
5. Failed evaluation caused by implementation: Engineering.
6. Failed evaluation caused by ambiguous product meaning: Product Strategy.
7. Invalid dataset, grader, environment, or SOP: Independent Evaluation.
8. Objective, KR, threshold, claim, budget, or irreversible action: user decision.

There is no fixed role chain. Research, architecture, context mapping, design, implementation, and testing are methods used inside the owning workstation unless the Full Profile is explicitly active.

## 5. Valid Assignment Starts Work / 有效任务直接开始

A complete assignment contains the accepted Objective, exact target KR, current failed evidence, one role deliverable, binary acceptance checks, authoritative inputs, and one artifact path.

The workstation starts immediately. It does not ask for `开始`, restate boundaries, or narrate progress. It returns only a consolidated user-owned blocker or the final short return.

This profile uses manual transport between separate conversations. Project Manager prints one copy-ready assignment; the user pastes it into the selected workstation. The workstation rereads `role_prompt_path`, performs the work, and returns one short result. Do not claim automatic dispatch.

## 6. One Professional Artifact / 一个主专业产物

Each work unit has one required primary professional artifact under `code-role/work/<milestone>/`.

Optional evidence files are allowed only when required to reproduce the result. They are referenced from the primary artifact. Project Manager reads the artifact directly and does not require format-only repair.

## 7. Engineering Candidate / 工程候选结果

Engineering owns the runnable candidate for the target KR:

- inspect current behavior and root cause;
- make necessary design, code, configuration, test, example, or documentation changes;
- run target checks and relevant regressions;
- record reproducible candidate evidence.

Analysis, plans, documents, or implementation claims alone cannot pass a development work unit. Candidate readiness is `1` only when every assigned engineering check passes and the result is ready for independent rerun.

## 8. Evaluation Before Pass / 通过前独立评估

Evaluation design is not a KR. It is the mechanism used to decide the KR.

- Freeze evaluation inputs and thresholds before Engineering optimizes against them.
- Independent Evaluation assesses the complete target KR, not only the latest diff.
- Target capability and regression checks are both required.
- Required unrun checks are `0`.
- Engineering cannot self-pass a KR.
- Prefer deterministic graders; calibrate model graders where deterministic judgment is insufficient.

## 9. Project Manager Decision / 项目经理决策

After each return, Project Manager:

1. reads the primary artifact and evidence;
2. accepts or rejects the role deliverable;
3. keeps the KR at `0` unless complete independent evidence supports `1`;
4. records the exact remaining failed evidence;
5. routes that evidence blocker to its owner;
6. updates the compact current-state board without appending workflow history.

## 10. Iteration Budget And Stop Rule / 迭代预算与停止条件

Default maximum: three failed Engineering-to-Evaluation attempts for the same KR.

默认上限：同一 KR 最多进行 three failed Engineering-to-Evaluation attempts。

After the limit, Project Manager stops implementation and requests one decision: revise the product definition, repair the evaluation mechanism, split the KR, change scope, or increase the accepted budget.

## 11. Human Gates / 人工闸门

Human confirmation is required for Objective/KR/threshold/dataset/grader/claim changes, budget expansion, private-data external transfer, and irreversible external actions.

Routine role routing, local work, public research, local tests, artifact writing, and normal project Git practice do not require an extra Code-role confirmation.
