# Incidencia: EasyOCR no soporta escritura etíope (2026-09-27)

## Problema
El script `15_ocr_tonto_geez.py` falló al intentar inicializar EasyOCR con
el código de idioma "am". Error: `ValueError: ({'am'}, 'is not supported')`.

## Diagnóstico
EasyOCR no incluye un modelo de reconocimiento para el script etíope en su
versión estándar. La lista de idiomas soportados (48-80 idiomas) no incluye
amárico, tigriña ni ge'ez. No es un problema de GPU ni de instalación: el
modelo simplemente no existe en la librería.

## Solución adoptada
Reemplazar EasyOCR por Tesseract con el paquete de datos para escritura
etíope (`tesseract-ocr-script-ethi`), que sí está disponible como modelo
oficial de Tesseract.

Instalación:
    sudo apt install tesseract-ocr tesseract-ocr-script-ethi
    pip install pytesseract pillow

## Script actualizado
`15_ocr_tonto_geez.py` usa ahora `pytesseract.image_to_string(img,
lang="script/Ethiopic")`.

## Estatus
PENDIENTE DE EJECUTAR. Verificar que el modelo etíope está instalado
(tesseract --list-langs) antes de correr el script.
