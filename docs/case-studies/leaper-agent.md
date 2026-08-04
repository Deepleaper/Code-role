# Leaper Agent Case: Why Pre-Code Evaluation Was Removed

# Leaper Agent 案例：为什么取消工程前评估

> Historical workflow note: this snapshot was produced by the older pre-code `baseline_freeze` route. The current Code-role standard does not route Test Evaluator before a runnable candidate. Product owns outcome thresholds and evidence requirements; Engineering builds the candidate; Test Evaluator then records and executes the SOP. The evidence below is preserved because it directly motivated that redesign.
>
> 历史流程说明：本快照来自旧版“工程前冻结评估基线”路线。当前 Code-role 不允许在可运行候选物产生前启动 Test Evaluator。产品负责结果阈值和证据要求，工程完成候选物后，评估师再记录并执行 SOP。保留以下证据，是因为它直接推动了本次流程修正。

## Snapshot / 案例快照

| Field | Value |
| --- | --- |
| Snapshot date | 2026-07-31 |
| Project type | Private enterprise AI Employee runtime |
| Milestone | Hermes-plus enterprise runtime productization |
| Historical target | Enterprise business outcomes exceed Hermes under same-condition evaluation |
| Historical target pass | `0` |
| Historical control state | pre-code evaluator baseline not accepted |
| Current-model interpretation | Product evidence contract incomplete; Test Evaluator route would be rejected until candidate readiness |
| Public evidence level | Sanitized aggregate workflow evidence from private project records |

## The Objective / 目标

The accepted Objective was deliberately stronger than “build an agent runtime.” Leaper Agent had to demonstrate better enterprise task outcomes and repeatability than Hermes under the same model/provider, tools, budget, environment, and scoring conditions.

The complete milestone used five non-compensating hard KRs, now represented as `MKR-1...MKR-5`:

1. Enterprise business outcomes exceed Hermes.
2. Repeat reliability and efficiency meet frozen thresholds.
3. Enterprise governance is measurably stronger.
4. Audit, replay, diagnosis, repair, and rerun form a closed loop.
5. New operators can use the product and independently reproduce the result.

A high score in one KR cannot compensate for missing evidence in another.

## The First Baseline Looked Professional / 第一版为什么看起来像完成了

Under the historical workflow, the Independent Evaluation workstation returned a detailed pre-code baseline document with task rules, holdout language, grader roles, same-condition requirements, and evidence manifests.

It was structurally professional, but the Project Manager checked whether the referenced objects actually existed and found six blocking failures:

| Gate | Failure |
| --- | --- |
| Task set | Referenced frozen task files did not exist and records still contained placeholders. |
| Holdout | Holdout content was readable from the shared attachment; isolation was declared rather than enforced. |
| Reserve pool | Reserve records were incomplete or placeholder-based. |
| Same-condition run | Provider, model, and backend values were not concretely frozen. |
| Grading | The roster contained role aliases rather than a committed executable grader mechanism. |
| Integrity | Hashes did not point to standalone canonical artifacts that could be reproduced. |

## The PM Decision / 项目经理如何处理

The Project Manager rejected the first evaluator return with `reason=evidence_missing`.

It did not:

- let the evaluator mark its own SOP as authoritative;
- route Engineering against nonexistent inputs;
- expose the holdout to the implementation workstation;
- reinterpret a polished Markdown plan as executable evidence;
- change KR1 from `0`.

Instead, it returned a precise correction assignment under the historical ownership model.

## What The Correction Produced / 打回后产生了什么

The corrected candidate baseline produced concrete artifacts rather than declarations:

- `60` primary tasks across `6` categories;
- `24` reserve tasks;
- `12/60` primary tasks physically separated as holdout;
- real input artifacts for each task;
- a visible-only Engineering extract;
- `0` public-extract holdout leakage findings;
- a concrete same-condition runtime contract;
- `7` grader slots and `6` sealed calibration cases;
- `198` files in the integrity index;
- explicit schemas, command contracts, hashes, and failure behavior.

The historical evaluator reported the corrected baseline as frozen, while Project Manager kept the milestone outcome at `0`. Under the current model, these artifacts would be accepted as Product/evidence inputs, not as a Test Evaluator pass and not as authorization to skip Engineering.

评估工位已经提交修正版并自报基线完成，但项目经理尚未验收，因此项目控制状态仍然是 `0`。这正是角色专业判断和里程碑控制权的边界。

## Why Code-role Mattered / Code-role 在这里解决了什么

Leaper Agent shows why the Project Manager cannot be a message-forwarding bot. Its job was not to rewrite the evaluator's professional content. Its job was to verify that the output could actually start the next workstation without guessing.

The correction transformed:

- task descriptions into machine-readable task artifacts;
- “20% holdout” into physical separation;
- grader role names into an executable grader mechanism;
- same-condition prose into frozen runtime fields;
- summary hashes into a reproducible integrity index.

The case exposed a real integrity problem, but it also exposed a role-order problem: evaluation design work had become a pre-code evaluator stage. Current Code-role keeps product thresholds and evidence requirements in the complete Product OKR, lets Engineering build the complete candidate, and starts independent evaluation only afterward.

## Claim Boundary / 宣传边界

This historical case supports two bounded claims: Code-role detected a non-executable evidence contract, and that experience justified removing pre-code Test Evaluator routing. It does not claim that Leaper Agent already beats Hermes, that any MKR passed, or that the product milestone is complete.
