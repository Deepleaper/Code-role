# Code-role Product Requirements Document

## 1. Product Definition

Code-role is a local role-control system for Codex-assisted software delivery.

It turns a software milestone into explicit ownership, professional artifacts, objective completion evidence, and independent evaluation. It does not replace engineering judgment, Git, an IDE, or a project tracker.

Code-role provides two current product profiles:

1. **Minimal Profile:** four workstations, the smallest complete milestone-control unit.
2. **Full Profile:** eight roles, separated professional ownership with one primary artifact per work unit and optional versioned audit evidence.

Neither profile is deprecated. They solve the same control problem at different levels of process depth.

## 2. Product Principle

The product is organized around observable milestone outcomes, not role activity.

A delivery KR must describe an observable user, business, product, or runtime outcome. Research, PRD, architecture, evaluation SOP, tests, reports, packets, and reviews are methods or evidence, not delivery KRs, unless the user explicitly accepts the artifact itself as the external milestone deliverable.

A role is not complete because it wrote a document, changed code, or ran a command. A required result is complete only when the accepted pass conditions have objective evidence and the designated independent evaluator confirms them.

Shared rules:

- Project Manager owns one complete milestone OKR: one Objective and the full `MKR-1...MKR-N` outcome set.
- Product owns one complete Product OKR: one Product Objective and the full `PKR-1...PKR-N` contract covering every MKR.
- Engineering alone decomposes the accepted product contract into staged `EKR-1...EKR-N` execution units.
- Professional roles own their professional conclusions; an EKR cannot redefine or pass an MKR or PKR.
- Required completion conditions are explicit before work is accepted.
- Missing required evidence equals failure, not partial success.
- Implementation cannot approve itself.
- Software delivery follows Product -> Engineering -> Independent Evaluation. Evaluation cannot start before a complete runnable candidate exists.
- Chat is an interaction surface, not the authoritative project state.
- Generated target-project `code-role/` content is local assistance, not product runtime or release content.

## 3. Problem Statement

AI-assisted software delivery commonly fails in four ways:

1. **Goal drift:** roles optimize their immediate output instead of the accepted milestone.
2. **Responsibility drift:** product, architecture, implementation, evaluation, and audit conclusions are mixed.
3. **Evidence drift:** activity or self-reported success is mistaken for independently verified completion.
4. **Process overload:** too many mandatory stages make small or well-understood work slower without improving quality.

One workflow depth cannot solve both process overload and high-risk traceability. Code-role therefore provides a minimal unit and a full professional configuration.

## 4. Target Users

Primary users:

- Solo builders using Codex for non-trivial software changes.
- Technical founders who need reliable AI-assisted delivery.
- Engineering leads defining repeatable AI engineering practices.
- Small teams that need stronger product and evaluation discipline without adopting a workflow SaaS.

Secondary users:

- AI workflow designers.
- Teams running high-risk, benchmark-sensitive, or audit-intensive engineering work.

## 5. Profile Model

### 5.1 Minimal Profile: Four Workstations

The Minimal Profile is the smallest profile that preserves:

- one accountable Project Manager;
- explicit product judgment;
- professional engineering execution;
- independent evaluation.

Workstations:

| Workstation | Owns |
| --- | --- |
| Project Manager | Complete milestone Objective and `MKR-*` set, global stage control, iteration budget, evidence acceptance, milestone closure |
| Product Strategy | Complete Product Objective and `PKR-*` set covering all MKRs, user value, product behavior, scope, thresholds, non-goals, claim boundaries |
| Engineering | `EKR-*` stage decomposition, engineering research, architecture and code context when needed, implementation, tests, complete runnable candidate evidence |
| Independent Evaluation | Post-candidate executable SOP, datasets, graders, commands, thresholds, complete MKR/PKR evaluation, observed binary results |

The Minimal Profile uses:

- one authoritative `milestone-board.md`;
- one role-specific assignment template for each professional workstation;
- one short return template per professional workstation;
- one required primary professional artifact per global delivery stage under `code-role/work/<milestone>/`;
- optional evidence annexes;
- one mandatory software-delivery order: complete Product OKR -> Engineering candidate -> Independent Evaluation -> Project Manager decision.

It does not require packets, manifests, readiness transitions, or locks.

### 5.2 Full Profile: Eight Roles

The Full Profile separates professional responsibilities when that separation materially reduces uncertainty or risk.

The Full Profile uses separate configured role instances. Each role has its own conversation and consumes explicit authoritative inputs. Switching through multiple roles inside one conversation is not a supported operating model.

Roles:

1. Workflow Orchestrator
2. Researcher
3. Product / PRD
4. Architect
5. Code Context
6. Implementer
7. Test Evaluator
8. Reviewer

The Full Profile uses:

- a confirmed milestone contract;
- Orchestrator state and routing;
- one assignment-named primary professional artifact per work unit;
- optional role-specific versioned packets and `handoff.manifest.json` provenance;
- binary role completion contracts;
- a post-candidate executable evaluation SOP derived from accepted MKR/PKR thresholds;
- optional strict packet locking when immutable evidence is required;
- final Reviewer audit of Orchestrator and every role's current final output.

The Full Profile supports `full-chain`, `mini-chain`, `patch-chain`, `docs-only-chain`, and `research-only`. For software-delivery milestones, those profiles may vary optional Research, Architecture, Code Context, or Reviewer depth, but they cannot skip Product / PRD, Implementer, or post-candidate Test Evaluator. Every professional role returns to Orchestrator before another role is started.

## 6. Profile Selection

Project Manager proposes a profile at milestone start. The user accepts it.

Choose the Minimal Profile when:

- product meaning is already clear or can be resolved by Product Strategy;
- architecture and code-context work can remain Engineering modes;
- one milestone board is sufficient authority;
- packet-level traceability would add more overhead than risk reduction.

Choose the Full Profile when:

- external and repository research require separate ownership;
- architecture decisions need independent review before code mapping;
- implementation scope is broad or safety-critical;
- multiple professional evidence sources must remain inspectable;
- evaluation and final milestone-drift audit need separate owners;
- regulatory, customer, benchmark, or release claims require a stronger audit chain.

Do not switch profiles silently during a milestone. A change requires:

1. an explicit reason;
2. a state-mapping plan;
3. user acceptance;
4. one authoritative control model after the switch.

## 7. Functional Requirements

### FR-1: Binary Milestone Definition

- Project Manager defines one Objective.
- Project Manager defines the complete milestone outcome set as `MKR-1...MKR-N`; a milestone has no more than five by default.
- Every MKR has an observable outcome, binary pass threshold, measurement method, evidence requirement, and claim boundary.
- Each MKR is `0` or `1`.
- Process artifacts are methods or evidence, not KRs, unless the user explicitly accepts the artifact itself as the milestone deliverable.

### FR-2: Complete Product OKR

- Product Strategy or Product / PRD defines one Product Objective and the complete `PKR-1...PKR-N` set for the milestone.
- The Product OKR maps every MKR to users, scenarios, product behavior, scope, acceptance rules, and claim boundaries.
- Product cannot send one MKR at a time to Engineering and cannot define Engineering execution stages.
- Product completion remains `0` while any accepted MKR lacks product coverage.

### FR-3: Engineering Execution KRs

- Engineering consumes the complete accepted MKR and PKR contracts.
- Engineering alone decomposes delivery into ordered `EKR-1...EKR-N` stages with dependencies, artifacts, verification, and stop conditions.
- Each EKR is `0` or `1`, but EKR pass does not imply PKR or MKR pass.
- Engineering must deliver one complete runnable candidate before Independent Evaluation can start.

### FR-4: Professional Ownership

- Project Manager does not invent or rewrite professional conclusions.
- Every professional role has a role-specific assignment and short return contract.
- Every global stage has one required primary professional artifact; Engineering may add EKR evidence annexes and packet metadata is optional.
- Detailed professional reasoning is stored in that role-owned primary artifact.
- Missing required professional evidence makes the assignment fail; imperfect chat formatting does not erase evidence already present in the artifact.

### FR-5: Independent Evaluation

- Independent Evaluation starts only when the complete runnable candidate and reproducible Engineering evidence exist.
- The evaluator records an executable SOP from already accepted MKR/PKR thresholds before inspecting candidate results; it does not redesign the product contract.
- Evaluation covers every MKR and PKR, not one EKR or only the latest diff.
- Targeted and regression checks are both required when specified.
- Unrun required checks equal `0`.
- Engineering or Implementer cannot self-pass.

### FR-6: Failure Loop

- Evaluation failure must include the failed MKR/PKR IDs, observed evidence, and correction owner when known.
- Project Manager decides whether the complete product contract needs correction, Engineering needs a new EKR repair plan, or the evaluation execution itself is invalid.
- The Minimal Profile defaults to three failed Engineering-to-Evaluation candidate attempts before stop and reframe.
- The Full Profile records the current global delivery stage and unmet contract in compact Orchestrator state; optional packet provenance may preserve audit history.

### FR-7: Local Initialization

- `scripts/init_loop_workflow.py` initializes the four-workstation Minimal Profile.
- `scripts/init_project_workflow.py` initializes the eight-role Full Profile.
- Both generate local role-control material without changing product source files.
- Both exclude generated `code-role/` through local `.git/info/exclude` when the target is already a Git repository.

### FR-8: Profile Validation

- Minimal validation confirms exactly four active prompts, complete MKR/PKR contracts, Engineering-owned EKR decomposition, candidate gating, and post-candidate independent evaluation.
- Full validation tests role prompts, MKR/PKR/EKR authority, mandatory stage order, global-stage artifacts, workflow protocol, optional packet metadata, and role completion gates.
- Repository tests prevent documentation and generated prompt contracts from drifting.

## 8. Non-Goals

Code-role does not:

- automatically dispatch work between Codex conversations;
- run an autonomous multi-agent coding pipeline;
- support Switching through multiple roles inside one conversation as a substitute for separate role instances;
- replace GitHub, an IDE, issue tracking, CI, or release management;
- make `code-role/` part of target product runtime;
- require every milestone to use eight roles;
- allow four-role work to bypass product definition or independent evaluation;
- treat qualitative progress as milestone completion;
- automatically approve merge, deploy, publish, delete, payment, or production mutation.

## 9. Success Criteria

The product succeeds when:

1. A user can choose the correct profile without guessing which one is "current."
2. A new target project can be initialized with one documented command.
3. Every active role knows its complete global-stage contract, professional deliverable, binary acceptance checks, authoritative inputs, and primary artifact path.
4. Project Manager can determine milestone status from objective evidence.
5. Engineering can stage execution with EKR plans without changing global outcomes, and Independent Evaluation can reproduce all MKR/PKR checks without relying on Implementer judgment.
6. The next role has less ambiguity than the previous role.
7. Small milestones can use the Minimal Profile without packet overhead.
8. Complex milestones can use the Full Profile without losing professional or audit traceability.

## 10. Quality Bar

Code-role should reduce:

- skipped requirements;
- scope drift;
- unsupported completion claims;
- evaluation baseline drift;
- implementation outside accepted scope;
- manual reconstruction of why a decision was made.

It should not increase:

- role count without risk reduction;
- documents without a downstream decision owner;
- workflow gates unrelated to product evidence;
- Git or release ceremony.

## 11. Product Artifacts

Current official artifacts:

- Top-level bilingual README and profile chooser.
- Minimal Profile contract, four prompts, transport templates, initializer, and validation tests.
- Full Profile workflow protocol, eight role definitions, role output standards, packet templates, initializer, validator, and tests.
- English and Chinese PRDs.
- Shareable Chinese HTML setup guide.
- Minimal target example.

## 12. Near-Term Improvements

1. Add one complete example milestone for each profile.
2. Add a profile-selection checklist to the generated Project Manager prompt.
3. Add Full Profile chain-level validation in addition to single-packet validation.
4. Measure setup time, iteration count, failed claim rate, and evaluator reproducibility across real projects.
5. Add optional dispatch automation only after manual transport remains stable and inspectable.
