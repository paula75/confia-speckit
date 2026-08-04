<!--
Sync Impact Report
- Version change: [TEMPLATE] → 1.0.0 (ratificación inicial, revisada tras comparar
  contra una constitution manual previa redactada con ChatGPT)
- Principios I-IV: sin cambios respecto al primer borrador. Mapean 1:1 los 22
  post-its del Architectural Context Canvas / Business Context Canvas (P1-P22)
  auditados por el pipeline 7Cs (C=1.000, T=0, V=1.000). No se agregó ni descartó
  ninguno.
- Principio V añadido: "Principios Adicionales del Equipo" — incorpora 3 ideas de
  la constitution manual (supervisión humana, canal conversacional único,
  independencia del proveedor de procesamiento conversacional externo) que NO
  provienen de los 22 post-its auditados. Se marcan explícitamente como decisión
  de equipo, no como traza de canvas, para no alterar C=1.000 sobre los 22
  originales. Los dos últimos se reescribieron sin nombrar tecnología (evitando
  "WhatsApp Business" y "LLM", ambos en la lista negra T=0 del auditor) — decisión
  del usuario: neutralizar en vez de omitir o citar tal cual.
- Sección "Flujo de Trabajo de Desarrollo" (antes TODO/SECTION_3): completada con
  6 principios de proceso tomados de la constitution manual (spec-driven, entrega
  incremental, fuente única de verdad, código simple, calidad verificable,
  trazabilidad spec→plan→tarea→criterio). Tampoco trazan a post-its; son
  metodología de equipo/Spec Kit.
- Sección "Restricciones Adicionales" (SECTION_2): permanece en TODO. El alcance
  de entrega (Tarea 4, integraciones concretas) se decidió dejar para
  `/speckit-plan`, donde sí se admite nombrar tecnología, en vez de esta
  constitution.
- Plantillas dependientes (.specify/templates/*.md) no fueron modificadas por
  este comando.
- TODOs pendientes: RATIFICATION_DATE (fecha de ratificación original no provista
  por ninguna de las dos fuentes), SECTION_2_CONTENT (alcance de entrega, diferido
  a plan.md).
-->

# Gestión Integral de Reservas — Constitution

## Propósito

Proveer "Gestión integral de Reservas".
<!-- Fuente: BCC / Business products & services (1 post-it) -->

Todos los integrantes del equipo, así como los asistentes de desarrollo basados en
IA, deberán respetar los principios de este documento durante el diseño, la
implementación y la evolución del sistema. En caso de conflicto entre una decisión
de implementación y esta constitución, prevalecerán los principios aquí definidos.

## Core Principles

### I. Estrategia de Negocio
- **P1**: El sistema DEBE automatizar la atención conversacional.
- **P2**: El sistema DEBE incrementar la ocupación efectiva de las agendas.
- **P3**: El sistema DEBE reducir la carga administrativa del centro.
- **P4**: El sistema DEBE poder escalar el servicio para múltiples centros de belleza.
- **P5**: El sistema DEBE brindar atención permanente mediante canales digitales 24/7.
- **P6**: El sistema DEBE mejorar la experiencia del cliente.
<!-- Fuente: ACC/Business strategy -->

### II. Estrategia de TI
- **P7**: El sistema DEBE construirse y operarse como una plataforma SaaS.
- **P8**: El sistema DEBE ser Cloud Native.
- **P9**: El sistema DEBE integrarse de forma desacoplada con sistemas existentes.
- **P10**: El sistema DEBE ofrecer configuración centralizada para múltiples centros.
<!-- Fuente: ACC/IT strategy -->

### III. Principios de Negocio
- **P11**: La experiencia del cliente TIENE prioridad sobre otras consideraciones de diseño.
- **P12**: La automatización DEBE lograrse sin modificar la operación del centro.
- **P13**: DEBE mantenerse una única fuente de información para las reservas.
- **P14**: El sistema DEBE facilitar la autogestión del cliente.
- **P15**: El diseño DEBE minimizar el impacto sobre los procesos actuales.
<!-- Fuente: ACC/Business principles -->

### IV. Principios Técnicos
- **P16**: El sistema DEBE mantener bajo acoplamiento entre componentes.
- **P17**: El sistema DEBE mantener alta cohesión dentro de cada componente.
- **P18**: El diseño DEBE priorizar la configuración antes que la personalización.
- **P19**: Los componentes DEBEN ser reutilizables.
- **P20**: El sistema DEBE soportar escalabilidad horizontal.
- **P21**: La integración con terceros DEBE realizarse mediante adapters.
- **P22**: El sistema DEBE proveer observabilidad mediante logging y monitoreo.
<!-- Fuente: ACC/Technical principles -->

### V. Principios Adicionales del Equipo
<!-- NOTA: estos 3 principios NO provienen de los 22 post-its auditados del
     pipeline 7Cs (no cuentan en C=1.000). Son decisión explícita del equipo,
     incorporada al comparar contra una constitution manual previa. -->
- **P23 (Negocio)**: El sistema DEBE automatizar la gestión de reservas sin
  reemplazar la toma de decisiones del administrador cuando esta requiera
  validación humana.
- **P24 (Arquitectura)**: El sistema DEBE operar, en esta iteración, sobre un
  único canal de mensajería conversacional externo. No se desarrollarán
  funcionalidades específicas para otros canales sin una actualización explícita
  de las especificaciones.
- **P25 (Arquitectura)**: La lógica de negocio NUNCA DEBE depender de un
  proveedor específico de procesamiento conversacional externo; dicho proveedor
  DEBE poder reemplazarse sin modificar las reglas de negocio.

## Restricciones Adicionales

TODO(SECTION_2_CONTENT): el alcance concreto de esta entrega (funcionalidad
representativa vs. sistema completo, integraciones específicas consideradas)
se definirá en `/speckit-plan`, donde sí se admite nombrar tecnología concreta.
No se completa aquí para mantener esta constitution libre de contaminación
técnica, consistente con T=0 exigido por la auditoría del pipeline 7Cs.

## Flujo de Trabajo de Desarrollo

- **Desarrollo guiado por especificaciones**: toda funcionalidad DEBE comenzar
  con una especificación (`spec.md`) previamente validada; no se implementará
  funcionalidad sin especificación aprobada.
- **Implementación incremental**: cada iteración DEBE entregar una
  funcionalidad pequeña, verificable y demostrable; se priorizan entregas
  frecuentes sobre implementaciones extensas.
- **Fuente única de verdad**: las decisiones funcionales se mantienen en las
  especificaciones; la documentación NO DEBE duplicar información
  innecesariamente entre README, Constitution, artefactos de Spec Kit y demás documentación del proyecto.
- **Código simple**: se privilegian soluciones simples, legibles y fáciles de
  mantener; se evita complejidad innecesaria.
- **Calidad verificable**: toda funcionalidad implementada DEBE contar con
  criterios de aceptación claramente definidos y mecanismos para verificar su
  correcto funcionamiento.
- **Trazabilidad**: toda implementación DEBE poder relacionarse con una
  especificación, un plan de implementación, una tarea y un criterio de
  aceptación.
<!-- Fuente: metodología de equipo / Spec Kit, no post-its de canvas -->

## Governance

Esta constitución prevalece sobre cualquier otra práctica o convención del
proyecto. Toda enmienda DEBE ser aprobada por el equipo antes de incorporarse
al repositorio, documentarse en este archivo, incluir un Sync Impact Report y
justificar el tipo de cambio (MAJOR/MINOR/PATCH) según versionado semántico.
Los principios aquí definidos DEBEN permanecer estables durante la evolución
del proyecto salvo enmienda explícita.

Todo plan (`/speckit-plan`), especificación (`/speckit-specify`) y revisión de
tareas DEBE verificar su alineación con los principios I-V antes de avanzar;
cualquier desviación DEBE justificarse explícitamente en el artefacto
correspondiente o elevarse como enmienda a esta constitución. La complejidad
añadida que no derive de un principio aquí listado DEBE justificarse o
eliminarse.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): fecha de ratificación original no provista | **Last Amended**: 2026-08-04
