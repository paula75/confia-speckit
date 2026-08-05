# Etapa I – Planificación de Implementación

Continúa el pipeline 7Cs → Spec Kit.

Ejecuta la skill `speckit-plan`.

## Entradas

Utiliza como fuente oficial de requisitos:

- `specs/001-gestion-integral-reservas/spec.md`

Utiliza además:

- `specs/001-gestion-integral-reservas/bundle-scope.md`

La Specification (`spec.md`) representa el sistema completo.

El archivo `bundle-scope.md` define el alcance de esta ejecución y restringe el diseño exclusivamente al bundle seleccionado.

Respeta estrictamente el contrato definido por la propia skill.

## Alcance de esta ejecución

El diseño deberá considerar exclusivamente el bundle definido en `bundle-scope.md`.

En particular:

- diseñar únicamente los requisitos funcionales pertenecientes al bundle seleccionado;
- diseñar únicamente las entidades utilizadas por dicho bundle;
- diseñar únicamente los contratos e interfaces necesarios para dicho bundle;
- diseñar únicamente los requisitos no funcionales aplicables al bundle;
- utilizar los demás bundles únicamente como dependencias arquitectónicas cuando exista una referencia explícita desde el bundle seleccionado.

## Restricciones

- No diseñar funcionalidades pertenecientes exclusivamente a otros bundles.
- No modificar `spec.md`.
- No modificar `bundle-scope.md`.
- No inventar nuevos requisitos funcionales.
- Resolver mediante decisiones de diseño únicamente aquellos aspectos que la Specification haya diferido explícitamente a esta etapa.
- Mantener la trazabilidad entre cada decisión de diseño y los requisitos correspondientes de `spec.md`.

## Artefactos esperados

Generar únicamente los artefactos definidos por `speckit-plan` para el bundle seleccionado, incluyendo cuando corresponda:

- `plan.md`
- `research.md`
- `data-model.md`
- `contracts/`
- `quickstart.md`

Todos los artefactos deberán describir exclusivamente el diseño del bundle Backend/Frontend Web.

## Criterios de calidad

El diseño deberá:

- respetar la Constitution del proyecto;
- mantener consistencia con la Specification oficial;
- respetar el alcance definido en `bundle-scope.md`;
- diferenciar claramente requisitos funcionales de decisiones de diseño;
- mantener trazabilidad completa entre Specification y Plan.

## Finalización

No ejecutar automáticamente ninguna etapa posterior.

Finaliza la ejecución una vez generado el plan y espera nuevas instrucciones.