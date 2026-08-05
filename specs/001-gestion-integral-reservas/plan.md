# Implementation Plan: Gestión Integral de Reservas — Bundle Backend/Frontend Web (BW)

**Branch**: `001-gestion-integral-reservas` | **Date**: 2026-08-05 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-gestion-integral-reservas/spec.md`, restringida
al bundle Backend/Frontend Web (BW) por `/specs/001-gestion-integral-reservas/bundle-scope.md`.

**Alcance de este plan**: exclusivamente el bundle Backend/Frontend Web. Agente Conversacional
(AC) y Backend Agendamiento (BA) se tratan únicamente como dependencias arquitectónicas donde
`spec.md` los referencia explícitamente desde un requisito de BW (contrato de API interna
compartido en FR-BW-029 a FR-BW-034; evento de agenda de FR-BW-044; eventos conversacionales de
FR-BW-016 a FR-BW-018). No se diseñó ninguna funcionalidad exclusiva de AC o BA.

**Nota de fuentes**: el contexto técnico de esta sección proviene de dos lugares: (1) decisiones de
diseño nuevas, tomadas aquí porque `spec.md` difiere explícitamente "el contexto técnico" y el
"esquema técnico" de los contratos compartidos y de 4 entidades a `/speckit.plan` (ver
`## Clarifications` y el pie de página de `spec.md`); (2) el stack ya declarado para el bundle
"Backend/Frontend Web" en `composed/plan_input.md` §"Contexto por bundle (Functional)", al cual el
propio pie de `spec.md` remite ("el contexto técnico se entrega por separado en /speckit.plan (ver
composed/plan_input.md)"). No se usó ninguna otra fuente. Donde el canvas no declaró nada y
`spec.md` no lo diferió explícitamente a esta etapa (p. ej. metas de desempeño, umbrales de NFR,
comportamiento ante fallo de FR-BW-044), se deja abierto — no se inventó.

## Summary

El bundle Backend/Frontend Web es el portal administrativo del sistema de "Gestión integral de
Reservas": permite crear/modificar profesionales, servicios y agenda, y modificar datos de
clientes (FR-BW-001 a FR-BW-044), restringido en esta etapa al rol "Administrador de la operación"
(aclarado en `spec.md` §Clarifications). Enfoque técnico: aplicación web con frontend en
JavaScript y backend en Python, ambos declarados para este bundle en `composed/plan_input.md`;
persistencia de negocio delegada al contrato de API interna que `spec.md` aclaró como compartido
con Backend Agendamiento (Disponibilidad/Servicios/Profesionales Query API y Crear/Actualizar/
Cancelar Reserva Command API); Object Storage propio para la entidad "Multimedia Web".

## Technical Context

**Language/Version**: Frontend: JavaScript (versión no especificada por el canvas ni por
`spec.md`). Backend: Python (versión no especificada). Ambos declarados en `composed/plan_input.md`
§Bundle "Backend/Frontend Web" → Stack declarado.

**Primary Dependencies**: Nginx (declarado en el stack de BW; usado como frontera HTTP —
servir el frontend y enrutar hacia el backend). Cliente de Object Storage (declarado en el stack,
para la entidad "Multimedia Web"). Decisión de diseño (ver `research.md`): frameworks concretos de
frontend/backend y librería de pruebas, porque `spec.md` no los declara y su elección no está
respaldada por ningún requisito — se documentan como decisión de plan, no como requisito.

**Storage**: Object Storage (declarado en el stack de BW, para "Multimedia Web"). BW **no** declara
una base de datos relacional propia: los datos de negocio que administra (Ficha clientes,
Disponibilidad Agenda, Catálogo de servicios, Profesionales y especialidades) se leen/escriben a
través del contrato de API interno compartido con Backend Agendamiento (FR-BW-009 a FR-BW-012 y
FR-BW-029 a FR-BW-034, aclarado en `spec.md` §Clarifications). Ver `data-model.md` para el detalle
de qué entidades son propias de BW (Multimedia Web) y cuáles son leídas de un contrato externo.

**Testing**: NEEDS CLARIFICATION → resuelto en `research.md` (decisión de diseño; ningún canvas ni
`spec.md` declara un framework de pruebas).

**Target Platform**: Aplicación web (navegador + servidor), contenedorizada con Docker (declarado
en el stack de BW).

**Project Type**: Web application (frontend + backend separados), acorde al Structural Canvas
("Pagina web admin locales" como frontend, "Backend / Pagina web admin locales (multi-tenant)"
como backend — referencia informativa de `composed/plan_input.md`, no una fuente de requisitos).

**Performance Goals**: No declarado para BW específicamente. `spec.md` solo declara
`NFR-TEC-5` "Baja latencia conversacional", que por su nombre corresponde al bundle Agente
Conversacional, no a BW. **No se infiere un objetivo de desempeño propio de BW** — queda abierto
(ver `checklists/bw-requirements.md` CHK002/CHK017).

**Constraints**: "GUI amigable" y "Recibir derivación de LLM para atención humana" (ambas
declaradas para el bundle BW en `composed/plan_input.md` §Constraints locales). La primera no está
cuantificada (consistente con CHK005/CHK006 del checklist de Etapa H) y no se inventa aquí una
métrica. La segunda corresponde a la dependencia ya identificada en FR-BW-018 "Error de
interpretacion (derivar)".

**Scale/Scope**: No declarado por ningún canvas ni por `spec.md`. No se infiere.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Evaluado contra `.specify/memory/constitution.md` v2.0.0, Principios I-IV (los únicos vigentes;
el Principio V fue removido en la Etapa E por no tener respaldo en el pipeline).

| Principio | Aplica a este diseño | Evaluación |
|---|---|---|
| P9 "Integración desacoplada con sistemas existentes" | Sí | El contrato interno compartido (FR-BW-029..034) se diseña como API, no como acceso directo a la base de datos de Backend Agendamiento → cumple. |
| P13 "Única fuente de información para las reservas" | Sí | BW no mantiene su propia copia de "Disponibilidad Agenda"/reservas; consume el contrato compartido → cumple. |
| P16 "Bajo acoplamiento" / P17 "Alta cohesión" | Sí | Separación frontend/backend + API interna compartida en vez de lógica duplicada → cumple. |
| P18 "Configuración antes que personalización" | Parcial | No hay suficiente información en `spec.md` para evaluarlo más allá de la estructura propuesta; no se fuerza una decisión no respaldada. |
| P20 "Escalabilidad horizontal" | Sí | Backend Python sin estado detrás de Nginx, en contenedor Docker → admite réplicas horizontales sin cambio de diseño. |
| P21 "Integración mediante adapters" | Sí | El acceso al contrato compartido se aísla en una capa de cliente/adaptador (ver `data-model.md` / `contracts/`), no llamadas dispersas. |
| P22 "Observabilidad mediante logging y monitoreo" | Abierto | `spec.md` no declara requisitos de observabilidad para BW; no se inventa un mecanismo concreto — queda como brecha reportada, no resuelta aquí. |
| P1-P8, P10-P12, P14-P15, P19 | No aplican directamente a un solo bundle backend/frontend administrativo (son de estrategia de negocio/TI o de todo el sistema) | Sin conflicto detectado. |

**Resultado**: PASA. Ninguna decisión de este plan contradice un principio de la Constitution.
No se requiere tabla de Complexity Tracking (sin violaciones que justificar).

## Project Structure

### Documentation (this feature)

```text
specs/001-gestion-integral-reservas/
├── plan.md              # Este archivo — alcance: bundle Backend/Frontend Web
├── research.md          # Fase 0 — decisiones de diseño y su justificación
├── data-model.md         # Fase 1 — entidades de BW
├── quickstart.md        # Fase 1 — guía de validación end-to-end de BW
├── contracts/
│   └── bw-shared-internal-api.md   # Fase 1 — contrato compartido con AC/BA (FR-BW-029..034)
└── tasks.md             # Fase 2 — NO generado por /speckit-plan
```

### Source Code (repository root)

```text
bw-frontend/
├── src/
│   ├── pages/          # Vistas administrativas: profesionales, servicios, agenda, clientes, dashboard
│   ├── components/
│   └── services/        # Cliente HTTP hacia bw-backend
└── tests/

bw-backend/
├── src/
│   ├── models/          # Multimedia Web (propio); DTOs de lectura para Ficha clientes,
│   │                     # Disponibilidad Agenda, Catálogo de servicios, Profesionales y
│   │                     # especialidades (ver data-model.md — no son tablas propias de BW)
│   ├── services/
│   ├── adapters/        # Cliente hacia el contrato de API interna compartido (FR-BW-029..034)
│   └── api/             # Endpoints que expone BW a bw-frontend
└── tests/
```

**Structure Decision**: Web application con frontend y backend separados (`bw-frontend/`,
`bw-backend/`), siguiendo el stack declarado para el bundle BW (JavaScript + Python) y aislando el
acceso al contrato compartido con AC/BA detrás de una capa `adapters/` (Principio P21). No se
reutilizan ni se crean directorios para los bundles AC o BA: quedan fuera del alcance de esta
etapa por `bundle-scope.md`.

## Complexity Tracking

*Sin violaciones de la Constitution que requieran justificación (ver Constitution Check: PASA).*
