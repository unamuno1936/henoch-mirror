# Cierre de sesión — Hallazgos consolidados (2026-09-27)

## 1. Resultado de la Prueba de Ceguera (cuenta Gemini limpia)

**Método**: Cuenta gratuita de Gemini sin historial previo, sin actividad,
sin contexto. Imagen folio_7v.png subida sin metadatos visibles.
Prompt neutral: "Transcribe el texto de la imagen. Si alguna parte no es
legible, márcala como [ilegible]."

**Resultado**: El modelo produjo una transcripción completa, fluida y sin
una sola marca [ilegible]. El texto coincide con las ediciones críticas
(Knibb 1978, Charles 1906/1912) en puntos donde el BnF Éthiopien 49
diverge por ser una copia del s. XVIII con errores de copista.

**Interpretación**: El modelo NO leyó la imagen. Accedió a su memoria
paramétrica del texto canónico y la regurgitó. La ausencia de [ilegible]
es la firma forense: si estuviera leyendo, encontraría zonas dudosas.
El BnF 49 tiene variantes conocidas que el modelo no reportó.

**Estatus**: HECHO. Evidencia guardada (screenshot de la conversación +
texto transcrito).

## 2. Script OCR "tonto" (línea base)

**Creado**: `scripts/15_ocr_tonto_geez.py` con EasyOCR (lang=am).
**Función**: Extrae caracteres etíopes de las imágenes SIN conocimiento
del contenido. No sabe de Enoc, Knibb, Charles ni filología. Solo trazos.

**Uso**: 
    python3 15_ocr_tonto_geez.py --imagen imagenes/folio_7v.png

**Salida**:
- `datos/ocr_tonto_<folio>.txt` (texto crudo)
- `datos/ocr_tonto_<folio>.json` (hash imagen, timestamp, confianza, tiempo)

**Propósito experimental**:
Contrastar tres capas de output sobre el mismo folio:
  (a) OCR tonto EasyOCR → lectura de trazos sin contexto
  (b) Gemini sin perfil (C1) → LLM sin protocolo
  (c) Gemini con perfil Tlacuilo (C2) → LLM con protocolo anti-anchoring

Si (a) produce basura y (c) produce texto perfecto, tenemos evidencia
cuantitativa de memorización. Si (c) marca más [ilegible] que (b),
tenemos evidencia de que el perfil reduce el anchoring.

**Estatus**: Script escrito y validado. PENDIENTE EJECUTAR y guardar
resultados.

## 3. Diferimiento del Track Web (prueba con cuenta de siempre + perfil)

**Decisión**: NO ejecutar la prueba web con la cuenta personal de Gemini
(con historial, con perfil, con prompt genérico) hasta haber completado
el Estudio 2 (Rylands).

**Razón**: Si el modelo regurgita el canon (probado en §1), darle Rylands
en cuenta contaminada produciría outputs indistinguibles entre "leyó
Rylands" y "recordó Knibb sobre Rylands". El experimento web perdería
valor diagnóstico.

**Plan**: Ejecutar el Track Web solo después de:
  - Estudio 1 (BnF 49 API, 90 llamadas) completado y analizado
  - Estudio 2 (Rylands API, mismo diseño) completado y analizado
  - Análisis comparativo entre BnF y Rylands establecido
  
Entonces el Track Web se convierte en "Track Ecológico" con hipótesis
claras sobre qué debería pasar si el modelo lee vs. si recuerda.

## 4. Actualización teórica: la hipótesis de co-evolución

**Observación**: no es solo que los LLM imiten el estilo humano. Es que
los humanos empiezan a imitar el estilo del LLM. Los estudios sobre
frecuencia de términos post-ChatGPT (aparecen en la entrevista de López
de Mántaras) muestran una curva exponencial de ciertos giros a partir
de 2023.

**Implicación para el estudio**: la "contaminación" no es unidireccional.
No solo el modelo contamina el estudio; el investigador se contamina
del modelo. Esto refuerza la necesidad de:
  - Pre-registro (documentar qué se esperaba antes de ver datos)
  - Cadena de custodia (hashes, logs)
  - Perfil anti-anchoring (prohibición explícita de reproducir canon)
  - Worklog (auditoría del proceso humano, no solo del output)

**Nota personal del autor** (a incluir en reflexión metodológica del preprint):
El autor sostiene que la interacción humano-modelo, cuando se hace con
perfil especializado, produce mejoras medibles en su propia capacidad
de trabajo intelectual. No es una hipótesis del estudio confirmatorio
(Estudio 1), pero es la motivación declarada del proyecto. Se reserva
para el Estudio 3/4.

## 5. Bibliografía entregada

Se entregaron 30 referencias (10 apoyo, 10 abogado del diablo, 10 matices),
con DOIs y resúmenes. PENDIENTE de revisión por el autor antes de
incorporarlas al preprint. Nota: las referencias deben verificarse contra
la fuente original antes de citar (regla anti-alucinación §3.5 del perfil).

## 6. Estatus de la sesión

**HECHO**:
- Prueba de ceguera (memorización confirmada)
- Script OCR tonto (escrito)
- Bitácoras del incidente de seguridad, corrección de ruta, siglas de
  Knibb, contexto Goncourt, estrategia de publicación
- Bibliografía preliminar (30 refs)

**PENDIENTE CRÍTICO para próxima sesión**:
- Ejecutar OCR tonto sobre folio_7v y verificar salida
- Re-ejecutar prueba C2 (Gemini + perfil + folio_7v) con max_tokens=32000
- Si C2 sale completo: ejecutar C1 completa (15 llamadas)
- Añadir sección al PROTOCOLO.md sobre BnF 49 como copia (Paris 32)

**DIFERIDO EXPLÍCITAMENTE**:
- Track Web (cuenta personal + perfil)
- Estudio 2 (Rylands)
- Estudio 3 (v2.1 ajustado)
- Estudio 4 (interacción humano-modelo)

## 7. Estado de ánimo / contexto

Autor reporta fatiga y hora tardía. Se cierra sesión. Toda la evidencia
está en disco, hasheada, con timestamps UTC. Próxima sesión retoma desde
"PENDIENTE CRÍTICO" §6.
