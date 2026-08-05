<!--
Sync Impact Report
- Version change: 1.0.0 → 2.0.0 (MAJOR — remoción retroactiva de contenido no
  respaldado por el pipeline 7Cs, por instrucción explícita de la Etapa E de
  regeneración: la constitution debe derivarse EXCLUSIVAMENTE de
  `composed/prompt_constitution.md`).
- Principios I-IV: SIN CAMBIOS de contenido. Siguen mapeando 1:1 los 22 post-its
  del Architectural Context Canvas / Business Context Canvas (P1-P22) auditados
  por el pipeline 7Cs (C=1.000, T=0, V=1.000). No se agregó ni descartó ninguno.
- REMOVIDO: Principio V "Principios Adicionales del Equipo" (P23, P24, P25). Estas
  3 reglas (supervisión humana, canal conversacional único, independencia del
  proveedor de procesamiento conversacional externo) no provienen de ningún
  post-it de `composed/prompt_constitution.md` — eran una decisión de equipo
  incorporada en la versión 1.0.0. Se retiran para que la constitution quede
  respaldada en su totalidad por el prompt de entrada del pipeline, tal como
  exige esta etapa. No se pierden: quedan documentadas aquí y pueden
  reincorporarse mediante una enmienda explícita si el equipo las ratifica de
  nuevo.
- REMOVIDO: sección "Flujo de Trabajo de Desarrollo" (SECTION_3), con sus 6
  principios de proceso (spec-driven, entrega incremental, fuente única de
  verdad, código simple, calidad verificable, trazabilidad spec→plan→tarea→
  criterio). Ninguno trazaba a un post-it del pipeline; vuelve a
  TODO(SECTION_3_CONTENT) por la misma razón que el punto anterior.
- Sección "Restricciones Adicionales" (SECTION_2): permanece en TODO, sin
  cambios. El alcance de entrega se sigue difiriendo a `/speckit-plan`, donde sí
  se admite nombrar tecnología, en vez de esta constitution.
- Governance: referencia a "principios I-V" corregida a "principios I-IV" para
  reflejar la remoción del Principio V.
- Plantillas dependientes (.specify/templates/*.md) no fueron modificadas por
  este comando.
- TODOs pendientes: RATIFICATION_DATE (fecha de ratificación original no provista
  por ninguna fuente), SECTION_2_CONTENT (alcance de entrega, diferido a
  plan.md), SECTION_3_CONTENT (flujo de trabajo, diferido — no respaldado por
  el pipeline).
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

## Restricciones Adicionales

TODO(SECTION_2_CONTENT): el alcance concreto de esta entrega (funcionalidad
representativa vs. sistema completo, integraciones específicas consideradas)
se definirá en `/speckit-plan`, donde sí se admite nombrar tecnología concreta.
No se completa aquí para mantener esta constitution libre de contaminación
técnica, consistente con T=0 exigido por la auditoría del pipeline 7Cs, y para
no incorporar contenido sin respaldo en `composed/prompt_constitution.md`.

## Flujo de Trabajo de Desarrollo

TODO(SECTION_3_CONTENT): el flujo de trabajo de desarrollo del equipo (proceso
spec-driven, cadencia de entregas, revisión de calidad, etc.) no está
respaldado por ningún post-it de `composed/prompt_constitution.md`. Se difiere
para no inventar política de proceso no proporcionada por el pipeline 7Cs;
puede incorporarse mediante una enmienda explícita del equipo.

## Governance

Esta constitución prevalece sobre cualquier otra práctica o convención del
proyecto. Toda enmienda DEBE ser aprobada por el equipo antes de incorporarse
al repositorio, documentarse en este archivo, incluir un Sync Impact Report y
justificar el tipo de cambio (MAJOR/MINOR/PATCH) según versionado semántico.
Los principios aquí definidos DEBEN permanecer estables durante la evolución
del proyecto salvo enmienda explícita.

Todo plan (`/speckit-plan`), especificación (`/speckit-specify`) y revisión de
tareas DEBE verificar su alineación con los principios I-IV antes de avanzar;
cualquier desviación DEBE justificarse explícitamente en el artefacto
correspondiente o elevarse como enmienda a esta constitución. La complejidad
añadida que no derive de un principio aquí listado DEBE justificarse o
eliminarse.

**Version**: 2.0.0 | **Ratified**: TODO(RATIFICATION_DATE): fecha de ratificación original no provista | **Last Amended**: 2026-08-05
