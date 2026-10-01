# Incidencia: Tesseract sin modelo etíope + aclaración conceptual (2026-09-27)

## 1. Problema técnico
El script `15_ocr_tonto_geez.py` falló con:
`Error opening data file /usr/share/tesseract-ocr/5/tessdata/script/Ethiopic.traineddata`

## Causa
Se instaló el wrapper Python (`pytesseract`) pero NO los datos del modelo
etíope a nivel de sistema. Son dos instalaciones separadas.

## Solución
sudo apt install tesseract-ocr tesseract-ocr-script-ethi
Verificar: tesseract --list-langs | grep -i eth

## 2. Aclaración conceptual: ¿usar OCR es usar IA?
Sí. EasyOCR, Tesseract (v4+ con LSTM), PaddleOCR, Gemini y todos los LLM
son sistemas de inteligencia artificial / machine learning.

La distinción relevante para el estudio NO es "IA vs no IA", sino:
  - IA como caja negra sin supervisión  → riesgo de alucinación silenciosa
  - IA como instrumento con operador humano informado → objeto del estudio

El preprint declara explícitamente:
  - Uso de LLM (Gemini, GLM, DeepSeek, GPT, Qwen) vía OpenRouter.
  - Uso de OCR basado en aprendizaje profundo (Tesseract, respaldo PaddleOCR).
  - Contribución humana: diseño experimental, perfil Tlacuilo, verificación,
    interpretación.

La transparencia radical es el escudo contra el escenario tipo Goncourt,
no la negación del uso de IA.

## 3. Estatus
PENDIENTE: instalar tesseract-ocr-script-ethi y re-ejecutar el script.
PaddleOCR instalado pero no se usará salvo fallo de Tesseract.
