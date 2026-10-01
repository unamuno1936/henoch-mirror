#!/usr/bin/env python3
"""
08_evaluar_imagenes.py — Evalúa resolución, nitidez y consistencia
de las imágenes manuales extraídas por Marco.

Uso:
    python3 08_evaluar_imagenes.py --dir /ruta/a/imagenes
    python3 08_evaluar_imagenes.py --dir /ruta/a/imagenes --csv resultados/calidad_imagenes.csv

Métricas por imagen:
    - Ancho, alto, megapíxeles
    - Relación de aspecto
    - Formato, modo de color
    - Peso en disco
    - Nitidez (varianza del Laplaciano)
    - Fracción de píxeles casi-blancos (para estimar recorte)
"""

import argparse
import csv
import statistics
import sys
from pathlib import Path

from PIL import Image, ImageFilter


def varianza_laplaciano(im: Image.Image) -> float:
    """Proxy de nitidez. Mayor = más nítida."""
    gris = im.convert("L")
    lap = gris.filter(ImageFilter.Kernel(
        size=(3, 3),
        kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
        scale=1, offset=0,
    ))
    px = list(lap.getdata())
    media = sum(px) / len(px)
    var = sum((p - media) ** 2 for p in px) / len(px)
    return var


def fraccion_blancos(im: Image.Image, umbral: int = 200) -> float:
    """Fracción de píxeles casi blancos. Alto = imagen con mucho margen (posible recorte agresivo)."""
    gris = im.convert("L")
    px = list(gris.getdata())
    return sum(1 for p in px if p >= umbral) / len(px)


def analizar(path: Path) -> dict:
    with Image.open(path) as im:
        w, h = im.size
        return {
            "archivo": path.name,
            "ancho_px": w,
            "alto_px": h,
            "megapixeles": round((w * h) / 1_000_000, 2),
            "aspecto": round(w / h, 3) if h else 0,
            "formato": im.format or path.suffix.lstrip(".").upper(),
            "modo": im.mode,
            "peso_kb": round(path.stat().st_size / 1024, 1),
            "nitidez": round(varianza_laplaciano(im), 1),
            "frac_blancos": round(fraccion_blancos(im), 3),
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, type=Path)
    ap.add_argument("--csv", type=Path, default=None)
    args = ap.parse_args()

    if not args.dir.is_dir():
        print(f"ERROR: no es directorio: {args.dir}", file=sys.stderr)
        sys.exit(1)

    extensiones = {".png", ".jpg", ".jpeg", ".tif", ".tiff"}
    archivos = sorted(
        [f for f in args.dir.iterdir() if f.suffix.lower() in extensiones]
    )

    if not archivos:
        print(f"Sin imágenes en {args.dir}", file=sys.stderr)
        sys.exit(1)

    filas = []
    for f in archivos:
        try:
            filas.append(analizar(f))
        except Exception as e:
            print(f"ERROR en {f.name}: {e}", file=sys.stderr)

    if not filas:
        sys.exit(1)

    # Reporte
    print("=" * 100)
    print(f"ANÁLISIS DE IMÁGENES — {args.dir}")
    print("=" * 100)
    print(f"{'Archivo':20s} {'Ancho':>6s} {'Alto':>6s} {'MPx':>6s} "
          f"{'Aspecto':>8s} {'KB':>8s} {'Nitidez':>9s} {'%Blanc':>7s}")
    print("-" * 100)
    for r in filas:
        print(f"{r['archivo']:20s} {r['ancho_px']:>6d} {r['alto_px']:>6d} "
              f"{r['megapixeles']:>6.2f} {r['aspecto']:>8.3f} "
              f"{r['peso_kb']:>8.1f} {r['nitidez']:>9.1f} "
              f"{r['frac_blancos']:>7.3f}")

    # Estadísticas globales
    anchos = [r["ancho_px"] for r in filas]
    altos = [r["alto_px"] for r in filas]
    mpxs = [r["megapixeles"] for r in filas]
    nitideces = [r["nitidez"] for r in filas]
    blancos = [r["frac_blancos"] for r in filas]

    print("-" * 100)
    print(f"{'MEDIA':20s} {statistics.mean(anchos):>6.0f} "
          f"{statistics.mean(altos):>6.0f} {statistics.mean(mpxs):>6.2f} "
          f"{'':>8s} {'':>8s} {statistics.mean(nitideces):>9.1f} "
          f"{statistics.mean(blancos):>7.3f}")
    print(f"{'DESV':20s} {statistics.stdev(anchos) if len(anchos)>1 else 0:>6.0f} "
          f"{statistics.stdev(altos) if len(altos)>1 else 0:>6.0f} "
          f"{statistics.stdev(mpxs) if len(mpxs)>1 else 0:>6.2f} "
          f"{'':>8s} {'':>8s} "
          f"{statistics.stdev(nitideces) if len(nitideces)>1 else 0:>9.1f} "
          f"{statistics.stdev(blancos) if len(blancos)>1 else 0:>7.3f}")
    print("=" * 100)

    # Diagnóstico
    print("\nDIAGNÓSTICO:")
    coef_var_ancho = statistics.stdev(anchos) / statistics.mean(anchos) if len(anchos) > 1 else 0
    coef_var_alto = statistics.stdev(altos) / statistics.mean(altos) if len(altos) > 1 else 0
    if coef_var_ancho > 0.15 or coef_var_alto > 0.15:
        print("  ⚠  Alta variabilidad en dimensiones (CV > 15%).")
        print("     Las imágenes manuales no son homogéneas. Documentar.")
    else:
        print("  ✓  Dimensiones homogéneas (CV < 15%).")

    media_mpx = statistics.mean(mpxs)
    if media_mpx < 1.0:
        print(f"  ⚠  Resolución baja ({media_mpx:.2f} MPx medio).")
        print("     Probablemente insuficiente para HTR de detalle fino.")
    elif media_mpx < 4.0:
        print(f"  ~  Resolución media ({media_mpx:.2f} MPx).")
        print("     Suficiente para prueba, documentar como limitación.")
    else:
        print(f"  ✓  Resolución alta ({media_mpx:.2f} MPx medio).")

    media_blancos = statistics.mean(blancos)
    if media_blancos < 0.3:
        print(f"  ⚠  Poca zona blanca ({media_blancos:.1%}).")
        print("     Posible recorte agresivo. Verificar que no se cortó texto.")
    elif media_blancos > 0.7:
        print(f"  ~  Mucha zona blanca ({media_blancos:.1%}).")
        print("     Posible inclusión de márgenes amplios.")
    else:
        print(f"  ✓  Fracción de blancos razonable ({media_blancos:.1%}).")

    # CSV
    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
            w.writeheader()
            w.writerows(filas)
        print(f"\nCSV escrito: {args.csv}")


if __name__ == "__main__":
    main()
