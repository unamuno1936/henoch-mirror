# Sesión 2026-09-27 — Selección y descarga de folios

## Hora de inicio
2026-09-27T01:31:27Z (timestamp registrado por el script)

## Objetivo
Fijar los 5 folios del estudio y descargar las imágenes en máxima calidad.

## Acciones ejecutadas

### 1. Extracción de páginas válidas del manifest IIIF
- Script: `01b_generar_candidatas_desde_manifest.py`
- Total canvases en manifest: 156
- Páginas con label de folio: 126
- Páginas válidas (cuerpo del manuscrito): 114
- Páginas excluidas: 12
  - 1r, 1v, 2r, 2v (en blanco)
  - 59r, 59v, 60r, 60v, 61r, 61v, 62r, 62v (transposición conocida)
- Archivos generados:
  - `config/paginas_candidatas.txt` (114 entradas)
  - `config/paginas_canvas_map.txt` (mapa folio → canvas IIIF)

### 2. Selección aleatoria reproducible
- Script: `01_seleccionar_paginas.py`
- Semilla: 20260926
- Timestamp UTC: 2026-09-27T01:31:27.061952+00:00
- Páginas seleccionadas:
  1. **7v**
  2. **5v**
  3. **4r**
  4. **40v**
  5. **17v**
- Archivo generado: `config/paginas_seleccionadas.txt`

### 3. Decisión sobre formato de imágenes
- Gallica sirve:
  - JPG nativo: ~2.9 MB, 28.9 MPx, con pérdida
  - PNG nativo: ~33.8 MB, 28.9 MPx, sin pérdida
- Verificación empírica a resolución equivalente (1.13 MPx):
  - JPG reducido: nitidez 1245.6
  - PNG manual (recortes): nitidez 1850.2
  - Diferencia: ~33% menos nitidez en JPG
- **Decisión**: usar PNG nativo del IIIF.
- **Justificación**: es el único formato que combina resolución nativa, ausencia de artefactos de compresión, y reproducibilidad total (sin sesgo de recorte humano).

### 4. Corrección del umbral de "fracción de blancos"
- Umbral anterior: 240 (casi blanco puro)
- Umbral nuevo: 200 (acomoda tono crema del pergamino)
- Resultado: las imágenes manuales muestran 44.7% de blancos, lo cual es coherente con el pergamino real. No hubo recorte agresivo.

## Pendiente para siguiente sesión
1. Descargar los 5 folios en PNG vía `10_descargar_folios_png.py`.
2. Generar hashes iniciales con `00_generar_hashes.py`.
3. Verificar integridad con `05_verificar_hashes.py`.
4. Generar ground truth de los 5 folios.
5. Verificar saldo y modelos de OpenRouter.

## Notas metodológicas
- No se modificó la semilla después de ver los resultados.
- No se modificó la lista de páginas candidatas después del sorteo.
- El diseño pre-registrado se mantiene intacto.
