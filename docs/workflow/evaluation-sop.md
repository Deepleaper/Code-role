# Evaluation SOP / 评估 SOP

Independent Evaluation records this SOP only after a complete runnable candidate exists and before candidate results are inspected. The accepted Project OKR and Product Contract already freeze outcomes, thresholds, measurement conditions, and claim boundaries.

独立评估只在完整可运行候选物存在后、查看候选结果之前记录本 SOP。产品结果、阈值、测量条件和 claim boundary 已由 KR 契约提前冻结。

```text
milestone:
sop_version:
sop_confirmed: 0 | 1
confirmed_by:

candidate_gate:
  candidate_ready_for_independent_evaluation: 0 | 1
  engineering_artifact_path:
  candidate_artifact_path:

project_okr_path:
product_contract_path:
evaluation_subject:
evaluation_objective:
datasets:
graders:
environment:

required_checks:
| Check ID | KR mapping | Expected observation | Command or method | Required evidence | Pass threshold |
| --- | --- | --- | --- | --- | --- |

required_regressions:
positive_cases:
negative_cases:

claim_boundary:
- allowed:
- forbidden:

accepted_time_or_cost_budget:
```

## Candidate Gate / 候选物门禁

Formal evaluation is invalid unless:

```text
candidate_ready_for_independent_evaluation = 1
candidate_artifact_exists = 1
complete_kr_contract_exists = 1
complete_kr_contract_exists = 1
```

If any condition is `0`, set `evaluation_executed=0` and return the missing gate. Do not evaluate product documents, architecture, STEP activity, or unfinished code.

## SOP Recording Rule / SOP 记录规则

The evaluator derives executable methods from the accepted Project OKR and Product Contract. Before inspecting candidate results, record datasets, graders, commands, environment, thresholds, positive and negative cases, regressions, budgets, and claim boundaries.

The evaluator may not invent or loosen product thresholds. If accepted KR meaning is not executable, report a product-contract blocker instead of changing it.

## Execution Evidence / 执行证据

Record exact inputs, versions, commands, environment, outputs, raw artifact paths, and evaluator identity. Keep Implementer-reported verification separate from evaluator-observed evidence.

Required checks not run are `0`. Scope may not be narrowed to one STEP, latest diff, or convenient subset.

## Binary Result / 二值结果

```text
evaluation_executed: 0 | 1
product_contract_pass: 0 | 1
KR-1...KR-N: 0 | 1
milestone_observed_pass: 0 | 1
```

`milestone_observed_pass=1` only when every required check ran and every accepted KR passed.

## Change Rule / 变更规则

After candidate results are observed, any SOP method change requires:

```text
user_approved_change = 1
new_sop_version_created = 1
all_affected_evidence_rerun = 1
```

Until all three are true, affected evaluation evidence is invalid.
