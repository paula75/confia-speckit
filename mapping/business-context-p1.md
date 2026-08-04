# Mapping — Business Context Canvas

Fuente COM: `com/arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-business_context-p1.json`

## Fragmento para /speckit.constitution

Propósito: Proveer “Gestión integral de Reservas”.
← BCC / Business products & services (1 post-it)

## Fragmento para /speckit.specify

## Contexto

### Actores organizacionales
- “Cliente”.
- “Profesionales del Centro”.
- “Administrador del centro”.
- “Recepcionista”.

### Productos y servicios

- “Gestión integral de Reservas”.

### Business infrastructure & equipment

- “PC del Encargado del Local”.
- “Dispositivos Móvil del Recepcionista”.
- “PC del Recepcionista”.
- “Dispositivo Móvil del Cliente”.
- “PC del Cliente”.
- “Dispositivo Móvil del Profesional”.
- “PC del Profesional”.
- “Servicio Cloud”.

### Business locations

- “Región Metropolitana”.

### Business facilities

- “Oficina Administracion”.
- “Recepción”.
- “Sala de espera”.
- “Estación de trabajo”.

## Perfiles de usuario

- “Administrador de la operación”: permisos no declarados.
- “Coordinador de agenda”: permisos no declarados.
- “Prestador del servicio”: permisos no declarados.
- “Solicitante de reserva”: permisos no declarados.

## Entidades clave

- “Cliente”: atributos abiertos.
- “Profesional”: atributos abiertos.
- “Local”: atributos abiertos.
- “Disponibilidad”: atributos abiertos.
- “Historial de atención”: atributos abiertos.
- “Servicio”: atributos abiertos.
- “Agenda”: atributos abiertos.
- “Reserva”: atributos abiertos.
- “Preferencias del cliente”: atributos abiertos.

## Escenarios de negocio (no son FR)

- EN-01: “Gestionar servicios disponibles”; actor, precondición y resultado observable por confirmar.
- EN-02: “Agendar una cita”; actor, precondición y resultado observable por confirmar.
- EN-03: “Confirmar una cita”; actor, precondición y resultado observable por confirmar.
- EN-04: “Reprogramar una cita”; actor, precondición y resultado observable por confirmar.
- EN-05: “Cancelar una cita”; actor, precondición y resultado observable por confirmar.
- EN-06: “Confirmar asistencia”; actor, precondición y resultado observable por confirmar.
- EN-07: “Seguimiento de reservas”; actor, precondición y resultado observable por confirmar.
- EN-08: “Identificar requerimiento del cliente”; actor, precondición y resultado observable por confirmar.

## Agrupadores de requisitos

- “Gestión de servicios”.
- “Gestión de agendas y disponibilidad”.
- “Gestión de clientes”.
- “Gestión de profesionales”.
- “Gestión de conversaciones”.
- “Gestión de reservas”.

## Índice de requisitos (System’s functional areas)

1. “Gestión de agenda”
2. “Gestión de profesionales”
3. “Gestión de servicios”
4. “Ejecución de servicio”
5. “Seguimiento de servicio agendado”
6. “Gestión de conversacional”

Balance: 51 post-it, 0 FR numerados, 51 trazas, 4 dudas.

## Trazas

| sticky_id | sección | target_id |
|---|---|---|
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BPS-01` | Business products & services | `constitution:Propósito` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BUA-01` | Business units & actors | `spec:Contexto/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BUA-02` | Business units & actors | `spec:Contexto/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BUA-03` | Business units & actors | `spec:Contexto/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BUA-04` | Business units & actors | `spec:Contexto/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BIE-01` | Business infrastructure & equipment | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BIE-02` | Business infrastructure & equipment | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BIE-03` | Business infrastructure & equipment | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BIE-04` | Business infrastructure & equipment | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BIE-05` | Business infrastructure & equipment | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BIE-06` | Business infrastructure & equipment | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BIE-07` | Business infrastructure & equipment | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BIE-08` | Business infrastructure & equipment | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BL-01` | Business locations | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BFA-01` | Business facilities | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BFA-02` | Business facilities | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BFA-03` | Business facilities | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BFA-04` | Business facilities | `spec:Contexto` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BR-01` | Business roles | `spec:Perfiles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BR-02` | Business roles | `spec:Perfiles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BR-03` | Business roles | `spec:Perfiles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BR-04` | Business roles | `spec:Perfiles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-01` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-02` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-03` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-04` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-05` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-06` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-07` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-08` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BO-09` | Business objects | `spec:Entidades clave` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BP-01` | Business processes | `spec:Escenario EN-01` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BP-02` | Business processes | `spec:Escenario EN-02` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BP-03` | Business processes | `spec:Escenario EN-03` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BP-04` | Business processes | `spec:Escenario EN-04` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BP-05` | Business processes | `spec:Escenario EN-05` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BP-06` | Business processes | `spec:Escenario EN-06` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BP-07` | Business processes | `spec:Escenario EN-07` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BP-08` | Business processes | `spec:Escenario EN-08` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BF-01` | Business functions | `spec:Agrupadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BF-02` | Business functions | `spec:Agrupadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BF-03` | Business functions | `spec:Agrupadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BF-04` | Business functions | `spec:Agrupadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BF-05` | Business functions | `spec:Agrupadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1BF-06` | Business functions | `spec:Agrupadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1SFA-01` | System’s functional areas | `spec:Índice/1` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1SFA-02` | System’s functional areas | `spec:Índice/2` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1SFA-03` | System’s functional areas | `spec:Índice/3` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1SFA-04` | System’s functional areas | `spec:Índice/4` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1SFA-05` | System’s functional areas | `spec:Índice/5` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P1SFA-06` | System’s functional areas | `spec:Índice/6` |

## Clarifications

- [NEEDS CLARIFICATION: permisos de cada perfil no declarados en el canvas]
- [NEEDS CLARIFICATION: atributos de las entidades de negocio no declarados en el canvas]
- [NEEDS CLARIFICATION: actores, precondiciones y resultados de los procesos de negocio no declarados]
- [NEEDS CLARIFICATION: Organization, Canvas, Version y Date están vacíos en la cabecera]
