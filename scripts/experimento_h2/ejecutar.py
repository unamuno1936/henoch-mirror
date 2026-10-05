#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ejecutar.py — Experimento H2 v1.1

Cambios respecto a v1.0:
  - sha256_texto() maneja None.
  - Detecta content=None (modelos reasoning puros) sin crashear.
  - Guarda 'crudo' siempre. Registra 'finish_reason' y 'reasoning'.
  - Logging completo de respuestas HTTP 400 (headers + body).
  - Reintentos más agresivos y pausas más largas.
  - Folios reducidos a 2000px para reducir payload.
"""
import argparse
import base64
import getpass
import hashlib
import json
import logging
import os
import random
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

from config import (
    RAIZ,
    CONFIG, DIR_FOLIOS, DIR_PROMPTS, DIR_SALIDAS,
    ARCHIVO_ESTADO, ARCHIVO_LOG,
)


def configurar_log():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(ARCHIVO_LOG, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


# ─── Hashes ─────────────────────────────────────────────────────────────────

def sha256_archivo(ruta: Path) -> str:
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def sha256_texto(texto) -> str:
    if texto is None:
        return ""
    if not isinstance(texto, str):
        texto = str(texto)
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def sha256_bytes(datos: bytes) -> str:
    return hashlib.sha256(datos).hexdigest()


# ─── Carga de recursos ──────────────────────────────────────────────────────

def cargar_texto(nombre: str) -> str:
    for ext in (".md", ".txt"):
        ruta = DIR_PROMPTS / f"{nombre}{ext}"
        if ruta.exists():
            return ruta.read_text(encoding="utf-8")
    raise FileNotFoundError(f"No encontrado en prompts/: {nombre}.md|.txt")


def cargar_folio_b64(folio_id: str):
    for ext in (".jpg", ".jpeg", ".png"):
        ruta = DIR_FOLIOS / f"{folio_id}{ext}"
        if ruta.exists():
            datos = ruta.read_bytes()
            mime = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"
            return base64.b64encode(datos).decode("ascii"), mime, sha256_bytes(datos)
    raise FileNotFoundError(f"Folio no encontrado: {folio_id}")


# ─── Estado ─────────────────────────────────────────────────────────────────

def cargar_estado() -> dict:
    if ARCHIVO_ESTADO.exists():
        return json.loads(ARCHIVO_ESTADO.read_text(encoding="utf-8"))
    return {"completadas": [], "lote": None}


def guardar_estado(estado: dict):
    ARCHIVO_ESTADO.write_text(
        json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8"
    )


# ─── API key ────────────────────────────────────────────────────────────────

def obtener_api_key() -> str:
    key = os.environ.get(CONFIG["api"]["api_key_env"])
    if key:
        print(f"✓ Usando {CONFIG['api']['api_key_env']} del entorno.")
        return key
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  OpenRouter API Key                                          ║")
    print("║  No se guarda en disco. Vive solo en la memoria del proceso. ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    key = getpass.getpass("  Pega tu API key (sk-or-...): ").strip()
    if not key:
        print("✗ API key vacía. Abortando.")
        sys.exit(1)
    if not key.startswith("sk-or-"):
        print("⚠ No empieza con 'sk-or-'. ¿Es de OpenRouter?")
        if input("  Continuar de todos modos? [s/N]: ").strip().lower() != "s":
            sys.exit(1)
    return key


# ─── Mensajes y llamada ─────────────────────────────────────────────────────

def construir_mensajes(prompt: str, perfil, img_b64: str, mime: str) -> list:
    mensajes = []
    if perfil:
        mensajes.append({"role": "system", "content": perfil})
    mensajes.append({
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url",
             "image_url": {"url": f"data:{mime};base64,{img_b64}"}},
        ],
    })
    return mensajes


def log_debug_respuesta(r):
    """Vuelca headers y body crudo para diagnóstico."""
    logging.error(f"    ╭─ DEBUG HTTP {r.status_code} ─────────────────────────")
    logging.error(f"    │ Request-ID: {r.headers.get('x-request-id', '—')}")
    logging.error(f"    │ CF-RAY: {r.headers.get('cf-ray', '—')}")
    logging.error(f"    │ Content-Type: {r.headers.get('content-type', '—')}")
    logging.error(f"    │ Body (primeros 2000 chars):")
    body = r.text[:2000] if r.text else "(vacío)"
    for linea in body.splitlines() or ["(sin líneas)"]:
        logging.error(f"    │   {linea}")
    logging.error(f"    ╰─────────────────────────────────────────────────────")


def llamar_api(modelo, mensajes, temperatura, api_key) -> dict:
    cfg = CONFIG["api"]
    payload = {
        "model": modelo,
        "messages": mensajes,
        "temperature": temperatura,
        "max_tokens": cfg["max_tokens"],
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/marco-vazquez/henoch",
        "X-Title": "Experimento H2 - BnF Ethiopien 49",
    }
    ultimo_error = None
    for intento in range(1, cfg["max_reintentos"] + 1):
        try:
            t0 = time.time()
            r = requests.post(cfg["endpoint"], json=payload, headers=headers,
                              timeout=cfg["timeout_s"])
            dt = time.time() - t0
            if r.status_code == 200:
                return {"ok": True, "respuesta": r.json(), "latencia_s": dt}
            if r.status_code in (429, 500, 502, 503, 504):
                ultimo_error = f"HTTP {r.status_code}: {r.text[:200]}"
            else:
                log_debug_respuesta(r)
                return {"ok": False,
                        "error": f"HTTP {r.status_code}: {r.text[:500]}"}
        except requests.exceptions.RequestException as e:
            ultimo_error = str(e)
        if intento < cfg["max_reintentos"]:
            espera = cfg["backoff_base_s"] * (2 ** (intento - 1))
            espera += random.uniform(0, cfg["backoff_jitter_s"])
            logging.warning(f"  Reintento {intento}/{cfg['max_reintentos']} "
                            f"en {espera:.1f}s: {ultimo_error}")
            time.sleep(espera)
    return {"ok": False, "error": f"Agotados reintentos: {ultimo_error}"}


# ─── Auditoría ──────────────────────────────────────────────────────────────

def escribir_llamada(archivo_jsonl: Path, registro: dict):
    with open(archivo_jsonl, "a", encoding="utf-8") as f:
        f.write(json.dumps(registro, ensure_ascii=False) + "\n")


# ─── Plan y lotes ───────────────────────────────────────────────────────────

def plan_llamadas(folios, condiciones) -> list:
    plan = []
    for folio in folios:
        for cond in condiciones:
            plan.append({
                "folio": folio,
                "condicion": cond["id"],
                "modelo": cond["modelo"],
                "prompt": cond["prompt"],
                "perfil": cond["perfil"],
                "clave": f"{folio}__{cond['id']}",
            })
    return plan


def crear_lote() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    lote = DIR_SALIDAS / f"lote_{ts}"
    lote.mkdir(parents=True, exist_ok=True)
    return lote


def congelar_config(lote: Path):
    (lote / "config_congelada.json").write_text(
        json.dumps(CONFIG, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    hashes = []
    nombres = {c["prompt"] for c in CONFIG["condiciones"]}
    nombres |= {c["perfil"] for c in CONFIG["condiciones"] if c["perfil"]}
    for nombre in sorted(nombres):
        for ext in (".md", ".txt"):
            ruta = DIR_PROMPTS / f"{nombre}{ext}"
            if ruta.exists():
                hashes.append(f"{sha256_archivo(ruta)}  prompts/{ruta.name}")
                break
    for folio in CONFIG["folios"]:
        for ext in (".jpg", ".jpeg", ".png"):
            ruta = DIR_FOLIOS / f"{folio}{ext}"
            if ruta.exists():
                hashes.append(f"{sha256_archivo(ruta)}  {ruta.relative_to(RAIZ)}")
                break
    (lote / "hashes.sha256").write_text("\n".join(hashes) + "\n", encoding="utf-8")


# ─── Ejecución ──────────────────────────────────────────────────────────────

def ejecutar_plan(plan, lote, reanudar, api_key):
    archivo_jsonl = lote / "llamadas.jsonl"
    estado = cargar_estado() if reanudar else {"completadas": [], "lote": str(lote)}
    completadas = set(estado["completadas"])

    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print(f"║  Ejecutando {len(plan):>3} llamadas                                       ║")
    print(f"║  Lote: {lote.name:<53}║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    for i, item in enumerate(plan, 1):
        if item["clave"] in completadas:
            logging.info(f"[{i}/{len(plan)}] {item['clave']} — ya completada")
            continue

        logging.info(f"[{i}/{len(plan)}] {item['clave']}  modelo={item['modelo']}")

        try:
            prompt = cargar_texto(item["prompt"])
            perfil = cargar_texto(item["perfil"]) if item["perfil"] else None
            img_b64, mime, img_sha = cargar_folio_b64(item["folio"])
        except FileNotFoundError as e:
            logging.error(f"  Recurso faltante: {e}")
            continue

        mensajes = construir_mensajes(prompt, perfil, img_b64, mime)

        t_inicio = time.time()
        resultado = llamar_api(item["modelo"], mensajes, 0.0, api_key)
        t_total = time.time() - t_inicio

        registro = {
            "clave": item["clave"],
            "folio": item["folio"],
            "condicion": item["condicion"],
            "modelo": item["modelo"],
            "prompt_nombre": item["prompt"],
            "perfil_nombre": item["perfil"],
            "temperatura": 0.0,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "hash_prompt": sha256_texto(prompt),
            "hash_perfil": sha256_texto(perfil) if perfil else None,
            "hash_imagen": img_sha,
            "latencia_total_s": round(t_total, 2),
            "ok": False,
        }

        if resultado["ok"]:
            data = resultado["respuesta"]
            choices = data.get("choices") or [{}]
            msg = choices[0].get("message") or {}
            contenido = msg.get("content")
            reasoning = msg.get("reasoning")
            finish = choices[0].get("finish_reason")

            registro["uso"] = data.get("usage", {})
            registro["modelo_reportado"] = data.get("model", item["modelo"])
            registro["crudo"] = data
            registro["finish_reason"] = finish

            if contenido is None or (isinstance(contenido, str) and not contenido.strip()):
                registro["ok"] = False
                registro["error"] = (
                    "content=None o vacío. "
                    f"reasoning_len={len(reasoning) if reasoning else 0} "
                    f"finish_reason={finish}"
                )
                registro["hash_respuesta"] = None
                registro["respuesta"] = None
                if reasoning:
                    registro["reasoning"] = reasoning
            else:
                registro["ok"] = True
                registro["hash_respuesta"] = sha256_texto(contenido)
                registro["respuesta"] = contenido
                if reasoning:
                    registro["reasoning"] = reasoning
        else:
            registro["error"] = resultado["error"]

        escribir_llamada(archivo_jsonl, registro)

        if registro["ok"]:
            completadas.add(item["clave"])
            estado["completadas"] = sorted(completadas)
            guardar_estado(estado)
            n_chars = len(registro.get("respuesta") or "")
            logging.info(f"  ✓ {n_chars} caracteres — {t_total:.1f}s")
        else:
            logging.info(f"  ✗ {registro.get('error', '')[:160]}")

        pausa = random.uniform(*CONFIG["api"]["pausa_entre_llamadas_s"])
        time.sleep(pausa)

    logging.info("Ejecución terminada.")
    generar_resumen(lote, archivo_jsonl)


def generar_resumen(lote: Path, archivo_jsonl: Path):
    if not archivo_jsonl.exists():
        return
    registros = [json.loads(l) for l in
                 archivo_jsonl.read_text(encoding="utf-8").splitlines() if l.strip()]
    lineas = [
        "# Resumen del lote H2",
        "",
        f"Lote: `{lote.name}`",
        f"Fecha UTC: {datetime.now(timezone.utc).isoformat()}",
        f"Total: {len(registros)}",
        f"Exitosas: {sum(1 for r in registros if r['ok'])}",
        f"Fallidas: {sum(1 for r in registros if not r['ok'])}",
        "",
        "| Clave | Modelo | OK | Chars | Lat (s) | finish_reason |",
        "|---|---|---|---|---|---|",
    ]
    for r in registros:
        n = len(r.get("respuesta") or "") if r["ok"] else 0
        fr = r.get("finish_reason") or "—"
        lineas.append(
            f"| {r['clave']} | {r['modelo']} | "
            f"{'✓' if r['ok'] else '✗'} | {n} | {r['latencia_total_s']} | {fr} |"
        )
    (lote / "resumen.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"\n📄 Resumen: {lote / 'resumen.md'}")
    print(f"📄 Datos crudos: {archivo_jsonl}")
    print(f"👁  Ver: python ver_lote.py {lote.name}\n")


# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--solo-listar", action="store_true")
    parser.add_argument("--reanudar", action="store_true")
    parser.add_argument("--folio", help="Ejecuta solo un folio (ej: f19).")
    args = parser.parse_args()

    configurar_log()
    DIR_SALIDAS.mkdir(parents=True, exist_ok=True)

    folios = [args.folio] if args.folio else CONFIG["folios"]
    plan = plan_llamadas(folios, CONFIG["condiciones"])

    if args.solo_listar:
        print(f"\nPlan de ejecución — {len(plan)} llamadas:\n")
        for item in plan:
            print(f"  {item['clave']:<50}  modelo={item['modelo']}")
        print()
        return

    api_key = obtener_api_key()

    if args.reanudar:
        estado = cargar_estado()
        if not estado.get("lote"):
            logging.error("No hay lote previo.")
            sys.exit(1)
        lote = Path(estado["lote"])
        logging.info(f"Reanudando lote: {lote.name}")
    else:
        lote = crear_lote()
        congelar_config(lote)
        logging.info(f"Lote nuevo: {lote}")

    ejecutar_plan(plan, lote, reanudar=args.reanudar, api_key=api_key)


if __name__ == "__main__":
    main()
