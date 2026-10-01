# Criterios pre-registrados

Fecha de fijación: 2026-09-26
Investigador: Marco Antonio Vázquez Elías
Analista de datos: Julia [apellido pendiente]

## Notación
- CER = Character Error Rate (menor es mejor)
- H   = tasa de alucinación (menor es mejor)
- ΔCER = CER(genérico) − CER(Tlacuilo). Positivo = Tlacuilo mejor.
- ΔH   = H(genérico) − H(Tlacuilo). Positivo = Tlacuilo mejor.

## Veredicto

### Alentador
ΔCER ≥ 10 pp en ≥ 2 de 3 modelos
Y ΔH ≥ 0.10 en ≥ 2 de 3 modelos
Y desviación estándar de Tlacuilo ≤ desviación del genérico en ≥ 2 de 3 modelos.

### Neutro
ΔCER entre 0 y 10 pp, o efecto inconsistente entre modelos.

### Desastroso
ΔCER < 0 en ≥ 2 de 3 modelos O ΔH < 0 en ≥ 2 de 3 modelos.

## Decisión posterior
- Alentador → continuar a los 63 folios.
- Neutro → revisar resolución, ajustar prompts, repetir 5 folios.
- Desastroso → publicar como resultado negativo, documentar causa.

## Regla de honestidad
Si los datos caen en zona gris, se reporta zona gris.
No se fuerza el veredicto.

## Definición operacional de alucinación
- H1: texto inventado que no está en la imagen.
- H2: falsa legibilidad (transcribe sin marcar [ilegible] donde hay laguna).
- H3: bibliografía o pasaje citado que no existe.
- H4: normalización silenciosa hacia la forma canónica sin marcar diferencia.

Tasa H = (respuestas con al menos una H_i) / (total de respuestas evaluadas).

## Nota sobre tradición textual
No existe Urtext único de 1 Enoc en ge'ez. Las ediciones de Knibb (1978) y
Charles (1906) reflejan decisiones textuales distintas. La evaluación en inglés
se realiza contra estándar de oro (Knibb/Charles). La evaluación en español es
exploratoria (sin estándar de oro comparable).

## Declaración de limitaciones
- Muestra pequeña (5 páginas).
- Sin filólogo externo.
- Ground truth asistido, no edición crítica.
- Isomorfismo como constructo no unívoco.
- Perfil Tlacuilo reservado; solo se publica descripción conceptual.
