#!/usr/bin/env python3
"""05_verificar_hashes.py — Verifica integridad contra hashes registrados."""

import hashlib
import json
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
MANIFEST = BASE / "hashes/manifest.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not MANIFEST.exists():
        print(f"ERROR: falta {MANIFEST}. Corre 00_generar_hashes.py primero.",
              file=sys.stderr)
        sys.exit(1)

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ok, cambiados, faltantes = 0, 0, 0

    print(f"Verificando hashes del {manifest['timestamp']}")
    print("=" * 70)

    for rel, digest_reg in manifest["archivos"].items():
        p = BASE / rel
        if not p.exists():
            print(f"FALTANTE  {rel}")
            faltantes += 1
            continue
        actual = sha256(p)
        if actual == digest_reg:
            ok += 1
        else:
            print(f"CAMBIADO  {rel}")
            print(f"  registrado: {digest_reg}")
            print(f"  actual:     {actual}")
            cambiados += 1

    for d, contenidos in manifest["directorios"].items():
        for rel, digest_reg in contenidos.items():
            p = BASE / rel
            if not p.exists():
                print(f"FALTANTE  {rel}")
                faltantes += 1
                continue
            actual = sha256(p)
            if actual == digest_reg:
                ok += 1
            else:
                print(f"CAMBIADO  {rel}")
                cambiados += 1

    print("=" * 70)
    print(f"OK: {ok} | CAMBIADOS: {cambiados} | FALTANTES: {faltantes}")
    sys.exit(0 if (cambiados == 0 and faltantes == 0) else 1)


if __name__ == "__main__":
    main()
