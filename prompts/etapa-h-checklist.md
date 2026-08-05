# Etapa H – Validación de la Specification

Continúa el pipeline 7Cs → Spec Kit.

Ejecuta la skill `speckit-checklist`.

## Entradas

Utiliza como fuente oficial de requisitos:

- `specs/001-gestion-integral-reservas/spec.md`

Utiliza además los siguientes artefactos generados durante el flujo:

- `specs/001-gestion-integral-reservas/bundle-scope.md`

La Specification (`spec.md`) representa el sistema completo y ya incorpora las aclaraciones aceptadas durante la etapa anterior.

El archivo `bundle-scope.md` define el alcance de esta ejecución y restringe la validación exclusivamente al bundle seleccionado.

El archivo `clarify-log.md` constituye el registro de las decisiones tomadas durante la etapa de clarificación y debe utilizarse únicamente como contexto y evidencia de trazabilidad, no como una fuente adicional de requisitos.

Respeta estrictamente el contrato definido por la propia skill.

## Alcance de esta ejecución

La validación deberá considerar exclusivamente el bundle definido en `bundle-scope.md`.

En particular:

- validar únicamente los requisitos funcionales pertenecientes al bundle seleccionado;
- validar únicamente las reglas de negocio, entidades, casos de borde e integraciones que afecten directamente a dicho bundle;
- validar únicamente los requisitos no funcionales aplicables al bundle.

## Dependencias

Los demás bundles deberán tratarse únicamente como dependencias arquitectónicas cuando exista una referencia explícita desde el bundle seleccionado.

No deberán generar observaciones independientes sobre funcionalidades fuera del alcance.

## Exclusiones

- No generar observaciones relacionadas con funcionalidades pertenecientes exclusivamente a otros bundles.
- No ampliar el alcance definido por `bundle-scope.md`.
- No modificar la Specification.
- No inventar requisitos, reglas, entidades o decisiones de diseño que no estén respaldadas por la Specification oficial.
- No volver a generar observaciones sobre aclaraciones ya resueltas y registradas durante la etapa `speckit-clarify`, salvo que detectes una inconsistencia con la Specification oficial.

## Resultado esperado

- Generar únicamente el checklist correspondiente al alcance definido por `bundle-scope.md`.
- Mantener la trazabilidad con la Specification oficial.
- Actualizar únicamente los artefactos definidos por la propia skill.
- No ejecutar automáticamente ninguna etapa posterior.

Finaliza la ejecución una vez completada la validación y espera nuevas instrucciones.