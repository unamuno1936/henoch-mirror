#!/usr/bin/env python3
"""07_descargar_iiif.py — Descarga páginas del BnF Éthiopien 49 vía IIIF.

IMPORTANTE: Lee y respeta los términos de uso de Gallica/BnF.
Este script es para uso de investigación. No redistribuir comercialmente.
"""
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: falta requests. Corre pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)


BASE = Path(__file__).resolve().parent.parent
IMG_DIR = BASE / "imagenes"
IMG_DIR.mkdir(parents=True, exist_ok=True)

# BnF Éthiopien 49 — ARK identifier (VERIFICAR EN GALLICA antes de correr)
ARK = "ark:/12148/btv1bXXXXXXX"

# Patrón IIIF: https://gallica.bnf.fr/iiif/{ARK}/f{N}/full/full/0/native.jpg
IIIF_TEMPLATE = "https://gallica.bnf.fr/iiif/{ark}/f{n}/full/full/0/native.jpg"


def descargar(pagina: str, salida: Path) -> bool:
    """
    pagina: '3r' o '3v' etc. Se convierte a número de folio entero.
    Para 3r -> f3, 3v -> f3 (mismo folio, diferente cara).
    Gallica usa numeración secuencial de imágenes: f1, f2, f3, ...
    """
    # Convertir 3r/3v a número de imagen secuencial aproximado.
    # Ajustar según la secuencia real del manuscrito en Gallica.
    folio = int(pagina[:-1])
    cara = pagina[-1]
    n = folio * 2 - (1 if cara == "r" else 0)
    # Ajuste: si el manuscrito empieza en f1 = 1r, la fórmula es n = (folio-1)*2 + 1
    # para recto, y n = (folio-1)*2 + 2 para verso.
    # MODIFICAR según verificación.

    url = IIIF_TEMPLATE.format(ark=ARK, n=n)
    print(f"  {pagina}: {url}")
    r = requests.get(url, timeout=120, headers={"User-Agent": "Jacobea-Research/1.0"})
    if r.status_code != 200:
        print(f"    HTTP {r.status_code}", file=sys.stderr)
        return False
    salida.write_bytes(r.content)
    print(f"    OK: {len(r.content)} bytes -> {salida}")
    return True


def main():
    sel = BASE / "config" / "paginas_seleccionadas.txt"
    if not sel.exists():
        print(f"ERROR: falta {sel}. Corre 01 primero.", file=sys.stderr)
        sys.exit(1)

    paginas = [l.strip() for l in sel.read_text().splitlines() if l.strip()]
    print(f"Descargando {len(paginas)} páginas...")
    for p in paginas:
        salida = IMG_DIR / f"{p}.jpg"
        if salida.exists():
            print(f"  {p}: ya existe, skip.")
            continue
        ok = descargar(p, salida)
        time.sleep(1)  # Rate limit amable con Gallica

    print("Descarga completa.")


if __name__ == "__main__":
    main()
