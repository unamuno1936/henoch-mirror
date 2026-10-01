#!/usr/bin/env python3
"""05_hashes.py — Snapshot SHA-256 de todos los artefactos del estudio."""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
LOGS = BASE / "logs"
LOGS.mkdir(parents=True, exist_ok=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def recolectar(base: Path, subdirs: list) -> dict:
    resultado = {}
    for sub in subdirs:
        d = base / sub
        if not d.exists():
            continue
        for f in sorted(d.rglob("*")):
            if f.is_file() and f.suffix in {".txt", ".md", ".csv", ".json", ".py", ".jpg", ".png", ".tif"}:
                rel = str(f.relative_to(base))
                resultado[rel] = {
                    "sha256": sha256(f),
                    "size": f.stat().st_size,
                    "mtime": datetime.fromtimestamp(f.stat().st_mtime, timezone.utc).isoformat(),
                }
    return resultado


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", required=True,
                    help="Nombre del snapshot: inicial, pre-ejecucion, final, etc.")
    args = ap.parse_args()

    subdirs = ["config", "scripts", "prompts", "ground_truth", "imagenes"]
    artefactos = recolectar(BASE, subdirs)

    ts = datetime.now(timezone.utc).isoformat()
    payload = {
        "snapshot": args.snapshot,
        "timestamp_utc": ts,
        "base": str(BASE),
        "n_artefactos": len(artefactos),
        "artefactos": artefactos,
    }

    out = LOGS / f"hashes_{args.snapshot}.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    print("=" * 60)
    print(f"Snapshot: {args.snapshot}")
    print(f"Timestamp UTC: {ts}")
    print(f"Artefactos hasheados: {len(artefactos)}")
    print(f"Archivo: {out}")
    print("=" * 60)
    for rel, meta in list(artefactos.items())[:20]:
        print(f"  {meta['sha256'][:16]}...  {rel}")
    if len(artefactos) > 20:
        print(f"  ... ({len(artefactos) - 20} más)")


if __name__ == "__main__":
    main()
