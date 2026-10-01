# Metáfora del bibliotecario y prueba español-primero (2026-09-27)

## 1. La metáfora del bibliotecario (refinada por el autor)

Un LLM no es un bibliotecario con catálogo. Es un bibliotecario que camina
a ciegas por la biblioteca, encuentra patrones por proximidad física, y se
orienta por vecindad. No recupera por índice, navega por espacio latente.

Analogía del autor: caminar por la Facultad de Filosofía y Letras, encontrar
patrones sin conocer el orden del catálogo, orientarse por intuición hacia
donde podría estar lo que se busca.

El perfil Tlacuilo añade reglas internas de honestidad: "si no estoy seguro
de lo que veo, lo digo, no lo invento." Es un bibliotecario con ética de
incertidumbre.

Esta metáfora es del autor, no mía. Va al preprint en la sección teórica.

## 2. Prueba español-primero (diseño propuesto)

Secuencia propuesta:
  A) Transcripción → isomorfa español → legible español
  B) Transcripción → isomorfa inglés → legible inglés

**Corrección técnica**: pedir A y B en LLAMADAS SEPARADAS. Si se piden en
la misma llamada, el modelo puede usar el inglés como pivote interno para
producir el español, contaminando la prueba. Separadas, el inglés no puede
ser pivote.

Razón del diseño: el español tiene poco corpus memorizado de Enoc. Si el
modelo produce español coherente, hay generación real. Si falla o produce
incoherencia, confiesa límite. En ambos casos, dato.

## 3. Web vs API: no es magia, son sistemas distintos

El perfil parece comportarse distinto en web vs API. Razones posibles:
  - System prompt interno de Google (en web) que el usuario no ve.
  - Versión del modelo distinta (web no hasheable).
  - Herramientas activas (búsqueda, código) en web.
  - Memoria de conversación (si no es Temporary Chat).
  - Temperatura interna desconocida en web.

No es que el perfil "funcione mejor" en web. Es que interactúa con un
sistema distinto. Es dato, no ventaja.

## 4. Turing: precisión

Turing (1950) no usó "fricción" ni "elemento novedoso". Discutió la
objeción de Lady Lovelace ("la máquina solo puede hacer lo que le
ordenamos") y respondió que las máquinas pueden sorprendernos.

La "fricción" es término operativo del autor, pero la idea es turingiana.
Cita sugerida:
  Turing, A. M. (1950). Computing machinery and intelligence. Mind, 59(236),
  433–460. §6.4 (objeción de Lady Lovelace).

## 5. Incertidumbre estocástica vs emergencia

Distinción importante:
  - Incertidumbre estocástica: sampling con temperatura > 0. Variabilidad
    entre runs, pero sin novedad estructural.
  - Emergencia: capacidades que aparecen con escala (Wei et al. 2022). No
    es lo mismo que el sampling.

Extensión posible del Track Web: repetir la prueba español-primero 3 veces.
Si outputs son estructuralmente distintos → más que sampling.
Si son variantes del mismo patrón → sampling.

## 6. Estatus
- Track Web: PLANIFICADO, no ejecutado.
- Prueba español-primero: PENDIENTE.
- Prueba de ceguera: HECHA.
- OCR Tesseract: HECHO.
