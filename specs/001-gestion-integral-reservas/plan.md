# Implementation Plan: Gestión Integral de Reservas — Bundle Backend/Frontend Web (BW)

**Branch**: `001-gestion-integral-reservas` | **Date**: 2026-08-08 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-gestion-integral-reservas/spec.md`, restringida
al bundle Backend/Frontend Web (BW) por `/specs/001-gestion-integral-reservas/bundle-scope.md`.

**Alcance de este plan**: exclusivamente el bundle Backend/Frontend Web. Agente Conversacional
(AC) y Backend Agendamiento (BA) se tratan únicamente como dependencias arquitectónicas donde
`spec.md` los referencia explícitamente desde un requisito de BW (contrato de API interna
compartido en FR-BW-029 a FR-BW-034; evento de agenda de FR-BW-044; eventos conversacionales de
FR-BW-016 a FR-BW-018). No se diseñó ninguna funcionalidad exclusiva de AC o BA.

**Nota de fuentes**: el contexto técnico de esta sección proviene de tres lugares: (1) decisiones de
diseño nuevas, tomadas aquí porque `spec.md` difiere explícitamente "el contexto técnico" y el
"esquema técnico" de los contratos compartidos y de 4 entidades a `/speckit.plan` (ver
`## Clarifications` y el pie de página de `spec.md`); (2) el stack ya declarado para el bundle
"Backend/Frontend Web" en `composed/plan_input.md` §"Contexto por bundle (Functional)", al cual el
propio pie de `spec.md` remite ("el contexto técnico se entrega por separado en /speckit.plan (ver
composed/plan_input.md)"); (3) el stack técnico concreto indicado explícitamente como entrada de
esta ejecución de `/speckit.plan` (`prompts/etapa-i-plan.md` §Stack: "Backend usa python con el
framework FastAPI", "Se incluyen test unitarios en backend", "Frontend usa React con typescript
estricto") — este último resuelve, para el bundle BW, las elecciones de framework/lenguaje que
`composed/plan_input.md` dejaba genéricas ("Javascript", "Python") y que `research.md` había tratado
como decisión de implementación abierta. No se usó ninguna otra fuente. Donde ninguna de las tres
fuentes declaró nada y `spec.md` no lo diferió explícitamente a esta etapa (p. ej. metas de
desempeño, umbrales de NFR), se deja abierto — no se inventó.

**Re-sincronización (2026-08-08)**: esta ejecución de `/speckit.plan` también incorpora la sesión
adicional de `/speckit.clarify` de la misma fecha (comportamiento ante fallo de FR-BW-029..034 y de
FR-BW-044) y los hallazgos I1/U1/U2/G1/C1 de `/speckit.analyze` (mismo día): define los parámetros
concretos de reintento que `spec.md` remitió a esta etapa, resuelve el tipo del campo
`especialidades`, agrega el contrato de exportación de datos que faltaba
(`contracts/bw-data-exports.md`), y agrega la justificación formal de P22 en §Complexity Tracking.
No se agregó ninguna decisión no solicitada por esas fuentes.

## Summary

El bundle Backend/Frontend Web es el portal administrativo del sistema de "Gestión integral de
Reservas": permite crear/modificar profesionales, servicios y agenda, y modificar datos de
clientes (FR-BW-001 a FR-BW-044), restringido en esta etapa al rol "Administrador de la operación"
(aclarado en `spec.md` §Clarifications). Enfoque técnico: aplicación web con frontend en React +
TypeScript estricto y backend en Python + FastAPI (lenguajes declarados para este bundle en
`composed/plan_input.md`; frameworks concretos y tipado estricto declarados explícitamente como
entrada de esta ejecución de `/speckit.plan`, ver `prompts/etapa-i-plan.md` §Stack); persistencia
de negocio delegada al contrato de API interna que `spec.md` aclaró como compartido con Backend
Agendamiento (Disponibilidad/Servicios/Profesionales Query API y Crear/Actualizar/Cancelar Reserva
Command API); Object Storage propio para la entidad "Multimedia Web".

## Technical Context

**Language/Version**: Frontend: TypeScript en modo estricto (`strict: true`), sobre React
(framework declarado explícitamente en `prompts/etapa-i-plan.md` §Stack: "Frontend usa React con
typescript estricto"; versión no especificada). Backend: Python con FastAPI (framework declarado
explícitamente en `prompts/etapa-i-plan.md` §Stack: "Backend usa python con el framework FastAPI";
versión de Python no especificada). El lenguaje base (JavaScript/Python) ya estaba declarado en
`composed/plan_input.md` §Bundle "Backend/Frontend Web" → Stack declarado; esta ejecución concreta
el framework y, en el caso del frontend, el modo de tipado.

**Primary Dependencies**: FastAPI (backend, declarado explícitamente para esta ejecución) con su
servidor ASGI estándar (uvicorn). React (frontend, declarado explícitamente) con TypeScript en modo
estricto. Nginx (declarado en el stack de BW; usado como frontera HTTP — servir el frontend y
enrutar hacia el backend). Cliente de Object Storage (declarado en el stack, para la entidad
"Multimedia Web"). Decisión de diseño (ver `research.md`): librería de pruebas de frontend, porque
ni el canvas ni `spec.md` ni el stack de esta ejecución la declaran — se documenta como decisión de
plan, no como requisito. La política de reintento del adaptador hacia el contrato compartido (T006)
queda definida en `research.md` §"Política de reintento del contrato compartido" (máx. 3 intentos,
backoff exponencial 1s/2s/4s) y §"Política de reintento y resincronización de FR-BW-044" (mismo
backoff, resincronización por reconsulta tras 3 intentos fallidos o evento fuera de orden).

**Storage**: Object Storage (declarado en el stack de BW, para "Multimedia Web"). BW **no** declara
una base de datos relacional propia: los datos de negocio que administra (Ficha clientes,
Disponibilidad Agenda, Catálogo de servicios, Profesionales y especialidades) se leen/escriben a
través del contrato de API interno compartido con Backend Agendamiento (FR-BW-009 a FR-BW-012 y
FR-BW-029 a FR-BW-034, aclarado en `spec.md` §Clarifications). Ver `data-model.md` para el detalle
de qué entidades son propias de BW (Multimedia Web) y cuáles son leídas de un contrato externo.

**Testing**: Backend: pruebas unitarias con pytest (declarado explícitamente en
`prompts/etapa-i-plan.md` §Stack: "Se incluyen test unitarios en backend"). Frontend: sin
framework de pruebas declarado explícitamente → resuelto como decisión de diseño en `research.md`
(ningún canvas, `spec.md` ni el stack de esta ejecución declaran un framework de pruebas de
frontend).

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
| P22 "Observabilidad mediante logging y monitoreo" | Abierto (justificado) | `spec.md` no declara requisitos de observabilidad para BW; no se inventa un mecanismo concreto. Justificación formal en §Complexity Tracking, requerida por Governance de la constitution para cualquier principio no resuelto. |
| P1-P8, P10-P12, P14-P15, P19 | No aplican directamente a un solo bundle backend/frontend administrativo (son de estrategia de negocio/TI o de todo el sistema) | Sin conflicto detectado. |

**Resultado**: PASA. Ninguna decisión de este plan contradice un principio de la Constitution. P22
permanece abierto por falta de requisito respaldatorio (ni FR ni NFR de BW lo declara); ver
§Complexity Tracking para su justificación formal.

## Project Structure

### Documentation (this feature)

```text
specs/001-gestion-integral-reservas/
├── plan.md              # Este archivo — alcance: bundle Backend/Frontend Web
├── research.md          # Fase 0 — decisiones de diseño y su justificación
├── data-model.md         # Fase 1 — entidades de BW
├── quickstart.md        # Fase 1 — guía de validación end-to-end de BW
├── contracts/
│   ├── bw-shared-internal-api.md   # Fase 1 — contrato compartido con AC/BA (FR-BW-029..034)
│   └── bw-data-exports.md          # Fase 1 — exportación de datos de BW (FR-BW-035..039; agregado en la re-sincronización 2026-08-08)
└── tasks.md             # Fase 2 — NO generado por /speckit-plan
```

### Source Code (repository root)

```text
bw-frontend/                # React + TypeScript estricto (tsconfig: "strict": true)
├── src/
│   ├── pages/          # Vistas administrativas: profesionales, servicios, agenda, clientes, dashboard
│   ├── components/
│   ├── types/           # Interfaces TS de las entidades de data-model.md y del contrato compartido
│   └── services/        # Cliente HTTP hacia bw-backend
├── tests/               # Framework de pruebas: decisión abierta, ver research.md
└── tsconfig.json         # "strict": true (declarado explícitamente para esta ejecución)

bw-backend/                 # Python + FastAPI
├── src/
│   ├── models/          # Esquemas Pydantic: Multimedia Web (propio); DTOs de lectura para Ficha
│   │                     # clientes, Disponibilidad Agenda, Catálogo de servicios, Profesionales y
│   │                     # especialidades (ver data-model.md — no son tablas propias de BW)
│   ├── services/
│   ├── adapters/        # Cliente hacia el contrato de API interna compartido (FR-BW-029..034)
│   └── api/             # Routers FastAPI que expone BW a bw-frontend
└── tests/
    └── unit/             # Pruebas unitarias con pytest (declarado explícitamente para esta ejecución)
```

**Structure Decision**: Web application con frontend y backend separados (`bw-frontend/`,
`bw-backend/`), siguiendo el stack declarado para el bundle BW (React + TypeScript estricto sobre
JavaScript; FastAPI sobre Python — lenguajes base de `composed/plan_input.md`, frameworks y modo de
tipado declarados explícitamente en `prompts/etapa-i-plan.md` §Stack) y aislando el acceso al
contrato compartido con AC/BA detrás de una capa `adapters/` (Principio P21). Las pruebas unitarias
de backend (`bw-backend/tests/unit/`, pytest) están declaradas explícitamente para esta ejecución;
no se declara explícitamente un framework de pruebas de frontend (ver `research.md`). No se
reutilizan ni se crean directorios para los bundles AC o BA: quedan fuera del alcance de esta etapa
por `bundle-scope.md`.

## Complexity Tracking

| Principio | Estado | Justificación |
|---|---|---|
| P22 "Observabilidad mediante logging y monitoreo" | Abierto — no resuelto en este plan | `spec.md` no declara ningún requisito (FR ni NFR) de logging/monitoreo para BW, y ningún canvas de origen lo aportó. Inventar un mecanismo concreto (librería de logging, formato de log, destino de métricas) sin un requisito que lo respalde violaría la restricción de esta etapa de no inventar decisiones no respaldadas por la Specification. Se documenta como brecha explícita — detectada por `/speckit.analyze` (hallazgo C1) — para resolverse mediante una decisión de producto/negocio explícita (p. ej. una sesión de `/speckit.clarify` que declare el requisito) antes de `/speckit.implement`, no inventándola aquí. |

Ninguna otra decisión de este plan contradice un principio de la Constitution (P9, P13, P16/P17,
P20 y P21 cumplen según la tabla de Constitution Check; P18 permanece "Parcial" por evaluación
insuficiente, no por violación, y no requiere entrada en esta tabla).
