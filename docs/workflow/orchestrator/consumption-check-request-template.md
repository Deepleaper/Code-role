# Short Role Return / 角色短回报

Use the selected role's `templates/return.md`. The common transport fields are:

```text
assignment_id:
assignment_pass: 0 | 1
check_results: <check_id -> 0|1>
packet_path:
evidence_paths:
substantive_blockers: none | <blocker ids>
return_to: workflow-orchestrator
```

This return is a pointer, not the professional source of truth. Workflow Orchestrator must read the packet documents and evidence before deciding.

本回报只是指针，不是专业事实来源。项目经理必须读取 packet 正文和证据后再判断。

Missing transport fields or field order do not justify a role revision when the packet contains enough evidence. Do not include a next-role recommendation, readiness request, packet-lock request, or repeated professional summary.
