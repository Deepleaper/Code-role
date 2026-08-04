# Milestone Contract / 里程碑合同

Workflow Orchestrator maintains one complete accepted Project OKR under [One Project OKR Standard](../okr-standard.md).

项目经理按照[单一项目 OKR 规范](../okr-standard.md)维护一份完整、已确认的项目 OKR。

```text
milestone:
objective:
objective_accepted: 0 | 1

milestone_key_results:
| KR | Observable outcome | Subject and scenario | Binary threshold and conditions | Required independent evidence | Claim boundary | Pass (0/1) |
| --- | --- | --- | --- | --- | --- | ---: |

non_goals:
- item:

product_contract_required_before_engineering: 1
product_contract_path:
candidate_required_before_evaluation: 1
runnable_candidate_path:
engineering_to_evaluation_attempt_limit: 3
accepted_time_or_cost_budget:
```

## Complete Global Contract / 完整全局契约

- Project Manager defines one complete Objective and two to five `KR-1...KR-N` with the user.
- Product / PRD later defines one complete Product Contract for every existing `KR-1...KR-N`.
- Workflow Orchestrator and Product / PRD do not issue one assignment per KR.
- Implementer alone defines `STEP-1...STEP-N` for engineering phases.
- STEP completion cannot pass a KR.

## KR Quality Gate / KR 质量门禁

Every KR names an observable user, business, product, or runtime outcome; subject and scenario; exact threshold and measurement conditions; independent evidence; and claim boundary.

Research, PRD, architecture, code, tests, evaluation SOP, reports, packets, and reviews are methods or evidence, not delivery KRs unless the user explicitly accepts that artifact as the external product.

Vague terms such as usable, stable, fast, high quality, better, complete, or production ready are invalid without an exact threshold and measurement context.

## Mandatory Stage Gates / 强制阶段门禁

```text
complete Project OKR
    -> complete Product Contract
    -> Architecture and Code Context when required
    -> Implementer STEP execution and complete runnable candidate
    -> Test Evaluator complete independent evaluation
    -> Reviewer when required
    -> closure
```

Test Evaluator must not start before `candidate_ready_for_independent_evaluation=1` and a runnable candidate artifact exists.

## Binary Rules / 二值规则

- Objective, KR definitions, KR scope or thresholds, datasets, graders, and claim boundaries require user acceptance.
- Every KR remains `0` until every required observation is independently evidenced.
- Missing, unrun, inferred, stale, contradictory, or qualitative required evidence is `0`.
- Product, architecture, STEP, implementation, self-tests, or review activity never substitutes for outcome evidence.
- There is no partial KR or milestone state.

## Stage Acceptance / 阶段接受

Workflow Orchestrator reads the complete stage artifact and evidence, then chooses one:

```text
accept_stage_and_advance
return_complete_stage_to_owner
request_user_decision
close_milestone
```

- Product stage acceptance requires every KR to have a complete Product Contract section.
- Architecture and Code Context acceptance require complete Product Contract coverage.
- Engineering acceptance requires all required STEPs, integration checks, and regressions plus a reproducible candidate.
- Evaluation acceptance requires complete KR execution with evaluator-owned evidence.
- Formatting, packet metadata, manifest status, or optional locks are not substantive gates.

## Drift Check / 漂移检查

For every submitted artifact:

- Does it cover the complete accepted global contract for its stage?
- Does it preserve KR meaning, thresholds, and claims?
- Are all stage acceptance checks evidenced?
- Does Implementer keep STEP decomposition separate from higher OKRs?
- Does Evaluation cover the complete runnable candidate and every KR?
- Are observed evidence, professional judgment, inference, and unknown separated?

## Closure / 关闭

Milestone pass is `1` only when every accepted KR is `1`, complete independent evaluation exists, any required final audit passes, and irreversible release actions follow the target project's normal human approval process.
