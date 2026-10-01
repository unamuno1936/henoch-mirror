#!/usr/bin/env python3
"""04_consistencia.py — Consistencia entre las 3 corridas."""
import csv
import re
import statistics
from collections import defaultdict
from itertools import combinations
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
GT_DIR = BASE / "ground_truth"
DATA_DIR = BASE / "datos"
OUT_DIR = BASE / "resultados"
OUT_CSV = OUT_DIR / "consistencia.csv"


def normalizar(texto: str) -> str:
    texto = re.sub(r"[\u1361-\u1368]", "", texto)
    return re.sub(r"\s+", "", texto)


def lev(a: str, b: str) -> int:
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            curr.append(min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = curr
    return prev[-1]


def cer(ref: str, hyp: str) -> float:
    r = normalizar(ref)
    h = normalizar(hyp)
    return lev(r, h) / len(r) if r else float("nan")


def parsear(archivo: Path):
    partes = archivo.stem.split("_")
    if len(partes) < 4:
        return None
    return {
        "modelo": partes[0],
        "prompt": "_".join(partes[1:-2]),
        "pagina": partes[-2],
        "run": partes[-1],
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    grupos = defaultdict(list)
    for archivo in sorted(DATA_DIR.glob("*.txt")):
        meta = parsear(archivo)
        if meta:
            grupos[(meta["modelo"], meta["prompt"], meta["pagina"])].append(archivo)

    filas = []
    for (modelo, prompt, pagina), archivos in sorted(grupos.items()):
        gt = GT_DIR / f"{pagina}.txt"
        if not gt.exists():
            continue
        ref = gt.read_text(encoding="utf-8")
        textos = [a.read_text(encoding="utf-8") for a in archivos]
        cers = [cer(ref, t) for t in textos]
        if len(cers) < 2:
            continue

        media = statistics.mean(cers)
        desv = statistics.stdev(cers) if len(cers) > 1 else 0.0
        rango = max(cers) - min(cers)
        identicos = len(set(normalizar(t) for t in textos)) == 1

        if len(textos) > 1:
            distancias = [lev(normalizar(a), normalizar(b))
                          for a, b in combinations(textos, 2)]
            dist_media = statistics.mean(distancias)
        else:
            dist_media = 0

        filas.append({
            "modelo": modelo, "prompt": prompt, "pagina": pagina,
            "n_runs": len(cers),
            "cer_medio": round(media, 4),
            "cer_desv": round(desv, 4),
            "cer_rango": round(rango, 4),
            "dist_media_entre_runs": round(dist_media, 2),
            "identicos": int(identicos),
        })

    if not filas:
        print("Sin grupos completos.")
        return

    campos = list(filas[0].keys())
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)

    print(f"Escrito: {OUT_CSV}")
    print(f"Grupos:  {len(filas)}")
    print()
    print(f"{'Modelo':12s} {'Prompt':12s} {'Pag':5s} {'CERmed':>7s} {'Desv':>7s} {'Rango':>7s} {'Id':>3s}")
    print("-" * 60)
    for r in filas:
        print(f"{r['modelo']:12s} {r['prompt']:12s} {r['pagina']:5s} "
              f"{r['cer_medio']:>7.4f} {r['cer_desv']:>7.4f} "
              f"{r['cer_rango']:>7.4f} {r['identicos']:>3d}")


if __name__ == "__main__":
    main()
