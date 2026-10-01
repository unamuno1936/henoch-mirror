#!/usr/bin/env python3
"""
07_probar_iiif.py — Prueba el acceso IIIF de Gallica para el BnF Éthiopien 49.

Objetivo:
    1. Descargar el manifest IIIF.
    2. Listar las páginas y sus dimensiones disponibles.
    3. Intentar descargar UNA página a máxima resolución como prueba.

Uso:
    python3 07_probar_iiif.py --pagina 19
    python3 07_probar_iiif.py --manifest

Salida:
    imagenes/iiif_test_f19.jpg  (si la descarga funciona)
    imagenes/iiif_manifest.json (si se obtiene el manifest)
    stdout: reporte detallado de lo que el servidor ofrece.
"""

import argparse
import json
import sys
from pathlib import Path

import requests


BASE = Path(__file__).resolve().parent.parent
IMG_DIR = BASE / "imagenes"
IMG_DIR.mkdir(exist_ok=True)

ARK = "ark:/12148/btv1b108488806"
MANIFEST_URL = f"https://gallica.bnf.fr/iiif/{ARK}/manifest.json"
IIIF_BASE = f"https://gallica.bnf.fr/iiif/{ARK}"

HEADERS = {
    "User-Agent": "Jacobea-Henoch-Study/0.1 (research; contact: marco.juridico2026@gmail.com)",
    "Accept": "application/json,image/jpeg,*/*",
}


def intentar_manifest():
    print(f"Intentando manifest: {MANIFEST_URL}")
    try:
        r = requests.get(MANIFEST_URL, headers=HEADERS, timeout=60)
        r.raise_for_status()
        data = r.json()

        out = IMG_DIR / "iiif_manifest.json"
        out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

        print(f"OK manifest descargado: {out}")
        print(f"  @id: {data.get('@id', '?')}")
        print(f"  label: {data.get('label', '?')}")

        # Extraer info de las secuencias
        seqs = data.get("sequences", [])
        if seqs:
            canvases = seqs[0].get("canvases", [])
            print(f"  total canvases: {len(canvases)}")
            for i, c in enumerate(canvases[:5]):
                label = c.get("label", "?")
                imgs = c.get("images", [])
                if imgs:
                    res = imgs[0].get("resource", {})
                    w = res.get("width", "?")
                    h = res.get("height", "?")
                    print(f"    canvas {i}: {label} → {w}x{h}")

        return data
    except Exception as e:
        print(f"FALLO manifest: {e}", file=sys.stderr)
        return None


def intentar_imagen(num_pagina: int):
    """
    Gallica IIIF típicamente acepta:
      /iiif/{ark}/{page}/full/full/0/native.jpg        (tamaño original)
      /iiif/{ark}/{page}/full/max/0/native.jpg         (máximo)
      /iiif/{ark}/{page}/full/!2000,2000/0/native.jpg  (forzado a 2000px)

    El "page" en Gallica es el número secuencial de la imagen (f1, f2...),
    no el número de folio. En este manuscrito, f19 corresponde a la página 19
    del contenedor digital, que suele coincidir con 3r si las 4 primeras
    páginas (1r, 1v, 2r, 2v) están en blanco.
    """
    intentos = [
        ("full", f"{IIIF_BASE}/f{num_pagina}/full/full/0/native.jpg"),
        ("max", f"{IIIF_BASE}/f{num_pagina}/full/max/0/native.jpg"),
        ("forzado_4000", f"{IIIF_BASE}/f{num_pagina}/full/!4000,4000/0/native.jpg"),
        ("forzado_2000", f"{IIIF_BASE}/f{num_pagina}/full/!2000,2000/0/native.jpg"),
    ]

    for nombre, url in intentos:
        print(f"  Probando {nombre}: {url}")
        try:
            r = requests.get(url, headers=HEADERS, timeout=120, stream=True)
            if r.status_code == 200:
                out = IMG_DIR / f"iiif_test_f{num_pagina}_{nombre}.jpg"
                with out.open("wb") as f:
                    for chunk in r.iter_content(chunk_size=65536):
                        f.write(chunk)
                size = out.stat().st_size
                print(f"    OK: {out} ({size / 1024:.1f} KB)")
                return out
            else:
                print(f"    status {r.status_code}")
        except Exception as e:
            print(f"    error: {e}")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pagina", type=int, default=19,
                    help="Número secuencial de imagen en Gallica (f1, f2...)")
    ap.add_argument("--manifest", action="store_true",
                    help="Solo descargar el manifest, sin imagen")
    args = ap.parse_args()

    print("=" * 70)
    print("PRUEBA IIIF — BnF Éthiopien 49 (Gallica)")
    print("=" * 70)

    if args.manifest:
        intentar_manifest()
        return

    print("\n--- Manifest ---")
    intentar_manifest()

    print(f"\n--- Imagen f{args.pagina} ---")
    out = intentar_imagen(args.pagina)

    if out:
        from PIL import Image
        with Image.open(out) as im:
            print(f"\nDimensiones: {im.size[0]} x {im.size[1]} px")
            print(f"Modo: {im.mode}")
    else:
        print("\nFALLO: no se pudo obtener ninguna imagen.")
        print("Documentar como limitación. Usar imágenes manuales.")


if __name__ == "__main__":
    main()
