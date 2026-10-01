#!/usr/bin/env python3
"""Prueba distintas variantes de calidad IIIF en Gallica."""
import requests
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
IMG = BASE / "imagenes/iiif_muestra"
IMG.mkdir(parents=True, exist_ok=True)

ARK = "ark:/12148/btv1b108488806"
PAG = 19
HEADERS = {"User-Agent": "Jacobea-Henoch-Study/0.1"}

variantes = [
    ("native_jpg",     f"https://gallica.bnf.fr/iiif/{ARK}/f{PAG}/full/full/0/native.jpg"),
    ("native_png",     f"https://gallica.bnf.fr/iiif/{ARK}/f{PAG}/full/full/0/native.png"),
    ("default_jpg",    f"https://gallica.bnf.fr/iiif/{ARK}/f{PAG}/full/full/0/default.jpg"),
    ("color_jpg",      f"https://gallica.bnf.fr/iiif/{ARK}/f{PAG}/full/full/0/color.jpg"),
    ("gray_jpg",       f"https://gallica.bnf.fr/iiif/{ARK}/f{PAG}/full/full/0/gray.jpg"),
    ("bitonal_png",    f"https://gallica.bnf.fr/iiif/{ARK}/f{PAG}/full/full/0/bitonal.png"),
]

for nombre, url in variantes:
    try:
        r = requests.get(url, headers=HEADERS, timeout=180, stream=True)
        if r.status_code == 200:
            out = IMG / f"f{PAG}_{nombre}"
            ext = ".png" if "png" in nombre else ".jpg"
            out = out.with_suffix(ext)
            with out.open("wb") as f:
                for chunk in r.iter_content(65536):
                    f.write(chunk)
            size = out.stat().st_size / 1024
            print(f"OK  {nombre:15s} {size:>10.1f} KB  →  {out.name}")
        else:
            print(f"KO  {nombre:15s} status {r.status_code}")
    except Exception as e:
        print(f"ERR {nombre:15s} {e}")
