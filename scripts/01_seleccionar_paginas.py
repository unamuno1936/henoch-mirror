#!/usr/bin/env python3
"""01_seleccionar_paginas.py — Selección aleatoria reproducible."""
import argparse
import random
import sys
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
CONFIG = BASE / "config"
ENTRADA = CONFIG / "paginas_candidatas.txt"
SALIDA = CONFIG / "paginas_seleccionadas.txt"


def cargar_paginas(path: Path) -> list:
    paginas = []
    for linea in path.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#"):
            continue
        paginas.append(linea)
    return paginas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--seed", type=int, default=20260926)
    args = ap.parse_args()

    if not ENTRADA.exists():
        print(f"ERROR: no existe {ENTRADA}", file=sys.stderr)
        sys.exit(1)

    paginas = cargar_paginas(ENTRADA)
    if len(paginas) < args.n:
        print(f"ERROR: solo {len(paginas)} páginas, se piden {args.n}.", file=sys.stderr)
        sys.exit(1)

    random.seed(args.seed)
    seleccion = random.sample(paginas, args.n)
    ts = datetime.now(timezone.utc).isoformat()

    SALIDA.write_text("\n".join(seleccion) + "\n", encoding="utf-8")

    print("=" * 60)
    print("Selección de páginas")
    print("=" * 60)
    print(f"Total candidatas: {len(paginas)}")
    print(f"Solicitadas:      {args.n}")
    print(f"Semilla:          {args.seed}")
    print(f"Timestamp:        {ts}")
    print(f"Archivo:          {SALIDA}")
    print("-" * 60)
    for i, p in enumerate(seleccion, 1):
        print(f"  {i}. {p}")
    print("=" * 60)


if __name__ == "__main__":
    main()
