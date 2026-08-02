# DeepBrain Case: Strong Evidence Is Not Completion

# DeepBrain 案例：证据很多，不等于里程碑完成

## Snapshot / 案例快照

| Field | Value |
| --- | --- |
| Snapshot date | 2026-07-31 |
| Project type | Private AI agent memory runtime |
| Milestone | Business runtime memory productization |
| Core question | Can DeepBrain produce source-grounded business answers, compare fairly with Hermes, diagnose losses, repair them, and reproduce the evidence? |
| Independent Evaluation result | `evaluation_executed=1`; `kr_observed_pass=0` |
| Weighted score | `73 / 100` |
| Milestone pass | `0` |
| Reviewer route allowed | `0` |
| Public evidence level | Sanitized aggregate metrics from private project records; not a public third-party audit |

## The Risk / 原来的风险

DeepBrain had accumulated enough positive results to make a broad completion claim feel plausible:

- `1,750` unit tests passed, with `25` skipped;
- `142` frontend/runtime tests passed;
- fresh S50 result was `50/50`;
- fresh Smoke20 result was `20/20`;
- fresh LongMemEval-S result was `499/500`;
- the business evidence set recorded memory decisions and grounded answer-source joins for `100/100` cases;
- replay, source-join, governance, and policy-gated memory-evolution artifacts existed.

这些结果都是真实进展，但它们回答的是不同层级的问题。如果把它们合并成一句“DeepBrain 已经完成产品化”，就会把局部能力证据扩大成产品、基准和生产结论。

## The Independent Gate / 独立评估如何判断

The evaluator separated accepted evidence from the product claims it could not support.

| Acceptance requirement | Result | Reason |
| --- | ---: | --- |
| Business task set exists | 1 | A 100-case business artifact set existed. |
| Runtime memory participation exists | 1 | Selected, rejected, and withheld memory records existed. |
| Memory decision evidence is inspectable | 1 | Decision evidence was present across the business set. |
| Answers are joined to selected sources | 1 | `100/100` answer-span source joins were recorded. |
| Fair DeepBrain/Hermes comparator | 0 | Provider evidence still used a local stub and did not establish a production-equivalent comparison. |
| Reliable case-level judgment | 0 | Adjudication records contained unresolved conflicts. |
| Repairable failure diagnosis | 0 | Representative DeepBrain-loss evidence remained insufficient. |
| Repair plus independent rerun | 0 | Several public suites were inspected from artifacts rather than rerun from raw dataset roots. |
| Clean reproducible evidence chain | 0 | Missing raw roots and a dirty worktree blocked clean reproduction. |

The evaluator also recorded that billed provider cost was unavailable and that runtime learning, actual L2 capture, and storage mutation remained disabled.

## The Decision / 最终控制决策

Code-role did not discard the positive evidence. It accepted the exact results that were proven and rejected the claims that were not:

- `milestone completed = 0`
- `Reviewer allowed = 0`
- `production ready = 0`
- `benchmark ready = 0`
- `memory ability OK = 0`
- `runtime self-learning = 0`
- `actual L2 capture = 0`
- `storage mutation = 0`

The next work was narrowed to fair comparison, representative raw benchmark reruns, conflict-free adjudication, repair evidence, clean reproduction, and cost/SLO proof.

## Why Code-role Mattered / Code-role 在这里解决了什么

Without a stable milestone contract, the project could easily have advertised the strongest numbers and ignored the missing product evidence. Code-role forced four separations:

1. Passing tests versus completing a product milestone.
2. Artifact-level evidence versus production runtime behavior.
3. A positive local comparator versus a fair, same-condition comparator.
4. Implementer output versus independently accepted evidence.

The valuable result was not a prettier report. It was an honest `0` with an exact list of evidence required to reach `1`.

这里真正有价值的结果，不是一份更漂亮的报告，而是一个诚实的 `0`，以及从 `0` 到 `1` 还缺哪些证据。

## Claim Boundary / 宣传边界

This case supports the claim that Code-role prevented premature milestone closure in a complex memory-runtime project. It does not publicly prove DeepBrain production readiness, benchmark leadership, or superiority over Hermes.
