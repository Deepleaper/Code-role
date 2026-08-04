# One Project OKR Standard / 单一项目 OKR 规范

This standard is authoritative for both Code-role profiles. One milestone has exactly one Project OKR: one Objective and one shared set of `KR-1...KR-N`. Every role works against that same OKR. Product, Engineering, and Evaluation do not create their own Objectives or KRs.

本规范同时适用于四角色最小版和八角色完整版。一个里程碑只能有一套项目 OKR：一个 Objective 和一组共享的 `KR-1...KR-N`。所有角色都围绕这套 OKR 工作；产品、工程和评估不得再创建自己的 Objective 或 KR。

## 1. One OKR, Four Responsibilities / 一套 OKR，四种职责

| Responsibility | Owner | Required artifact | Allowed IDs | Completion authority |
| --- | --- | --- | --- | --- |
| Define and govern the Project OKR | Project Manager + user | Objective, complete KR table, non-goals, claim boundaries | `KR-1...KR-N` | Project Manager records user acceptance and final independent results |
| Make every KR product-complete | Product Strategy / Product PRD | Product Contract attached to the existing KRs | Existing `KR-*` only | Project Manager accepts product-definition completeness; Product does not pass KRs |
| Build the complete candidate | Engineering / Implementer | Engineering Execution Plan and runnable candidate | `STEP-1...STEP-N`, each mapped to `KR-*` | Engineering verifies steps and candidate readiness; steps do not pass KRs |
| Independently test the outcome | Independent Evaluation / Test Evaluator | Recorded SOP, raw evidence, and one `0|1` result per existing KR | Existing `KR-*` and evaluator check IDs | Independent Evaluation observes KR results; Project Manager decides closure |

Hard rules:

1. No role may create a second Objective or KR set.
2. Product elaborates the existing KRs into observable behavior and acceptance rules without renaming, splitting, replacing, or adding KRs.
3. Engineering may create implementation steps because steps describe work order, not outcomes. A passed step never implies a passed KR.
4. Independent Evaluation evaluates the complete runnable candidate against every accepted KR, not against role activity or the latest diff.
5. Only the user and Project Manager may accept a changed Objective, KR, threshold, measurement condition, non-goal, or claim boundary.

## 2. Objective Standard / Objective 规范

One milestone has one Objective. It must state:

- **subject:** the named user, operator, business, product, or runtime;
- **scenario:** the real situation in which value is observed;
- **changed outcome:** the end state that must become true;
- **scope or time boundary:** where and when the claim applies;
- **claim boundary:** what the milestone will not prove.

Recommended form:

```text
For <subject> in <scenario>, change <current problem> into <observable end state>
within <scope/time boundary>, without claiming <explicit exclusions>.
```

An Objective must not prescribe role activity, documents, tools, or implementation steps unless the accepted product itself is that artifact or tool.

## 3. Shared KR Standard / 共享 KR 规范

Use two to five non-duplicative KRs. Every role must preserve these IDs and meanings.

| Field | Requirement |
| --- | --- |
| `kr_id` | Stable ID: `KR-1...KR-N` |
| `observable_outcome` | A user, business, product, or runtime result, not work performed |
| `subject_and_scenario` | Who or what exhibits the result, under which conditions |
| `binary_threshold` | Exact numerator, denominator, sample size, time window, tolerance, and non-compensable failures |
| `measurement_conditions` | Fixed environment, inputs, comparator, budget, and required regressions where applicable |
| `independent_evidence` | Evidence an evaluator can obtain without trusting Engineering self-report |
| `claim_boundary` | The strongest statement this KR permits and explicit statements it does not permit |
| `pass` | `0` or `1`; missing, inferred, unrun, contradictory, or failed evidence is `0` |

Reject a KR when any answer is unclear:

1. Who or what changes?
2. What can an external observer see?
3. Under exactly which conditions?
4. What number or binary rule separates pass from fail?
5. Which independent artifact or run proves it?
6. Which broader claim remains forbidden?

Research, PRD, architecture, code, tests, SOPs, reports, packets, and reviews are methods or evidence. They are not delivery KRs unless the user explicitly accepts that artifact as the external product.

Words such as “usable”, “stable”, “high quality”, “fast”, “complete”, “better”, or “production ready” are invalid without explicit conditions and thresholds.

## 4. Product Contract Standard / 产品契约规范

Product consumes the entire accepted Project OKR and makes every existing KR product-complete. It does not define another Objective or KR set.

For every existing `KR-*`, the Product Contract adds:

| Field | Requirement |
| --- | --- |
| `kr_id` | The unchanged Project OKR ID |
| `user_or_operator` | Named actor |
| `trigger_and_inputs` | Observable starting condition and valid inputs |
| `observable_behavior` | Exact product behavior or output required to realize the KR |
| `failure_behavior` | Observable invalid-input, error, timeout, and recovery behavior |
| `binary_acceptance` | Product-level acceptance detail consistent with the KR threshold |
| `evidence_required` | What Engineering must expose and Evaluation must observe |
| `scope_and_non_goals` | Included behavior and explicit exclusions |

The Product Contract must also provide complete user flows, states, permissions, data boundaries, failure handling, and unresolved decisions. Optional requirement or scenario labels may organize detail, but they do not create another goal hierarchy.

`product_contract_accepted=1` requires every accepted KR to be fully specified without changing its outcome, threshold, evidence requirement, or claim boundary.

## 5. Engineering Execution Plan / 工程执行计划

Engineering consumes the accepted Project OKR and Product Contract, inspects the real repository, and creates only the implementation decomposition needed to build the candidate.

Each step includes:

| Field | Requirement |
| --- | --- |
| `step_id` | Stable execution ID: `STEP-1...STEP-N` |
| `source_krs` | One or more existing KRs enabled by this step |
| `phase_result` | Concrete integrated behavior or engineering artifact that becomes true |
| `dependencies` | Earlier steps, external dependencies, credentials, environments, or decisions |
| `implementation_scope` | Expected code, configuration, migration, fixture, or test areas |
| `binary_verification` | Commands and observable results proving the phase result |
| `regression_scope` | Existing behavior that must remain true |
| `status` | `0` or `1` |

Engineering may revise steps when repository facts require it. Any requested change to product behavior, KR threshold, scope, or claim boundary returns to Project Manager and Product.

`candidate_ready_for_independent_evaluation=1` requires:

1. every required step is `1`;
2. the complete integrated candidate is runnable;
3. target checks and required regressions pass;
4. Evaluation can reproduce the candidate from named artifacts, commands, and environment;
5. remaining unsupported claims are explicit.

Candidate readiness is an engineering gate. It does not set any KR to `1`.

## 6. Mandatory Software Delivery Order / 软件交付强制顺序

```text
Project Manager + user: accept one complete Project OKR
    -> Product: complete the Product Contract for every existing KR
    -> Engineering: plan steps, implement, integrate, and self-verify
    -> Independent Evaluation: evaluate every existing KR on the runnable candidate
    -> Project Manager: close or return the failed responsibility
```

- Product Contract acceptance is required before Engineering starts.
- A complete runnable candidate is required before Independent Evaluation starts.
- Independent Evaluation rejects an assignment when candidate readiness is not `1` or the candidate artifact is missing.
- Product defines required outcomes and constraints. Evaluation records the executable SOP before inspecting candidate results, then runs it against the candidate.
- Reviewer, when used, runs only after independent evaluation.

## 7. Independent Evaluation Standard / 独立评估规范

Independent Evaluation consumes the accepted Project OKR, Product Contract, runnable candidate, reproducibility evidence, required datasets, graders, environments, budgets, regressions, and claim boundaries.

It reports:

```text
evaluation_executed: 0 | 1
KR-1...KR-N: 0 | 1
product_contract_pass: 0 | 1
milestone_observed_pass: 0 | 1
```

`evaluation_executed=1` requires the complete recorded SOP to run. `milestone_observed_pass=1` requires every accepted KR to pass with evaluator-owned evidence. Engineering step status is context, never independent acceptance evidence.

## 8. Change Control / 变更控制

- Changing the Objective, any KR, threshold, measurement condition, non-goal, or claim boundary requires user acceptance.
- A KR change invalidates affected Product Contract sections, Engineering steps, and evaluation checks until each is updated and rerun.
- Changing an engineering step does not change the Project OKR when observable product behavior remains unchanged.
- Changing an evaluation method after candidate results are observed requires explicit user approval and rerun of every affected check.
- No role may silently reuse an existing ID after changing its meaning.

## 9. Example / 示例

Invalid KR:

```text
KR-1: Complete the Telegram-Hermes-Codex implementation and tests.
```

Valid shared KR:

```text
KR-1: In five independent Telegram-triggered runs, role_id, profile_version,
session_id, and task_id remain identical across Telegram, Hermes, and Codex;
all five runs pass with no missing boundary evidence.
```

Product adds the trigger, valid and invalid inputs, visible states, timeout behavior, and evidence obligations directly under `KR-1`. It does not create a second KR.

Engineering may define `STEP-1` for canonical identity creation, `STEP-2` for Hermes propagation, `STEP-3` for Codex propagation, and `STEP-4` for Telegram return and integrated regression. These steps organize implementation; only independent five-run evidence can pass `KR-1`.
