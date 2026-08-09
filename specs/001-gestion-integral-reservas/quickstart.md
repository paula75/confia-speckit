# Quickstart: Validación end-to-end del bundle Backend/Frontend Web (BW)

**Alcance**: valida únicamente el flujo administrativo de BW. No cubre Agente Conversacional ni
Backend Agendamiento salvo como dependencia simulada (mock) del contrato compartido — ver
`contracts/bw-shared-internal-api.md`.

## Prerrequisitos

- `bw-backend` corriendo localmente (Python + FastAPI, ver `plan.md` §Technical Context) con un
  doble de prueba (mock/stub) del contrato `contracts/bw-shared-internal-api.md` en lugar de una
  conexión real a Backend Agendamiento — el contrato real entre bundles no se implementa en esta
  etapa.
- `bw-frontend` corriendo localmente (React + TypeScript estricto, ver `plan.md` §Technical
  Context) apuntando a `bw-backend`.
- Una sesión autenticada con el rol "Administrador de la operación" (único rol autorizado para las
  4 acciones administrativas de BW, aclarado en `spec.md` §Clarifications). Este quickstart no
  cubre el mecanismo de autenticación en sí: `spec.md` no lo declara (permisos de los demás roles
  quedan fuera de alcance, ver `checklists/bw-requirements.md` CHK013).

## Escenario 1 — Crear/modificar un profesional (FR-BW-005)

1. Enviar "Datos de profesionales" (`nombre`, ver `data-model.md` §Profesionales y
   especialidades) desde `bw-frontend`.
2. **Resultado esperado**: `bw-backend` persiste el registro y responde con un resultado
   observable (Escenario de FR-BW-005 en `spec.md`); la ficha aparece en "Ficha Profesionales"
   (FR-BW-025).

## Escenario 2 — Crear/modificar un servicio (FR-BW-006)

1. Enviar "Datos de servicios" (`nombre`, ver `data-model.md` §Catálogo de servicios).
2. **Resultado esperado**: el servicio queda disponible para "Crear Reserva Command API"
   (`contracts/bw-shared-internal-api.md`) en futuras consultas de disponibilidad.

## Escenario 3 — Modificar la agenda (FR-BW-007) y verificar sincronización en tiempo real (FR-BW-044)

1. Modificar un bloque de "Disponibilidad Agenda" desde `bw-frontend`.
2. Con el doble de prueba del contrato compartido, emitir un evento simulado de cambio de agenda
   "desde Backend Agendamiento".
3. **Resultado esperado**: `bw-backend` aplica el cambio de inmediato (disparador en tiempo real
   aclarado para FR-BW-044 en `spec.md` §Clarifications), sin esperar un sondeo periódico.
4. **Comportamiento ante fallo del evento** (resuelto, Clarifications Sesión 2026-08-08 +
   `research.md` §"Política de reintento y resincronización de FR-BW-044"): con el doble de prueba,
   simular una falla al procesar el evento (p. ej. forzar una excepción) y verificar que `bw-backend`
   reintenta hasta 3 veces; luego simular que el evento se pierde definitivamente y verificar que
   `bw-backend` invoca `GET /internal/disponibilidad` para resincronizar el rango afectado en vez de
   quedar desactualizado indefinidamente.

## Escenario 4 — Modificar datos de un cliente (FR-BW-008)

1. Enviar "Modificar datos Clientes" para un `Ficha clientes.id` existente.
2. **Resultado esperado**: resultado observable según el escenario de FR-BW-008; el cambio se
   refleja en "Ficha clientes" (FR-BW-024) y en el export (FR-BW-036).

## Escenario 5 — Autorización (aclaración de Etapa G)

1. Repetir el Escenario 1 con una sesión que **no** tenga el rol "Administrador de la operación".
2. **Resultado esperado**: la acción debe rechazarse. `spec.md` no define el código/mensaje de
   rechazo (ver `checklists/bw-requirements.md` CHK013) — este quickstart valida solo que la
   acción NO se ejecuta, no la forma exacta del rechazo.

## Pruebas unitarias de backend

`bw-backend` incluye pruebas unitarias con pytest (`bw-backend/tests/unit/`, declarado
explícitamente en `prompts/etapa-i-plan.md` §Stack). Este quickstart valida el flujo end-to-end
manualmente; la ejecución de `pytest` sobre `bw-backend/tests/unit/` es el mecanismo de
verificación automatizada de la lógica de backend y se define en `/speckit.tasks`, no aquí.

## Fuera de alcance de este quickstart

- Flujo conversacional (Agente Conversacional) y agendamiento automático (Backend Agendamiento):
  otros bundles, fuera de `bundle-scope.md`.
- Validación de umbrales de NFR-TEC/NFR-OP: no declarados para BW (ver `plan.md` §Technical
  Context → Performance Goals).
- Carga de "Multimedia Web": ningún FR-BW define su flujo (ver `data-model.md` y CHK003).
