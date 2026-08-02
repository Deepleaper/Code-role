# Workflow Validation / 工作流校验

Validation checks whether Full Profile is controlling delivered outcomes. It is local by default and is not product CI unless the target team explicitly adopts it.

## Default Delivery Checks / 默认交付校验

### Milestone Contract

- Objective is user-accepted.
- Every delivery KR describes an observable user, business, product, or runtime outcome.
- Every KR has a binary threshold and required independent evidence.
- Research, PRD, architecture, SOPs, tests, reports, packets, and reviews are not delivery KRs unless the user explicitly accepted the artifact itself as the external deliverable.

### Current State

- Workflow state contains one target KR and one exact current failed evidence item.
- The current owner is the professional role able to repair or decide that evidence.
- Accepted primary artifact and independent evidence paths exist when recorded.
- Active state does not append chronological process logs.

### Work Unit Assignment

A valid assignment contains:

```text
objective
target_kr
current_failed_evidence
role_deliverable
authoritative_inputs
acceptance_checks
required_artifact_path
```

- Task-specific exclusions appear only when genuinely necessary.
- The assignment does not require a precomputed per-file writable whitelist.
- A complete assignment starts work immediately.

### Primary Artifact

- Exactly one primary professional artifact is required.
- The artifact addresses the assigned failed evidence and every acceptance check.
- Optional annexes exist only for useful evidence or reproducibility.
- Chat return formatting, manifest readiness, and lock state are not substantive acceptance gates.

### Implementation And Evaluation

- Implementer produces a runnable candidate and reproducible candidate evidence.
- Analysis, plans, documents, and implementation claims alone cannot pass an implementation work unit.
- Test Evaluator reports `evaluation_executed=0|1` separately from `kr_observed_pass=0|1`.
- Required unrun, missing, inferred, unsupported, or environment-invalid evidence is `0`.
- Reviewer, when required, audits the current accepted final artifacts against the original milestone.

## Optional Strict Audit / 可选严格审计

Only when the user explicitly requests immutable packet provenance:

- validate `handoff.manifest.json` structure and listed document paths;
- record exact consumed upstream artifact versions;
- require `ready_for_next_role` and `packet.lock.json`;
- compare locked hashes and create a new packet version after any locked change.

Strict audit metadata must not delay ordinary delivery or become a delivery KR.

## Privacy And Project Boundary / 隐私与项目边界

Validation must not call paid providers, transmit private project data, mutate production, or perform irreversible external actions without the applicable user decision. Public-source research remains available to professional roles. Target-project Git and release actions follow that project's normal process.
