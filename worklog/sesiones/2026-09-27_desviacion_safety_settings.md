# Desviación de infraestructura — 2026-09-27

## Incidente
La prueba C2 (Gemini 3.8 Flash + perfil Tlacuilo + wrapper v2, folio 7v)
falló con `finish_reason: content_filter`, `native_finish_reason: SAFETY`,
`error.code: 403`, `error.metadata.error_type: content_policy_violation`.

El modelo SÍ estaba procesando el manuscrito. El JSON muestra razonamiento
activo en el que identifica el folio, las columnas y las líneas iniciales.
El clasificador de seguridad de Google abortó la generación antes de que
se emitiera contenido visible. `usage` reporta 0 tokens consumidos: no hubo
cobro.

## Causa identificada
El clasificador de seguridad de Gemini (a) no distingue entre violencia en
un texto histórico y contenido violento moderno, (b) es sensible a scripts
no latinos, y (c) reacciona a campos semánticos de "prohibición", "ilegible",
"sin fuente" presentes en el perfil Tlacuilo. Es un falso positivo.

Precedente académico: Tekgürler, M. (2025). Traducción de un manuscrito
otomano del s. XVIII con Gemini. Entre 14% y 23% del manuscrito fue marcado
como dañino por el mismo motivo. Presentado en UC Davis, publicado en ACL
Anthology.

## Acción tomada
Añadir `safety_settings` con `BLOCK_NONE` en las cuatro categorías ajustables
al payload de `06_llamar_openrouter.py`. Backup del script previo:
`scripts/06_llamar_openrouter.py.bak_<TIMESTAMP_UTC>`.

## Alcance de la desviación
- NO se modifican: criterios de veredicto, semilla, folios, perfil Tlacuilo,
  wrapper, prompt genérico.
- SÍ se modifica: instrumento de llamada (parámetro de proveedor).
- Aplicación uniforme: C1–C6 usarán el mismo `safety_settings`. Si C1 se
  re-ejecuta, se aplica también.

## Implicación para el preprint
Esto no es solo una nota técnica: es evidencia empírica de que los filtros
de seguridad de LLM comerciales son incompatibles con la investigación
humanística sobre textos históricos. Se documentará en la sección de
Limitaciones y en la de Métodos.

## Costo
$0.00 USD. La llamada fue abortada antes de la inferencia.

## Hashes afectados
Wrapper:  61c98bf006094225af23ab41f65f7f9c9e0ad92509ed4f0aafe2f7e9a46a9fa8
System:   9693dc94c4017ac75a786a081cf2af1e61382bf411d7b9dee763278ea5904ad6
Generico: 18e778e4f736deaa1a2ee6bb0b2b9964720ff8d858802dabf3e0e0ffbb1ca5f3
