# 2026-10-04 — El día después: cierre de H2, apertura de Proyecto Sacy y nota sobre resiliencia académica

**Estado:** Cierre de línea experimental + apertura de nueva línea.
**Bitácora previa relacionada:** Cierre de H2 (2026-10-04).
**Naturaleza de esta entrada:** Decisión de operador + reflexión metodológica + actualización operativa.

---

## English

### Context

The H2 experiment (automatic Ethiopic Enoch transcription via multimodal models) was closed with a negative methodological note. The reason was structural, not technical: without verified ground truth and without the operator's ability to produce independent transcription, no pipeline output is contrastable. An uncontrastable result is not data.

This entry documents the closure, the opening of Project Sacy (translation of Silvestre de Sacy's *Notice du livre d'Énoch*, 1800), and a reflection on academic resilience as a methodological stance.

### Decision on H2

The three-pass redesign (cold read → human intervention → reference comparison) was designed but **not executed**. The decision to close was based on the following:

1.  **The operator does not read Ge'ez.** Without this skill, the human intervention pass (Pass 2) could not function as an independent control. The operator could only compare visually, not transcribe manually.
2.  **The "black box" problem.** Even if the model produced a perfect-looking transcription, the operator would have no certainty about whether it was read from the image or retrieved from training data. Without ground truth, this uncertainty is irreducible.
3.  **Hardware limitations.** The operator cannot run large models locally. Commercial APIs impose constraints (token limits, opaque reasoning processes) that the operator cannot inspect or control.
4.  **A decision of common sense.** In the operator's words: *"It is much more honest to stand on the shoulders of those who came before me and translate them, because this way I invent nothing that I cannot discover."*

### New Line: Project Sacy

The new line translates an existing critical edition from its language of publication into Spanish. This is methodologically clean because:

1.  **Ground truth exists.** The source text is citable and visible.
2.  **Source languages are well-represented in training corpora.** 18th-century academic French and Latin are abundant in LLM training data.
3.  **Attribution is clean.** You translate Dillmann by translating Dillmann. You do not invent a text that does not exist.
4.  **Verifiability.** Any reader with access to the original can check the translation against the source.

See `worklog/2026-10-04_proyecto_sacy_inicio.md` for the full pipeline.

### On Academic Resilience

This project documents a negative result and opens a new line. This is not failure; it is the scientific method in action. The H2 run produced:

-   A **taxonomy of failure modes** (Type A: reasoning stuck; Type B: truncated emission; Type C: rigor paralysis; Type D: degenerative hallucination; honest abstention).
-   An **observation on model variance**: inter-model variance is an order of magnitude greater than inter-prompt variance.
-   A **methodological note**: without ground truth and without qualified human intervention, multimodal pipelines for low-resource scripts produce uninterpretable output.

These are real, generalizable results. They will be published as a negative methodological note with a DOI.

### On Measuring "Junk"

A question arose: is it valid to measure the *junk* produced by cheap models (Qwen, DeepSeek) when the impossibility of obtaining anything else is acknowledged?

**Answer: yes, under three conditions:**

1.  **Full transparency.** The run must be documented as a *stress test* of failure modes, not as a test of transcription fidelity.
2.  **No cherry-picking.** All outputs must be archived, including the most absurd.
3.  **No claims about "quality."** The output is measured as a *behavioral artifact* of the model under adverse conditions, not as an attempt at a correct transcription.

Under these conditions, measuring "junk" is methodologically valid and can produce interesting, even humorous, results. It is a *documentation of failure modes*, not an evaluation of performance.

### On OpenAI and Opacity

The operator noted: *"They could not pass an anti-doping control, and they could not genuinely explain it well, and it is very possible that it is not even reproducible with other models."*

This is a well-founded observation. OpenAI's September 2026 claim to have solved the Navier-Stokes Millennium Problem was met with skepticism. The solution **was not independently verified**, and mathematicians **questioned whether the AI had access to unpublished research**. This case illustrates a broader problem: **closed-source models are not replicable**, and their results cannot be independently verified. This is a transparency deficit, not a scientific result.

### Next Actions

-   [ ] Push H2 closure and Project Sacy to GitLab (main) and GitHub (mirror).
-   [ ] Run pipeline stage 1 on the Sacy PDF.
-   [ ] Decide on OCR engine (Tesseract `fra` vs Calamari `18th_century_french`).
-   [ ] Write the "El día después" companion piece (humorous stress-test documentation).

---

## Español

### Contexto

El experimento H2 (transcripción automática del Enoc etíope vía modelos multimodales) se cerró con nota metodológica negativa. La razón fue estructural, no técnica: sin ground truth verificado y sin capacidad del operador para producir una transcripción independiente, ningún output del pipeline es contrastable. Un resultado incontrastable no es un dato.

Esta entrada documenta el cierre, la apertura del Proyecto Sacy (traducción de la *Notice du livre d'Énoch* de Silvestre de Sacy, 1800) y una reflexión sobre la resiliencia académica como postura metodológica.

### Decisión sobre H2

El rediseño de tres pasadas (lectura en frío → intervención humana → comparación con referencia) se diseñó pero **no se ejecutó**. La decisión de cerrar se basó en lo siguiente:

1.  **El operador no lee ge'ez.** Sin esta habilidad, la pasada de intervención humana (Pasada 2) no podía funcionar como control independiente. El operador solo podía comparar visualmente, no transcribir manualmente.
2.  **El problema de la "caja negra".** Incluso si el modelo produjera una transcripción perfecta, el operador no tendría certeza de si fue leída de la imagen o recuperada de los datos de entrenamiento. Sin ground truth, esta incertidumbre es irreducible.
3.  **Limitaciones de hardware.** El operador no puede correr modelos grandes localmente. Las APIs comerciales imponen restricciones (límites de tokens, procesos de razonamiento opacos) que el operador no puede inspeccionar ni controlar.
4.  **Una decisión de sentido común.** En palabras del operador: *"Es mucho más honesto subirme a los hombros de los que me antecedieron y traducirlos, porque de esta manera no me invento nada que no pueda descubrir."*

### Nueva línea: Proyecto Sacy

La nueva línea traduce una edición crítica existente desde su lengua de publicación al español. Esto es metodológicamente limpio porque:

1.  **El ground truth existe.** El texto fuente es citable y visible.
2.  **Las lenguas de origen están bien representadas en los corpus de entrenamiento.** El francés académico del s. XVIII y el latín son abundantes en los datos de entrenamiento de los LLM.
3.  **La atribución es limpia.** Traduces a Dillmann traduciendo a Dillmann. No inventas un texto que no existe.
4.  **Verificabilidad.** Cualquier lector con acceso al original puede contrastar la traducción contra la fuente.

Ver `worklog/2026-10-04_proyecto_sacy_inicio.md` para el pipeline completo.

### Sobre la resiliencia académica

Este proyecto documenta un resultado negativo y abre una nueva línea. Esto no es fracaso; es el método científico en acción. La corrida de H2 produjo:

-   Una **taxonomía de modos de fallo** (Tipo A: razonamiento atascado; Tipo B: emisión truncada; Tipo C: parálisis por rigor; Tipo D: alucinación degenerativa; abstención honesta).
-   Una **observación sobre la varianza entre modelos**: la varianza inter-modelo es un orden de magnitud mayor que la varianza inter-prompt.
-   Una **nota metodológica**: sin ground truth y sin intervención humana calificada, los pipelines multimodales para escrituras de bajos recursos producen output no interpretable.

Estos son resultados reales y generalizables. Se publicarán como nota metodológica negativa con DOI.

### Sobre medir "basura"

Surgió una pregunta: ¿es válido medir la *basura* que producen modelos baratos (Qwen, DeepSeek) cuando se reconoce la imposibilidad de obtener otra cosa?

**Respuesta: sí, bajo tres condiciones:**

1.  **Transparencia total.** La corrida debe documentarse como un *stress test* de modos de fallo, no como una prueba de fidelidad de transcripción.
2.  **Sin selección arbitraria.** Todos los outputs deben archivarse, incluidos los más absurdos.
3.  **Sin afirmaciones sobre "calidad".** El output se mide como *artefacto conductual* del modelo bajo condiciones adversas, no como un intento de transcripción correcta.

Bajo estas condiciones, medir "basura" es metodológicamente válido y puede producir resultados interesantes, incluso divertidos. Es una *documentación de modos de fallo*, no una evaluación de rendimiento.

### Sobre OpenAI y la opacidad

El operador señaló: *"No podrían pasar un control antidopaje, y no podrían, genuinamente, explicarlo bien del todo, y es muy posible que ni siquiera fuera reproducible con otros modelos."*

Esta es una observación bien fundada. La afirmación de OpenAI en septiembre de 2026 de haber resuelto el Problema del Milenio de Navier-Stokes se encontró con escepticismo. La solución **no fue verificada de forma independiente**, y los matemáticos **cuestionaron si la IA tuvo acceso a investigación no publicada**. Este caso ilustra un problema más amplio: **los modelos de código cerrado no son replicables**, y sus resultados no pueden ser verificados de forma independiente. Esto es un déficit de transparencia, no un resultado científico.

### Próximas acciones

-   [ ] Hacer push del cierre de H2 y del Proyecto Sacy a GitLab (principal) y GitHub (espejo).
-   [ ] Ejecutar la etapa 1 del pipeline sobre el PDF de Sacy.
-   [ ] Decidir el motor OCR (Tesseract `fra` vs Calamari `18th_century_french`).
-   [ ] Escribir la pieza complementaria "El día después" (documentación humorística de stress-test).

---

*Fin de la entrada. H2 cerrado. Proyecto Sacy abierto. La resiliencia académica queda documentada como postura metodológica.*
