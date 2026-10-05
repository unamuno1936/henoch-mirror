#!/usr/bin/env python3
import base64, json, os, requests
from pathlib import Path

key = input("API key: ").strip()

# Cargar un folio real
folio = Path("datos/folios/f19.jpg")
print(f"Folio: {folio}")
print(f"Existe: {folio.exists()}")
if not folio.exists():
    # Seguir symlink
    folio = folio.resolve()
    print(f"Resuelto: {folio}")
    print(f"Existe: {folio.exists()}")

tamano = folio.stat().st_size
print(f"Tamaño: {tamano} bytes ({tamano/1024/1024:.2f} MB)")
if tamano == 0:
    print("✗ Archivo vacío")
    exit(1)

datos = folio.read_bytes()
b64 = base64.b64encode(datos).decode("ascii")
print(f"Base64: {len(b64)} caracteres ({len(b64)/1024/1024:.2f} MB)")

# Payload mínimo con imagen — SIN prompt, SIN system
payload_min = {
    "model": "google/gemini-3.8-flash",
    "messages": [{
        "role": "user",
        "content": [
            {"type": "text", "text": "¿Qué ves en esta imagen? Una frase."},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
        ],
    }],
    "max_tokens": 200,
}

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/marco-vazquez/henoch",
    "X-Title": "Diagnóstico H2",
}

print("\n=== Enviando payload con imagen real ===")
print(f"Payload size: {len(json.dumps(payload_min))} bytes")

r = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers, json=payload_min, timeout=120,
)

print(f"\nSTATUS: {r.status_code}")
print(f"CONTENT-TYPE: {r.headers.get('content-type')}")
print(f"CONTENT-LENGTH: {r.headers.get('content-length')}")
print(f"\nBODY COMPLETO (crudo):\n{r.text!r}")  # !r muestra repr con escapes

if r.status_code == 200:
    data = r.json()
    print(f"\n✓ ÉXITO")
    print(f"Modelo: {data.get('model')}")
    print(f"Respuesta: {data['choices'][0]['message']['content'][:500]}")
