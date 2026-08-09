Genera tasks.md con estas reglas: 

# Alcance de la ejecucion
- Utiliza como fuente de requisitos `specs/001-gestion-integral-reservas/spec.md` y `specs/001-gestion-integral-reservas/bundle-scope.md` y restinge el diseño exclusivamente al bundle seleccionado
- Genera tareas únicamente para el feature de "Gestión de profesionales"

# Artefactos estperados
- Formato oficial: - [ ] Tnnn [P?] [USn] descripción con ruta.
- Despues de [USn], incluir [AC:<AC-IDs>].
- Cada tarea declara rutas exactas y asunto de commit esperado.
- No agrupar criterios no relacionados.
- No marcar paralelas tareas que modifican el mismo archivo.
- Crear primero el verificador de trazabilidad.
- Incluir una tarea final que registre SHA reales en traceability.md.
- Incluir Coverage Audit con todos los AC-IDs y sus tareas.
Organiza por setup, foundational, US-001, US-002, US-003, US-004 y válidacion final.
