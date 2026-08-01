# SOP Calibration / SOP 校准

- sop_followed_without_change: 0 | 1 [sop_calibration]
- changed_after_candidate: 0 | 1 [sop_calibration]
- user_approved_change: 0 | 1 | not_applicable [sop_calibration]
- new_sop_version_created: 0 | 1 | not_applicable [sop_calibration]
- affected_evidence_rerun: 0 | 1 | not_applicable [sop_calibration]
- calibration_pass: 0 | 1 [sop_calibration]
- failed_check_ids: none | <check ids>

If `changed_after_candidate=1`, calibration cannot pass until the user approves the change, a new SOP version exists, and all affected evidence is rerun.
