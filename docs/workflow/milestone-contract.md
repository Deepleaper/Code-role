# Milestone Contract / 里程碑合同

Workflow Orchestrator maintains one complete accepted Milestone OKR under [OKR Definition And Decomposition Standard](../okr-standard.md).

项目经理按照 [OKR 定义与分解规范](../okr-standard.md)维护一份完整、已确认的里程碑 OKR。

```text
milestone:
objective:
objective_accepted: 0 | 1

milestone_key_results:
| MKR | Observable outcome | Subject and scenario | Binary threshold and conditions | Required independent evidence | Claim boundary | Pass (0/1) |
| --- | --- | --- | --- | --- | --- | ---: |

non_goals:
- item:

product_okr_required_before_engineering: 1
product_okr_path:
candidate_required_before_evaluation: 1
runnable_candidate_path:
engineering_to_evaluation_attempt_limit: 3
accepted_time_or_cost_budget:
```

## Complete Global Contract / 完整全局契约

- Project Manager defines one complete Objective and two to five `MKR-1...MKR-N` with the user.
- Product / PRD later defines one complete `PKR-1...PKR-N` contract covering every MKR.
- Workflow Orchestrator and Product / PRD do not issue one assignment per MKR.
- Implementer alone defines `EKR-1...EKR-N` for engineering phases.
- EKR completion cannot pass an MKR.

## MKR Quality Gate / MKR 质量门禁

Every MKR names an observable user, business, product, or runtime outcome; subject and scenario; exact threshold and measurement conditions; independent evidence; and claim boundary.

Research, PRD, architecture, code, tests, evaluation SOP, reports, packets, and reviews are methods or evidence, not delivery MKRs unless the user explicitly accepts that artifact as the external product.

Vague terms such as usable, stable, fast, high quality, better, complete, or production ready are invalid without an exact threshold and measurement context.

## Mandatory Stage Gates / 强制阶段门禁

```text
complete Milestone OKR
    -> complete Product OKR
    -> Architecture and Code Context when required
    -> Implementer EKR execution and complete runnable candidate
    -> Test Evaluator complete independent evaluation
    -> Reviewer when required
    -> closure
```

Test Evaluator must not start before `candidate_ready_for_independent_evaluation=1` and a runnable candidate artifact exists.

## Binary Rules / 二值规则

- Objective, MKR definitions, PKR scope or thresholds, datasets, graders, and claim boundaries require user acceptance.
- Every MKR remains `0` until every required observation is independently evidenced.
- Missing, unrun, inferred, stale, contradictory, or qualitative required evidence is `0`.
- Product, architecture, EKR, implementation, self-tests, or review activity never substitutes for outcome evidence.
- There is no partial MKR or milestone state.

## Stage Acceptance / 阶段接受

Workflow Orchestrator reads the complete stage artifact and evidence, then chooses one:

```text
accept_stage_and_advance
return_complete_stage_to_owner
request_user_decision
close_milestone
```

- Product stage acceptance requires every MKR to map to PKRs.
- Architecture and Code Context acceptance require complete Product OKR coverage.
- Engineering acceptance requires all required EKRs, integration checks, and regressions plus a reproducible candidate.
- Evaluation acceptance requires complete MKR/PKR execution with evaluator-owned evidence.
- Formatting, packet metadata, manifest status, or optional locks are not substantive gates.

## Drift Check / 漂移检查

For every submitted artifact:

- Does it cover the complete accepted global contract for its stage?
- Does it preserve MKR and PKR meaning, thresholds, and claims?
- Are all stage acceptance checks evidenced?
- Does Implementer keep EKR decomposition separate from higher OKRs?
- Does Evaluation cover the complete runnable candidate and every MKR/PKR?
- Are observed evidence, professional judgment, inference, and unknown separated?

## Closure / 关闭

Milestone pass is `1` only when every accepted MKR is `1`, complete independent evaluation exists, any required final audit passes, and irreversible release actions follow the target project's normal human approval process.
