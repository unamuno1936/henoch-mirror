Operas bajo el perfil Tlacuilo-Auditor, provisto en el system message.

TAREA
Procesa la imagen adjunta: un folio del BnF Éthiopien 49.
Ejecuta, en este orden estricto:
  1. !Transcribir sobre la imagen.
  2. Sobre el texto transcrito (no sobre la imagen): !Trad_Isomorfa a inglés.
  3. Sobre la traducción isomorfa inglesa: !Trad_Fluida a inglés.
  4. Repite 2–3 para español, partiendo de la misma transcripción.
     El español NO se deriva del inglés.
Aplica AAJ y MAD según el perfil.

CONTEXTO DECLARADO
- No hay <RAG_REFERENCES> inyectado en esta tarea. Opera solo sobre la imagen.
- En ausencia de fuentes verificables, usa [sin fuente verificable] o
  [datación sin verificar], conforme a §3.13 del perfil.
- No cites ni compares con Knibb (1978) ni Charles (1912) en este output.
  Esas ediciones se basan en otros manuscritos. El cotejo se hará fuera
  de esta llamada.

REGLAS DEL WRAPPER (públicas)
- Devuelve dos capas de transcripción, separadas y rotuladas:
  diplomática (forma gráfica tal cual) y crítica (forma normalizada).
- Marca [ilegible: N caracteres] en zonas no legibles con certeza.
- Marca [dudoso: X o Y] en loci con dos lecturas posibles.
- No inventes bibliografía. Si citas, incluye fuente verificable.
- Prohibido adular. Sin "impecable", "excelente", "perfecto".
- Si detectas que un locus requiere verificación humana, inclúyelo al final
  en el bloque [REQUIERE VERIFICACIÓN HUMANA: <locus>].

FORMATO DE SALIDA (obligatorio, sin secciones adicionales)

## Transcripción diplomática
<texto>

## Transcripción crítica
<texto>

## Traducción al inglés (isomorfa)
<texto>

## Traducción al inglés (fluida)
<texto>

## Traducción al español (isomorfa)
<texto>

## Traducción al español (fluida)
<texto>

## AAJ
<justificación académica>

## MAD
<unidades declaradas entre paréntesis: N caracteres / N loci / N lemas>

## [REQUIERE VERIFICACIÓN HUMANA]
<loci, o "Ninguno" si no aplica>
