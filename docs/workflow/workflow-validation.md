# Workflow Validation / 工作流校验

Validation checks whether Full Profile is controlling delivered outcomes. It is local by default and is not product CI unless the target team explicitly adopts it.

## Default Delivery Checks / 默认交付校验

### Milestone Contract

- Objective is user-accepted.
- Project Manager defines the complete milestone KR set as `MKR-1...MKR-N`; no accepted milestone outcome is omitted or deferred to an unnamed future task.
- Every MKR describes an observable user, business, product, or runtime outcome.
- Every MKR has a binary threshold, measurement method, evidence requirement, and claim boundary.
- Research, PRD, architecture, SOPs, tests, reports, packets, and reviews are not delivery KRs unless the user explicitly accepted the artifact itself as the external deliverable.

### Product Contract

- Product Strategy or Product / PRD defines one complete Product OKR for the whole milestone.
- `PKR-1...PKR-N` collectively map every accepted MKR to user behavior, product behavior, scope, acceptance rules, and product claim boundaries.
- Product does not choose one MKR for implementation, create Engineering execution stages, or route directly to evaluation.
- Missing MKR coverage keeps `product_okr_accepted=0`.

### Current State

- Workflow state names exactly one global delivery stage: `milestone_definition`, `product_definition`, `engineering_delivery`, `independent_evaluation`, or `milestone_decision`.
- The current owner is the role responsible for that complete stage contract.
- Accepted milestone, product, engineering candidate, and independent-evaluation paths exist when recorded.
- `candidate_ready_for_independent_evaluation=1` only when Engineering has delivered the complete runnable candidate and its reproducible evidence.
- Independent Evaluation cannot be the current stage before the candidate gate passes.
- Active state does not append chronological process logs.

### Stage Assignment

A valid assignment contains:

```text
milestone
objective
delivery_stage
complete_milestone_kr_set
accepted_global_contract_paths
stage_deliverable
authoritative_inputs
acceptance_checks
required_artifact_path
```

- Task-specific exclusions appear only when genuinely necessary.
- The assignment does not require a precomputed per-file writable whitelist.
- A complete assignment starts work immediately.
- Research, Product, Architecture, and Code Context assignments cover the complete milestone contract.
- Engineering may define `EKR-1...EKR-N` inside its execution plan; no upstream role pre-slices those EKR stages.
- Evaluation assignments contain the complete candidate path and all accepted MKR/PKR checks.

### Primary Artifact

- Exactly one primary professional artifact is required.
- The artifact addresses the complete assigned stage contract and every acceptance check.
- Optional annexes exist only for useful evidence or reproducibility.
- Chat return formatting, manifest readiness, and lock state are not substantive acceptance gates.

### Implementation And Evaluation

- Implementer produces a runnable candidate and reproducible candidate evidence.
- Engineering reports every EKR as `0|1`, but EKR completion cannot set any MKR or PKR to `1`.
- Analysis, plans, documents, and implementation claims alone cannot pass Engineering delivery unless the accepted external deliverable is itself documentation.
- Test Evaluator starts only after the complete candidate gate passes and independently evaluates every accepted MKR/PKR contract.
- Test Evaluator reports `evaluation_executed=0|1` and one `mkr_observed_pass=0|1` result per MKR.
- Required unrun, missing, inferred, unsupported, or environment-invalid evidence is `0`.
- Reviewer, when required, audits the complete current artifact chain, MKR/PKR coverage, EKR traceability, stage order, evidence integrity, and final claims against the original milestone.

## Optional Strict Audit / 可选严格审计

Only when the user explicitly requests immutable packet provenance:

- validate `handoff.manifest.json` structure and listed document paths;
- record exact consumed upstream artifact versions;
- require `ready_for_next_role` and `packet.lock.json`;
- compare locked hashes and create a new packet version after any locked change.

Strict audit metadata must not delay ordinary delivery or become a delivery KR.

## Privacy And Project Boundary / 隐私与项目边界

Validation must not call paid providers, transmit private project data, mutate production, or perform irreversible external actions without the applicable user decision. Public-source research remains available to professional roles. Target-project Git and release actions follow that project's normal process.
