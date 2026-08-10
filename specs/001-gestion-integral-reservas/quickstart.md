# Quickstart: Validación end-to-end del backend del bundle Backend/Frontend Web (BW)

**Alcance**: valida únicamente el backend administrativo de BW (`bw-backend`). No cubre `bw-frontend`
(fuera de esta ejecución, `prompts/etapa-i-plan.md`), Agente Conversacional ni Backend Agendamiento
salvo como dependencia simulada (mock) del contrato consumido — ver
`contracts/bw-shared-internal-api.md` §Parte 2.

## Prerrequisitos

- `docker compose up` en `bw-backend/` (ver `plan.md` §Project Structure): levanta el contenedor de
  `bw-backend` (FastAPI) y un contenedor PostgreSQL (imagen oficial `postgres`), declarados
  explícitamente en `prompts/etapa-i-plan.md` §Stack.
- Migraciones de Alembic aplicadas contra ese PostgreSQL (`data-model.md`).
- Un doble de prueba (mock/stub) de Backend Agendamiento para las 3 operaciones de Reserva
  Command API y el evento de agenda que BW consume (`contracts/bw-shared-internal-api.md` §Parte 2)
  — la conexión real entre bundles no se implementa en esta etapa.
- Una sesión autenticada con el rol "Administrador de la operación" (único rol autorizado para las 4
  acciones administrativas de BW, aclarado en `spec.md` §Clarifications). Este quickstart no cubre el
  mecanismo de autenticación en sí: `spec.md` no lo declara.
- Sin `bw-frontend`: todas las llamadas de este quickstart se hacen directamente contra `bw-backend`
  (p. ej. `curl`/`httpx`/`TestClient` de FastAPI), no a través de una interfaz web.

## Escenario 1 — Crear/modificar un profesional (FR-BW-005)

1. `POST /profesionales` con `{"nombre": "..."}` (ver `data-model.md` §Profesionales y
   especialidades), autenticado como "Administrador de la operación".
2. **Resultado esperado**: `bw-backend` persiste el registro en su tabla PostgreSQL propia y
   responde con un resultado observable (Escenario de FR-BW-005); `GET /profesionales/{id}` (FR-BW-025)
   devuelve el registro recién creado.

## Escenario 2 — Crear/modificar un servicio (FR-BW-006)

1. `POST /servicios` con `{"nombre": "..."}` (ver `data-model.md` §Catálogo de servicios).
2. **Resultado esperado**: el servicio queda persistido en PostgreSQL y disponible vía
   `GET /servicios/query` (Parte 1 de `contracts/bw-shared-internal-api.md`).

## Escenario 3 — Modificar la agenda (FR-BW-007) y verificar sincronización en tiempo real (FR-BW-044)

1. `PUT /agenda/{id}` para modificar un bloque de "Disponibilidad Agenda".
2. Con el doble de prueba de Backend Agendamiento, emitir un evento simulado de cambio de agenda.
3. **Resultado esperado**: `bw-backend` aplica el cambio de inmediato a su tabla PostgreSQL
   (disparador en tiempo real aclarado para FR-BW-044 en `spec.md` §Clarifications).
4. **Comportamiento ante fallo del evento** (resuelto, Clarifications Sesión 2026-08-08 +
   `research.md` §"Política de reintento y resincronización de FR-BW-044"): con el doble de prueba,
   simular una falla al procesar el evento y verificar que `bw-backend` reintenta hasta 3 veces;
   luego simular que el evento se pierde definitivamente y verificar que `bw-backend` reconsulta el
   rango afectado directamente al doble de prueba de Backend Agendamiento (no a su propio
   `GET /agenda/query`) y sobrescribe su copia local.

## Escenario 4 — Modificar datos de un cliente (FR-BW-008)

1. `PUT /clientes/{id}` para un `Ficha clientes.id` existente.
2. **Resultado esperado**: resultado observable según FR-BW-008; el cambio se refleja en
   `GET /clientes/{id}` (FR-BW-024) y en `GET /clientes/export` (FR-BW-036).

## Escenario 5 — Autorización (aclaración de Etapa G)

1. Repetir el Escenario 1 con una sesión que **no** tenga el rol "Administrador de la operación".
2. **Resultado esperado**: la API rechaza la solicitud. `spec.md` no define el código/mensaje exacto
   de rechazo — este quickstart valida solo que la acción NO se ejecuta. El ocultamiento de la
   acción en una interfaz de usuario queda fuera de esta ejecución (sin `bw-frontend`).

## Pruebas unitarias de backend

`bw-backend` incluye pruebas unitarias con pytest (`bw-backend/tests/unit/`, declarado
explícitamente en `prompts/etapa-i-plan.md` §Stack), cada una corriendo contra una sesión aislada de
base de datos (transacción con rollback sobre el mismo PostgreSQL de `docker-compose.yml` — ver
`research.md` §"Estrategia de aislamiento de base de datos en pruebas"), por lo que `pytest` puede
correr repetidamente sin dejar datos residuales entre corridas. Este quickstart valida el flujo
end-to-end manualmente; la ejecución de `pytest` sobre `bw-backend/tests/unit/` es el mecanismo de
verificación automatizada de la lógica de backend y se define en `/speckit.tasks`, no aquí.

## Fuera de alcance de este quickstart

- `bw-frontend`: excluido de esta ejecución de `/speckit-plan` (`prompts/etapa-i-plan.md`).
- Flujo conversacional (Agente Conversacional) y agendamiento automático (Backend Agendamiento):
  otros bundles, fuera de `bundle-scope.md`.
- Validación de umbrales de NFR-TEC/NFR-OP: no declarados para BW.
- Carga de "Multimedia Web": ningún FR-BW define su flujo (ver `data-model.md`).
- Alta disponibilidad/clustering de PostgreSQL: se usa una única instancia vía Docker (ver
  `research.md` §"Fuera de alcance de esta investigación").
