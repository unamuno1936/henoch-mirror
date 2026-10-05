# config.py — Configuración congelada del experimento H2.
# NO MODIFICAR una vez iniciada la primera llamada.

from pathlib import Path

RAIZ           = Path(__file__).resolve().parent
DIR_FOLIOS     = RAIZ / "datos" / "folios_reducidos"   # ← folios a 2000px
DIR_PROMPTS    = RAIZ / "prompts"
DIR_SALIDAS    = RAIZ / "salidas"
ARCHIVO_ESTADO = RAIZ / "estado.json"
ARCHIVO_LOG    = RAIZ / "experimento.log"

CONFIG = {
    "version": "1.1",
    "fecha_congelamiento": "2026-10-04",
    "bitacora": "worklog/sesiones/2026-10-03_h2_rediseno_experimental.md",

    "api": {
        "endpoint": "https://openrouter.ai/api/v1/chat/completions",
        "api_key_env": "OPENROUTER_API_KEY",
        "timeout_s": 240,
        "max_reintentos": 6,           # ↑ de 4
        "backoff_base_s": 6,           # ↑ de 4
        "backoff_jitter_s": 4,
        "pausa_entre_llamadas_s": (10, 20),  # ↑ de 6-14
        "max_tokens": 8000,
    },

    "folios": ["f19", "f20", "f21", "f22", "f23"],

    "condiciones": [
        # ── Gemini 3.8 Flash ──
        {"id": "gemini38flash__simple", "modelo": "google/gemini-3.8-flash",
         "prompt": "generico", "perfil": None, "temperatura": 0.0},
        {"id": "gemini38flash__perfil", "modelo": "google/gemini-3.8-flash",
         "prompt": "wrapper_tlacuilo", "perfil": "system_tlacuilo", "temperatura": 0.0},
        # ── Qwen 3.8 Flash ──
        {"id": "qwen38flash__simple", "modelo": "qwen/qwen3.8-flash",
         "prompt": "generico", "perfil": None, "temperatura": 0.0},
        {"id": "qwen38flash__perfil", "modelo": "qwen/qwen3.8-flash",
         "prompt": "wrapper_tlacuilo", "perfil": "system_tlacuilo", "temperatura": 0.0},
        # ── DeepSeek V4.1 Flash ──
        {"id": "deepseek41flash__simple", "modelo": "deepseek/deepseek-v4.1-flash",
         "prompt": "generico", "perfil": None, "temperatura": 0.0},
        {"id": "deepseek41flash__perfil", "modelo": "deepseek/deepseek-v4.1-flash",
         "prompt": "wrapper_tlacuilo", "perfil": "system_tlacuilo", "temperatura": 0.0},
    ],
}
