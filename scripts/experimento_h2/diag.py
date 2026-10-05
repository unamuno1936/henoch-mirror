#!/usr/bin/env python3
import json, sys, requests

key = input("API key: ").strip()

def probar(nombre, payload, headers_extra=None):
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    if headers_extra:
        headers.update(headers_extra)
    print(f"\n=== {nombre} ===")
    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers, json=payload, timeout=60,
        )
        print(f"STATUS: {r.status_code}")
        print(f"HEADERS: {dict(r.headers)}")
        print(f"BODY (primeros 1500):\n{r.text[:1500]}")
    except Exception as e:
        print(f"EXCEPCIÓN: {e}")

# 1) Mínimo: solo texto
probar("1. Texto simple, modelo gemini-3.8-flash", {
    "model": "google/gemini-3.8-flash",
    "messages": [{"role": "user", "content": "Di 'hola'"}],
})

# 2) Listar modelos disponibles (endpoint distinto)
print("\n=== 2. Listar modelos (buscar gemini y qwen) ===")
try:
    r = requests.get(
        "https://openrouter.ai/api/v1/models",
        headers={"Authorization": f"Bearer {key}"},
        timeout=30,
    )
    print(f"STATUS: {r.status_code}")
    if r.status_code == 200:
        modelos = r.json().get("data", [])
        for m in modelos:
            mid = m.get("id", "")
            if "gemini" in mid.lower() or "qwen" in mid.lower() or "deepseek" in mid.lower():
                print(f"  {mid}")
    else:
        print(r.text[:500])
except Exception as e:
    print(f"EXCEPCIÓN: {e}")
