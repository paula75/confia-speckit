# Reporte de reconstrucción de `prompt_specify`

## Fuentes utilizadas

- Fragmentos de `mapping/`.
- `composed/trace_annex.md`.
- Canvas Object Models de `com/`.

No se utilizaron README, Constitution ni documentos manuales.

## Resultado

- Identificadores ausentes analizados: **29**.
- Requisitos recuperados por pérdida real: **23**.
- Requisitos absorbidos cuyo ID original fue restaurado: **6**.
- Requisitos imposibles de expresar sin tecnología: **0**.

Las referencias a productos, proveedores y tecnologías fueron sustituidas por capacidades funcionales neutrales, como “canal de mensajería conversacional”, “capacidad externa de procesamiento”, “servicio externo de geolocalización”, “contrato de integración” y “conectividad externa”.

## Requisitos recuperados

### Funcionales

- `FR-AC-004` — recepción de ubicación.
- `FR-AC-005` — recepción de documentos.
- `FR-AC-009` — recepción contractual de notificaciones de mensajes.
- `FR-AC-044` — emisión contractual hacia procesamiento conversacional externo.
- `FR-BA-008` — recepción contractual de resultados conversacionales externos.
- `FR-BA-010` — lectura de respuestas conversacionales importadas.

### Integraciones

- `INT-1` — entrada desde mensajería conversacional externa.
- `INT-2` — entrada desde procesamiento conversacional externo.
- `INT-3` — entrada desde geolocalización externa.
- `INT-4` — salida hacia mensajería conversacional externa.
- `INT-5` — salida hacia procesamiento conversacional externo.

### Restricciones

- `R-1` a `R-12` — se restauraron las doce políticas y restricciones, anonimizando únicamente las referencias tecnológicas.

## Requisitos absorbidos

- `FR-AC-001` — equivalente adicional: `FR-AC-017` y `FR-AC-046`.
- `FR-AC-002` — equivalente adicional: `FR-AC-018`.
- `FR-AC-003` — equivalente adicional: `FR-AC-018`.
- `FR-BA-034` — equivalente adicional: `FR-AC-049`.
- `FR-SCC-001` — equivalente adicional: `FR-AC-017`.
- `FR-SCC-002` — equivalentes adicionales: `FR-AC-030` y `FR-AC-046`.

Estos IDs fueron restaurados explícitamente para que `trace_annex` no apunte a requisitos inexistentes. Las equivalencias quedaron documentadas junto a cada requisito.

## Elementos que requieren aclaración

Ningún requisito resultó imposible de expresar sin tecnología. Permanecen abiertas, sin resolver, las dudas ya sustentadas por los fragmentos sobre:

- contratos, esquemas y comportamiento ante error de las integraciones;
- contraparte de contratos funcionales;
- periodicidad, ventana de ejecución y comportamiento ante fallo de la limpieza programada.

No se inventaron valores ni decisiones para cerrar esas dudas.
