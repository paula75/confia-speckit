---
name: 7cs-system-context
description: Skill de mapeo del pipeline 7Cs→Spec Kit. Convierte el COM de un System Context Canvas en §Alcance, §Integraciones y FR de entrada/salida de frontera para /speckit.specify, con lista negativa de fuera-de-alcance, trazas y dudas. Usar cuando exista un COM con canvas == "system_context" dentro del pipeline 7Cs, o cuando el usuario pida mapear el System Context Canvas (frontera, interfaces, integraciones) a una especificación Spec Kit.
---

# 7cs-system-context — Mapeo · System Context Canvas

**Lectura estructural:** el canvas es una retícula de 4 clases de contraparte (usuarios,
sistemas, repositorios, dispositivos) × 4 columnas (origen, interfaz de entrada, interfaz
de salida, destino). **Cada fila poblada es una arista de la frontera**, y cada arista se
convierte en un requisito de integración con dirección declarada. Lo que no aparece como
arista queda fuera de alcance.

**Este canvas define el alcance.** La lista negativa es tan importante como los
requisitos: evita que `/speckit.plan` invente integraciones.

Leer `references/reglas-reescritura.md` y `references/com-schema.md` antes de emitir salida.

## Contrato

```yaml
name: 7cs-system-context
when_to_use: >
  El COM tiene canvas == "system_context".
inputs:
  com: CanvasObjectModel        # única fuente de verdad; prohibido volver al PDF
  delivery_id: string
outputs:
  fragment: markdown            # §Alcance, §Integraciones, FR de frontera, §Fuera de alcance
  traces: [ {sticky_id, section, target_id} ]
  clarifications: [ string ]
procedure:
  1. Verificar la retícula 4×4 (16 celdas). Celdas ausentes → clarification.
  2. Para cada celda aplicar SU regla de mapeo (tabla fija).
  3. Reconstruir aristas: origen → interfaz entrada → [sistema] → interfaz salida → destino.
  4. Normalizar cada post-it a una frase verificable (R1–R7); emitir traza por post-it.
  5. Derivar la sección "Fuera de alcance (por complemento)".
guardrails:
  - Prohibido inventar frecuencias, esquemas o contrapartes no declaradas.
  - Prohibido escribir nombres de producto en el fragmento (van a plan.md).
  - Texto literal del post-it siempre citado entre comillas.
acceptance:
  - traces.length == total_stickies
  - toda integración declarada tiene dirección (lectura/escritura) explícita
  - existe la sección "Fuera de alcance (por complemento)"
```

## Tabla de mapeo (una fila por celda; destino único)

| Columna / fila | Qué produce el skill |
|---|---|
| Source users → Target users | Actor que inicia y actor que recibe en cada escenario de usuario |
| User data input interfaces | **FR de entrada por interfaz humana** (galerías, comentarios, redacción, cargas manuales) |
| User data output interfaces | FR de salida visible (interfaces web, blog) |
| Source systems | §Integraciones: un INT-n por sistema externo |
| System data input interfaces | **Contrato por integración**: API de lectura, consulta asíncrona, callback |
| System data output interfaces | Salidas hacia sistemas (redirecciones, entrega a servidores) |
| Target systems | Consumidores del contenido (pantallas, navegadores) |
| Repositories (4 celdas) | Requisitos de persistencia observables (protocolos de subida, servidor de archivos) |
| Devices (4 celdas) | Canales soportados y NFR de responsividad |

## Reglas específicas de este skill

- **Regla de completitud de arista (R-A).** Si una fila tiene origen sin interfaz de
  entrada, o interfaz sin destino, emitir duda: `"integración declarada sin contrato"`.
  Las filas incompletas **se reportan, no se completan**.
- **Un post-it puede producir dos escenarios** (feliz y de error) siempre que describa
  una entrada de datos. El canvas rara vez declara el error: esa asimetría queda como duda.
- **Dudas, no invenciones.** Esquemas de archivos (columnas de un CSV) y frecuencias de
  refresco que no estén en el canvas producen `[NEEDS CLARIFICATION: ...]`. Un agente sin
  guardrails escribiría "cada 5 minutos" y el equipo lo descubriría en producción.
- **El alcance se define por complemento.** Cerrar el fragmento con
  `## Fuera de alcance (por complemento)`: todo intercambio que no aparezca como arista
  queda fuera (p.ej. escritura hacia sistemas cuyas integraciones declaradas son de
  lectura; software instalado en dispositivos si la celda está vacía).
- **Nombres de producto, fuera** (regla R-T del pipeline): en la especificación se escribe
  la capacidad ("sistema institucional de identidad"); el nombre concreto vive en `plan.md`.

## Formato de salida

```markdown
## Integraciones (frontera del sistema)
INT-1 {sistema} — {dirección y naturaleza}.
...

## Requisitos funcionales (de frontera)
FR-001 El sistema DEBE {verbo observable} {objeto} {condición}.
  ← SCC/{celda} "{texto literal}" [+ causa: ACC/R-n si aplica]
  Escenario: Dado ..., cuando ..., entonces ...
  [Escenario de error si el post-it describe entrada de datos]
  [NEEDS CLARIFICATION: ...]

## Fuera de alcance (por complemento)
{lista negativa derivada de la retícula}
```

Cerrar con el balance: n post-it, n integraciones, n FR de frontera, n dudas, n celdas
vacías reportadas.
