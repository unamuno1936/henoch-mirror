#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ver_lote.py — Visualizador interactivo de resultados del experimento H2.
"""
import argparse
import json
import sys
from pathlib import Path

from config import DIR_SALIDAS, ARCHIVO_ESTADO


def lotes_disponibles():
    if not DIR_SALIDAS.exists():
        return []
    return sorted(
        [p for p in DIR_SALIDAS.iterdir()
         if p.is_dir() and p.name.startswith("lote_")],
        reverse=True,
    )


def cargar_llamadas(lote: Path):
    archivo = lote / "llamadas.jsonl"
    if not archivo.exists():
        return []
    return [json.loads(l) for l in
            archivo.read_text(encoding="utf-8").splitlines() if l.strip()]


def listar_lotes():
    lotes = lotes_disponibles()
    if not lotes:
        print("No hay lotes.")
        return
    print(f"\n{len(lotes)} lote(s):\n")
    for lote in lotes:
        ll = cargar_llamadas(lote)
        ok = sum(1 for r in ll if r["ok"])
        print(f"  {lote.name}  —  {ok}/{len(ll)} OK")
    print()


def mostrar_llamada(r: dict):
    print(f"\n{'─' * 72}")
    print(f"  CLAVE: {r['clave']}")
    print(f"  Modelo: {r['modelo']}")
    print(f"  Prompt: {r['prompt_nombre']}  |  Perfil: {r['perfil_nombre'] or '—'}")
    print(f"  Timestamp: {r['timestamp_utc']}")
    print(f"  Latencia: {r['latencia_total_s']}s")
    if r.get("finish_reason"):
        print(f"  Finish reason: {r['finish_reason']}")
    if r.get("uso"):
        u = r["uso"]
        rt = (u.get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
        print(f"  Tokens: prompt={u.get('prompt_tokens')} "
              f"completion={u.get('completion_tokens')} "
              f"reasoning={rt} total={u.get('total_tokens')}")
    print(f"{'─' * 72}\n")
    if r["ok"]:
        print(r.get("respuesta", ""))
    else:
        print(f"✗ ERROR: {r.get('error')}")
        if r.get("reasoning"):
            print(f"\n─── reasoning (len={len(r['reasoning'])}) ───")
            print(r["reasoning"][:2000])
    print()


def mostrar_lote(lote: Path):
    llamadas = cargar_llamadas(lote)
    if not llamadas:
        print(f"Sin llamadas en {lote.name}.")
        return
    print(f"\n{'═' * 72}")
    print(f"  LOTE: {lote.name}")
    print(f"  {len(llamadas)} llamadas — {sum(1 for r in llamadas if r['ok'])} OK")
    print(f"{'═' * 72}\n")
    for i, r in enumerate(llamadas, 1):
        estado = "✓" if r["ok"] else "✗"
        n = len(r.get("respuesta") or "") if r["ok"] else 0
        fr = r.get("finish_reason") or "—"
        print(f"  [{i:>2}] {estado}  {r['clave']:<45}  {n:>6} chars  ({fr})")
    print()
    while True:
        try:
            sel = input("Número para ver (Enter=salir): ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not sel:
            return
        try:
            idx = int(sel) - 1
            if 0 <= idx < len(llamadas):
                mostrar_llamada(llamadas[idx])
            else:
                print(f"  Rango: 1-{len(llamadas)}")
        except ValueError:
            print("  Ingresa un número.")


def mostrar_por_clave(lote: Path, clave: str):
    for r in cargar_llamadas(lote):
        if r["clave"] == clave:
            mostrar_llamada(r)
            return
    print(f"No se encontró '{clave}' en {lote.name}.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lote", nargs="?")
    ap.add_argument("--lista", action="store_true")
    ap.add_argument("--clave")
    ap.add_argument("--estado", action="store_true")
    args = ap.parse_args()

    if args.estado:
        if ARCHIVO_ESTADO.exists():
            print(ARCHIVO_ESTADO.read_text(encoding="utf-8"))
        else:
            print("Sin estado.json")
        return

    if args.lista:
        listar_lotes()
        return

    if args.lote:
        lote = DIR_SALIDAS / args.lote
        if not lote.exists():
            print(f"No existe: {lote}")
            sys.exit(1)
    else:
        lotes = lotes_disponibles()
        if not lotes:
            print("Sin lotes. Ejecuta primero: python ejecutar.py")
            sys.exit(1)
        lote = lotes[0]

    if args.clave:
        mostrar_por_clave(lote, args.clave)
    else:
        mostrar_lote(lote)


if __name__ == "__main__":
    main()
