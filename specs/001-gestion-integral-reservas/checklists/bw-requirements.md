# Backend/Frontend Web (BW) Requirements Quality Checklist: Gestión Integral de Reservas

**Purpose**: Validar la calidad (completitud, claridad, consistencia, medibilidad, cobertura) de
los requisitos correspondientes exclusivamente al bundle "Backend/Frontend Web (BW)", antes de
avanzar a `/speckit.plan`. No valida implementación ni comportamiento del sistema — valida cómo
está escrita la especificación.

**Created**: 2026-08-05
**Feature**: [spec.md](../spec.md)
**Alcance**: restringido por [bundle-scope.md](../bundle-scope.md) al bundle Backend/Frontend Web
(BW). Los bundles Agente Conversacional (AC) y Backend Agendamiento (BA) solo se consideran cuando
un requisito de BW los referencia explícitamente (contratos compartidos, eventos conversacionales,
dependencia de Backend Agendamiento en FR-BW-044).

**Nota**: Este checklist no repite las 4 ambigüedades ya resueltas en `## Clarifications` de
`spec.md` (Sesión 2026-08-05: contrato compartido FR-BW-029..034, permisos de FR-BW-005..008,
disparador de FR-BW-044, diferimiento de atributos de 4 entidades). Donde aparecen abajo, es
porque la resolución deja un ángulo distinto todavía sin especificar (ver referencia de cada ítem).

## Requirement Completeness

- [ ] CHK001 - ¿Se especifica cuáles de las 12 restricciones (R-1 a R-12) aplican específicamente al bundle Backend/Frontend Web, en vez de asumir que todas aplican por igual a todo el sistema? [Completeness, Gap, Spec §Restricciones]
- [ ] CHK002 - ¿Se especifica cuáles de los requisitos no funcionales (NFR-TEC-1..6, NFR-OP-1..3) aplican al bundle Backend/Frontend Web específicamente, o si tiene umbrales propios distintos a los del resto del sistema? [Completeness, Gap, Spec §Non-Functional Requirements]
- [x] CHK003 - ¿Existen requisitos funcionales para la entidad "Multimedia Web" (declarada como objeto de datos propio de BW) más allá de su mención en Key Entities — por ejemplo, carga, límites de almacenamiento o recuperación? [Completeness, Gap, Spec §Key Entities] — Resuelto (Clarifications, Sesión 2026-08-08): decisión explícita de dejarlo fuera de alcance de esta iteración, no un vacío sin examinar.
- [ ] CHK004 - ¿Se define algún requisito sobre qué datos compone el "Dashboard resumen" (FR-BW-022)? [Completeness, Gap, Spec §FR-BW-022]

## Requirement Clarity

- [ ] CHK005 - ¿Está definido "resultado observable" (usado de forma genérica en FR-BW-022 a FR-BW-028) con algún criterio concreto y verificable, o queda como frase de relleno? [Clarity, Ambiguity, Spec §FR-BW-022..028]
- [ ] CHK006 - ¿Está aclarado qué información específica debe mostrar el "Dashboard resumen" (FR-BW-022)? [Clarity, Ambiguity, Spec §FR-BW-022]

## Requirement Consistency

- [x] CHK007 - ¿Está explícita la relación entre los "Actores organizacionales" de §Contexto (Cliente, Profesionales del Centro, Administrador del centro, Recepcionista) y los "perfiles"/roles de §Perfiles de Usuario y Permisos (Administrador de la operación, Coordinador de agenda, Prestador del servicio, Solicitante de reserva), de modo que quede claro qué actor organizacional ejerce el rol "Administrador de la operación" ahora autorizado para FR-BW-005 a FR-BW-008? [Consistency, Ambiguity, Spec §Contexto vs §Perfiles de Usuario y Permisos] — Resuelto (Clarifications, Sesión 2026-08-08): "Administrador del centro".
- [ ] CHK008 - ¿Especifican los "Helpers" que BW comparte de nombre con otro bundle (FR-BW-020 "Selección de horarios" y FR-BW-021 "Validación de reservas", también presentes como FR-BA-014/FR-BA-015) si BW ejecuta su propia lógica o invoca la misma implementación compartida ya aclarada para los contratos de API en FR-BW-029 a FR-BW-034? [Consistency, Ambiguity, Spec §FR-BW-020, §FR-BW-021, §Clarifications]
- [ ] CHK009 - Ahora que FR-BW-029 a FR-BW-034 quedaron aclarados como un contrato de API interna compartido, ¿especifica la sección de Edge Cases sobre falla de contrato interno si el manejo de error es centralizado en la implementación compartida o debe replicarse en cada bundle consumidor, incluyendo BW? [Consistency, Gap, Spec §Edge Cases vs §Clarifications]
- [ ] CHK010 - ¿Son consistentes en el dato o disparador que esperan los tres requisitos de BW que reaccionan a eventos conversacionales originados en otro bundle (FR-BW-016 "Mensaje recibido", FR-BW-017 "Estado de mensaje recibido", FR-BW-018 "Error de interpretacion (derivar)"), dado que los mismos nombres de evento también son requisitos del bundle Agente Conversacional? [Consistency, Dependency, Spec §FR-BW-016..018]

## Acceptance Criteria Quality

- [ ] CHK011 - ¿Puede verificarse objetivamente el escenario de aceptación compartido por casi todos los FR-BW ("...el sistema completa [X] y deja un resultado observable") sin más detalle sobre qué constituye ese resultado observable en cada caso? [Measurability, Spec §FR-BW-001..044]
- [ ] CHK012 - ¿Están definidas métricas a nivel de bundle para la contribución de Backend/Frontend Web a los Criterios de Éxito del sistema (p. ej. CE-2 "incrementar conversión", CE-5 "mantener sincronizada la agenda", CE-7 "centralizar la gestión de reservas"), o solo existen a nivel de sistema completo? [Measurability, Gap, Spec §Success Criteria]

## Scenario Coverage

- [x] CHK013 - ¿Se especifican flujos negativos/de excepción para las 4 acciones de BW restringidas a "Administrador de la operación" (FR-BW-005 a FR-BW-008) — por ejemplo, qué ocurre si un rol no autorizado intenta ejecutarlas? [Coverage, Gap, Spec §FR-BW-005..008] — Resuelto (Clarifications, Sesión 2026-08-08): la interfaz oculta la acción para cualquier otro rol.
- [ ] CHK014 - ¿Existe un requisito sobre qué debe mostrar o hacer Backend/Frontend Web cuando los datos de "Disponibilidad Agenda", "Ficha clientes", "Catálogo de servicios" o "Profesionales y especialidades" están vacíos o aún no disponibles (estado cero)? [Coverage, Edge Case, Gap, Spec §FR-BW-009..012]

## Edge Case Coverage

- [x] CHK015 - ¿Se aborda en algún lugar de la especificación el "comportamiento ante fallo" de FR-BW-044 (reintentos, orden de eventos, eventos perdidos), más allá de quedar señalado como no resuelto? [Edge Case, Gap, Spec §FR-BW-044] — Resuelto (Clarifications, Sesión 2026-08-08): reintento y resincronización por reconsulta.
- [x] CHK016 - ¿Existe un requisito sobre qué debe hacer Backend/Frontend Web cuando los contratos de API interna compartidos (FR-BW-029 a FR-BW-034) no están disponibles o devuelven error, dado que el esquema y el formato de error quedaron explícitamente diferidos a `/speckit.plan`? [Edge Case, Gap, Spec §FR-BW-029..034] — Resuelto (Clarifications, Sesión 2026-08-08): reintento automático.

## Non-Functional Requirements

- [ ] CHK017 - ¿Existen requisitos no funcionales propios de Backend/Frontend Web (p. ej. tiempo de carga de página, sesiones administrativas concurrentes) más allá de los NFR-TEC-1..6 y NFR-OP-1..3 de todo el sistema? [Completeness, Gap, Spec §Non-Functional Requirements]
- [ ] CHK018 - ¿Se define qué ve o se le informa a "Administrador de la operación" cuando una actualización de agenda (FR-BW-044) todavía no se ha propagado, dado que el requisito ahora especifica sincronización en tiempo real por evento? [Coverage, Gap, Spec §FR-BW-044]

## Dependencies & Assumptions

- [ ] CHK019 - ¿Está validado o al menos señalado como supuesto que el bundle Backend Agendamiento siempre emite el evento de cambio de agenda que requiere el disparador en tiempo real ya aclarado para FR-BW-044? [Assumption, Spec §FR-BW-044, §Clarifications]
- [ ] CHK020 - ¿Están las entidades que BW importa pero no posee (Reglas de negocio, Historial Conversación, Configuración conversacional — FR-BW-013 a FR-BW-015) referenciadas hacia el bundle responsable de su esquema? [Dependency, Gap, Spec §FR-BW-013..015]

## Ambiguities & Conflicts

- [ ] CHK021 - ¿Se refleja de forma consistente el diferimiento del esquema de atributos de Ficha clientes, Disponibilidad Agenda, Catálogo de servicios y Profesionales y especialidades (registrado en §Clarifications) en todos los lugares donde esas entidades aparecen dentro de los requisitos funcionales de BW (imports, exports, UI-processing), o solo en §Key Entities? [Consistency, Spec §Key Entities vs §FR-BW-001..044]
- [ ] CHK022 - ¿Tienen los tres roles ahora excluidos de FR-BW-005 a FR-BW-008 ("Coordinador de agenda", "Prestador del servicio", "Solicitante de reserva") algún otro requisito propio de BW que implique que necesitan acceder al bundle, generando un posible conflicto con la aclaración "solo Administrador de la operación"? [Conflict, Ambiguity, Spec §FR-BW-001..044 vs §Clarifications]

## Notes

- **Sesión 2026-08-08**: sesión adicional de `/speckit.clarify` (bundle BW) resolvió CHK003, CHK007,
  CHK013, CHK015 y CHK016 — ver `## Clarifications` en `spec.md`, Sesión 2026-08-08. CHK018,
  CHK019 y CHK022 quedan pendientes: la resolución de FR-BW-044 cubre el mecanismo de
  reintento/resincronización pero no qué ve el Administrador durante la ventana de propagación
  (CHK018), ni valida explícitamente el supuesto de que Backend Agendamiento siempre emite el
  evento (CHK019); CHK022 (conflicto de acceso de los 3 roles excluidos) no fue parte de esta
  sesión.
- Check items off as completed: `[x]`
- Este checklist valida la ESCRITURA de los requisitos de BW (completitud/claridad/consistencia/medibilidad/cobertura), no el comportamiento del sistema ni la implementación.
- No se generaron ítems sobre funcionalidad exclusiva de Agente Conversacional (AC) o Backend Agendamiento (BA), salvo donde un requisito de BW los referencia explícitamente (FR-BW-016..018, FR-BW-020..021, FR-BW-029..034, FR-BW-044).
- No se modificó `spec.md` en esta etapa.
