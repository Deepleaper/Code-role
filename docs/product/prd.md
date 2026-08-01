# Code-role Product Requirements Document

## 1. Product Definition

Code-role is a local role-control system for Codex-assisted software delivery.

It turns a software milestone into explicit ownership, professional artifacts, objective completion evidence, and independent evaluation. It does not replace engineering judgment, Git, an IDE, or a project tracker.

Code-role provides two current product profiles:

1. **Minimal Profile:** four workstations, the smallest complete milestone-control unit.
2. **Full Profile:** eight roles, separated professional ownership with versioned packet evidence and final chain audit.

Neither profile is deprecated. They solve the same control problem at different levels of process depth.

## 2. Product Principle

The product is organized around milestone completion, not role activity.

A role is not complete because it wrote a document, changed code, or ran a command. A required result is complete only when the accepted pass conditions have objective evidence and the designated independent evaluator confirms them.

Shared rules:

- Project Manager owns the milestone.
- Professional roles own professional conclusions.
- Required completion conditions are explicit before work is accepted.
- Missing required evidence equals failure, not partial success.
- Implementation cannot approve itself.
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
| Project Manager | Objective, binary KRs, current KR, routing, iteration budget, evidence acceptance, milestone closure |
| Product Strategy | User value, product behavior, scope, thresholds, non-goals, claim boundaries |
| Engineering | Engineering research, architecture when needed, code-context mapping when needed, implementation, tests, candidate evidence |
| Independent Evaluation | Evaluation baseline, datasets, graders, commands, thresholds, targeted checks, regression checks, observed binary results |

The Minimal Profile uses:

- one authoritative `milestone-board.md`;
- one role-specific assignment template for each professional workstation;
- one short return template per professional workstation;
- professional attachments under `code-role/work/<milestone>/`;
- dynamic routing for one accepted `KR=0` at a time.

It does not require packets, manifests, readiness transitions, locks, or a fixed role chain.

### 5.2 Full Profile: Eight Roles

The Full Profile separates professional responsibilities when that separation materially reduces uncertainty or risk.

The Full Profile uses separate configured role instances. Each role has its own conversation and consumes explicit upstream documents. Switching through multiple roles inside one conversation is not a supported operating model.

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
- role-specific versioned packets;
- exact upstream `handoff.manifest.json` inputs;
- binary role completion contracts;
- a frozen evaluation SOP;
- optional strict packet locking when immutable evidence is required;
- final Reviewer audit of Orchestrator and every role's current final output.

The Full Profile supports `full-chain`, `mini-chain`, `patch-chain`, `docs-only-chain`, and `research-only`, but every professional role returns to Orchestrator before another role is started.

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
- multiple evidence packets must remain inspectable;
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
- A milestone has no more than five observable Key Results by default.
- Every KR has a pass condition and required independent evidence.
- Each KR is `0` or `1`.

### FR-2: One Current Delivery Target

- Each iteration targets exactly one accepted `KR=0`.
- Regression checks may cover other KRs, but they cannot become hidden delivery targets.
- Project Manager records the current owner and iteration count.

### FR-3: Professional Ownership

- Project Manager does not invent or rewrite professional conclusions.
- Every professional role has a role-specific assignment and short return contract.
- Detailed professional reasoning is stored in role-owned artifacts.
- Missing required professional evidence makes the assignment fail; imperfect chat formatting does not erase evidence already present in the artifact.

### FR-4: Independent Evaluation

- Evaluation criteria, data, graders, environment, commands, and thresholds are frozen before optimization.
- Evaluation covers the complete required milestone scope, not only the latest diff.
- Targeted and regression checks are both required when specified.
- Unrun required checks equal `0`.
- Engineering or Implementer cannot self-pass.

### FR-5: Failure Loop

- Evaluation failure must include observed evidence and an actionable owner when known.
- Project Manager routes the failure to Product Strategy/Product, Engineering/Implementer, or evaluation-definition repair.
- The Minimal Profile defaults to three failed Engineering-to-Evaluation attempts per KR before stop and reframe.
- The Full Profile records failed attempts through its packet and Orchestrator state model.

### FR-6: Local Initialization

- `scripts/init_loop_workflow.py` initializes the four-workstation Minimal Profile.
- `scripts/init_project_workflow.py` initializes the eight-role Full Profile.
- Both generate local role-control material without changing product source files.
- Both exclude generated `code-role/` through local `.git/info/exclude` when the target is already a Git repository.

### FR-7: Profile Validation

- Minimal validation confirms exactly four active prompts, required templates, the binary loop contract, and the independent evaluation contract.
- Full validation tests role prompts, workflow protocol, source map, packet schema, and role completion gates.
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
3. Every active role knows its professional input, output, authority, and stop condition.
4. Project Manager can determine milestone status from objective evidence.
5. Independent Evaluation can reproduce the required checks without relying on Implementer judgment.
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
