# Product / PRD Reports

Product / PRD report packets are stored here.

Expected layout:

```text
reports/
  <milestone>/
    latest.json
    packet-v001/
      handoff.manifest.json
      product-brief.md
      prd.md
      acceptance-criteria.md
      non-goals.md
      decision-log.md
```

Rules:

- Read the upstream Researcher `handoff.manifest.json` before writing.
- Record the exact upstream packet version in `input_packets`.
- Create a new packet version for material changes.
- Do not edit a packet after it is marked `ready_for_next_role`.
- Update `latest.json` only as a pointer.

