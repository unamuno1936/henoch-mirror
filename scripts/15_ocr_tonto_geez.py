#!/usr/bin/env python3
"""
15_ocr_tonto_geez.py — OCR "tonto" para extracción cruda de caracteres etíopes.
Usa Tesseract con el modelo de script etíope (tesseract-ocr-script-ethi).

Objetivo:
    Producir una línea base de "lectura de trazos" SIN conocimiento del
    contenido. Este script no sabe nada de Enoc, Knibb, Charles ni ge'ez
    académico. Solo extrae lo que Tesseract "ve" en la imagen.

Uso:
    python3 15_ocr_tonto_geez.py --imagen imagenes/folio_7v.png
    python3 15_ocr_tonto_geez.py --carpeta imagenes/ --patron "folio_*.png"

Salida:
    - datos/ocr_tonto_<folio>.txt      (texto extraído, crudo)
    - datos/ocr_tonto_<folio>.json     (metadatos: timestamp, hash imagen,
                                        confianza media, tiempo)

Requiere:
    sudo apt install tesseract-ocr tesseract-ocr-script-ethi
    pip install pytesseract pillow
"""

import argparse
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import pytesseract
    from PIL import Image
except ImportError:
    print("ERROR: faltan dependencias.", file=sys.stderr)
    print("Ejecuta: pip install pytesseract pillow", file=sys.stderr)
    sys.exit(1)


BASE = Path("/media/joblak/41112ade-da41-4393-a9fb-53dc958b2f9e/multimedia/herramientas_extraccion/protocolos_investigacion/henoch")
DATOS = BASE / "datos"
DATOS.mkdir(exist_ok=True)


def hash_archivo(ruta: Path) -> str:
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def extraer_geez(ruta_imagen: Path) -> dict:
    t0 = time.time()
    ts = datetime.now(timezone.utc).isoformat()

    img = Image.open(ruta_imagen)

    # Forzar el idioma de script etíope.
    # El nombre exacto del modelo es "script/Ethiopic" según Tesseract.
    config = "--psm 6"
    texto = pytesseract.image_to_string(img, lang="script/Ethiopic", config=config)

    tiempo = time.time() - t0

    return {
        "imagen": str(ruta_imagen),
        "imagen_sha256": hash_archivo(ruta_imagen),
        "timestamp_utc": ts,
        "modelo_ocr": "tesseract-script-Ethiopic",
        "n_caracteres": len(texto.strip()),
        "tiempo_segundos": round(tiempo, 2),
        "texto": texto.strip(),
    }


def procesar_una(ruta: Path):
    nombre = ruta.stem
    salida_txt = DATOS / f"ocr_tonto_{nombre}.txt"
    salida_json = DATOS / f"ocr_tonto_{nombre}.json"

    print(f"[OCR] Procesando: {ruta.name}")
    try:
        resultado = extraer_geez(ruta)
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return

    salida_txt.write_text(resultado["texto"], encoding="utf-8")
    meta = {k: v for k, v in resultado.items() if k != "texto"}
    salida_json.write_text(json.dumps(meta, ensure_ascii=False, indent=2),
                           encoding="utf-8")

    print(f"  Caracteres: {resultado['n_caracteres']}")
    print(f"  Tiempo:     {resultado['tiempo_segundos']}s")
    print(f"  Texto → {salida_txt}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--imagen", type=Path, default=None)
    ap.add_argument("--carpeta", type=Path, default=None)
    ap.add_argument("--patron", type=str, default="folio_*.png")
    args = ap.parse_args()

    if not args.imagen and not args.carpeta:
        ap.error("Indica --imagen o --carpeta.")

    imagenes = []
    if args.imagen:
        imagenes.append(args.imagen)
    if args.carpeta:
        imagenes.extend(sorted(args.carpeta.glob(args.patron)))

    for ruta in imagenes:
        if not ruta.exists():
            print(f"ERROR: no existe {ruta}", file=sys.stderr)
            continue
        procesar_una(ruta)


if __name__ == "__main__":
    main()
