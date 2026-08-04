# Global Stage Assignment Template / 全局阶段任务书模板

This is one complete professional delivery stage, not a single-MKR task or workflow tutorial. Workflow Orchestrator fills the selected role's exact `templates/assignment.md` from accepted global contracts.

## Required Core / 必填核心

```text
assignment_id:
milestone:
delivery_stage:
milestone_okr_path:
role_deliverable:
authoritative_inputs:
- path:
acceptance_checks:
| check_id | complete stage result | required evidence |
| --- | --- | --- |
required_artifact_path:
irreversible_actions: none
```

Role-specific additions:

- Researcher and Product / PRD: `milestone_okr_scope: all_accepted_mkrs`.
- Product / PRD: complete Product OKR and MKR-to-PKR traceability.
- Architect and Code Context: complete `product_okr_path` and whole-product coverage.
- Implementer: complete MKR/PKR contracts, Engineering objective, and EKR/candidate requirements.
- Test Evaluator: candidate artifact plus `candidate_ready_for_independent_evaluation: 1`.
- Reviewer: complete accepted final outputs and independent evaluation artifact.

Use the role-specific template under `roles/<role>/templates/assignment.md`.

Exact templates:

- `roles/researcher/templates/assignment.md`
- `roles/product-prd/templates/assignment.md`
- `roles/architect/templates/assignment.md`
- `roles/code-context/templates/assignment.md`
- `roles/implementer/templates/assignment.md`
- `roles/test-evaluator/templates/assignment.md`
- `roles/reviewer/templates/assignment.md`

## Rules / 规则

- Project Manager and Product / PRD assignments cover the complete global OKR, not one isolated MKR.
- Implementer alone defines and manages `EKR-1...EKR-N`.
- Test Evaluator cannot be assigned before a complete runnable candidate exists.
- Reviewer cannot be assigned before independent evaluation.
- Freeze stage acceptance checks before work starts.
- Require one primary professional artifact; annexes are optional evidence.
- A complete assignment starts immediately.
- Do not ask for startup acknowledgement, `开始`, readiness conversion, packet lock, or next-role recommendation.

If the prior stage gate, complete upstream contract, deliverable, inputs, acceptance checks, or artifact path is missing, do not issue the assignment. Ask once for the complete missing user-decision set.
