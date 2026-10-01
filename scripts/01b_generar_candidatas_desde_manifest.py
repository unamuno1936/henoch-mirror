#!/usr/bin/env python3
"""
01b_generar_candidatas_desde_manifest.py

Extrae del manifest IIIF las páginas válidas (cuerpo de 1 Enoc) y
genera config/paginas_candidatas.txt con la nomenclatura folio (3r, 3v...).

Reglas de exclusión:
  - Portadas, guardas, cortes, lomo, contracubierta (labels no-folio)
  - Folios 1r-2v (en blanco, según nota del manuscrito)
  - Folios 59r-62v (transposición conocida)
"""

import json
import re
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
MANIFEST = BASE / "imagenes/iiif_manifest.json"
SALIDA = BASE / "config/paginas_candidatas.txt"
SALIDA_CANVAS = BASE / "config/paginas_canvas_map.txt"

# Regex para label tipo "3r", "63v", "1r", etc. (folio con recto/verso)
RE_FOLIO = re.compile(r"^(\d{1,3})([rv])$")

# Folios a excluir por reglas conocidas del manuscrito
EXCLUIR_FOLIOS = set()
for n in (1, 2):
    EXCLUIR_FOLIOS.add(f"{n}r")
    EXCLUIR_FOLIOS.add(f"{n}v")
for n in (59, 60, 61, 62):
    EXCLUIR_FOLIOS.add(f"{n}r")
    EXCLUIR_FOLIOS.add(f"{n}v")


def main():
    if not MANIFEST.exists():
        print(f"ERROR: falta {MANIFEST}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    canvases = data["sequences"][0]["canvases"]

    validas = []
    canvas_map = []  # (folio, canvas_id, indice_iiif)
    excluidas = []

    for idx, c in enumerate(canvases):
        label = c.get("label", "").strip()
        m = RE_FOLIO.match(label)
        if not m:
            continue
        folio = label
        # El índice IIIF es f{idx+1} porque f1 es el primer canvas
        iiif_index = idx + 1

        if folio in EXCLUIR_FOLIOS:
            excluidas.append((folio, iiif_index, c.get("width"), c.get("height")))
            continue

        validas.append(folio)
        canvas_map.append((folio, iiif_index, c.get("width"), c.get("height")))

    # Escribir candidatas
    SALIDA.write_text("\n".join(validas) + "\n", encoding="utf-8")

    # Escribir mapa folio → canvas IIIF
    lineas_mapa = ["# folio\tiiif_fN\tancho\talto"]
    for folio, idx, w, h in canvas_map:
        lineas_mapa.append(f"{folio}\tf{idx}\t{w}\t{h}")
    SALIDA_CANVAS.write_text("\n".join(lineas_mapa) + "\n", encoding="utf-8")

    print("=" * 70)
    print("EXTRACCIÓN DE PÁGINAS VÁLIDAS DEL MANIFEST IIIF")
    print("=" * 70)
    print(f"Total canvases en manifest: {len(canvases)}")
    print(f"Páginas con label de folio: {len(validas) + len(excluidas)}")
    print(f"  → válidas:    {len(validas)}")
    print(f"  → excluidas:  {len(excluidas)}")
    print()
    print("Páginas excluidas por regla:")
    for folio, idx, w, h in excluidas:
        print(f"  {folio:>5s}  (f{idx})  {w}x{h}")
    print()
    print(f"Escrito: {SALIDA}")
    print(f"Escrito: {SALIDA_CANVAS}")
    print()
    print("Primeras 5 válidas:", validas[:5])
    print("Últimas  5 válidas:", validas[-5:])


if __name__ == "__main__":
    main()
