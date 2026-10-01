#!/usr/bin/env python3
"""03_alucinaciones.py — Registro manual + cálculo de tasa H."""
import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "datos"
OUT_DIR = BASE / "resultados"
ALU_CSV = OUT_DIR / "alucinaciones.csv"
TASA_CSV = OUT_DIR / "tasa_alucinacion.csv"

CAMPOS = ["archivo", "modelo", "prompt", "pagina", "run",
          "H1", "H2", "H3", "H4", "notas"]


def init_plantilla():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with ALU_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for archivo in sorted(DATA_DIR.glob("*.txt")):
            partes = archivo.stem.split("_")
            w.writerow({
                "archivo": archivo.name,
                "modelo": partes[0] if partes else "?",
                "prompt": "_".join(partes[1:-2]) if len(partes) >= 4 else "?",
                "pagina": partes[-2] if len(partes) >= 4 else "?",
                "run": partes[-1] if len(partes) >= 4 else "?",
                "H1": 0, "H2": 0, "H3": 0, "H4": 0, "notas": "",
            })
    print(f"Plantilla: {ALU_CSV}")
    print("Edita el CSV marcando 1 donde aplique cada categoría.")


def compute():
    if not ALU_CSV.exists():
        print(f"ERROR: falta {ALU_CSV}. Corre --init.", file=sys.stderr)
        sys.exit(1)

    filas = []
    with ALU_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            tiene_h = any(int(row[c]) > 0 for c in ("H1", "H2", "H3", "H4"))
            filas.append({**row, "tiene_alucinacion": int(tiene_h)})

    total = len(filas)
    con_alucinacion = sum(r["tiene_alucinacion"] for r in filas)
    tasa = con_alucinacion / total if total else float("nan")

    print(f"Total:               {total}")
    print(f"Con al menos una H:  {con_alucinacion}")
    print(f"Tasa H global:       {tasa:.4f}")

    grupos = defaultdict(lambda: {"total": 0, "con": 0})
    for r in filas:
        key = (r["modelo"], r["prompt"])
        grupos[key]["total"] += 1
        grupos[key]["con"] += r["tiene_alucinacion"]

    with TASA_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["modelo", "prompt", "total", "con_alucinacion", "tasa"])
        for (m, p), d in sorted(grupos.items()):
            t = d["con"] / d["total"] if d["total"] else float("nan")
            w.writerow([m, p, d["total"], d["con"], round(t, 4)])
            print(f"  {m:20s} {p:20s} {d['con']}/{d['total']} = {t:.4f}")

    print(f"Escrito: {TASA_CSV}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--compute", action="store_true")
    args = ap.parse_args()
    if args.init:
        init_plantilla()
    elif args.compute:
        compute()
    else:
        print("Uso: --init | --compute", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
