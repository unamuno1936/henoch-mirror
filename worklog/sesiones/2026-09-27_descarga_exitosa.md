# Sesión 2026-09-27 — Descarga exitosa de los 5 folios

## Hora de inicio
2026-09-27T02:18:46Z

## Hora de fin
2026-09-27T02:26:08Z

## Duración
~7 minutos 22 segundos (incluyendo pausas de 15s entre descargas)

## Objetivo
Descargar en PNG nativo los 5 folios seleccionados del BnF Éthiopien 49,
generar hashes SHA-256 iniciales, y verificar integridad.

## Acciones ejecutadas

### 1. Descarga de folios vía IIIF
- Script: `10_descargar_folios_png.py`
- API: Gallica/BnF IIIF, formato `native.png`
- Pausa entre descargas: 15s (respeta límite de 5 req/min de Gallica)
- Resultado: 5/5 exitosos

| Folio | Canvas IIIF | Peso (MB) | SHA-256 (primeros 16) |
|---|---|---|---|
| 7v | f28 | 28.76 | 4683e03f4d2120c6 |
| 5v | f24 | 30.44 | 229a779a4ad6e8b4 |
| 4r | f21 | 37.69 | 34c9525c5e86a247 |
| 40v | f94 | 28.42 | 3bfade9f5b305bf2 |
| 17v | f48 | 28.50 | e72af827eb975332 |

- Tamaño total: ~154 MB
- Log completo: `logs/descarga_iiif.json`

### 2. Generación de hashes iniciales
- Script: `00_generar_hashes.py`
- Archivos hasheados: 37
- Artefactos:
  - `config/paginas_candidatas.txt`
  - `config/paginas_seleccionadas.txt`
  - `config/paginas_canvas_map.txt`
  - `config/criterios_preregistrados.md`
  - `config/plan_analisis_julia.md`
  - `prompts/generico.txt`
  - `prompts/wrapper_tlacuilo.txt`
  - Las 5 imágenes PNG descargadas
  - Los 11 scripts
- Salida:
  - `hashes/hashes.txt`
  - `hashes/manifest.json`

### 3. Verificación de integridad
- Script: `05_verificar_hashes.py`
- Resultado: **OK: 37 | CAMBIADOS: 0 | FALTANTES: 0**

## Estado del pipeline

| Componente | Estado |
|---|---|
| Selección aleatoria | ✅ Completada |
| Descarga de imágenes | ✅ Completada (5/5) |
| Formato | ✅ PNG nativo sin pérdida |
| Hashes SHA-256 | ✅ Generados |
| Verificación | ✅ Sin discrepancias |
| Log de descarga | ✅ Automático |

## Observaciones

- No hubo errores 429 (rate limit). Las pausas de 15s fueron suficientes.
- Los tamaños son coherentes: cada folio pesa entre 28 y 38 MB en PNG.
- El folio 4r (f21) es el más pesado, posiblemente por más contenido o
  mayor cantidad de tinta.
- Los hashes son únicos, lo que confirma que cada imagen es distinta.

## Pendiente para siguiente sesión

1. Generar el ground truth de los 5 folios (transcripción diplomática).
2. Verificar el saldo de OpenRouter y los modelos disponibles.
3. Ajustar el script 06_llamar_openrouter.py a la API real.
4. Verificar que la clave de OpenRouter esté en .env.
5. Primera llamada de prueba con un folio y un modelo.

## Notas metodológicas

- La lista de páginas candidatas NO se modificó después del sorteo.
- La semilla NO se cambió.
- Los criterios pre-registrados NO se ajustaron.
- El log de descarga incluye timestamp UTC, URL exacta, tamaño y hash
  de cada imagen, lo que constituye cadena de custodia.
