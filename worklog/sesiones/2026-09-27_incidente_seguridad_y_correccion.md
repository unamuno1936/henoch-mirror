# Incidente de Seguridad y Corrección de Ruta (2026-09-27)

## 1. Incidente del filtro de seguridad de Gemini
**Síntoma:** Las primeras llamadas C2 fallaron con `finish_reason: content_filter` y `native_finish_reason: SAFETY`.
**Evidencia:** El razonamiento del modelo mostraba que estaba procesando el manuscrito correctamente (identificó folio, columnas y líneas), pero el clasificador de seguridad de Google abortó la generación por un falso positivo. El JSON confirmó `usage: { prompt_tokens: 0, completion_tokens: 0, cost: 0 }`.
**Causa:** El clasificador de seguridad de Gemini no distingue entre violencia en un texto histórico (Libro de Enoc) y contenido violento moderno. Es un problema de contexto, no de intención.
**Precedente académico:** Tekgürler (2025) documenta que Gemini marcó entre 14% y 23% de un manuscrito otomano del siglo XVIII como dañino por la misma razón[reference:0].
**Solución aplicada:** Se añadió el parámetro `safety_settings` con `BLOCK_NONE` en `extra_body` al payload del script `06_llamar_openrouter.py`. Con esto, la llamada C2 funcionó.
**Costo:** $0.00 USD (la llamada fue abortada antes de la inferencia).

## 2. Agotamiento de tokens por razonamiento excesivo
**Síntoma:** La llamada C2 exitosa se cortó con `finish_reason: length`.
**Evidencia:** El JSON mostró `completion_tokens: 8188`, de los cuales `reasoning_tokens: 7864` (96% del total). El modelo gastó casi todo su presupuesto de salida en razonar y dejó solo ~324 tokens para el output visible.
**Solución aplicada:** Se modificó el script `06_llamar_openrouter.py` para cambiar el valor por defecto de `--max-tokens` de 8192 a 32000.

## 3. Descubrimiento: BnF Éthiopien 49 es una copia (Paris 32)
**Hallazgo:** El manuscrito objeto de estudio (BnF Éthiopien 49) es una copia del siglo XVIII del Bodleian MS 5, realizada por orden de James Bruce y regalada a Luis XV. Corresponde a la sigla "Paris 32" en la erudición.
**Consecuencia:** Knibb (1978) y Charles (1906, 1912) **no incluyen este manuscrito en sus aparatos críticos** porque es un *codex descriptus*: una copia que no aporta información nueva para reconstruir el texto original. Esto lo confirma la propia lista de siglas de Knibb (Vol. 1, pp. xv-xvi) y su texto introductorio, donde menciona que "Charles thus left completely out of account only four manuscripts: Abb 16, Abb 30, Paris 114, and Paris 32."
**Implicación para el estudio:** El ground truth es BnF Éthiopien 49. Knibb y Charles son testigos comparativos, no fuentes de variantes para este manuscrito específico. El locus marcador debe construirse mediante comparación visual con el Rylands MS 23 o mediante la comparación del texto de Knibb (que es el Rylands) con la transcripción del modelo para BnF 49.

## 4. Tarea pendiente: Prueba de Ceguera Contextual
**Objetivo:** Determinar si el modelo lee o recuerda. Crear una situación donde no pueda saber qué está viendo.
**Método:** Usar una cuenta de Gemini completamente nueva (gratuita, sin historial, sin actividad). Subir la imagen `folio_7v.png` sin contexto visual (sin bordes, sin marcas de catálogo). Usar un prompt neutral: "Transcribe el texto de la imagen. Si alguna parte no es legible, márcala como [ilegible]."
**Interpretación:** Si el modelo menciona "Enoch" o el capítulo 13 → memorización. Si intenta transcribir y marca [ilegible] → lectura.
**Estado:** [PENDIENTE DE EJECUTAR]
