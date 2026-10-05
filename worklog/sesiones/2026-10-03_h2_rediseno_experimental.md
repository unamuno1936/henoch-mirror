# Sesión 2026-10-03 — Rediseño experimental H2, versión final

## Motivo del rediseño

El diseño original de H2 preveía:

    15 folios × 5 modelos × 2 prompts = 150 llamadas
    Modelos: Gemini Flash, Gemini Flash extended, Gemini Pro,
             DeepSeek-V3, DeepSeek-R1
    Prompts: genérico simple vs. wrapper Tlacuilo

Este diseño es inviable en las condiciones reales del proyecto. Se
reduce y se congela aquí.

## Diseño final congelado

    Folios:   5 (los cinco primeros del BnF Éthiopien 49)
    Modelos:  Gemini 3.8 Flash + 2 modelos adicionales
    Prompts:  genérico simple, con y sin inyección del perfil Tlacuilo
    Llamadas: 1 por celda (sin repetición)
    Total:    entre 15 y 20 llamadas

### Tabla de condiciones

| ID                        | Modelo              | Prompt    | Perfil    |
|---------------------------|---------------------|-----------|-----------|
| gemini38flash__simple     | Gemini 3.8 Flash    | genérico  | ninguno   |
| gemini38flash__perfil     | Gemini 3.8 Flash    | genérico  | Tlacuilo  |
| modelo2__simple           | [a definir]         | genérico  | ninguno   |
| modelo2__perfil           | [a definir]         | genérico  | Tlacuilo  |
| modelo3__simple           | [a definir]         | genérico  | ninguno   |
| modelo3__perfil (opcional)| [a definir]         | genérico  | Tlacuilo  |

Los modelos 2 y 3 se definen en la config congelada del script.

## Justificaciones

### Por qué 5 folios

Los primeros cinco folios cubren material enoquiano sustantivo y son
suficientes para cotejar contra Sacy (caps. 1–16). No hay necesidad
de ampliar sin ground truth adicional.

### Por qué 3 modelos y no 5

Tres modelos permiten contraste suficiente. Dos no permiten descartar
idiosincrasias de proveedor. Cuatro o más no añaden información en
esta fase.

### Por qué una sola llamada por celda

Razón crítica, en palabras del autor del proyecto:

> "Hacer tres llamadas a la API de lo mismo por separado solo
> demostrará que nuestro modelo puede ser inconsistente. Si eso es
> valioso, lo fundamentamos. Porque no puedo hacerle ningún ajuste
> a los prompts para la segunda y tercera llamadas, porque violo la
> metodología."

Esto es correcto. Tres llamadas con prompt idéntico miden la
**temperatura del modelo**, no su fidelidad. Un solo disparo por
celda es lo que mide la capacidad del modelo en condiciones reales.

### Por qué inyectar el perfil Tlacuilo a los modelos 2 y 3

Es una variable experimental válida. Si el perfil **mejora** a Gemini
pero **empeora** a otros modelos, eso es un hallazgo publicable:
demuestra que el perfil no es universalmente beneficioso y que su
efecto depende del modelo. Se documenta como resultado, no como
fracaso.

Si un modelo rechaza la inyección del perfil (por límite de contexto,
política del proveedor, o formato), **el rechazo mismo se documenta
como resultado** y la celda se marca como N/A.

## Hipótesis H2 (sin cambios)

H2: Flash simple produce transcripciones más fieles que Pro o Flash
extended. El razonamiento extendido perjudica la percepción visual.

Este diseño reducido es suficiente para poner H2 a prueba.

## Limitaciones declaradas

1. **Ground truth único y débil.** Sacy es el único traductor
   conocido de BnF Éthiopien 49, y su cotejo con Woide y Laurence es
   débil por razones documentadas en bitácoras previas.

2. **Woide no accesible.** El manuscrito Bodleian MS. Clar. Press
   d. 10 (transcripción de Woide) no está digitalizado ni disponible
   en línea al momento de esta sesión.

3. **Sarnelli no aporta ground truth.** Su comentario de 1710 es
   contexto histórico, no texto base. Confirmado en bitácora
   `2026-10-03_sarnelli_primer_comentario_enoc.md`.

4. **Vat. et. 71 fuera de alcance.** Microfilmado, no digitalizado
   en IIIF público. Se documenta en bitácora
   `2026-10-03_vat_et_71_cuarto_manuscrito_bruce.md`. Se reserva
   para fase posterior.

5. **Oxford no entra en esta fase.** MS. Bodl. Or. 531 y MS. Bruce 74
   son copias de menor calidad y aumentarían artificialmente la tasa
   de alucinación. Se reservan para fase posterior.

6. **Intervención humana imposible.** No hay presupuesto de tiempo
   para corrección manual intermedia. Se declara como condición del
   experimento, no como defecto.

## Definición operacional de alucinación (heredada de §5.7)

| Categoría     | Definición                                              |
|---------------|---------------------------------------------------------|
| Inserción     | Palabra/frase que no está en la imagen.                 |
| Normalización | Forma modificada hacia lo canónico.                     |
| Omisión       | Carácter o palabra visible no transcrito.               |

## Decisión

Proceder con el diseño reducido. Esta bitácora queda congelada como
pre-registro antes de ejecutar la primera llamada.

## Pendientes inmediatos

- [ ] Definir los modelos 2 y 3 exactos en `config.yaml`.
- [ ] Confirmar acceso al texto latino de Sacy (caps. 1–16, 22, 31).
- [ ] Ejecutar script `ejecutar.py` (ver `scripts/experimento_h2/`).
- [ ] Analizar resultados sin modificar el diseño.
