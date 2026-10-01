# Estrategia de Publicación ante el Escándalo del Goncourt (2026-09-27)

## Contexto
El escándalo del Premio Goncourt 2026 ha puesto el foco mediático sobre el uso de IA en la creación literaria. Esto genera un ambiente de sospecha que podría afectar la recepción de nuestro preprint si no se maneja con cuidado.

## Estrategia de blindaje
1. **Transparencia radical:** El preprint declarará explícitamente que se utilizó IA (Gemini, DeepSeek, etc.) como herramienta de investigación, no como autora. El perfil Tlacuilo se declara en Métodos, no en Resultados.
2. **Cadena de custodia:** Hashes SHA-256 de todos los artefactos, logs con timestamps UTC, worklogs detallados. Esto permite auditar cada paso del proceso.
3. **Enfoque en el método, no en el producto:** El preprint no presenta la transcripción como un producto final, sino como un *objeto de estudio* para investigar el comportamiento de los LLM. El "producto" es el análisis metodológico.
4. **Declaración de limitaciones:** Se incluirá una sección explícita sobre las limitaciones del estudio, incluyendo la contaminación por memoria paramétrica y los falsos positivos de seguridad.
5. **No publicar el perfil Tlacuilo completo:** El perfil se reserva. Se declara su existencia y sus principios generales, pero no se reproduce íntegramente para evitar que sea utilizado sin el contexto del estudio.

## Implicación para el preprint
El preprint debe posicionarse como un estudio metodológico sobre el comportamiento de los LLM en tareas de humanidades digitales, no como una herramienta de transcripción automática. El foco está en la *interacción humano-modelo*, no en el output del modelo por sí solo.
