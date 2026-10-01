#!/usr/bin/env python3
"""10_descargar_folios_png.py — Descarga folios seleccionados en PNG nativo."""

import argparse
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests


BASE = Path(__file__).resolve().parent.parent
CONFIG = BASE / "config"
IMAGENES = BASE / "imagenes"
LOGS = BASE / "logs"
IMAGENES.mkdir(exist_ok=True)
LOGS.mkdir(exist_ok=True)

ARK = "ark:/12148/btv1b108488806"
HEADERS = {
    "User-Agent": "Jacobea-Henoch-Study/0.1 (research; contact: marco.juridico2026@gmail.com)",
    "Accept": "image/png,image/jpeg,*/*",
}
PAUSA_SEG = 15


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def cargar_mapa() -> dict:
    mapa = {}
    path = CONFIG / "paginas_canvas_map.txt"
    for linea in path.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#"):
            continue
        partes = linea.split("\t")
        if len(partes) >= 2:
            mapa[partes[0]] = partes[1]
    return mapa


def descargar(folio: str, canvas: str, formato: str = "png") -> dict:
    ext = "png" if formato == "png" else "jpg"
    url = f"https://gallica.bnf.fr/iiif/{ARK}/{canvas}/full/full/0/native.{ext}"
    salida = IMAGENES / f"folio_{folio}.{ext}"

    ts = datetime.now(timezone.utc).isoformat()
    print(f"[{ts}] Descargando {folio} ({canvas}) → {salida.name}")

    r = requests.get(url, headers=HEADERS, timeout=300, stream=True)
    r.raise_for_status()

    with salida.open("wb") as f:
        for chunk in r.iter_content(chunk_size=65536):
            f.write(chunk)

    size = salida.stat().st_size
    digest = sha256(salida)

    resultado = {
        "folio": folio,
        "canvas": canvas,
        "formato": formato,
        "url": url,
        "timestamp": ts,
        "archivo": str(salida),
        "bytes": size,
        "mb": round(size / 1_048_576, 2),
        "sha256": digest,
    }
    print(f"  OK: {resultado['mb']} MB, SHA256: {digest[:16]}...")
    return resultado


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fallback-jpg", action="store_true",
                    help="Usar JPG si PNG falla")
    args = ap.parse_args()

    mapa = cargar_mapa()
    seleccion = (CONFIG / "paginas_seleccionadas.txt").read_text(
        encoding="utf-8").splitlines()
    seleccion = [s.strip() for s in seleccion if s.strip()]

    print("=" * 70)
    print("DESCARGA DE FOLIOS SELECCIONADOS — PNG NATIVO IIIF")
    print("=" * 70)
    print(f"Folios a descargar: {len(seleccion)}")
    print(f"Pausa entre descargas: {PAUSA_SEG}s")
    print()

    resultados = []
    for i, folio in enumerate(seleccion, 1):
        if folio not in mapa:
            print(f"ERROR: folio {folio} no está en el mapa")
            continue
        canvas = mapa[folio]

        try:
            res = descargar(folio, canvas, formato="png")
            resultados.append(res)
        except Exception as e:
            print(f"  FALLO PNG: {e}")
            if args.fallback_jpg:
                print(f"  Intentando fallback JPG...")
                try:
                    res = descargar(folio, canvas, formato="jpg")
                    resultados.append(res)
                except Exception as e2:
                    print(f"  FALLO JPG también: {e2}")
                    resultados.append({"folio": folio, "error": str(e2)})

        if i < len(seleccion):
            print(f"  Esperando {PAUSA_SEG}s...")
            time.sleep(PAUSA_SEG)

    log_path = LOGS / "descarga_iiif.json"
    log_path.write_text(
        json.dumps({
            "timestamp_inicio": resultados[0]["timestamp"] if resultados else None,
            "timestamp_fin": datetime.now(timezone.utc).isoformat(),
            "total": len(resultados),
            "exitosos": sum(1 for r in resultados if "sha256" in r),
            "resultados": resultados,
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print()
    print("=" * 70)
    print(f"Escrito: {log_path}")
    print(f"Exitosos: {sum(1 for r in resultados if 'sha256' in r)}/{len(resultados)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
