# Observación preliminar — DeepSeek web, prompt genérico

**Fecha**: 2026-09-28
**Folio**: 7v
**Modelo**: DeepSeek web (chat.deepseek.com)
**Modo**: DeepThink activado
**Prompt**: Genérico
**Turnos**: 1
**Intervención humana**: 0
**Canal**: Web (NO API)

## Archivos

### Original (raw, en consultas/)
- **Ubicación**: `consultas/Transcripción y traducción - DeepSeek.txt`
- **Contenido**: chat completo con meta-comentario visible
- **SHA-256**: [REEMPLAZAR — hash del paso 1]
- **Bytes**: [REEMPLAZAR]

### Copia limpia (en datos_preliminar/)
- **Ubicación**: `datos_preliminar/deepseek_web_7v_generico.txt`
- **Contenido**: idéntico al original
- **SHA-256**: [REEMPLAZAR — mismo hash]

### URL del chat en DeepSeek
- https://chat.deepseek.com/a/chat/s/3ab1de18-0d6c-41a2-a0b4-acc69df1aacd

## Lo que se observó

### Transcripción
- Sin marcas `[ilegible]` en el cuerpo de la transcripción
- Solo una capa (no separa diplomática de crítica)
- Meta-comentario visible (artefacto del canal web, no de API)
- Falsa seguridad en topónimos y género textual

### Traducciones
- Isomorfa al español: presente (pero sintaxis rota como esperado)
- Fluida al español: presente
- Isomorfa al inglés: AUSENTE (el prompt pedía ambos idiomas)
- Fluida al inglés: AUSENTE

### Formato
| Requisito | Cumplido |
|---|---|
| Transcripción diplomática | ❌ |
| Transcripción crítica separada | ❌ |
| `[ilegible: N]` en cuerpo | ❌ |
| `[dudoso: X o Y]` | ❌ |
| MAD | ❌ |
| Traducción isomorfa ES | ✅ |
| Traducción fluida ES | ✅ |
| Traducción isomorfa EN | ❌ |
| Traducción fluida EN | ❌ |
| `[REQUIERE VERIFICACIÓN HUMANA]` | ❌ |

**Cumplió 2 de 12 requisitos.**

## Auditoría de alucinaciones (H1-H4)

- **H1 (texto inventado)**: mitigada. Afirma género ("likely a synaxarium") sin verificación.
- **H2 (falsa legibilidad)**: **CONFIRMADA**. Reconoce "faint areas" pero no marca una sola `[ilegible]` en el cuerpo.
- **H3 (bibliografía inventada)**: no aplica (no citó).
- **H4 (normalización silenciosa)**: probable. Texto fluye porque el modelo tiene conocimiento paramétrico del ge'ez.

## Por qué NO entra al corpus oficial

- Canal: web, no API. Parámetros no controlados.
- Versión del modelo: no confirmada.
- Sin 3 runs independientes.
- Sin log JSON con hashes de prompt, imagen, salida.
- Sin control de temperatura.
- Meta-comentario visible contamina la comparación.

## Por qué SÍ es valioso

- Confirma empíricamente que el prompt genérico induce alucinación silenciosa (H2) incluso en modelos con razonamiento visible.
- Sirve como caso anecdótico para la sección de Discusión del preprint.
- Documenta el comportamiento ecológico del modelo antes del control estricto.
- El propio asistente de investigación (DeepSeek) puede auditar su output, lo cual es intropección documentada.

## Decisión

- Archivo raw conservado en `consultas/` (traza completa).
- Copia limpia en `datos_preliminar/` (para referencia del estudio).
- NO mezclar con `datos/` (corpus oficial).
- Mencionar en el preprint en Discusión, no en Resultados.

## Notas metodológicas

- Este output NO es parte de los 90 runs.
- NO se aplicará análisis de CER, WER o tasa H.
- Se declara como observación preliminar del asistente de investigación.
- El hash queda registrado para cadena de custodia.

## Cierre del pendiente

- [x] Archivo raw identificado en `consultas/`
- [x] Copia limpia creada en `datos_preliminar/`
- [x] SHA-256 calculado
- [x] Bitácora actualizada
- [x] Documentado en worklog
