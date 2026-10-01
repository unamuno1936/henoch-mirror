# Track Web (exploratorio) y control español (2026-09-27)

## 1. Validez metodológica del Track Web

**Decisión**: el Track Web (Gemini web, cuenta gratuita virgen, con y sin
perfil Tlacuilo) es un canal EXPLORATORIO, no confirmatorio. No compite
con el Estudio 1 (API + OpenRouter + perfil v2.0 congelado + BnF 49).

**Condiciones de validez**:
1. Declaración explícita en bitácora y preprint como Track Web.
2. Cuenta limpia de verdad (sin historial de ge'ez, Enoch, Tlacuilo, BnF).
3. Hash del perfil y del wrapper en el momento de la prueba.

**Razón**: el canal web no permite fijar versión del modelo, no expone
`reasoning_details` de forma hasheable, y no tiene cadena de custodia
criptográfica. Pero sí permite ver comportamiento ecológico del perfil.

## 2. Control español: el hallazgo metodológico más importante del día

**Observación**: el Libro de Enoc tiene:
- Original arameo (fragmentos Qumrán).
- Griego (Codex Panopolitanus, citas de Syncellus).
- Ge'ez (BnF 49, Rylands 23, tradición etíope extensa).
- Inglés (traducciones modernas: Charles 1912, Knibb 1978, Nickelsburg
  2001, Charlesworth 1983, etc.).
- **Español: casi nada, y moderno (Piñero 2000s, BAC).**

**Implicación experimental**: la traducción al español es el control más
limpio del pipeline. Si el modelo produce una traducción coherente al
español y distinta de las existentes, hay evidencia de traducción real.
Si coincide con una traducción española conocida, hay memorización
también en español. Si falla, falla.

**Diseño actual del wrapper** (correcto): el español se deriva de la
transcripción ge'ez, NO del inglés. Esto fuerza al modelo a no pasar
por el pivote inglés, donde podría recitar.

**Acción**: mantener este diseño. Probar en Track Web con el mismo wrapper.
Comparar outputs español con:
- Transcripción ge'ez del propio modelo.
- Traducciones inglesas recitadas.
- Traducciones españolas publicadas (Piñero, BAC) — sin reproducirlas,
  solo clasificando coincidencias.

## 3. Turing y el principio de interrogatorio adversarial

**Precisión**: Turing (1950, "Computing Machinery and Intelligence") no
usó la palabra "fricción", pero discutió la objeción de Lady Lovelace
("la máquina solo puede hacer lo que le ordenamos") y propuso el
interrogatorio adversarial como método para detectar comportamiento
no-memorístico.

**Aplicación en este estudio**: la prueba de ceguera contextual y el
Track Web con cuenta limpia aplican el principio turingiano. No basta
con observar si el modelo acierta: hay que observar si acierta cuando
no puede recitar.

**Cita sugerida**:
Turing, A. M. (1950). Computing machinery and intelligence. Mind, 59(236),
433–460. https://doi.org/10.1093/mind/LIX.236.433

## 4. Sobre la metáfora del "bibliotecario"

Refinamiento: el LLM no es un bibliotecario (no sabe lo que tiene, no
puede buscarlo). Es un ventrílocuo con memoria masiva. Cuando le pides
algo que está en su corpus, recita. Cuando le pides algo que no está,
improvisa o alucina.

El perfil Tlacuilo funciona como detector de mentiras: fuerza al
ventrílocuo a decir "no sé" o "no veo" en lugar de improvisar. Eso es
lo que la prueba de Track Web evaluaría.

## 5. Estatus

- Track Web: PLANIFICADO, no ejecutado. Depende de finalizar Estudio 1.
- Control español: PENDIENTE. Se ejecutará dentro del Track Web.
- Prueba de ceguera: HECHA (memorización confirmada).
- OCR tonto Tesseract: HECHO (817 caracteres, lectura real con errores).
