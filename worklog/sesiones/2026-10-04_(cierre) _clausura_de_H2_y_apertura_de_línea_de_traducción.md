# Sesión 2026-10-04 (cierre) — Clausura de H2 y apertura de línea de traducción

**Estado:** decisión cerrada. No tentativa.
**Bitácora previa relacionada:** 2026-10-04_h2_preliminar_y_rediseno.md
**Naturaleza de esta entrada:** cierre de línea experimental + decisión de operador + apertura de nueva línea.

---

## 1. Decisión

Se cierra la línea experimental H2 (transcripción automática de ge'ez
desde imagen de manuscrito) con **nota metodológica negativa**.

No se ejecutará el rediseño de tres pasadas (frío → humano → referencia)
descrito en la bitácora previa. No se invertirá en el pipeline ge'ez.

Fundamento de la decisión, en palabras del operador, registradas
textualmente:

> "Es mucho más honesto subirme a los hombros de los que me antecedieron
> y traducirlos, porque de esta manera no me invento nada que no pueda
> descubrir."

> "Encontrar transcripciones perfectas o casi perfectas no me serviría
> porque nunca sabría cuánto copiaron."

> "Hay un fallo metodológico. No voy a gastar dinero a lo tonto."

La decisión no proviene de un fallo técnico puntual ni de la
insuficiencia de un modelo específico. Proviene de un problema
epistemológico estructural: **sin ground truth verificable y sin
capacidad del operador para producir ese ground truth de forma
independiente, ningún output del pipeline es contrastable**. Un
resultado incontrastable no es un dato. No es un experimento.

---

## 2. Qué queda como resultado de H2

A pesar del cierre negativo, la corrida produjo **un resultado real y
generalizable**, que se archiva:

**2.1 Taxonomía de modos de fallo bajo perfil estricto sin guía humana.**
Cinco categorías cualitativamente distintas (no grados del mismo fallo):
- Tipo A: reasoning atascado (`content=None` por agotamiento de tokens).
- Tipo B: emisión truncada (`finish_reason: length`).
- Tipo C: parálisis por rigor (meta-comentario sin transcripción).
- Tipo D: alucinación degenerativa (bucle de repetición).
- Éxito honesto: declaración de imposibilidad de lectura.

**2.2 Observación sobre variabilidad entre modelos.**
La varianza entre modelos es un orden de magnitud mayor que la varianza
entre condiciones de prompt dentro del mismo modelo. N=5, no concluyente,
pero direccional.

**2.3 Observación sobre dependencia modelo-perfil.**
El mismo perfil produce abstención honesta en un modelo y parálisis por
análisis en otro. Hipótesis a testear, no hallazgo. Se archiva como
hipótesis, no como resultado.

**2.4 Confirmación operativa.**
Los modelos multimodales comerciales, en tareas no genéricas sobre
escritura histórica escasamente representada en corpus, sin elemento
humano guiando, se descontrolan, se paralizan o alucinan. No hay manera
sencilla de controlarlos mediante prompt engineering puro. Esto es
consistente con la literatura sobre HITL y sobre tareas críticas
asistidas por IA, y no es específico del ge'ez.

**2.5 Nota metodológica publicable.**
"Corrimos N llamadas sobre folios de BnF Éthiopien 49 con tres modelos
multimodales bajo perfil estricto. Documentamos cinco modos de fallo
distintos. Concluimos que sin ground truth verificable y sin capacidad
de intervención humana calificada, el pipeline no produce datos
interpretables." Esto es honesto y potencialmente útil para otros.

Lo que **NO** queda como resultado:
- H2 no se valida ni se refuta.
- No hay comparación de fidelidad entre modelos.
- No hay comparación de fidelidad entre condiciones.
- No hay conclusiones sobre la calidad del perfil Tlacuilo en abstracto.
- No hay conclusiones sobre capacidad de lectura de ge'ez por ningún
  modelo específico.

---

## 3. Motivos técnicos reconocidos del fallo (para constancia)

- `max_tokens=8000` insuficiente para modelos con reasoning habilitado.
- Sin ground truth verificado contra el cual medir fidelidad.
- Sin Levenshtein ge'ez-ge'ez (no había fuente en ge'ez disponible al
  momento del pre-registro).
- N=5 folios sin potencia estadística.
- 1 llamada por celda, sin estimación de varianza intra-modelo.
- Confound de modelo no controlado.
- Perfil Tlacuilo diseñado para uso dialógico humano-AI, no para
  corridas autónomas single-shot. Usado fuera de contexto de diseño.
- El operador no escribe ge'ez y no puede producir transcripción manual
  independiente. Sin esta capacidad, la Pasada 2 del rediseño era
  inviable como control.
- Hardware del operador insuficiente para correr modelos locales que
  podrían haber permitido iteración sin costo por llamada.

Ninguno de estos motivos, individualmente, habría bastado para cerrar la
línea. La combinación sí.

---

## 4. Material crítico disponible (registrado, para uso futuro)

El operador tiene acceso completo verificado a:

- **Dillmann, A. (1851).** *Liber Henoch Aethiopice, ad quinque codicum
  fidem editus, cum variis lectionibus.* Lipsiae: sumptibus F.C.G.
  Vogelii. Texto ge'ez crítico.
- **Charles, R. H. (1912).** *The Book of Enoch or 1 Enoch.* Oxford:
  Clarendon Press. Traducción al inglés con notas.
- **Flemming, J., & Radermacher, L. (1901).** *Das Buch Henoch.* Leipzig:
  J.C. Hinrichs. Ge'ez + alemán paralelo.
- **Laurence, R. (1821).** *The Book of Enoch the Prophet.* Londres.
  Traducción al inglés.
- **Sacy, S. de (1800).** *Notice sur le livre d'Enoch.* Notices et
  extraits des manuscrits de la Bibliothèque nationale, vol. 6.

**Acceso confirmado por el operador, incluyendo verificación visual de
páginas de Dillmann y Flemming en esta misma sesión.** No es ya material
"reportado pero no verificado". Es material en mano.

Esto habilita la nueva línea descrita en §5.

---

## 5. Nueva línea: traducción al español de ediciones críticas

### 5.1 Qué es

Traducir al español, con atribución explícita, las ediciones críticas
existentes del Libro de Enoc (y potencialmente otros textos del canon
etíope) desde sus lenguas de publicación originales.

### 5.2 Por qué es una línea metodológicamente limpia

1. **Hay ground truth.** El texto fuente existe, es citable, está a la
   vista. La tarea es transformación, no reconstrucción desde imagen
   ambigua.
2. **Las lenguas de origen están bien representadas en corpus.** Alemán
   académico del s. XIX, inglés de Clarendon, francés de Notices et
   extraits. No hay escasez de datos como con el ge'ez.
3. **Atribución limpia.** Se traduce a Dillmann traduciendo a Dillmann.
   No se inventa un texto que no existe.
4. **Cambio epistemológico del rol del modelo.** En traducción alemán→
   español o inglés→español, el modelo no decide qué dice el manuscrito.
   Reformula lo que ya está decidido por una edición crítica del s. XIX.
   El modelo es herramienta, no oráculo.
5. **Verificabilidad.** Cualquier lector con acceso al original puede
   contrastar la traducción contra la fuente. No hay caja negra.

### 5.3 Protocolo propuesto (borrador, para refinar)

- Fuente primaria: una edición crítica por texto (p.ej. Charles 1912
  para el Enoc etíope, por ser la más citada en lengua inglesa).
- Fuentes secundarias: las demás ediciones, como contraste cuando hay
  divergencia entre ediciones.
- Traducción asistida por modelo, con revisión humana sobre cada párrafo.
- Registro obligatorio: para cada párrafo, qué edición se está
  traduciendo, y qué diverge con las otras ediciones, si diverge.
- Output: texto en español con aparato de procedencia.
- Sin ge'ez. Sin imágenes. Sin OCR. Sin HTR. Sin RAG.

### 5.4 Presupuesto

- Coste estimado de traducción de un texto completo del tamaño del
  Libro de Enoc vía modelo comercial: órdenes de magnitud por debajo
  del pipeline ge'ez.
- Presupuesto asignado: a definir por el operador. No hay prisa.
- Comparación relevante: por el costo de un solo folio mal transcrito,
  se traducen varios capítulos de un texto crítico bien establecido.

### 5.5 Alcance declarado

- **NO es trabajo filológico original.** Es divulgación.
- **NO pretende sustituir a las ediciones críticas.** Las cita.
- **NO pretende fidelidad al manuscrito.** Fidelidad a la edición
  crítica traducida, que es lo que se está traduciendo.
- **SÍ pretende poner en español material que hoy es de difícil acceso
  fuera de ámbitos académicos.**

### 5.6 Lo que NO se va a hacer en esta línea (todavía)

- No se amplía a otros libros del canon etíope sin traducir (hay trabajo
  real ahí, pero fuera de alcance por formación, capacidades, hardware
  e intereses del operador, según declaración registrada).
- No se traduce directamente desde ge'ez. Solo desde las lenguas de
  publicación de las ediciones críticas.
- No se publica nada hasta tener un capítulo completo revisado y con
  aparato de procedencia.

---

## 6. Reflexiones del operador (registradas)

Textual, para no perderlas:

> "Los modelos NUNCA podrán hacer lo que los humanos. No son
> inteligentes, ni creativos, simplifican, promedian, aplanan, y lo
> vuelven todo promedio."

> "La llamada 'caja negra' del Deep Learning no son más que una cantidad
> inmensa de matrices compuestas por números que se suman, restan y
> multiplican."

> "Los GANs son elementos complejos y polémicos en el área del
> entrenamiento de los modelos, porque se fabrican imágenes falsas
> positivas para que los modelos aprendan a discriminar. Esto en el
> terreno de las falsificaciones se vuelve una paradoja."

> "Mi iMac de finales del 2013, mi tarjeta NVIDIA es mucho más potente
> que las 32 tarjetas gráficas que conectó el Dr. Buck, y sin embargo
> estoy imposibilitado por arquitectura a siquiera acercarme a lo que él
> logró."

> "No pretendo que nadie y ningún modelo me sustituya a mí en ningún
> momento mientras viva. No me escondo y doy la cara."

**Nota de la bitácora sobre estas reflexiones:**

- La afirmación "los modelos NUNCA podrán..." es una predicción, no un
  hecho. Las predicciones sobre el futuro de la IA tienen historial
  pésimo. La formulación más defendible es: *con la arquitectura actual,
  los datos actuales, y este tipo de tarea, no pueden hacer lo que un
  humano hace*. Eso sí es verdadero y observable.
- La mención de cadenas de Markov es direccionalmente correcta pero
  técnicamente imprecisa. Los modelos autoregresivos comparten con
  Markov la dependencia de estado, pero el estado es el contexto
  completo, no solo el token anterior. La dependencia no es markoviana
  en sentido clásico; es de orden variable mediada por atención.
- La "caja negra" como opacidad de escala, no de principio: las matrices
  son legibles, el efecto agregado de millones de operaciones sobre
  millones de parámetros no admite interpretación semántica directa.
  Es una opacidad práctica, no teórica.
- La paradoja GPU (más FLOPS que Buck 2003, incapaz de reproducir su
  resultado) es real, pero la causa principal no es cómputo bruto: es
  obsolescencia de la pila de software. CUDA abandonó Kepler/Maxwell
  hace años. El hardware podría, el ecosistema no lo soporta.

Estas reflexiones se archivan como posición del operador, no como
conclusiones técnicas de la bitácora.

---

## 7. Estado final de H2

| Aspecto | Estado |
|---|---|
| Corrida experimental | Ejecutada (30 llamadas, 2026-10-04) |
| Datos crudos | Archivados |
| Ground truth | Inexistente |
| Rediseño de tres pasadas | No ejecutado, descartado |
| Publicación | Nota metodológica negativa, pendiente de redacción |
| Presupuesto asignado | Cero |
| Reapertura | Solo si aparece ground truth verificable + capacidad humana de intervención calificada |

H2 queda cerrado.

---

## 8. Pendientes de la nueva línea

**Coste cero:**
- [ ] Decidir edición crítica de partida (Charles 1912 es la candidata).
- [ ] Escribir protocolo de traducción con aparato de procedencia.
- [ ] Elegir capítulo piloto (¿1 Enoc 1–5? ¿1 Enoc 6–11?).
- [ ] Definir formato de salida (Markdown, LaTeX, ambos).

**Coste bajo:**
- [ ] Correr traducción de capítulo piloto.
- [ ] Revisar párrafo por párrafo con original a la vista.
- [ ] Contrastar contra las otras ediciones cuando haya divergencia.

**Coste medio, después del piloto:**
- [ ] Si el piloto funciona: escalar a libro completo.
- [ ] Si no: revisar protocolo antes de escalar.

**NO hacer:**
- [ ] No traducir desde ge'ez.
- [ ] No usar OCR ni HTR.
- [ ] No reabrir H2 sin cambio de condiciones materiales.
- [ ] No publicar hasta tener capítulo completo revisado.

---

## 9. Frase de cierre

> "No sé si lo que estoy diciendo tiene algún sentido, pero es lo que he
> aprendido sobre el camino. No pretendo que nadie y ningún modelo me
> sustituya a mí en ningún momento mientras viva."

Registrado. La decisión de cerrar H2 y abrir la línea de traducción es
coherente con esta posición. No es rendición. Es reconocimiento de
alcance y de herramientas.

---

*Fin de la bitácora de cierre. H2 cerrado. Nueva línea abierta. Revisar
dentro de dos semanas para decidir capítulo piloto.*
