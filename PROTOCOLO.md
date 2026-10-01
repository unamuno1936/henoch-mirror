# PROTOCOLO — Estudio preliminar Henoch/Tlacuilo

## 1. Pregunta
¿Un perfil especializado con protocolo anti-alucinación (Tlacuilo) mejora
la transcripción y traducción de ge'ez manuscrito en VLMs no entrenados
específicamente en esa lengua, respecto a un prompt genérico?

## 2. Corpus
BnF Éthiopien 49 (1 Enoc en ge'ez).
Excluidas: 1r, 1v, 2r, 2v (blanco); 59r-62v (transposición).
Selección: 5 páginas al azar, semilla 20260926, reproducible.

## 3. Modelos (3 vía OpenRouter, verificar disponibilidad)
- M1: Gemini (referencia personal)
- M2: modelo alterno (contraste de arquitectura)
- M3: modelo alterno (contraste de proveedor)

## 4. Prompts
- generico.txt: instrucción directa, sin protocolo.
- wrapper_tlacuilo.txt: wrapper público + perfil en system message.

## 5. Diseño A (pre-registrado)
Por cada (modelo × prompt × página): 3 corridas independientes.
Total: 3 × 2 × 5 × 3 = 90 corridas.
Cada corrida: 1 transcripción + 4 traducciones (EN-iso, EN-flu, ES-iso, ES-flu).
Total outputs: 450.

## 6. Métricas
- CER (Character Error Rate) vs ground truth.
- WER (Word Error Rate) vs ground truth.
- Tasa H (alucinación) con H1-H4.
- Consistencia entre réplicas: media, desv., rango, distancia.

## 7. Criterios (pre-registrados)
Ver config/criterios_preregistrados.md

## 8. Trazabilidad
- worklog: scope jacobea_monetizacion/henoch_tlacuilo_estudio_01
- Clew: DAG SHA-256 de todos los artefactos
- 05_hashes.py: snapshots inicial/pre-ejecucion/final
- logs/openrouter_log.jsonl: log crudo de cada llamada
- OpenRouter con ZDR (data_collection=deny, zdr=true)

## 9. Publicación
Zenodo preprint con DOI. Estructura: intro, métodos, resultados,
discusión, limitaciones, anexos (prompt genérico, hashes, bitácora).

## 10. Lo que se reserva
- Reglas específicas de Tlacuilo.
- System message completo.
- Comandos operativos.
- Tablas de MAD.

## 11. Lo que se publica
- Hipótesis, método, resultados, limitaciones.
- Descripción conceptual del protocolo.
- Prompt genérico íntegro.
- Scripts de análisis.
- Hashes de verificación.

## 12. Flujo operativo
1. bash scripts/00_instalar.sh
2. source entorno/venv/bin/activate
3. Llenar config/paginas_candidatas.txt
4. python3 scripts/01_seleccionar_paginas.py --n 5 --seed 20260926
5. python3 scripts/07_descargar_iiif.py
6. python3 scripts/05_hashes.py --snapshot inicial
7. Generar ground truth asistido
8. python3 scripts/06_openrouter_client.py (repetir 90 veces)
9. python3 scripts/02_metricas_cer_wer.py --batch
10. python3 scripts/03_alucinaciones.py --init (editar CSV) --compute
11. python3 scripts/04_consistencia.py
12. python3 scripts/05_hashes.py --snapshot final
13. Redacción del preprint
14. Subida a Zenodo

---

## 13. Plan de análisis

El plan completo de análisis está en `config/plan_analisis_julia.md`.

**Resumen**:
- Bloque 1 (pre-registrado): estadísticas descriptivas, agregación,
  diferencias, aplicación del criterio de veredicto. Se ejecuta siempre.
- Bloque 2 (exploratorio): análisis de sensibilidad, inferencial
  exploratorio, cualitativo. Se activa condicionalmente y se reporta
  separado.

Ningún análisis exploratorio se presenta como confirmatorio.

---

## 14. Bitácora y logs

### Bitácora
- Ubicación: `worklog/sesiones/`
- Formato: Markdown por sesión
- Contenido: objetivo, acciones, archivos generados, decisiones tomadas,
  pendientes
- Cada entrada incluye timestamp UTC

### Logs automatizados
- `logs/descarga_iiif.json`: descargas de Gallica (script 10)
- `logs/{run}.json`: cada llamada a OpenRouter (script 06)

### Logs manuales
- `logs/gemini_web_sesiones.md`: sesiones en Gemini web
- `logs/consultas_manuales.md`: consultas a catálogos, cotejos

### Hashes
- `hashes/hashes.txt`: hashes SHA-256 de todos los artefactos
- `hashes/manifest.json`: estructura completa con timestamps

---

## 15. Hardware y sistema

Ver `HARDWARE.md`. Se documenta:
- Modelo del dispositivo
- SO y versión del kernel
- CPU, RAM, almacenamiento
- Entorno Python (versión, paquetes)
- Herramientas de IA usadas
- Limitaciones de hardware
- Presupuesto operativo

---

## 18. Intervención humana en el Estudio 1

**Decisión**: en el Estudio 1, la intervención humana NO modifica los
outputs que se miden. Los 3 runs son estáticos.

**Lo que se mide**:
- Frecuencia de solicitudes de verificación de Tlacuilo.
- Precisión de esas solicitudes contra el ground truth.

**Lo que se reserva para el Estudio 2**:
- Efecto de la intervención humana en la calidad.
- Delta de CER entre "Tlacuilo solo" y "Tlacuilo + humano".

**Justificación**: intervenir contaminaría la comparación con el prompt
genérico, que no tiene intervención. Se preserva la validez del diseño.

## 19. Declaración de construcción del perfil

El perfil Tlacuilo-Auditor fue construido por el autor mediante
interacción humano-modelo dirigida (Gemini web, DeepSeek). Se declara
en Métodos. Las sesiones no se publican (perfil reservado), pero se
documentan en el worklog. Los prompts del estudio sí son públicos.

---

## 18. Intervención humana en el Estudio 1

**Decisión**: en el Estudio 1, la intervención humana NO modifica los
outputs que se miden. Los 3 runs son estáticos.

**Lo que se mide**:
- Frecuencia de solicitudes de verificación de Tlacuilo.
- Precisión de esas solicitudes contra el ground truth.

**Lo que se reserva para el Estudio 2**:
- Efecto de la intervención humana en la calidad.
- Delta de CER entre "Tlacuilo solo" y "Tlacuilo + humano".

**Justificación**: intervenir contaminaría la comparación con el prompt
genérico, que no tiene intervención. Se preserva la validez del diseño.

## 19. Declaración de construcción del perfil

El perfil Tlacuilo-Auditor fue construido por el autor mediante
interacción humano-modelo dirigida (Gemini web, DeepSeek). Se declara
en Métodos. Las sesiones no se publican (perfil reservado), pero se
documentan en el worklog. Los prompts del estudio sí son públicos.
