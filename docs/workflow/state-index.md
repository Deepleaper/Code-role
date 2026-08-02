# State Index / 状态索引

The state index is an optional navigation shortcut for a new role conversation. It is not authoritative and must not become a second workflow state system.

状态索引只是新角色对话的可选导航页，不是权威状态，也不得变成第二套工作流。

## Authority / 权威来源

Read these sources directly:

1. accepted milestone contract;
2. compact Orchestrator workflow state;
3. assignment-named accepted primary professional artifacts;
4. frozen evaluation contract and latest independent evidence;
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
target_kr
current_failed_evidence
current_evidence_owner
current_assignment_path
accepted_primary_artifact_path
latest_independent_evidence_path
milestone_pass
pending_human_decision
authoritative_source_paths
```

Do not append role-by-role chronology, packet status narratives, readiness conversion instructions, residual-risk prose, or next-role recommendations.

## Role Index / 角色索引

A role index may list only:

- stable role responsibility from that role's `ROLE.md`;
- the exact current failed evidence assigned to the role, if any;
- authoritative input paths;
- required primary artifact path;
- task-specific exclusions, if any;
- the authoritative milestone and workflow-state paths.

It must not restate the full role prompt, create a startup confirmation gate, choose a successor, or infer acceptance.

## Refresh / 刷新

Refresh only when an accepted current-state pointer changes. Updating the index is a navigation operation and cannot change Objective, KR, routing, artifact acceptance, or milestone status.

## Release Boundary / 发布边界

`state-index/` is local governance navigation. It is not product runtime content and is excluded from target-project release artifacts by default.
