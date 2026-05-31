# Architect Reports

Architect report packets are stored here.

Expected layout:

```text
reports/
  <milestone>/
    latest.json
    packet-v001/
      handoff.manifest.json
      architecture-plan.md
      boundary-map.md
      interface-contracts.md
      data-flow.md
      test-strategy.md
      risk-register.md
```

Rules:

- Read upstream Product / PRD manifest first.
- Lock exact upstream packet versions in `input_packets`.
- Create a new packet version for material changes.
- Do not edit a packet after `ready_for_next_role`.

