# Libro de Henoch / Tlacuilo

## 📖 Qué es esto

Un proyecto de investigación independiente sobre la transmisión textual del
**Libro de Enoc**, desde Génesis 6 hasta la edición crítica de Knibb (1978).
Pero es, al mismo tiempo, un **estudio de caso sobre colaboración humano-IA**
documentado con rigor: cada prompt, cada bitácora, cada error y cada
corrección.

No es un proyecto de software. No es un paper académico en el sentido
tradicional. Es un **cuaderno de laboratorio abierto** de un investigador que
no tiene laboratorio, que trabajó varios meses desde un teléfono Android con Termux y
desde mayo de este año, pudo recuperar su iMac de finales del 2013, a la cual desde principios del 2025, le instalo con grandes trabajo una distribución de Linux llamada Linux Mint, pase por Linux Mint Debian y terminé usando Debian 13 Trixie, sobra decir que el cambio del MacOS a Linux en una iMac, fue durísimo. Por estas y muchas otras razones he decidido documentar hasta el último detalle de cómo piensa, cómo pregunta y cómo se equivoca.

---

## 🧑‍🔬 Sobre el autor

Soy **Marco Antonio Vázquez Elías**, médico cirujano mexicano, 60 años.
Ejerzo la medicina desde hace décadas. En **abril de 2025**, un quiebre
—que yo mismo provoqué de varias formas— me sacó de mi zona de confort de
manera violenta. En algunas cosas me equivoqué mucho. En otras fui
brutalmente asertivo. Las dos cosas son verdad al mismo tiempo. He aprendido
a asumir las consecuencias de mis actos: no lloro por ellas, me supero, y
trato de no volver a equivocarme. El trato injusto que recibí me lo reservo,
por ahora, para mí. **Lo que me va a validar es mi trabajo, no mis quejas.**

Aprendí a programar desde cero. Aprendí a usar Termux en un teléfono Android.
Aprendí Rust, Julia, C, C++, Go, Python y ensamblador —no como experto, ni siquiera programador, sino
como alguien que necesitaba resolver problemas concretos. Acumulé unos 90 GB
de scripts en ese proceso. Aprendí a moverme en manuscritos etiopes en ge'ez para trabajar con el Libro de Henoch en su única versión completa que se conocé hasta ahora. No sé ni una palabra de dicho idioma, pero he podido, y lo que se ve acá es ese proceso, con sus errores, equivocaciones, dudas y, finalmente, los aciertos. Aprendí a usar modelos de lenguaje, las distintas IAs, como asistentes de investigación,
no como oráculos.

No cuento esto como una historia de superación. Lo cuento porque es **el dato
metodológico más importante de este proyecto**: si un individuo, en
condiciones adversas y sin formación técnica formal, puede construir un
pipeline de investigación reproducible, entonces el problema de la
accesibilidad a la investigación no es de capacidad. Es de **diseño
institucional**. Aunque lo mío, fue un instinto muy potente de supervivencia, y para ello estar en modo creativo, preservó mi salud mental y física. 

Comí cacahuates japoneses y amaranto y agua. Dormite en un albergue y pase varios meses en la Terminal 1 del ASeropuerto Internacional de la CDMX, no es melodrama, ni un discurso de superación personal y mucho menos un reproche. Es lo que es, una ruta de viaje. Quizás, menos amable que la de James Bruce, el escoces que trajó a Henoch a Europa desde Etiopía a finales del siglo XVIII, La analogía perfecta es la del amaranto: cuando se le reduce el agua, no solo sobrevive; produce más
semilla. Como los adaptógenos: crecen en la madera, en el frío, en la
adversidad, y producen compuestos que ayudan a otros organismos a resistir.
No todos los individuos responden igual al estrés. Algunos se rompen. Otros
se reorganizan. **Este proyecto es el caso documentado de uno que se
reorganizó.** No es representativo. No es prescriptivo. Es evidencia de que
el fenómeno existe. Pero no es para todos, se puede romper la gente, no tengo duda. 

---

## 🧠 Posicionamiento: no soy programador

Tiene que quedar muy claro: **aprender a programar, en el sentido formal, no
lo he aprendido.** Si me preguntan comandos básicos, no sabría aplicarlos sin
contexto. No pienso como un programador. Una de mis ventajas. 

Pero si me preguntan si en un teléfono Android podría hacer cosas en Python
así, nada más, diría que no —y explicaría por qué. Habría que crear un
proceso pausado, que se dé tiempo para fragmentarse, para ir limpiando la
basura que se genera, para cuidar la memoria. Las limitaciones de Python, que
está lejos del metal. Los cálculos en R también están lejos del metal. Por eso
Julia. Por eso Rust. Por eso C++, que es un arma de fuego: puede reventarte un
proyecto o un hardware en un solo descuido. Todo eso yo lo sé.

Soy un buen gestor de proyectos. Sé escoger herramientas, sé encontrar
atajos, sé construir perfiles. Pero formalmente no soy programador, reitero no pienso
como uno. Soy yo pensando de forma no reduiccionista y fragmentaria, porque es absurdo autolimitarse con las especizaliaciones, que son más una excusa para no adentrarse en las complejidades de un ser humano. Mi opinión. soy médico general, con orgullo y competencias, a las pruebas, me remito. Sé investigar y lo que hago con el fin de resolver problemas, ese es mi motor y la razón de mi existencia. No pararé de dudar y preguntar, la certeza no va conmigo. 

Lo que sí puedo es **usar y aplicar**. He aplicado hasta Refal, la herramienta
lógica soviética, que es compleja. La entendí y la usé. No me sé cada comando
de memoria, pero sé perfectamente para qué sirve, para qué sirve Prolog, para
qué sirven las demás. No las pongo de adorno. **Diseño sistemas, diseño
soluciones, diseño atajos, y me los construyo yo mismo.** Soy tozudo,
persistente, resiliente. No acepto un "no" como respuesta. Pero tampoco me
obsesiono estúpidamente con que las cosas tengan que salir de una sola forma.

Eso es lo que me he construido. Y me lo construí porque mi respuesta ante
situaciones límite fue **ordenarme mentalmente como pude** y, con un teléfono,
empezar a construir cosas. Esa construcción fue la que me permitió sobrevivir
al desorden, al desastre a mi alrededor, a la indefensión, a la vulnerabilidad
absoluta. Me construí una coraza que ahora, cuando lo pienso, no sé ni cómo,
pero hay **90 GB que lo justifican**. Y ahora lo estoy ordenando en un
teléfono. Imposible, pero ahí está.

---

## 🧠 Método híbrido humano-IA

Este proyecto **usa inteligencia artificial de forma intensiva y
documentada**. No lo esconde. Lo estudia.

- Los scripts son míos. La estrategia de consulta también.
- La IA es una herramienta, no una autoridad.
- Cada hipótesis se clasifica como **evidencia documental** o **duda
  razonable**.
- Las bitácoras son, en sí mismas, el corpus de estudio del método.

### Clasificación de hipótesis

| Categoría | Significado | Presentación |
|---|---|---|
| **Evidencia documental** | Fuente primaria o secundaria que lo confirma | Hecho, con cita |
| **Duda razonable** | Silencio documental o indicios, sin prueba | Hipótesis declarada como tal |

Esta distinción no es cosmética. Es la línea que separa la especulación
publicable de la afirmación irresponsable.

---

## 🔬 Ejemplo documentado de pensamiento asociativo

El 30 de septiembre de 2026, mientras trabajaba en el proyecto, me encontré
con un video de YouTube: una entrevista del neurólogo Dr. David Perlmutter
al Dr. M. Marc Abreu sobre un caso de reversión de ELA mediante hipertermia
cerebral controlada. Lo compartí con una amiga rehabilitadora que tiene una paciente
con ELA, y le escribí lo siguiente:

> *"Me acabo encontrar esto, no tengo claro si es una realidad o no, pero hay
> algo en los mecanismos de la fiebre que me ha puesto a pensar. Aclaro que
> es muy posible que no sirva, o sea útil solo para ciertos pacientes. La
> fiebre y los mecanismos que echa a andar podría componer en teoría algunas
> cosas que suceden con la ELA, me refiero al plegamiento anómalo de ciertas
> proteínas, y eso sí creo que es un dato legítimo. No lo dice así este
> médico brasileño, pero yo lo entendí así."*

Y más tarde, abundé:

> *"Tengo dudas en cuanto a cómo eleva la temperatura del cerebro, si es algo
> seguro y si está respaldado por datos sólidos. Los costos no deben ser
> bajos, pero la fiebre sí puede revertir esas proteínas mal plegadas y
> explicar alguna de las mejorías que él ha visto. De ahí a que sea aplicable
> a todos los casos y ofrezca algo más, es muy complicado de asegurar. Pero
> los tratamientos actuales de ELA no ofrecen tampoco gran cosa; son muy
> caros y han sido comparados con placebos. El principal error del modelo
> predominante actual es pensar que con UNA sola molécula o unas cuantas vas
> a resolver un estropicio del tamaño de la ELA; eso es imposible y es
> carísimo. En cambio estos hongos ofrecen algo más que una molécula, son un
> montón de moléculas, y es ahí en donde puede haber una oportunidad."*

### Lo que este episodio revela

Esta cadena de asociaciones no es un producto de la IA. Es el resultado de un
**pensamiento interdisciplinario forjado por la experiencia vital, la
neurodivergencia y la necesidad de resolver problemas sin recursos
institucionales**. La IA documenta, organiza y verifica. El humano conecta,
intuye y decide qué vale la pena investigar.

El autor conectó:

1. La observación histórica de Wagner-Jauregg (Nobel 1927) sobre fiebre
   inducida por malaria para tratar la neurosífilis.
2. El hallazgo de que en ambos casos (neurosífilis y ELA) aparece la proteína
   TDP-43 mal plegada.
3. El mecanismo de las **proteínas de choque térmico (HSPs)** como chaperonas
   moleculares.
4. La literatura sobre **adaptógenos** (hongos como *Hericium erinaceus* o
   compuestos como la withaferina A) que activan esas mismas vías.
5. La observación botánica de que el estrés hídrico controlado mejora la
   producción de ciertas plantas (el amaranto).
6. La hipótesis, contra el modelo dominante, de que las enfermedades
   neurodegenerativas son **sistémicas**, no exclusivamente cerebrales.

Esta hipótesis se clasifica como **duda razonable con mecanismo biológico
plausible**. No es un hecho. No se presenta como una cura. Se presenta como
una línea de investigación que merece ser explorada con cohortes bien
seleccionadas y rigor metodológico.

---

## 📂 Estructura del repositorio

henoch/
├── scripts/ # Código fuente (AGPLv3)
├── worklog/ # Bitácoras de sesión (CC BY 4.0)
├── config/ # Metadatos, criterios preregistrados
├── traducciones/ # Textos de fuentes primarias
├── hashes/ # Verificación de integridad
├── logs/ # Registros de ejecución
├── resultados/ # Métricas y análisis
├── prompts/ # Sistema de prompts documentado
├── fuentes/ # Corpus bibliográfico (metadatos; PDFs en .gitignore)
├── README.md # Este documento
├── LICENSE-CODE # AGPLv3
└── LICENSE-DOCS # CC BY 4.0

---

## ⚖️ Licencias

Este proyecto utiliza un **modelo de licencia dual**, diferenciando entre
tipos de contenido:

- **Código** (scripts, pipelines, notebooks): **AGPLv3**
- **Documentación** (bitácoras, textos, análisis): **CC BY 4.0**

### ¿Por qué dual?

Porque el software y la documentación son obras de naturaleza distinta. La
AGPLv3 protege el código frente a su uso en servicios en red. CC BY 4.0
permite la máxima difusión y reutilización del contenido textual, con la sola
obligación de atribuir.

### Transparencia radical

Este proyecto **no reserva** su metodología. Publica los prompts, la secuencia
de consultas, la curaduría de fuentes y las bitácoras completas. El valor de
este trabajo no está en una fórmula secreta: está en la manera irrepetible en
que un individuo concreto piensa, pregunta y se equivoca. La fórmula no es un
procedimiento. La fórmula es el autor.

---

## 🚫 Sobre los vetos al uso de IA

Algunos repositorios, como Codeberg, excluyen proyectos que usan IA de forma
intensiva. Este proyecto **no se somete a ese veto**. Usar IA no es hacer
trampa. Es usar las herramientas disponibles en el siglo XXI para hacer
preguntas del siglo I. Un investigador independiente sin acceso a
infraestructura institucional merece las mismas oportunidades que uno con
presupuesto.

---

## 🌍 Idiomas

Este proyecto es multilingüe por vocación. El README y las bitácoras se
publican en:

| Idioma | Estado | Notas |
|---|---|---|
| **Español** (es) | ✅ Primario | Lengua materna del autor |
| **Inglés** (en) | ✅ Primario | Lengua franca de la investigación |
| **Portugués** (pt) | 🔄 En curso | Conexión con Brasil y la comunidad latinoamericana |
| **Otros** | ⏳ Planificado | Árabe, hebreo y amhárico son candidatos naturales |

---

## 📬 Contacto

- **GitLab** (repositorio principal):
  [republica_imperfecta-group/henoch](https://gitlab.com/republica_imperfecta-group/henoch)
- **GitHub** (espejo de solo lectura):
  [unamuno1936/henoch](https://github.com/unamuno1936/henoch)
- **Email**: `1936.unamuno.libre@proton.me`

---

## 📝 Nota final

Este README no es una declaración de resultados. Es una **declaración de
método**.

No afirmo que la fiebre cure la ELA. No afirmo que los hongos adaptógenos
sean un tratamiento. No afirmo que mi caso sea replicable. Afirmo que hay
**patrones** —el estrés controlado, las chaperonas, el plegamiento proteico,
la respuesta sistémica— que merecen ser investigados con rigor, y que mi
manera de conectar esos patrones, forjada en circunstancias atípicas, produce
hipótesis que otros no formulan.

Si alguien entiende esto, bienvenido. Si nadie lo entiende, también. El
trabajo está hecho y está documentado. Eso es lo que importa.

---

*Última actualización: 2026-10-01*
*Versión: 2.0*
