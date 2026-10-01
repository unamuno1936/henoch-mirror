#!/usr/bin/env python3
"""06_openrouter_client.py — Llamadas a OpenRouter con ZDR y logging."""
import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
    from dotenv import load_dotenv
except ImportError as e:
    print(f"ERROR: falta dependencia: {e}", file=sys.stderr)
    print("Corre: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)


BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

API_KEY = os.getenv("OPENROUTER_API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"
DATA_DIR = BASE / "datos"
LOGS = BASE / "logs"
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOGS.mkdir(parents=True, exist_ok=True)


def cargar_prompt(nombre: str) -> str:
    p = BASE / "prompts" / f"{nombre}.txt"
    if not p.exists():
        raise FileNotFoundError(f"No existe {p}")
    return p.read_text(encoding="utf-8")


def cargar_imagen_b64(ruta: Path) -> str:
    import base64
    return base64.b64encode(ruta.read_bytes()).decode("ascii")


def hash_texto(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def llamar(modelo: str, prompt: str, imagen_b64: str) -> dict:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://jacobea.local",
        "X-Title": "Henoch-Tlacuilo-Study",
    }
    payload = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Transcribe y traduce."},
                    {"type": "image_url",
                     "image_url": {"url": f"data:image/jpeg;base64,{imagen_b64}"}},
                ],
            },
        ],
        "temperature": 0.2,
        "provider": {
            "data_collection": "deny",
            "zdr": True,
        },
    }
    t0 = time.perf_counter()
    r = requests.post(URL, headers=headers, json=payload, timeout=300)
    dt = time.perf_counter() - t0
    r.raise_for_status()
    resp = r.json()
    resp["_tiempo_s"] = dt
    return resp


def main():
    if not API_KEY:
        print("ERROR: falta OPENROUTER_API_KEY en .env", file=sys.stderr)
        sys.exit(1)

    ap = argparse.ArgumentParser()
    ap.add_argument("--modelo", required=True, help="ID de modelo en OpenRouter")
    ap.add_argument("--prompt", required=True, choices=["generico", "wrapper_tlacuilo"])
    ap.add_argument("--imagen", required=True, type=Path, help="Ruta al archivo de imagen")
    ap.add_argument("--pagina", required=True, help="Ej: 3r")
    ap.add_argument("--run", required=True, type=int, help="Número de corrida (1, 2, 3)")
    ap.add_argument("--tag", required=True, help="Alias del modelo (M1, M2, M3)")
    args = ap.parse_args()

    if not args.imagen.exists():
        print(f"ERROR: no existe {args.imagen}", file=sys.stderr)
        sys.exit(1)

    prompt_texto = cargar_prompt(args.prompt)
    imagen_b64 = cargar_imagen_b64(args.imagen)

    print(f"Llamando {args.modelo} / {args.prompt} / {args.pagina} / run{args.run} ...")
    resp = llamar(args.modelo, prompt_texto, imagen_b64)

    contenido = resp["choices"][0]["message"]["content"]

    # Guardar output
    out_txt = DATA_DIR / f"{args.tag}_{args.prompt}_{args.pagina}_run{args.run}.txt"
    out_txt.write_text(contenido, encoding="utf-8")

    # Guardar log crudo
    log_entry = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "modelo_id": args.modelo,
        "tag": args.tag,
        "prompt": args.prompt,
        "pagina": args.pagina,
        "run": args.run,
        "prompt_hash": hash_texto(prompt_texto),
        "imagen_hash": hash_texto(imagen_b64),
        "output_hash": hash_texto(contenido),
        "output_chars": len(contenido),
        "tiempo_s": round(resp.get("_tiempo_s", 0), 2),
        "usage": resp.get("usage", {}),
        "modelo_reportado": resp.get("model", ""),
        "finish_reason": resp["choices"][0].get("finish_reason", ""),
    }
    log_file = LOGS / "openrouter_log.jsonl"
    with log_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

    print(f"OK: {out_txt}")
    print(f"Output hash: {log_entry['output_hash'][:16]}...")
    print(f"Tiempo: {log_entry['tiempo_s']}s")
    print(f"Tokens: {log_entry['usage']}")


if __name__ == "__main__":
    main()
