#!/usr/bin/env python3
"""00_generar_hashes.py — Hashes SHA-256 de todos los artefactos clave."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
HASHES_DIR = BASE / "hashes"

ARTEFACTOS = [
    "config/paginas_candidatas.txt",
    "config/paginas_seleccionadas.txt",
    "config/paginas_canvas_map.txt",
    "config/criterios_preregistrados.md",
    "config/plan_analisis_julia.md",
    "prompts/generico.txt",
    "prompts/wrapper_tlacuilo.txt",
    "resultados/metricas_cer_wer.csv",
    "resultados/alucinaciones.csv",
    "resultados/tasa_alucinacion.csv",
    "resultados/consistencia.csv",
]

DIRECTORIOS = ["ground_truth", "scripts", "datos", "imagenes"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    HASHES_DIR.mkdir(exist_ok=True)
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "archivos": {},
        "directorios": {},
    }
    lineas = [
        "# Hashes SHA-256",
        f"# Generado: {manifest['timestamp']}",
        "",
    ]

    for rel in ARTEFACTOS:
        p = BASE / rel
        if p.exists():
            digest = sha256(p)
            manifest["archivos"][rel] = digest
            lineas.append(f"{digest}  {rel}")

    for d in DIRECTORIOS:
        p = BASE / d
        if not p.exists():
            continue
        contenidos = {}
        for f in sorted(p.rglob("*")):
            if f.is_file() and not f.name.startswith("."):
                rel = str(f.relative_to(BASE))
                digest = sha256(f)
                contenidos[rel] = digest
                lineas.append(f"{digest}  {rel}")
        manifest["directorios"][d] = contenidos

    (HASHES_DIR / "hashes.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    (HASHES_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    total = len(manifest["archivos"]) + sum(len(v) for v in manifest["directorios"].values())
    print(f"Escrito: {HASHES_DIR / 'hashes.txt'}")
    print(f"Escrito: {HASHES_DIR / 'manifest.json'}")
    print(f"Total archivos hasheados: {total}")


if __name__ == "__main__":
    main()
