# Evaluation SOP / 评估 SOP

The milestone evaluation SOP is frozen before candidate optimization and remains the stable acceptance anchor.

评估 SOP 必须在候选优化前冻结，并作为稳定验收锚点。

```text
milestone:
sop_version:
sop_confirmed: 0 | 1
confirmed_by:
confirmed_at:

evaluation_subject:
evaluation_objective:

datasets:
- id:
  version_or_hash:
  inclusion_rule:
  exclusion_rule:

graders:
- id:
  deterministic: 0 | 1
  calibration_reference:

environment:
- field:
  value:

required_checks:
| Check ID | Expected observation | Command or method | Required evidence | Pass threshold |
| --- | --- | --- | --- | --- |

required_regressions:
- check_id:

positive_cases:
- case_id:

negative_cases:
- case_id:

claim_boundary:
- allowed:
- forbidden:

accepted_time_or_cost_budget:
```

## Binary Evaluation / 二值评估

```text
check_pass = 1 only when expected observation and evidence satisfy the frozen threshold
check_pass = 0 otherwise
evaluation_executed = 1 only when every required check was run under this frozen SOP with evaluator-owned evidence
evaluation_executed = 0 otherwise
kr_observed_pass = 1 only when evaluation_executed = 1 and every target-KR check_pass = 1
kr_observed_pass = 0 otherwise
```

Required `not_run`, missing, inferred, unsupported, or environment-invalid checks are `0`. Risks and blocker codes are recorded separately and never create a third gate status.

## Independence / 独立性

- Implementer reports are leads, not evaluator-observed evidence.
- Evaluate the complete frozen scope, not only the latest diff.
- Prefer deterministic outcome checks.
- Calibrate model graders with human-reviewed reference cases.
- Record exact commands, inputs, versions, outputs, and artifact paths.
- Test both required and forbidden behavior.

## SOP Change / SOP 变更

Before candidate results, the user may accept a clarified SOP version. After candidate results exist, any SOP change requires:

```text
user_approved_change = 1
new_sop_version_created = 1
affected_evidence_rerun = 1
```

Until all three are true, affected evaluation evidence is invalid for the new SOP version, so `evaluation_executed=0` and `kr_observed_pass=0`.
