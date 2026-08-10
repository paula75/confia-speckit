# Implementation Plan: Gestión Integral de Reservas — Bundle Backend/Frontend Web (BW), solo Backend

**Branch**: `001-gestion-integral-reservas` | **Date**: 2026-08-09 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-gestion-integral-reservas/spec.md`, restringida
al bundle Backend/Frontend Web (BW) por `/specs/001-gestion-integral-reservas/bundle-scope.md`, y
restringida además **exclusivamente al componente backend** de ese bundle por instrucción explícita
de esta ejecución (`prompts/etapa-i-plan.md`: "diseñar unicamente el bundle de backend"). Agente
Conversacional (AC) y Backend Agendamiento (BA) se tratan únicamente como dependencias
arquitectónicas donde `spec.md` los referencia explícitamente desde un requisito de BW (contrato de
API interna compartido en FR-BW-029 a FR-BW-034; evento de agenda de FR-BW-044; eventos
conversacionales de FR-BW-016 a FR-BW-018). No se diseñó ninguna funcionalidad exclusiva de AC o BA.

**Re-sincronización (2026-08-09b)**: esta ejecución reemplaza por completo la versión anterior de
este plan (2026-08-09) en cuatro aspectos declarados explícitamente como nueva entrada de
`prompts/etapa-i-plan.md`:

1. **Solo backend**: se elimina todo diseño de `bw-frontend` (React/TypeScript). El diseño de la
   interfaz web queda diferido a una futura ejecución de `/speckit-plan` que la incluya
   explícitamente en su entrada — no se diseña "por adelantado" aquí.
2. **PostgreSQL como base de datos propia** ("Base de datos postgresql a través de una imagen de
   docker"), no declarada en la ejecución del 2026-08-08. Esto **revierte** la decisión previa "BW no
   declara una base de datos relacional propia", que dependía explícitamente de que ningún canvas ni
   entrada de stack declarara una BD (`plan.md` v.2026-08-08 §Storage: "ningún canvas ni la entrada
   de plan declaró una base de datos"). Con esta nueva entrada, la premisa de esa decisión ya no es
   cierta, y esta ejecución la reemplaza — ver `research.md` §"Persistencia propia de BW (PostgreSQL)"
   para el detalle. Esto también resuelve, sin inventar alcance de negocio, la brecha crítica
   detectada por `/speckit-analyze` (hallazgo I1, sesión 2026-08-09): cómo persisten las escrituras
   administrativas de BW (crear/modificar profesional, servicios, agenda, clientes — FR-BW-005 a
   FR-BW-008) dado que el contrato compartido documentado no tenía ninguna operación de escritura
   para esas entidades.
3. **Dockerización del backend**, no declarada en la ejecución del 2026-08-08.
4. **Pruebas unitarias con sesión aislada de DB** ("Se incluyen test unitarios en backend que usan
   una sesion aislada de DB"), precisión no declarada en la ejecución del 2026-08-09. Resuelve, con
   evidencia de stack (no por invención), el hallazgo HIGH de la sesión de `/speckit-analyze`
   inmediatamente posterior a esa ejecución: ningún task definía cómo las pruebas unitarias
   obtenían una base de datos aislada para ejercitar `ProfesionalService` contra PostgreSQL real —
   ver `research.md` §"Estrategia de aislamiento de base de datos en pruebas".

## Summary

El backend de Backend/Frontend Web (`bw-backend`) es el servicio administrativo del sistema de
"Gestión integral de Reservas": expone la API que permite crear/modificar profesionales, servicios y
agenda, y modificar datos de clientes (FR-BW-001 a FR-BW-044), restringido al rol "Administrador de
la operación" (aclarado en `spec.md` §Clarifications). Enfoque técnico: servicio backend en Python +
FastAPI, persistiendo directamente en PostgreSQL (contenedorizado vía Docker) las 4 entidades que
`spec.md` §Clarifications identificó como administradas por CRUD por BW (Ficha clientes,
Disponibilidad Agenda, Catálogo de servicios, Profesionales y especialidades); la operación de
Reserva (crear/actualizar/cancelar) permanece delegada al contrato de API interna compartido con
Backend Agendamiento, porque "Reserva" no es una de esas 4 entidades administradas por BW. El diseño
de `bw-frontend` (React + TypeScript) queda explícitamente fuera de esta ejecución.

## Technical Context

**Language/Version**: Python (versión no especificada) con FastAPI (framework declarado
explícitamente en `prompts/etapa-i-plan.md` §Stack: "Backend usa python con el framework FastAPI").

**Primary Dependencies**: FastAPI con su servidor ASGI estándar (uvicorn). SQLAlchemy como ORM sobre
PostgreSQL y Alembic para migraciones — decisión de diseño (ver `research.md` §"Motor de base de
datos y ORM"), porque el stack de esta ejecución declara PostgreSQL pero no declara un ORM ni una
herramienta de migraciones. Cliente de adaptador hacia el contrato de API interna compartido con
Backend Agendamiento (Reserva Command API + evento de sincronización de agenda, FR-BW-032..034 y
FR-BW-044), con reintento automático (`research.md` §"Política de reintento del contrato
compartido"). Driver `psycopg` para la conexión a PostgreSQL.

**Storage**: PostgreSQL, corriendo vía imagen de Docker (declarado explícitamente en
`prompts/etapa-i-plan.md` §Stack). Es la base de datos propia de `bw-backend`: almacena las 4
entidades que BW administra por CRUD (Ficha clientes, Disponibilidad Agenda, Catálogo de servicios,
Profesionales y especialidades — ver `data-model.md`). La entidad "Multimedia Web" permanece
declarada pero sin requisito funcional propio en esta iteración (Clarifications, Sesión 2026-08-08:
"fuera de alcance por ahora"); no se decide su mecanismo de almacenamiento porque ningún FR-BW lo
exige todavía. La entidad "Reserva" **no** se persiste en el PostgreSQL de BW: sigue siendo
propiedad de Backend Agendamiento, consumida mediante el contrato compartido (Principio de
constitution P13 "única fuente de información para las reservas" — ver §Constitution Check).

**Testing**: pruebas unitarias con pytest, cada una ejecutándose contra una **sesión aislada de
base de datos** (declarado explícitamente en `prompts/etapa-i-plan.md` §Stack: "Se incluyen test
unitarios en backend que usan una sesion aislada de DB"). Se resuelve como una transacción
SQLAlchemy por test con rollback automático al finalizar (ver `research.md` §"Estrategia de
aislamiento de base de datos en pruebas") — no una base de datos física separada por test, sino una
sesión aislada dentro del mismo PostgreSQL de `docker-compose.yml`, consistente con la literalidad
de "sesión aislada" (no "base de datos aislada"). Sin alcance de frontend en esta ejecución.

**Target Platform**: Servicio backend contenedorizado con Docker (declarado explícitamente:
"Backend se dockeriza"), con PostgreSQL como contenedor dependiente (declarado explícitamente: "a
través de una imagen de docker"). Sin navegador/cliente en el alcance de esta ejecución — `spec.md`
sigue describiendo un sistema con interfaz web, pero su diseño queda diferido a una ejecución futura
de `/speckit-plan` que incluya `bw-frontend` en su entrada.

**Project Type**: Servicio backend único (API REST), acorde a la restricción explícita de esta
ejecución ("diseñar unicamente el bundle de backend"). No es una "Web application" de
frontend+backend en esta pasada — a diferencia de la ejecución anterior (2026-08-08), que sí incluía
`bw-frontend`.

**Performance Goals**: No declarado para BW específicamente. Sin cambios respecto a la ejecución
anterior — `spec.md` no declara un objetivo de desempeño propio de BW (ver
`checklists/bw-requirements.md` CHK002/CHK017); no se infiere aquí.

**Constraints**: "Recibir derivación de LLM para atención humana" (declarada para el bundle BW en
`composed/plan_input.md` §Constraints locales, corresponde a la dependencia ya identificada en
FR-BW-018 "Error de interpretacion (derivar)", vigente para el backend). La constraint "GUI amigable"
(también declarada para BW) es exclusivamente de interfaz de usuario — no aplica al backend y queda
diferida a la futura ejecución de `/speckit-plan` que diseñe `bw-frontend`.

**Scale/Scope**: No declarado por ningún canvas ni por `spec.md`. No se infiere.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Evaluado contra `.specify/memory/constitution.md` v2.0.0, Principios I-IV (los únicos vigentes; el
Principio V fue removido en la Etapa E por no tener respaldo en el pipeline).

| Principio | Aplica a este diseño | Evaluación |
|---|---|---|
| P9 "Integración desacoplada con sistemas existentes" | Sí | El contrato interno compartido con Backend Agendamiento (Reserva Command API, FR-BW-032..034; evento de agenda, FR-BW-044) se diseña como API/evento a través de un adaptador dedicado, no como acceso directo a la base de datos de Backend Agendamiento → cumple. |
| P13 "Única fuente de información para las reservas" | Sí, con matiz explícito | BW **no** persiste la entidad "Reserva" en su PostgreSQL propio; la crea/modifica/cancela exclusivamente a través del contrato compartido con Backend Agendamiento, que sigue siendo la única fuente para reservas. La "Disponibilidad Agenda" que BW sí persiste localmente es un reflejo sincronizado en tiempo real de los cambios que "Backend Agendamiento" emite (FR-BW-044), no una fuente independiente: ante evento perdido o fuera de orden, BW resincroniza reconsultando a Backend Agendamiento en vez de confiar en su copia local desactualizada (ver `research.md`). Se documenta explícitamente por ser una relectura de la decisión de la ejecución anterior (2026-08-08), motivada por la nueva entrada de PostgreSQL. |
| P16 "Bajo acoplamiento" / P17 "Alta cohesión" | Sí | Capa `adapters/` aislada para el único contrato externo real (Reserva Command API + evento de agenda de Backend Agendamiento) separada de la capa `db/` de persistencia propia → cumple. |
| P18 "Configuración antes que personalización" | Parcial | Sin cambios respecto a la ejecución anterior: no hay suficiente información en `spec.md` para evaluarlo más allá de la estructura propuesta. |
| P20 "Escalabilidad horizontal" | Sí | Backend Python sin estado propio en memoria (el estado vive en PostgreSQL), contenedorizado con Docker → admite réplicas horizontales del servicio backend sin cambio de diseño (el propio PostgreSQL no se diseña aquí como clúster de alta disponibilidad — ningún FR-BW ni NFR de esta ejecución lo exige). |
| P21 "Integración mediante adapters" | Sí | El acceso al contrato compartido con Backend Agendamiento (Reserva Command API + evento de agenda) se aísla en `adapters/`. El acceso a PostgreSQL **no** es "integración con terceros" en el sentido de P21 — es la base de datos propia del servicio, vía la capa `db/`/ORM, no un adapter hacia un sistema externo. |
| P22 "Observabilidad mediante logging y monitoreo" | Abierto (justificado) | Sin cambios respecto a la ejecución anterior: `spec.md` no declara requisitos de observabilidad para BW. Justificación formal en §Complexity Tracking. |
| P1-P8, P10-P12, P14-P15, P19 | No aplican directamente a un solo servicio backend administrativo (son de estrategia de negocio/TI o de todo el sistema) | Sin conflicto detectado. |

**Resultado**: PASA. Ninguna decisión de este plan contradice un principio de la Constitution. P13
requirió una justificación explícita por el cambio de "sin BD propia" a "con BD propia" (ver tabla);
P22 permanece abierto por falta de requisito respaldatorio; ver §Complexity Tracking para ambas.

## Project Structure

### Documentation (this feature)

```text
specs/001-gestion-integral-reservas/
├── plan.md              # Este archivo — alcance: bundle Backend/Frontend Web, solo backend
├── research.md          # Fase 0 — decisiones de diseño y su justificación
├── data-model.md         # Fase 1 — entidades de BW (ahora persistidas en PostgreSQL)
├── quickstart.md        # Fase 1 — guía de validación end-to-end del backend de BW
├── contracts/
│   ├── bw-shared-internal-api.md   # Fase 1 — contrato con Backend Agendamiento (consumido: Reserva Command API + evento de agenda; servido: Disponibilidad/Servicios/Profesionales Query API)
│   └── bw-data-exports.md          # Fase 1 — exportación de datos de BW (FR-BW-035..039)
└── tasks.md             # Fase 2 — NO generado por /speckit-plan; requiere regenerarse tras esta re-sincronización
```

### Source Code (repository root)

```text
bw-backend/                 # Python + FastAPI + PostgreSQL, dockerizado
├── src/
│   ├── models/          # Modelos SQLAlchemy (tablas propias de BW en PostgreSQL): Ficha clientes,
│   │                     # Disponibilidad Agenda, Catálogo de servicios, Profesionales y
│   │                     # especialidades (ver data-model.md); schemas Pydantic de entrada/salida
│   ├── services/
│   ├── adapters/        # Cliente hacia Backend Agendamiento: Reserva Command API (consumida,
│   │                     # FR-BW-032..034) y receptor del evento de sincronización de agenda
│   │                     # (FR-BW-044) — único acceso externo real de BW (Principio P21)
│   ├── api/              # Routers FastAPI: endpoints administrativos propios de BW (profesionales,
│   │                     # servicios, agenda, clientes) y los que BW sirve al resto del sistema
│   │                     # (Disponibilidad/Servicios/Profesionales Query API, FR-BW-029..031)
│   └── db/               # Conexión a PostgreSQL (SQLAlchemy engine/session), migraciones Alembic
├── tests/
│   ├── conftest.py       # Fixture de sesión aislada de DB por test (transacción + rollback sobre
│   │                     # el PostgreSQL de docker-compose.yml — ver research.md)
│   └── unit/             # Pruebas unitarias con pytest (declarado explícitamente para esta ejecución)
├── Dockerfile             # Dockerización del backend (declarado explícitamente para esta ejecución)
└── docker-compose.yml     # Orquesta bw-backend + contenedor PostgreSQL (imagen oficial postgres)
```

**Structure Decision**: Servicio backend único (`bw-backend/`), sin `bw-frontend/` en esta ejecución
(restricción explícita de `prompts/etapa-i-plan.md`). PostgreSQL como base de datos propia,
contenedorizada junto al backend vía `docker-compose.yml`. El único acceso externo real que conserva
BW es el contrato con Backend Agendamiento (Reserva Command API + evento de agenda), aislado detrás
de `adapters/` (Principio P21); el resto de la persistencia (Ficha clientes, Disponibilidad Agenda,
Catálogo de servicios, Profesionales y especialidades) es responsabilidad directa de `bw-backend`
sobre su propio PostgreSQL, sin pasar por ningún contrato externo para escribir.

## Complexity Tracking

| Principio | Estado | Justificación |
|---|---|---|
| P13 "Única fuente de información para las reservas" | Resuelto con matiz — ver Constitution Check | Esta ejecución revierte la decisión previa "BW sin BD propia" porque el stack de esta ejecución declara PostgreSQL explícitamente (`prompts/etapa-i-plan.md`), premisa que no existía en la ejecución anterior. Para no crear una segunda fuente de verdad para reservas, se acota expresamente: (1) la entidad "Reserva" nunca se persiste en el PostgreSQL de BW — solo se consume vía el contrato compartido con Backend Agendamiento; (2) "Disponibilidad Agenda" sí se persiste localmente, pero como copia sincronizada en tiempo real desde Backend Agendamiento (FR-BW-044), con resincronización por reconsulta ante evento perdido o fuera de orden (ver `research.md`), nunca como fuente independiente que Backend Agendamiento deba consultar. |
| P22 "Observabilidad mediante logging y monitoreo" | Abierto — no resuelto en este plan | Sin cambios respecto a la ejecución anterior: `spec.md` no declara ningún requisito (FR ni NFR) de logging/monitoreo para BW. Inventar un mecanismo concreto violaría la restricción de esta etapa de no inventar decisiones no respaldadas por la Specification. Se documenta como brecha explícita — detectada originalmente por `/speckit.analyze` (hallazgo C1, sesión previa) — para resolverse mediante una decisión de producto/negocio explícita antes de `/speckit.implement`. |

Ninguna otra decisión de este plan contradice un principio de la Constitution (P9, P16/P17, P20 y
P21 cumplen según la tabla de Constitution Check; P18 permanece "Parcial" por evaluación
insuficiente, no por violación).
