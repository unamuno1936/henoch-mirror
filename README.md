# Estudio preliminar: Tlacuilo vs. prompt genérico para ge'ez manuscrito

## Objetivo
Evaluar si un perfil especializado con protocolo anti-alucinación (Tlacuilo)
mejora la transcripción y traducción isomórfica/fluida de ge'ez manuscrito
en modelos de visión no entrenados específicamente en esa lengua.

## Diseño
- Corpus: BnF Éthiopien 49, 5 páginas seleccionadas al azar (semilla documentada).
- Excluidas: 1r, 1v, 2r, 2v (blanco); 59r-62v (transposición conocida).
- Modelos: 3 VLMs vía OpenRouter.
- Prompts: genérico vs. wrapper Tlacuilo.
- Réplicas: 3 corridas independientes por combinación (Diseño A).
- Traducciones: inglés y español, isomorfas y fluidas, sin pivote.
- Trazabilidad: worklog + Clew + hashes SHA-256 + logs OpenRouter con ZDR.

## Estructura
- config/       → lista de páginas, criterios pre-registrados, semilla
- scripts/      → selección, descarga, hashes, métricas, consistencia
- prompts/      → prompt genérico y wrapper Tlacuilo
- datos/        → outputs crudos por corrida
- resultados/   → CSV con métricas calculadas
- ground_truth/ → transcripción diplomática de referencia
- imagenes/     → folios descargados vía IIIF
- logs/         → hashes, logs de API, bitácora técnica

## Flujo
    bash scripts/00_instalar.sh
    source entorno/venv/bin/activate
    cd scripts
    python3 01_seleccionar_paginas.py --n 5 --seed 20260926
    python3 07_descargar_iiif.py
    python3 05_hashes.py --snapshot inicial
    # ... generar ground truth asistido ...
    python3 06_openrouter_client.py --modelo M1 --prompt generico --pagina 3r --run 1
    python3 02_metricas_cer_wer.py --batch
    python3 03_alucinaciones.py --init
    python3 04_consistencia.py
    python3 05_hashes.py --snapshot final

## Estado
Pre-registro: pendiente de fijar lista de páginas válidas.
Ejecución: pendiente.
Publicación: Zenodo (preprint, con DOI).

## Licencia
- Documentos: CC BY 4.0
- Scripts: AGPLv3
