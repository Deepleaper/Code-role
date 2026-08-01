# Changelog / 变更日志

All notable public changes to Code-role are documented here.

Code-role 的重要公开变更记录在这里。

## [Unreleased]

### Added

- A shared bilingual dialogue-control contract for both the four-workstation and eight-role profiles.
- Role-specific assignment and short-return templates for every professional role.
- Historical-conversation regression tests covering startup chatter, format-only rework, role self-routing, incomplete evaluation setup, SOP drift, and narrated Orchestrator checks.

### Changed

- Complete assignments now start work immediately; startup acknowledgements, routine progress narration, readiness-only turns, and format-only rework are removed from normal flow.
- Project Manager now accepts professional artifacts before judging chat transport format and routes only from substantive failed checks.
- Evaluation and review gates are strictly binary, with risks mapped to failed checks, new accepted KRs, or explicit non-goals.
- Full Profile manifests return to Workflow Orchestrator instead of hard-coding a fixed successor.
- Implementer scope uses assignment-authorized modules or directories instead of accumulated historical per-file whitelists.
- Both initializers now generate the same dialogue controls; Full Profile refresh preserves durable milestone and evaluation state.
- The public four-workstation walkthrough now demonstrates separate Engineering and Independent Evaluation assignments with short returns.

### Verification

- Repository test suite: `75 passed`.

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

[0.3.1]: https://github.com/Deepleaper/Code-role/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/Deepleaper/Code-role/compare/v0.1.1...v0.3.0
