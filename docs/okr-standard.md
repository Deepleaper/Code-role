# OKR Definition And Decomposition Standard / OKR 定义与分解规范

This standard is authoritative for both Code-role profiles. It prevents milestone control, product design, engineering execution, and independent evaluation from using the same ambiguous `KR1...KRn` namespace.

本规范同时适用于四角色最小版和八角色完整版。它防止里程碑控制、产品设计、工程执行和独立评估混用同一组含义不清的 `KR1...KRn`。

## 1. Three OKR Layers / 三层 OKR

| Layer | Owner | Purpose | IDs | Completion authority |
| --- | --- | --- | --- | --- |
| Milestone OKR | Project Manager + user | Defines the complete delivered business, user, product, or runtime result | `MKR-1...MKR-N` | Project Manager, using independent evidence |
| Product OKR | Product Strategy / Product PRD | Defines the complete observable product behavior and acceptance contract that realizes every MKR | `PKR-1...PKR-N` | Project Manager accepts the product contract; it does not pass the milestone |
| Engineering Execution KRs | Engineering / Implementer | Decomposes the complete product contract into ordered implementation phases | `EKR-1...EKR-N` | Engineering verifies EKR completion; it does not pass MKRs or PKRs |

Rules:

1. Project Manager defines the complete milestone OKR once. It does not assign one MKR at a time to Product.
2. Product defines one complete Product OKR covering every accepted MKR. It does not return a sequence of isolated product decisions.
3. Engineering owns the only execution decomposition. It may create, order, revise, and complete EKR stages while preserving the accepted MKR and PKR contracts.
4. Independent Evaluation evaluates the complete runnable candidate against MKRs and PKRs. It does not evaluate EKR activity or the latest diff.
5. `MKR`, `PKR`, and `EKR` are separate namespaces. A passed EKR never implies a passed PKR or MKR.

## 2. Milestone Objective Standard / 里程碑 Objective 规范

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

An Objective must not prescribe implementation steps, role activity, documents, or tools unless the accepted product itself is that artifact or tool.

## 3. Milestone KR Standard / 里程碑 MKR 规范

Use two to five non-duplicative MKRs. Every MKR must include:

| Field | Requirement |
| --- | --- |
| `mkr_id` | Stable ID: `MKR-1...MKR-N` |
| `observable_outcome` | A user, business, product, or runtime result, not work performed |
| `subject_and_scenario` | Who or what exhibits the result, under which conditions |
| `binary_threshold` | Exact numerator, denominator, sample size, time window, tolerance, and non-compensable failures |
| `measurement_conditions` | Fixed environment, inputs, comparator, budget, and required regressions where applicable |
| `independent_evidence` | Evidence an evaluator can obtain without trusting Engineering self-report |
| `claim_boundary` | The strongest statement this MKR permits and explicit statements it does not permit |
| `pass` | `0` or `1`; missing, inferred, unrun, contradictory, or failed evidence is `0` |

Reject an MKR when any answer is unclear:

1. Who or what changes?
2. What can an external observer see?
3. Under exactly which conditions?
4. What number or binary rule separates pass from fail?
5. Which independent artifact or run proves it?
6. Which broader claim remains forbidden?

Forbidden delivery MKRs include:

- finish research;
- write a PRD or architecture;
- implement code;
- write or run tests;
- freeze an evaluation SOP;
- produce a report, packet, review, or release note.

Words such as “usable”, “stable”, “high quality”, “fast”, “complete”, “better”, or “production ready” are invalid without explicit measurement conditions and thresholds.

## 4. Product OKR Standard / 产品 PKR 规范

Product Strategy consumes the entire accepted Milestone OKR and produces one complete Product OKR. The Product OKR must cover every MKR before Engineering starts.

Each PKR must include:

| Field | Requirement |
| --- | --- |
| `pkr_id` | Stable ID: `PKR-1...PKR-N` |
| `source_mkrs` | One or more MKRs this product result realizes |
| `user_or_operator` | Named actor |
| `trigger_and_inputs` | Observable starting condition and valid inputs |
| `observable_behavior` | Exact product behavior or output |
| `failure_behavior` | Observable invalid-input, error, timeout, and recovery behavior |
| `binary_acceptance` | Exact product-level pass/fail rule |
| `evidence_required` | What Engineering must expose and Independent Evaluation must observe |
| `scope_and_non_goals` | Included behavior and explicit exclusions |

Product Strategy must also provide:

- an MKR-to-PKR traceability matrix with no uncovered MKR;
- complete user flows and state transitions;
- data, permission, safety, and failure boundaries;
- acceptance criteria that do not require Engineering or Evaluation to invent product meaning.

Product Strategy does not choose implementation architecture, split engineering phases, or pass any MKR.

## 5. Engineering EKR Standard / 工程 EKR 规范

Engineering consumes the complete accepted MKR and PKR contracts, inspects the repository, and creates an execution decomposition appropriate to the actual system.

Each EKR must include:

| Field | Requirement |
| --- | --- |
| `ekr_id` | Stable ID: `EKR-1...EKR-N` |
| `source_pkrs` | PKRs enabled by this engineering result |
| `phase_result` | Concrete integrated behavior or engineering artifact that becomes true |
| `dependencies` | Earlier EKR, external dependency, credential, environment, or decision required |
| `implementation_scope` | Expected code, configuration, migration, fixture, or test areas |
| `binary_verification` | Commands and observable results proving the phase result |
| `regression_scope` | Existing behavior that must remain true |
| `status` | `0` or `1` |

Engineering may revise EKR decomposition when repository facts require it, provided MKRs and PKRs do not change. A change to product behavior, threshold, scope, or claim boundary must return to Project Manager and Product Strategy.

`candidate_ready_for_independent_evaluation=1` requires:

1. every required EKR is `1`;
2. the complete integrated candidate is runnable;
3. target checks and required regressions pass;
4. evaluation can reproduce the candidate from named artifacts, commands, and environment;
5. remaining unsupported claims are explicit.

## 6. Mandatory Software Delivery Order / 软件交付强制顺序

```text
Project Manager: complete Milestone OKR accepted
    -> Product Strategy: complete Product OKR accepted
    -> Engineering: EKR decomposition, implementation, integration, self-verification
    -> Independent Evaluation: complete MKR/PKR evaluation
    -> Project Manager: close or return the failed contract owner
```

For a software-delivery milestone:

- Product acceptance must be complete before Engineering starts.
- A runnable candidate must exist before Independent Evaluation starts.
- Independent Evaluation must reject an assignment when `candidate_ready_for_independent_evaluation != 1` or the candidate artifact is missing.
- Evaluation design, datasets, graders, and commands are acceptance mechanisms, not a pre-code role route. Product defines required outcomes and constraints; the evaluator records the executable SOP before inspecting candidate results, then runs it against the candidate.
- Reviewer, when used, runs only after independent evaluation.

## 7. Independent Evaluation Standard / 独立评估规范

Independent Evaluation consumes:

- the accepted Milestone OKR;
- the complete Product OKR and traceability matrix;
- the runnable candidate and reproducibility evidence;
- required datasets, graders, environments, budgets, regressions, and claim boundaries.

It reports separately:

```text
evaluation_executed: 0 | 1
MKR-1...MKR-N: 0 | 1
product_contract_pass: 0 | 1
milestone_observed_pass: 0 | 1
```

`milestone_observed_pass=1` only when the complete required evaluation ran and every accepted MKR passed. Engineering EKR status is context, not acceptance evidence.

## 8. Change Control / 变更控制

- Changing the Objective, MKR, threshold, measurement condition, or claim boundary requires user acceptance.
- Changing a PKR requires Product Strategy to update the complete Product OKR and traceability matrix, then Engineering must assess affected EKR and rerun affected work.
- Changing an EKR does not require redefining higher OKRs when product behavior remains unchanged.
- Changing an evaluation method after candidate results are observed requires explicit user approval and rerun of every affected check.
- No layer may silently reuse an existing ID after changing its meaning.

## 9. Example / 示例

Invalid milestone KR:

```text
KR1: Complete the Telegram-Hermes-Codex implementation and tests.
```

Valid Milestone KR:

```text
MKR-1: In five independent Telegram-triggered runs, role_id, profile_version,
session_id, and task_id remain identical across Telegram, Hermes, and Codex;
all five runs pass with no missing boundary evidence.
```

Derived Product KR:

```text
PKR-1: After Telegram accepts a valid CPO task, the user sees one canonical
identity tuple, and every processing, completion, or failure state returns the
same tuple in the original conversation.
```

Engineering may then define `EKR-1` for canonical identity creation, `EKR-2` for Hermes propagation, `EKR-3` for Codex propagation, and `EKR-4` for Telegram return and integrated regression. Those EKR stages organize implementation; only independent five-run evidence can pass `MKR-1`.
