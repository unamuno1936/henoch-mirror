#!/usr/bin/env python3
"""
11_ejecutar_experimento.py — Orquesta las 90 llamadas del diseño final.

6 condiciones:
  C1: gemini-3.8-flash SIN perfil  (15 llamadas)
  C2: gemini-3.8-flash CON perfil  (15 llamadas)
  C3: glm-5.3-flash CON perfil     (15 llamadas)
  C4: deepseek-v4.1-flash CON perfil (15 llamadas)
  C5: gpt-5.6-luna CON perfil      (15 llamadas)
  C6: qwen3.8-27b:free CON perfil  (15 llamadas, gratis)
"""

import argparse
import subprocess
import time
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent

CONDICIONES = [
    {"nombre": "c1_gemini_sin",   "modelo": "google/gemini-3.8-flash",       "prompt": "generico", "system": None},
    {"nombre": "c2_gemini_con",   "modelo": "google/gemini-3.8-flash",       "prompt": "tlacuilo", "system": BASE / "prompts/system_tlacuilo.txt"},
    {"nombre": "c3_glm_con",      "modelo": "z-ai/glm-5.3-flash",            "prompt": "tlacuilo", "system": BASE / "prompts/system_tlacuilo.txt"},
    {"nombre": "c4_deepseek_con", "modelo": "deepseek/deepseek-v4.1-flash",  "prompt": "tlacuilo", "system": BASE / "prompts/system_tlacuilo.txt"},
    {"nombre": "c5_gpt_con",      "modelo": "openai/gpt-5.6-luna",           "prompt": "tlacuilo", "system": BASE / "prompts/system_tlacuilo.txt"},
    {"nombre": "c6_qwen_con",     "modelo": "qwen/qwen3.8-27b:free",         "prompt": "tlacuilo", "system": BASE / "prompts/system_tlacuilo.txt"},
]

FOLIOS = ["4r", "5v", "7v", "17v", "40v"]
RUNS = [1, 2, 3]
PAUSA = 5


def llamada(cond, folio, run, dry=False):
    nombre = f"{cond['nombre']}_{folio}_run{run}.txt"
    salida = BASE / f"datos/{nombre}"
    if salida.exists():
        print(f"  SKIP: {nombre}")
        return True

    prompt_path = BASE / f"prompts/{cond['prompt']}.txt"
    cmd = [
        "python3", str(BASE / "scripts/06_llamar_openrouter.py"),
        "--modelo", cond["modelo"],
        "--prompt", str(prompt_path),
        "--imagen", str(BASE / f"imagenes/folio_{folio}.png"),
        "--salida", str(salida),
        "--temp", "0.2", "--max-tokens", "8192",
    ]
    if cond["system"]:
        cmd += ["--system", str(cond["system"])]

    if dry:
        print(f"  [DRY] {nombre}")
        return True

    print(f"  → {nombre}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"    ERROR: {r.stderr[:200]}")
        return False
    print(f"    OK")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--condicion", default="all")
    args = ap.parse_args()

    conds = CONDICIONES if args.condicion == "all" else \
        [c for c in CONDICIONES if c["nombre"] == args.condicion]

    print("=" * 70)
    print(f"EXPERIMENTO HENOCH — {len(conds)} condiciones × 5 folios × 3 runs")
    print(f"Total llamadas: {len(conds) * 15}")
    print("=" * 70)

    total = ok = 0
    for cond in conds:
        print(f"\n### {cond['nombre']}")
        for folio in FOLIOS:
            for run in RUNS:
                total += 1
                if llamada(cond, folio, run, args.dry_run):
                    ok += 1
                if not args.dry_run:
                    time.sleep(PAUSA)

    print()
    print("=" * 70)
    print(f"TOTAL: {ok}/{total} exitosas")
    print("=" * 70)


if __name__ == "__main__":
    main()
