#!/usr/bin/env python3
"""
06_llamar_openrouter.py — Cliente OpenRouter con Zero Data Retention.

Uso:
    python3 06_llamar_openrouter.py \
        --modelo google/gemini-3.8-flash \
        --prompt prompts/generico.txt \
        --imagen imagenes/folio_7v.png \
        --salida datos/c1_gemini_sin_7v_run1.txt

Requiere:
    - .env con OPENROUTER_API_KEY
    - pip install requests python-dotenv pillow
"""

import argparse
import base64
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path

import requests
from dotenv import load_dotenv
from PIL import Image


BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

API_URL = "https://openrouter.ai/api/v1/chat/completions"
LOGS_DIR = BASE / "logs"
LOGS_DIR.mkdir(exist_ok=True)

MAX_DIM = 2500


def encode_imagen(path: Path) -> tuple[str, str, dict]:
    with Image.open(path) as im:
        orig_size = im.size
        if max(im.size) > MAX_DIM:
            im.thumbnail((MAX_DIM, MAX_DIM), Image.LANCZOS)
        buf = BytesIO()
        im.convert("RGB").save(buf, format="JPEG", quality=92)
        data = buf.getvalue()
        new_size = im.size

    b64 = base64.b64encode(data).decode("utf-8")
    meta = {
        "original_size": list(orig_size),
        "sent_size": list(new_size),
        "bytes_jpeg": len(data),
    }
    return b64, "image/jpeg", meta


def hash_texto(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modelo", required=True)
    ap.add_argument("--prompt", required=True, type=Path)
    ap.add_argument("--imagen", required=True, type=Path)
    ap.add_argument("--salida", required=True, type=Path)
    ap.add_argument("--system", type=Path, default=None)
    ap.add_argument("--temp", type=float, default=0.2)
    ap.add_argument("--max-tokens", type=int, default=32000)
    ap.add_argument("--retry", type=int, default=2)
    args = ap.parse_args()

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: falta OPENROUTER_API_KEY en .env", file=sys.stderr)
        sys.exit(1)

    prompt_texto = args.prompt.read_text(encoding="utf-8").strip()
    system_texto = args.system.read_text(encoding="utf-8").strip() if args.system else None

    print(f"Preparando imagen {args.imagen.name}...")
    imagen_b64, mime, meta_img = encode_imagen(args.imagen)
    print(f"  Original: {meta_img['original_size']}")
    print(f"  Enviado:  {meta_img['sent_size']} ({meta_img['bytes_jpeg']} bytes JPEG)")

    mensajes = []
    if system_texto:
        mensajes.append({"role": "system", "content": system_texto})
    mensajes.append({
        "role": "user",
        "content": [
            {"type": "text", "text": prompt_texto},
            {"type": "image_url",
             "image_url": {"url": f"data:{mime};base64,{imagen_b64}"}},
        ],
    })

    payload = {
        "model": args.modelo,
        "messages": mensajes,
        "temperature": args.temp,
        "max_tokens": args.max_tokens,
        "provider": {"data_collection": "deny", "zdr": True},
        "extra_body": {
            "safety_settings": [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ],
        },
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/jacobea/henoch",
        "X-Title": "Henoch Tlacuilo Study",
    }

    ts = datetime.now(timezone.utc).isoformat()
    print(f"[{ts}] Llamando a {args.modelo}...")

    last_error = None
    data = None
    for intento in range(args.retry + 1):
        try:
            r = requests.post(API_URL, headers=headers, json=payload, timeout=300)
            if r.status_code == 429:
                print(f"  429 rate limit, esperando 30s...")
                time.sleep(30)
                continue
            r.raise_for_status()
            data = r.json()
            break
        except Exception as e:
            last_error = str(e)
            print(f"  Error intento {intento+1}: {e}")
            if intento < args.retry:
                time.sleep(10)

    if data is None:
        print(f"FALLO tras {args.retry+1} intentos: {last_error}", file=sys.stderr)
        sys.exit(1)

        # DIAGNOSTICO: dump raw ANTES de parsear
    raw_path = args.salida.with_suffix(".raw.json")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    msg = data["choices"][0].get("message", {})
    respuesta = msg.get("content")
    finish = data["choices"][0].get("finish_reason")
    if respuesta is None:
        print(f"ALERTA: content=None. finish_reason={finish}")
        print(f"Keys del message: {list(msg.keys())}")
        print(f"Raw completo en: {raw_path}")
        sys.exit(2)

    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_text(respuesta, encoding="utf-8")

    log = {
        "timestamp": ts,
        "modelo": args.modelo,
        "prompt_archivo": str(args.prompt),
        "prompt_hash": hash_texto(prompt_texto),
        "system_hash": hash_texto(system_texto) if system_texto else None,
        "imagen": str(args.imagen),
        "imagen_meta": meta_img,
        "salida": str(args.salida),
        "salida_hash": hash_texto(respuesta),
        "temperature": args.temp,
        "max_tokens": args.max_tokens,
        "usage": data.get("usage", {}),
        "zdr": True,
        "data_collection": "deny",
    }
    log_path = LOGS_DIR / f"{args.salida.stem}.json"
    log_path.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Escrito: {args.salida}")
    print(f"Log:     {log_path}")
    print(f"Tokens:  {data.get('usage', {})}")


if __name__ == "__main__":
    main()
