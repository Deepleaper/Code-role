# State Index / 状态索引

The state index is an optional navigation shortcut for a new role conversation. It is not authoritative and must not become a second workflow state system.

状态索引只是新角色对话的可选导航页，不是权威状态，也不得变成第二套工作流。

## Authority / 权威来源

Read these sources directly:

1. accepted milestone contract;
2. compact Orchestrator workflow state;
3. assignment-named accepted primary professional artifacts;
4. accepted KR evaluation requirements, post-candidate executable SOP, and latest independent evidence;
5. optional strict packet manifest and lock only when immutable audit was explicitly requested.

If the index conflicts with any authoritative source, ignore the index.

## Optional Location / 可选位置

```text
code-role/state-index/
  README.md
  current-workflow-index.md
  roles/
    workflow-orchestrator.md
    researcher.md
    product-prd.md
    architect.md
    code-context.md
    implementer.md
    test-evaluator.md
    reviewer.md
```

## Current Workflow Index / 当前工作索引

Keep only current navigation fields:

```text
milestone
objective
delivery_stage
project_okr_accepted
product_contract_accepted
candidate_ready_for_independent_evaluation
evaluation_executed
current_assignment_path
accepted_milestone_contract_path
accepted_product_contract_path
accepted_engineering_plan_path
current_candidate_artifact_path
latest_independent_evidence_path
milestone_pass
current_blocking_contract
pending_human_decision
authoritative_source_paths
```

Do not append role-by-role chronology, packet status narratives, readiness conversion instructions, residual-risk prose, or next-role recommendations.

## Role Index / 角色索引

A role index may list only:

- stable role responsibility from that role's `ROLE.md`;
- the current global delivery stage and its unmet contract, if any;
- authoritative input paths;
- required primary artifact path;
- task-specific exclusions, if any;
- the authoritative milestone and workflow-state paths.

It must not restate the full role prompt, create a startup confirmation gate, choose a successor, infer acceptance, or duplicate Engineering's internal `STEP-*` execution plan.

## Refresh / 刷新

Refresh only when an accepted current-state pointer changes. Updating the index is a navigation operation and cannot change Objective, KR, routing, artifact acceptance, or milestone status.

## Release Boundary / 发布边界

`state-index/` is local governance navigation. It is not product runtime content and is excluded from target-project release artifacts by default.
