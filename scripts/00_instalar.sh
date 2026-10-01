#!/usr/bin/env bash
# 00_instalar.sh — Crea venv, instala dependencias, verifica.
set -euo pipefail

BASE="/media/joblak/41112ade-da41-4393-a9fb-53dc958b2f9e/multimedia/herramientas_extraccion/protocolos_investigacion/henoch"
cd "$BASE"

echo "=== Proyecto Henoch — Instalación ==="
echo "Ruta base: $BASE"
echo

# 1. Verificar Python
if ! command -v python3 &>/dev/null; then
  echo "ERROR: python3 no encontrado." >&2
  exit 1
fi
PYVER=$(python3 --version)
echo "Python detectado: $PYVER"

# 2. Crear entorno virtual
if [ ! -d "$BASE/entorno/venv" ]; then
  echo "Creando venv en entorno/venv ..."
  python3 -m venv "$BASE/entorno/venv"
else
  echo "venv ya existe en entorno/venv"
fi

# 3. Activar y actualizar pip
# shellcheck disable=SC1091
source "$BASE/entorno/venv/bin/activate"
python -m pip install --upgrade pip wheel setuptools

# 4. Instalar dependencias
echo "Instalando dependencias ..."
pip install -r "$BASE/requirements.txt"

# 5. Verificar instalación
echo
echo "=== Verificación ==="
python - <<'PYEOF'
import sys
mods = ["requests", "httpx", "PIL", "numpy", "scipy", "pandas", "dotenv", "rich", "tqdm"]
for m in mods:
    try:
        __import__(m)
        print(f"  OK  {m}")
    except ImportError as e:
        print(f"  FAIL {m}: {e}")
        sys.exit(1)
print("Todas las dependencias OK.")
PYEOF

# 6. Crear .env de ejemplo si no existe
if [ ! -f "$BASE/.env" ]; then
  cat > "$BASE/.env.example" <<'ENVEOF'
# Clave de OpenRouter (obligatoria para scripts 06)
OPENROUTER_API_KEY=sk-or-v1-...

# Opcional: ruta al store de Clew
CLEW_STORE=local

# Opcional: nivel de log
LOG_LEVEL=INFO
ENVEOF
  echo
  echo "Creado .env.example. Copia a .env y llena la clave."
fi

echo
echo "=== Instalación completa ==="
echo "Para activar el entorno:"
echo "    source $BASE/entorno/venv/bin/activate"
echo
echo "Para correr scripts:"
echo "    cd $BASE/scripts"
echo "    python3 01_seleccionar_paginas.py --n 5 --seed 20260926"
