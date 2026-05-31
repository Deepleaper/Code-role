#!/usr/bin/env python3
"""Local validator for document workflow packets.

This tool is intentionally small and local-only. It validates packet structure
and basic consumption rules without touching runtime code, network, or provider
APIs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


REQUIRED_MANIFEST_FIELDS = {
    "schema_version",
    "role",
    "milestone",
    "packet_version",
    "status",
    "created_at",
    "updated_at",
    "summary",
    "documents",
    "input_packets",
    "source_scopes",
    "handoff_to",
    "open_questions",
    "blocked",
    "required_confirmations",
}

VALID_PACKET_STATUSES = {"draft", "blocked", "ready_for_next_role", "superseded"}


class ValidationError(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid json: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"json root must be object: {path}")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_manifest(packet_dir: Path) -> dict[str, Any]:
    manifest_path = packet_dir / "handoff.manifest.json"
    if not manifest_path.exists():
        raise ValidationError(f"missing handoff.manifest.json: {packet_dir}")

    manifest = load_json(manifest_path)
    missing = sorted(REQUIRED_MANIFEST_FIELDS - set(manifest))
    if missing:
        raise ValidationError(f"manifest missing required fields: {', '.join(missing)}")

    status = manifest["status"]
    if status not in VALID_PACKET_STATUSES:
        raise ValidationError(f"invalid packet status: {status}")

    documents = manifest["documents"]
    if not isinstance(documents, list):
        raise ValidationError("manifest documents must be a list")

    for doc in documents:
        if not isinstance(doc, dict) or "path" not in doc:
            raise ValidationError("each document must be an object with path")
        doc_path = Path(doc["path"])
        if doc_path.is_absolute() or ".." in doc_path.parts:
            raise ValidationError(f"document path must be packet-relative: {doc['path']}")
        full_path = packet_dir / doc_path
        if doc.get("required", True) and not full_path.exists():
            raise ValidationError(f"required document missing: {doc['path']}")

    return manifest


def validate_consumable(manifest: dict[str, Any], allow_draft: bool) -> None:
    status = manifest["status"]
    if status == "ready_for_next_role":
        return
    if status == "draft" and allow_draft:
        return
    raise ValidationError(
        "packet is not consumable: status must be ready_for_next_role "
        "unless --allow-draft is explicitly set"
    )


def build_lock(packet_dir: Path) -> dict[str, Any]:
    manifest = validate_manifest(packet_dir)
    files = []
    for path in sorted(packet_dir.iterdir()):
        if path.is_file() and path.name != "packet.lock.json":
            files.append(
                {
                    "path": path.name,
                    "sha256": sha256_file(path),
                }
            )
    return {
        "schema_version": "0.1",
        "role": manifest["role"],
        "milestone": manifest["milestone"],
        "packet_version": manifest["packet_version"],
        "status": manifest["status"],
        "files": files,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a local workflow packet.")
    parser.add_argument("packet_dir", type=Path)
    parser.add_argument("--for-consumption", action="store_true")
    parser.add_argument("--allow-draft", action="store_true")
    parser.add_argument("--print-lock", action="store_true")
    args = parser.parse_args()

    try:
        manifest = validate_manifest(args.packet_dir)
        if args.for_consumption:
            validate_consumable(manifest, args.allow_draft)
        if args.print_lock:
            print(json.dumps(build_lock(args.packet_dir), indent=2, sort_keys=True))
        else:
            print(
                json.dumps(
                    {
                        "ok": True,
                        "role": manifest["role"],
                        "milestone": manifest["milestone"],
                        "packet_version": manifest["packet_version"],
                        "status": manifest["status"],
                    },
                    indent=2,
                    sort_keys=True,
                )
            )
        return 0
    except ValidationError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2, sort_keys=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
