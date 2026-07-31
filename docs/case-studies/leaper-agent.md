# Leaper Agent Case: A Plan Is Not A Frozen Baseline

# Leaper Agent 案例：评估方案不等于可执行基线

## Snapshot / 案例快照

| Field | Value |
| --- | --- |
| Snapshot date | 2026-07-31 |
| Project type | Private enterprise AI Employee runtime |
| Milestone | Hermes-plus enterprise runtime productization |
| Current KR | Enterprise business outcomes exceed Hermes under frozen same-condition evaluation |
| Current KR pass | `0` |
| Project Manager control state | `evaluation_sop_frozen = 0` pending acceptance of the corrected evaluator return |
| Engineering route allowed | `0` until the Project Manager accepts an executable baseline |
| Public evidence level | Sanitized aggregate workflow evidence from private project records |

## The Objective / 目标

The accepted Objective was deliberately stronger than “build an agent runtime.” Leaper Agent had to demonstrate better enterprise task outcomes and repeatability than Hermes under the same model/provider, tools, budget, environment, and scoring conditions.

The complete milestone used five non-compensating hard KRs:

1. Enterprise business outcomes exceed Hermes.
2. Repeat reliability and efficiency meet frozen thresholds.
3. Enterprise governance is measurably stronger.
4. Audit, replay, diagnosis, repair, and rerun form a closed loop.
5. New operators can use the product and independently reproduce the result.

A high score in one KR cannot compensate for missing evidence in another.

## The First Baseline Looked Professional / 第一版为什么看起来像完成了

The Independent Evaluation workstation returned a detailed baseline-freeze document with task rules, holdout language, grader roles, same-condition requirements, and evidence manifests.

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

Instead, it returned a precise correction assignment to Independent Evaluation.

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

The evaluator reported the corrected baseline as frozen. However, the Project Manager control board still remains `evaluation_sop_frozen=0` until it independently accepts the return. This distinction is intentional: professional roles own professional conclusions, but only the Project Manager changes milestone control state.

评估工位已经提交修正版并自报基线完成，但项目经理尚未验收，因此项目控制状态仍然是 `0`。这正是角色专业判断和里程碑控制权的边界。

## Why Code-role Mattered / Code-role 在这里解决了什么

Leaper Agent shows why the Project Manager cannot be a message-forwarding bot. Its job was not to rewrite the evaluator's professional content. Its job was to verify that the output could actually start the next workstation without guessing.

The correction transformed:

- task descriptions into machine-readable task artifacts;
- “20% holdout” into physical separation;
- grader role names into an executable grader mechanism;
- same-condition prose into frozen runtime fields;
- summary hashes into a reproducible integrity index.

Engineering was protected from starting against an invalid test contract, and the eventual comparison was protected from implementation leakage.

## Claim Boundary / 宣传边界

This case supports the claim that Code-role detected and corrected a non-executable evaluation baseline before Engineering started. It does not claim that Leaper Agent already beats Hermes, that KR1 has passed, or that the product milestone is complete.
