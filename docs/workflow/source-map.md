# Source Map

This source map tells each role where to read and write by default.

## Global Read Defaults

Every role may read:

- [Document Workflow](README.md)
- [Handoff Protocol](handoff-protocol.md)
- [Packet Schema](packet-schema.md)
- [Workflow Chain Policy](workflow-chain-policy.md)
- [State Index](state-index.md), only when optional state-index files are generated
- its own `ROLE.md`
- upstream packet manifests explicitly provided by the user or by the previous role
- target-project `code-role/state-index/roles/<role>.md` when present

## Orchestrator Read Scope

The Orchestrator may read:

- `docs/workflow/`
- role `ROLE.md` files
- upstream packet manifests explicitly provided by the user
- current packet manifests needed to determine workflow state

The Orchestrator should not read broad runtime code by default. It controls process state, not implementation.

## Orchestrator Write Scope

The Orchestrator writes only:

```text
docs/workflow/orchestrator/workflow-state.md
docs/workflow/orchestrator/milestone-registry.md
docs/workflow/orchestrator/decision-log.md
docs/workflow/orchestrator/final-packet-index.md
```

The Orchestrator must not write role report packets, code, tests, product docs, architecture docs, or release docs.

In an initialized target project, an explicitly authorized optional indexing step may write `code-role/state-index/`. That index remains non-authoritative navigation and must not replace Orchestrator state or packet manifests.

## Researcher Read Scope

The Researcher may read these repo areas when needed to verify facts:

- `docs/architecture/`
- `docs/runtime/`
- `docs/opc-agent/`
- `docs/benchmarks/`
- `docs/release/`
- `docs/reports/`
- `examples/`
- `tests/`
- `src/`

Code and tests should be read for factual verification only. The Researcher does not change runtime code, tests, product requirements, or architecture decisions.

## Researcher Write Scope

The Researcher writes only under:

```text
docs/workflow/roles/researcher/reports/<milestone>/packet-vNNN/
```

The Researcher must not write outside its reports folder without explicit user confirmation.

## Product / PRD Read Scope

The Product / PRD role may read:

- upstream Researcher packet manifests explicitly provided by the user or previous role
- files listed in the upstream Researcher manifest
- `docs/PRD.md` and existing product docs when needed for consistency
- `docs/release/` only to avoid contradicting release boundaries
- `docs/workflow/` protocol and role files

The Product / PRD role should not read broad code paths by default. If product scope depends on current implementation facts, ask for confirmation or hand off to Code Context.

## Product / PRD Write Scope

The Product / PRD role writes only under:

```text
docs/workflow/roles/product-prd/reports/<milestone>/packet-vNNN/
```

The Product / PRD role must not write product source docs, architecture docs, release docs, code, or tests without explicit user confirmation.

## Architect Read Scope

The Architect may read:

- Product / PRD packet manifests explicitly provided by the user or Orchestrator
- Researcher packet manifests when needed for evidence traceability
- files listed in upstream manifests
- `docs/architecture/`
- `docs/runtime/`
- `docs/opc-agent/`
- relevant `src/` and `tests/` for factual verification only

The Architect should not read broad repo paths by default. If architecture depends on implementation details, ask for the Code Context role to map them.

## Architect Write Scope

The Architect writes only under:

```text
docs/workflow/roles/architect/reports/<milestone>/packet-vNNN/
```

The Architect must not write runtime code, tests, release docs, or product source docs without explicit user confirmation.

## Code Context Read Scope

The Code Context role may read:

- Architect packet manifests
- Product / PRD packet manifests
- files listed in upstream manifests
- `src/`, `tests/`, `examples/`, and relevant docs within the scope approved by Architect or Orchestrator

The Code Context role may inspect broad repo paths only when the upstream packet or Orchestrator explicitly requires an impact map.

## Code Context Write Scope

The Code Context role writes only under:

```text
docs/workflow/roles/code-context/reports/<milestone>/packet-vNNN/
```

The Code Context role must not modify code, tests, examples, product docs, architecture docs, or release docs.

## Implementer Read Scope

The Implementer may read:

- Code Context packet
- Architect packet
- Product / PRD packet
- files explicitly listed in upstream implementation scope
- relevant code, tests, examples, and docs needed to implement the approved scope

The Implementer must not begin from chat-only instruction. Orchestrator must approve Implementer start.

## Implementer Write Scope

The Implementer may write:

- approved code files
- approved tests
- approved examples
- docs required by the approved implementation
- its own packet under `docs/workflow/roles/implementer/reports/<milestone>/packet-vNNN/`

The Implementer must not write outside approved scope, change release claims, or change license without explicit user confirmation.

## Test Evaluator Read Scope

The Test Evaluator may read:

- Implementer packet
- Product / PRD acceptance criteria
- Architect test strategy
- relevant code and tests
- test output

The Test Evaluator may run tests when the user allows the cost and scope.

## Test Evaluator Write Scope

The Test Evaluator writes only under:

```text
docs/workflow/roles/test-evaluator/reports/<milestone>/packet-vNNN/
```

The Test Evaluator must not modify code or tests unless explicitly reassigned as Implementer for a new packet.

## Reviewer Read Scope

The Reviewer may read:

- all packet manifests in the selected chain
- packet documents listed by those manifests
- git status and diffs when needed
- relevant test output
- relevant source files only to verify review findings

## Reviewer Write Scope

The Reviewer writes only under:

```text
docs/workflow/roles/reviewer/reports/<milestone>/packet-vNNN/
```

The Reviewer must not implement fixes, modify tests, change packet history, or approve unresolved P0.

## External Sources

Public-source network research is allowed by default when relevant to the milestone. Each role must declare planned network purpose and source types in its first response, and must record external sources in its packet.

Downloads, execution of remote content, authenticated/private resources, provider APIs, or sending secrets/project-private data externally require separate explicit user approval for that exact action.
