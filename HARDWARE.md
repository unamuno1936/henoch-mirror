# Hardware y sistema operativo del estudio

## Dispositivo principal
- **Modelo**: [pendiente — Marco debe ejecutar `cat /proc/cpuinfo` y `lsblk`]
- **SO**: Debian Linux
- **Kernel**: [pendiente — `uname -a`]
- **CPU**: [pendiente — `lscpu`]
- **RAM**: [pendiente — `free -h`]
- **Almacenamiento**: Disco externo (ruta base del proyecto)

## Entorno de desarrollo
- **Python**: 3.10+
- **Pillow**: 12.3.0
- **requests**: instalado
- **python-dotenv**: instalado
- **venv**: `.venv` en la raíz del proyecto

## Herramientas de IA utilizadas
- **Gemini web**: entorno principal de desarrollo de perfiles
- **DeepSeek**: apoyo en razonamiento y documentación
- **OpenRouter API**: para llamadas programáticas a modelos
- **Zero Data Retention**: activado en todas las llamadas

## Limitaciones de hardware
- Sin GPU dedicada
- Sin servidor propio
- Todo el procesamiento es en CPU
- Almacenamiento en disco externo USB

## Presupuesto operativo
- ~5,000 MXN
- Costo estimado del estudio: < $1 USD en llamadas API
