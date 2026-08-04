# Changelog / 变更日志

All notable public changes to Code-role are documented here.

Code-role 的重要公开变更记录在这里。

## [Unreleased]

### Added

- A shared single-OKR standard: one Project Objective and `KR-*` set, Product Contract detail attached to those KRs, and Engineering-owned execution steps (`STEP-*`).
- Candidate-readiness gates that prevent Independent Evaluation from starting before a complete runnable implementation exists.
- Regression coverage for complete KR scope, Engineering-only STEP decomposition, mandatory Product -> Engineering -> Evaluation order, and pre-candidate evaluation rejection.

### Changed

- Project Manager now owns the complete project OKR and drives global delivery stages instead of dispatching one KR at a time.
- Product Strategy and Product / PRD now deliver one complete Product Contract covering every accepted KR.
- Engineering and Implementer now own staged STEP decomposition and must deliver one complete reproducible candidate.
- Independent Evaluation and Test Evaluator now run only after candidate readiness and evaluate the complete Project OKR.
- Minimal and Full initializers, role prompts, state templates, examples, PRDs, and public guidance now use the same mandatory software-delivery order.

## [0.4.0] - 2026-08-02

### Added

- A shared bilingual dialogue-control contract for both the four-workstation and eight-role profiles.
- An OKR Delivery Contract that permits only observable user, business, product, or runtime outcomes as delivery KRs.
- One-primary-artifact assignment and return contracts for both profiles.
- Role-specific assignment and short-return templates for every professional role.
- Historical-conversation regression tests covering process KRs, startup chatter, format-only rework, role self-routing, incomplete evaluation setup, SOP drift, narrated Orchestrator checks, and bloated state history.

### Changed

- Complete assignments now start work immediately; startup acknowledgements, routine progress narration, readiness-only turns, and format-only rework are removed from normal flow.
- Project Manager now accepts professional artifacts before judging chat transport format and routes only from substantive failed checks.
- Project Manager now assigns one exact failed evidence item instead of a broad `KR=0` agenda or fixed role chain.
- Research, PRDs, architecture, evaluation SOPs, tests, reports, packets, and reviews are explicitly methods or evidence rather than delivery KRs.
- Both Minimal and Full profiles require one primary professional artifact per work unit; annexes and packet metadata are optional.
- Evaluation and review gates are strictly binary, with risks mapped to failed checks, new accepted KRs, or explicit non-goals.
- Test Evaluator now reports `evaluation_executed` and `kr_observed_pass` as separate binary facts.
- Full Profile manifests return to Workflow Orchestrator instead of hard-coding a fixed successor.
- Implementer receives task-specific exclusions instead of accumulated historical per-file writable whitelists.
- Both initializers now generate the same dialogue controls; Full Profile refresh preserves durable milestone and evaluation state.
- Active milestone boards and Full Profile workflow state are compact current-state records rather than chronological process logs.
- The public four-workstation walkthrough now demonstrates failed-evidence routing, one primary artifact, separate Engineering candidate evidence, and Independent Evaluation outcome evidence.

### Verification

- Repository test suite: `83 passed`.

## [0.3.1] - 2026-07-31

### Added

- Sanitized bilingual case studies from DeepBrain and Leaper Agent.
- A two-case launch article explaining how Code-role prevented premature closure and invalid Engineering startup.
- README proof points that preserve the actual `0` gates rather than presenting unfinished milestones as success stories.

### Changed

- Launch materials now lead with real project evidence instead of hypothetical workflow claims.
- Public case disclosure explicitly excludes private source, repository paths, customer data, and implementation details.

## [0.3.0] - 2026-07-30

### Added

- The four-workstation Minimal Profile: Project Manager, Product Strategy, Engineering, and Independent Evaluation.
- A single milestone board with binary Objective/KR control.
- Fixed PM assignment and role-return contracts for the Minimal Profile.
- Profile initialization, synchronization, and validation through `scripts/init_loop_workflow.py`.
- An evidence-complete goal-loop walkthrough from `KR=0` to independently accepted `KR=1`.
- Public Roadmap, structured Issue forms, social preview assets, and bilingual launch materials.

### Changed

- Defined the four-workstation Minimal Profile and eight-role Full Profile as two current operating choices.
- Tightened role completion so missing required evidence remains `0`.
- Clarified that generated target-project `code-role/` files are local assistance and stay out of product runtime and releases by default.
- Moved the README quickstart and product distinction into the first visitor viewport.

### Verification

- Repository test suite: `68 passed`.
- Social preview: `1280 x 640`, PNG under `1 MB`.

[Unreleased]: https://github.com/Deepleaper/Code-role/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/Deepleaper/Code-role/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/Deepleaper/Code-role/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/Deepleaper/Code-role/compare/v0.1.1...v0.3.0
