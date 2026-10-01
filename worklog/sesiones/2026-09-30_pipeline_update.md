# Sesion 2026-09-30 — Actualizacion del pipeline

## Cambios tecnicos
1. aria2c corregido: usar --max-download-limit, no --limit-rate.
2. Manifiesto IIIF del Rylands descargado y funcional.
   Endpoint: https://www.digitalcollections.manchester.ac.uk/iiif/MS-ETHIOPIC-00023
3. Los 5 volumenes de Bruce descargados.
4. Symlink recursivo $BASE/henoch -> $BASE eliminado.

## Reorganizacion estructural
- bibliografía/ -> bibliografia/ (sin acento).
- scripts/_archivo/ creado. Backups y duplicados movidos:
  - 05_hashes.py
  - 06_openrouter_client.py
  - 06_llamar_openrouter.py.bak
  - 06_llamar_openrouter.py.bak_20260928T005640Z
- fuentes/ reorganizado en subcarpetas:
  - boccaccini/
  - piovanelli/ (vacio, pendiente)
  - ehro_stuckenbruck/ (vacio, pendiente)
  - langstaff/ (vacio, pendiente)
  - bruce/ (Travels)
  - otros/ (PDFs sin categoria clara)
- imagenes_rylands/ creado (vacio, pendiente).
- chat/ eliminado (vacio).

## Cambio en criterio de seleccion de folios
- Antes: sorteo aleatorio sobre 114 paginas del BnF 49.
- Ahora: folios que contengan pasajes traducidos por Sacy
  (capitulos 1-3, 6-16, 22, 32).
- Motivo: validar Tlacuilo contra la primera traduccion moderna de Enoc.

## Script 01: necesita parche
Anadir flag --manuscrito con valores bnf | rylands.
Rutas:
- bnf: config/paginas_candidatas.txt -> config/paginas_seleccionadas.txt
- rylands: config/paginas_candidatas_rylands.txt ->
  config/paginas_seleccionadas_rylands.txt

## Pendientes
- Generar config/paginas_candidatas_rylands.txt (134 paginas: 67 x 2).
- Localizar los 5 folios del BnF 49 correspondientes a Sacy.
- Lanzar las 90 llamadas (~$2.50 USD).
- Adaptar script 10 al manifiesto del Rylands.
- Configurar git con Codeberg + GitLab (privados).
