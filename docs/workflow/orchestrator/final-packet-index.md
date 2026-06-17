# Final Packet Index

This file records the current final packet for each role in the active milestone.

The Orchestrator owns this file. Reviewer uses it as the authoritative index for final-version milestone drift audit.

It is not a history log. If a role produces `packet-v002`, reports `role_completion_status=1`, and the user accepts it as the current final output for the milestone, update that role row to `packet-v002`.

## Current Milestone Anchor

| Field | Value |
| --- | --- |
| Milestone | TBD |
| Original business goal | TBD |
| Original delivery goal | TBD |
| Success criteria | TBD |
| Non-goals | TBD |
| Anchor source | user_input / orchestrator_state / packet_evidence / unknown |

## Final Role Outputs

| Role | Current final output | Status | Accepted for milestone audit | Notes |
| --- | --- | --- | --- | --- |
| workflow-orchestrator | workflow-state.md, milestone-registry.md, decision-log.md, final-packet-index.md, latest next-role handoff brief if available | initialized | yes | Orchestrator output is audited by Reviewer for milestone drift. |
| researcher | none | not_started | no | Update after user accepts Researcher final packet. |
| product-prd | none | not_started | no | Update after user accepts Product / PRD final packet. |
| architect | none | not_started | no | Update after user accepts Architect final packet. |
| code-context | none | not_started | no | Update after user accepts Code Context final packet. |
| implementer | none | not_started | no | Update after user accepts Implementer final packet. |
| test-evaluator | none | not_started | no | Update after user accepts Test Evaluator final packet. |
| reviewer | none | not_started | no | Reviewer fills current packet during final audit. |

## Update Rule

- Update this file only after `role_completion_status=1` and the user accepts a role output as the current final version for this milestone.
- Do not list every historical packet version here.
- Do not scan for newest files to infer final versions.
- If a role output is revised, point the role row to the new accepted packet.
- If a role is skipped by chain type, set status to `not_applicable` and explain why in Notes.

## Reviewer Use

Reviewer reads this file before `milestone-drift-audit.md`.

Reviewer audits only the current final outputs listed here unless the user explicitly asks for historical audit.
