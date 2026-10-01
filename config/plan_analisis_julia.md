# Plan de análisis — Julia

## Principio rector

El análisis se divide en dos bloques **explícitamente separados**:

1. **Análisis pre-registrado** (confirmatorio). Definido antes de ver datos.
2. **Análisis exploratorio** (no confirmatorio). Solo se activa si los
   datos lo ameritan, y se reporta como exploratorio.

Ningún análisis exploratorio se presenta como confirmatorio. La distinción
se mantiene en el preprint.

---

## Bloque 1 — Análisis pre-registrado

Estos cálculos se ejecutan **siempre**, independientemente de los resultados.
No hay decisión post-hoc.

### 1.1 Estadísticas descriptivas por celda

Para cada combinación (modelo × prompt × folio × run):

| Métrica | Cálculo | Fuente |
|---|---|---|
| CER | `02_metricas_cer_wer.py` | `resultados/metricas_cer_wer.csv` |
| WER | `02_metricas_cer_wer.py` | `resultados/metricas_cer_wer.csv` |
| Tasa H | `03_alucinaciones.py --compute` | `resultados/tasa_alucinacion.csv` |
| Longitud ref vs hip | `02_metricas_cer_wer.py` | `resultados/metricas_cer_wer.csv` |

### 1.2 Agregación por modelo × prompt

| Métrica | Cálculo |
|---|---|
| CER medio | `mean(CER)` por (modelo, prompt) |
| CER desviación | `std(CER)` por (modelo, prompt) |
| CER rango | `max - min` por (modelo, prompt) |
| Tasa H media | `mean(H)` por (modelo, prompt) |

### 1.3 Diferencia Tlacuilo vs. genérico

| Métrica | Cálculo |
|---|---|
| ΔCER | `CER(genérico) - CER(Tlacuilo)` por modelo |
| ΔH | `H(genérico) - H(Tlacuilo)` por modelo |
| Δdesv | `desv(genérico) - desv(Tlacuilo)` por modelo |

### 1.4 Consistencia entre runs

| Métrica | Cálculo |
|---|---|
| Identidad entre runs | `1` si los 3 outputs normalizados son idénticos, `0` si no |
| Distancia media entre runs | Media de Levenshtein entre pares |
| Rango de CER intra-celda | `max - min` entre las 3 runs |

### 1.5 Aplicación del criterio pre-registrado

Con las tablas anteriores, se aplica el criterio:

- **Alentador**: ΔCER ≥ 10 pp en ≥2/3 modelos Y ΔH ≥ 0.10 en ≥2/3
  Y desv. Tlacuilo ≤ desv. genérico en ≥2/3.
- **Neutro**: ΔCER entre 0 y 10 pp, o efecto inconsistente.
- **Desastroso**: ΔCER < 0 en ≥2/3 modelos O ΔH < 0 en ≥2/3.

El veredicto se reporta como pre-registrado.

---

## Bloque 2 — Análisis exploratorio (condicional)

Este bloque **no se activa por defecto**. Se activa solo si:

- Los resultados del Bloque 1 caen en zona gris, o
- Los datos muestran un patrón no anticipado que merece examen, o
- El tamaño del efecto es ambiguo y se necesita cuantificar mejor.

Cuando se activa, el análisis exploratorio se reporta en una sección
separada del preprint titulada **"Análisis exploratorio (no confirmatorio)"**.

### 2.1 Análisis de sensibilidad

| Análisis | Cuándo se justifica |
|---|---|
| CER sin caracteres diacríticos | Si el CER total es alto y se sospecha que diacríticos inflan el error |
| CER por líneas vs por caracteres | Si el output tiene segmentación inconsistente |
| Exclusión de folios atípicos | Si un folio muestra CER anómalo (outlier) |
| Ponderación por longitud de folio | Si los folios tienen longitudes muy dispares |

### 2.2 Análisis inferencial exploratorio

Si los datos lo permiten, y solo como exploratorio:

| Análisis | Justificación | Limitación explícita |
|---|---|---|
| Wilcoxon rank-sum pareado | Comparar Tlacuilo vs genérico por modelo | n=5 páginas, potencia limitada |
| Cohen's d | Estimar tamaño del efecto | Con n pequeño, IC amplios |
| Bootstrap de CER | Estimar IC al 95% sin asumir normalidad | Resampling de 5 puntos es inestable |
| Modelos bayesianos jerárquicos | Estimar efecto entre modelos | Requiere priors informados, no triviales |

**Declaración obligatoria**: cualquier resultado de este bloque se reporta
con la frase "Análisis exploratorio. No confirmatorio. La potencia
estadística con n=5 es limitada."

### 2.3 Análisis cualitativo complementario

| Análisis | Output |
|---|---|
| Tipología de errores | Tabla de categorías con ejemplos |
| Patrones de alucinación | Análisis de los H_i más frecuentes |
| Eventos espontáneos | Registro de cuándo un genérico pidió verificación humana |
| Convergencia entre modelos | Similitud coseno entre traducciones de distintos modelos |

Este bloque **no** requiere justificación previa: es análisis cualitativo
exploratorio, no inferencial.

---

## Regla de honestidad

Cualquier cálculo que **no** esté en el Bloque 1 se reporta como
exploratorio. No se mueve nada del Bloque 2 al Bloque 1 después de ver
los datos.

Si durante el análisis exploratorio se descubre algo importante que
amerita un estudio de seguimiento, se documenta como **"hipótesis para
estudio 2"**, no como hallazgo de este estudio.

---

## Output esperado de Julia

### Archivos obligatorios (Bloque 1)
- `resultados/metricas_cer_wer.csv` (por celda)
- `resultados/consistencia.csv` (por modelo × prompt × folio)
- `resultados/tasa_alucinacion.csv` (por modelo × prompt)
- `resultados/delta_cer_h.csv` (ΔCER y ΔH por modelo)
- `resultados/veredicto.md` (aplicación del criterio pre-registrado)

### Archivos opcionales (Bloque 2, si aplica)
- `resultados/exploratorio_*.csv` (análisis de sensibilidad)
- `resultados/cualitativo_tipologia.md` (análisis de errores)

### Documento de cierre
- `resultados/informe_julia.md` con:
  - Descripción de los datos
  - Resultados del Bloque 1
  - Veredicto pre-registrado
  - Sección separada: análisis exploratorio (si aplica)
  - Limitaciones
