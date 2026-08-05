# Etapa G – Clarificación del alcance de implementación

Continúa el pipeline 7Cs → Spec Kit.

Ejecuta la skill `speckit-clarify`.

## Entradas

Utiliza como fuente oficial de requisitos:

- `specs/001-gestion-integral-reservas/spec.md`

Utiliza además el documento:

- `specs/001-gestion-integral-reservas/bundle-scope.md`

La Specification (`spec.md`) representa el sistema completo.

El archivo `bundle-scope.md` define el alcance de esta ejecución y restringe el análisis al bundle seleccionado.

Respeta estrictamente el contrato definido por la propia skill.

## Alcance de esta ejecución

Todas las preguntas, aclaraciones y observaciones deberán limitarse exclusivamente al bundle definido en `bundle-scope.md`.

En particular:

- considera únicamente los requisitos funcionales pertenecientes al bundle seleccionado;
- considera únicamente las reglas de negocio, entidades, casos de borde e integraciones que afecten directamente a dicho bundle;
- considera únicamente los requisitos no funcionales aplicables al bundle.

## Dependencias

Los demás bundles deberán tratarse únicamente como dependencias arquitectónicas cuando exista una referencia explícita desde el bundle seleccionado.

No deberán generar preguntas de aclaración independientes.

## Exclusiones

No generar preguntas relacionadas con funcionalidades pertenecientes exclusivamente a otros bundles.

No ampliar el alcance definido por `bundle-scope.md`.

No resolver automáticamente elementos marcados como `[NEEDS CLARIFICATION]`.

No inventar requisitos, reglas, entidades o decisiones de diseño que no estén respaldadas por la Specification oficial.

## Resultado esperado

Generar únicamente las aclaraciones correspondientes al alcance definido por `bundle-scope.md`.

Conservar la trazabilidad con la Specification oficial.

No ejecutar automáticamente ninguna etapa posterior.

Finaliza la ejecución una vez completada la clarificación y espera nuevas instrucciones.