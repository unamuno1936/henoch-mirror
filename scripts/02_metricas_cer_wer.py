#!/usr/bin/env python3
"""02_metricas_cer_wer.py — CER y WER contra ground truth."""
import argparse
import csv
import re
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
GT_DIR = BASE / "ground_truth"
DATA_DIR = BASE / "datos"
OUT_DIR = BASE / "resultados"
OUT_CSV = OUT_DIR / "metricas_cer_wer.csv"


def normalizar_geez(texto: str) -> str:
    texto = re.sub(r"[\u1361-\u1368]", "", texto)
    return re.sub(r"\s+", "", texto)


def levenshtein(a: str, b: str) -> int:
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
    r = normalizar_geez(ref)
    h = normalizar_geez(hyp)
    if not r:
        return float("nan")
    return levenshtein(r, h) / len(r)


def wer(ref: str, hyp: str) -> float:
    r = ref.split()
    h = hyp.split()
    if not r:
        return float("nan")
    m, n = len(r), len(h)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if r[i - 1] == h[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[m][n] / m


def parsear_nombre(nombre: str) -> dict:
    stem = nombre.replace(".txt", "")
    partes = stem.split("_")
    if len(partes) < 4:
        return {"modelo": "?", "prompt": "?", "pagina": "?", "run": "?"}
    return {
        "modelo": partes[0],
        "prompt": "_".join(partes[1:-2]),
        "pagina": partes[-2],
        "run": partes[-1],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", type=Path)
    ap.add_argument("--hyp", type=Path)
    ap.add_argument("--batch", action="store_true")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    filas = []

    if args.batch:
        for hyp_path in sorted(DATA_DIR.glob("*.txt")):
            meta = parsear_nombre(hyp_path.name)
            ref_path = GT_DIR / f"{meta['pagina']}.txt"
            if not ref_path.exists():
                print(f"SKIP: sin GT para {meta['pagina']}", file=sys.stderr)
                continue
            ref = ref_path.read_text(encoding="utf-8")
            hyp = hyp_path.read_text(encoding="utf-8")
            filas.append({
                **meta, "archivo": hyp_path.name,
                "cer": round(cer(ref, hyp), 4),
                "wer": round(wer(ref, hyp), 4),
                "len_ref_chars": len(normalizar_geez(ref)),
                "len_hyp_chars": len(normalizar_geez(hyp)),
            })
    else:
        if not (args.ref and args.hyp):
            print("Uso: --ref <gt> --hyp <out> | --batch", file=sys.stderr)
            sys.exit(1)
        ref = args.ref.read_text(encoding="utf-8")
        hyp = args.hyp.read_text(encoding="utf-8")
        filas.append({
            "archivo": args.hyp.name, **parsear_nombre(args.hyp.name),
            "cer": round(cer(ref, hyp), 4),
            "wer": round(wer(ref, hyp), 4),
            "len_ref_chars": len(normalizar_geez(ref)),
            "len_hyp_chars": len(normalizar_geez(hyp)),
        })

    if not filas:
        print("Sin datos.", file=sys.stderr)
        sys.exit(1)

    campos = ["archivo", "modelo", "prompt", "pagina", "run",
              "cer", "wer", "len_ref_chars", "len_hyp_chars"]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for fila in filas:
            w.writerow(fila)

    print(f"Escrito: {OUT_CSV}")
    print(f"Filas:   {len(filas)}")


if __name__ == "__main__":
    main()
