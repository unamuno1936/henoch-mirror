# 2026-10-03 — Ajuste del experimento H2: alcance, modelos y metodología

**Proyecto:** Henoch
**Autor:** Marco Antonio Vázquez Elías
**Estado:** Decisión metodológica

---

## Contexto

Tras la revisión del Capítulo 4 de *Rediscovering Enoch?* y la
validación de las sospechas sobre Sarnelli, Ludolf y el Vaticano,
se hace necesario **ajustar el experimento de transcripción** para
que sea viable sin violar la metodología.

Las siguientes decisiones se toman **antes de ejecutar** el
experimento y quedan congeladas en este archivo.

---

## Decisiones

1. **Alcance reducido**: solo **5–10 folios del principio** del
   BnF Éthiopien 49. Es material suficiente para cotejar contra
   Sacy (que tradujo caps. 1–16, 22, 31).

2. **H2**: contrastar **Flash simple vs. dos modelos más** (Pro y
   Flash extended). Una sola llamada por modelo por folio.

3. **Sin intervención humana**: no es posible hacerla ahora. El
   autor lo llama "megacuchareo" — un esfuerzo manual enorme que
   además introduciría sesgo.

4. **Sin repeticiones controladas**: hacer tres llamadas separadas
   con el mismo input solo demostraría que el modelo puede ser
   inconsistente. Si eso es valioso, se documenta como hallazgo
   secundario, pero **no es el objetivo de H2**. El autor lo dice:
   "si eso es valioso, lo fundamentamos".

5. **Prompts idénticos**: no se pueden ajustar los prompts para la
   segunda y tercera llamadas sin violar la metodología. La
   comparación debe ser limpia.

6. **Woide no disponible**: no está digitalizado o no está a la
   mano. Se documenta como limitación.

---

## Justificación

- **5–10 folios** son suficientes para cotejar contra Sacy y
  validar el diseño.
- **Una sola llamada** por modelo evita la variabilidad de la API
  y mantiene el diseño limpio.
- **Sin intervención humana** evita el sesgo del investigador.
- **Sin repeticiones** evita confundir inconsistencia con
  fidelidad.
- **Prompts idénticos** garantizan que las diferencias se deban al
  modelo, no al prompt.

---

## Limitaciones declaradas

- **Woide no disponible**: no se puede triangular con su
  transcripción.
- **Laurence no es ground truth**: usó otros manuscritos, no BnF
  Éthiopien 49.
- **Sacy es el único ground truth directo**, con las reservas ya
  declaradas.
- **No hay ground truth independiente** para los folios que Sacy
  no tradujo.
- **La triangulación completa** (Sacy + Apéndice Hessayon + Woide +
  Laurence) queda pendiente hasta que se digitalicen o localicen
  las fuentes faltantes.

---

## Diseño final

| Variable        | Valor                                       |
|-----------------|---------------------------------------------|
| Folios          | 5–10 del principio de BnF Éthiopien 49      |
| Modelos         | Flash simple, Flash extended, Pro           |
| Llamadas        | 1 por modelo por folio                      |
| Prompt          | Idéntico para todos                         |
| Ground truth    | Sacy (latín, caps. 1–16, 22, 31)            |
| Métricas        | CER, WER, tasa de alucinación, tasa de abstención |

---

## Advertencia sobre H2

El autor advierte: "no puedo trabajar con el manuscrito del
Vaticano, quizás lo pudiera hacer con otro de los manuscritos de
Bruce, los que están en Oxford, pero la copia es mucho mejor que
los originales, porque ahí sí nuestro modelo de IA va a alucinar
fuerte, porque va a costar mucho trabajo".

Por tanto, el experimento se limita a BnF Éthiopien 49. Los otros
manuscritos quedan como posibilidad de mejora posterior, no como
base del experimento actual.

---

## Pendientes

- [ ] Congelar el diseño en un archivo `.md` en el repo.
- [ ] Escribir el script del experimento.
- [ ] Ejecutar las llamadas.
- [ ] Analizar sin modificar el diseño.

---

## Referencias

- Liu, C., et al. (2025). *More Thinking, Less Seeing?*
  arXiv:2505.21523.
- Mohanty, A., et al. (2025). *The Future of MLLM Prompting is
  Adaptive*. arXiv:2504.10179.
- Tian, X., et al. (2026). *More Thought, Less Accuracy?*
  ICLR 2026.
