## CL-001
Los contratos internos que usa el bundle Backend/Frontend Web (FR-BW-029 a FR-BW-034: Disponibilidad Query API, Servicios Query API, Profesionales Query API, Historial de conversación Query, Crear/Actualizar/Cancelar Reserva Command API) tienen el mismo nombre que los que usan Agente Conversacional (FR-AC-037..043) y Backend Agendamiento (FR-BA-001..008, 016..021). ¿Es la misma API interna compartida por los tres bundles, o una implementación propia de BW?

❯ 1. Misma API compartida (Recomendado)
     Los tres bundles consumen/exponen la misma API interna. Consistente con el principio de constitution P13 'única fuente de información para las reservas'.
  2. Implementación propia de BW
     BW tiene su propia implementación de estos contratos, independiente de AC y BA, aunque comparta el nombre.
  3. No se puede determinar aún
     Queda como decisión abierta para /speckit.plan; no se resuelve en esta etapa.
  4. Type something.
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  5. Chat about this


## CL-002
Spec.md marca 'permisos no declarados' para los 4 roles de negocio. Para las acciones administrativas propias de BW (crear/modificar profesional, crear/modificar servicios, modificar agenda, modificar datos de clientes — FR-BW-005 a FR-BW-008), ¿qué rol(es) deben poder ejecutarlas?

❯ 1. Solo Administrador de la operación (Recomendado)
     Únicamente ese rol puede ejecutar las 4 acciones administrativas de BW.
  2. Administrador + Coordinador de agenda
     Ambos roles pueden ejecutar las acciones administrativas; el resto no.
  3. Los 4 roles, diferenciado por acción
     Cada uno de los 4 roles declarados tiene permisos distintos según la acción; el detalle exacto se define en /speckit.plan.
  4. Type something.
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  5. Chat about this

  ## CL-003
  FR-BW-044 ('Actualización de agenda proveniente de Backend Agendamiento') no declara periodicidad, ventana de ejecución ni comportamiento ante fallo. ¿Cómo debe actualizarse la agenda en BW?

❯ 1. Tiempo real dirigido por evento (Recomendado)
     BW se actualiza inmediatamente cuando Backend Agendamiento emite el cambio. Consistente con la restricción R-9 'sincronizar disponibilidad y reservas en tiempo real'.
  2. Sondeo periódico corto (1-5 min)
     BW consulta a Backend Agendamiento a intervalos cortos en vez de reaccionar a un evento.
  3. Proceso batch (diario o similar)
     La agenda de BW se actualiza en un lote programado, no en tiempo real.
  4. Type something.
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  5. Chat about this

  ## CL-004
  Las entidades que BW administra por CRUD (Ficha clientes, Catálogo de servicios, Profesionales y especialidades, Disponibilidad Agenda) están marcadas en spec.md como 'atributos por/abiertos confirmar', sin ningún atributo declarado. ¿Cómo se debe tratar esa falta de esquema en esta etapa?

❯ 1. Diferir explícitamente a /speckit.plan (Recomendado)
     Se registra la decisión de diferir sin inventar atributos aquí, ya que el canvas no los declaró y esta etapa prohíbe inventar entidades/atributos no respaldados por la Specification.
  2. Proviene de un sistema externo a importar tal cual
     El esquema ya existe en el sistema de gestión/ERP del centro (R-7) y debe importarse en vez de definirse de cero.
  3. Type something.
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  4. Chat about this