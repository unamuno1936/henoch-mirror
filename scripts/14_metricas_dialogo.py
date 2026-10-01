#!/usr/bin/env python3
"""
14_metricas_dialogo.py — Métricas simples sobre los diálogos de construcción.

Mide: longitud, TTR, entropía, densidad léxica.
Aplicable a exports de chats (formato texto plano, separador "---").

Uso:
    python3 14_metricas_dialogo.py --archivo consultas/dialogo.txt
"""

import argparse
import math
import re
from collections import Counter
from pathlib import Path


def ttr(texto: str) -> float:
    palabras = re.findall(r"\w+", texto.lower())
    if not palabras:
        return 0.0
    return len(set(palabras)) / len(palabras)


def entropia_shannon(texto: str) -> float:
    chars = list(texto)
    if not chars:
        return 0.0
    frec = Counter(chars)
    total = len(chars)
    return -sum((v / total) * math.log2(v / total) for v in frec.values())


def analizar(texto: str) -> dict:
    chars = len(texto)
    palabras = re.findall(r"\w+", texto)
    return {
        "caracteres": chars,
        "palabras": len(palabras),
        "longitud_media_palabra": round(sum(len(p) for p in palabras) / max(len(palabras), 1), 2),
        "ttr": round(ttr(texto), 4),
        "entropia_shannon": round(entropia_shannon(texto), 4),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archivo", type=Path, required=True)
    args = ap.parse_args()

    texto = args.archivo.read_text(encoding="utf-8")
    m = analizar(texto)
    print(f"Archivo: {args.archivo.name}")
    for k, v in m.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
