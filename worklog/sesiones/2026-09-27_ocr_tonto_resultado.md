# Resultado: OCR tonto con Tesseract (2026-09-27)

## Setup técnico
- Modelo: Tesseract 5.5.0 + script/Ethiopic.traineddata (tessdata_best)
- Instalación: sudo apt install tesseract-ocr-script-ethi + descarga manual
  del .traineddata desde github.com/tesseract-ocr/tessdata_best
- Script: scripts/15_ocr_tonto_geez.py
- Imagen: imagenes/folio_7v.png (SHA-256 4683e03f...)
- Timestamp: 2026-09-28T05:19:18Z
- Tiempo de cómputo: 20.18s (CPU)
- Output: 817 caracteres

## Análisis del output
El texto extraído contiene:
- Palabras ge'ez reconocibles: ተዝካረ, ስአለቶሙ, እግዚአብሔር, ሰማይ
- Errores de lectura típicos de OCR:
  - Confusión vocálica (መጋባረ vs ምግባረ)
  - Ruido de segmentación (|, *, -, 0, D, 7)
  - Fallos en separación de columnas
- NINGUNA marca [ilegible] (Tesseract no las produce, por diseño)
- NINGUNA palabra completa inventada

## Interpretación
Tesseract ESTÁ LEYENDO. El patrón de errores es consistente con OCR sobre
manuscrito histórico: confunde trazos pero ve caracteres reales. No accede
a memoria del canon.

## Comparación con Gemini (prueba de ceguera)
| Métrica | Tesseract | Gemini ciego |
|---|---|---|
| Caracteres | 817 | ~1300 |
| Marcas [ilegible] | N/A | 0 |
| Coincidencia con canon | Parcial | Total |
| Ruido OCR | Abundante | Ninguno |

## Conclusión
La línea base de "lectura real" (Tesseract, especializado, con errores)
contrasta con la "perfección" de Gemini (generalista, sin [ilegible]).
La brecha es evidencia cuantitativa de memorización paramétrica en Gemini.

## Limitaciones declaradas
- Tesseract no está entrenado para manuscritos etíopes históricos.
- Categorías de modelos distintas (OCR vs LLM multimodal).
- Un solo folio. Pendiente replicar sobre 4r, 5v, 17v, 40v.

## Estatus
HECHO. Output guardado en:
- datos/ocr_tonto_folio_7v.txt (817 chars)
- datos/ocr_tonto_folio_7v.json (metadatos + hash)
