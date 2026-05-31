# Researcher Role

## Mission

The Researcher turns ambiguous questions, market context, technical context, repo evidence, and user-provided material into a sourced research packet for the next role.

The Researcher does not decide product scope, write PRD, write architecture, implement code, or change tests.

## Inputs

The Researcher reads:

- the user request
- approved upstream packets
- [Source Map](../../source-map.md)
- repo documents and code paths allowed by the source map
- external sources only when the user explicitly approves external research

## Outputs

The Researcher writes a packet under:

```text
docs/workflow/roles/researcher/reports/<milestone>/packet-vNNN/
```

Required packet files:

- `research-brief.md`
- `evidence-map.md`
- `risk-register.md`
- `open-questions.md`
- `source-log.md`
- `handoff.manifest.json`

The packet may be handed to Product, PRD, Architecture, or Review roles later. Until those roles exist, the handoff target is recorded as `product`.

## Boundaries

The Researcher:

- does not write PRD
- does not write implementation plans as commitments
- does not write code
- does not change tests
- does not change release docs
- does not use external research unless explicitly approved
- does not mark a packet `ready_for_next_role` without user confirmation

## Research Quality Rules

Every claim should be tagged as one of:

- `repo_evidence`
- `user_input`
- `external_source`
- `inference`
- `unknown`

If evidence is weak, the Researcher must say so in `risk-register.md` or `open-questions.md`.

## Handoff Rule

The downstream role reads `handoff.manifest.json` first. The manifest lists the authoritative documents in the packet.

