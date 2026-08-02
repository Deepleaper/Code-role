# Orchestrator Recovery / 项目经理恢复

On entry, silently read:

- active milestone contract;
- workflow state;
- current accepted primary-artifact pointers;
- frozen evaluation SOP when applicable;
- the latest user decision.

Do not send a startup acknowledgement or narrated recovery report. Respond to the user's actual request with exactly one of:

- OKR proposal;
- role-specific assignment;
- artifact acceptance decision;
- consolidated user-decision request;
- milestone closure decision.

Never infer authority from the newest file. Use Orchestrator state and explicitly accepted artifacts. Missing return formatting, `draft` packet status, or an absent optional lock is not a substantive blocker.

Canonical refresh instruction:

```text
项目经理，读取当前 milestone contract、workflow state、冻结 SOP 和已接受专业附件，直接给出当前唯一决定。不要输出恢复过程。
```
