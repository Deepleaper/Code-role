# Researcher Reports

Researcher report packets are stored here.

Expected layout:

```text
reports/
  <milestone>/
    latest.json
    packet-v001/
      handoff.manifest.json
      research-brief.md
      evidence-map.md
      risk-register.md
      open-questions.md
      source-log.md
```

Rules:

- Create a new packet version for material changes.
- Do not edit a packet after it is marked `ready_for_next_role`.
- Update `latest.json` only as a pointer.
- Keep packet paths stable so downstream roles can lock exact versions.

