---
name: 7cs-canvas-ingest
description: Etapa A del pipeline 7Cs→Spec Kit. Convierte un PDF de entrega de canvas 7Cs (Business Context, Architectural Context, System Context, Structural, Functional, Deployment) en Canvas Object Models (COM) trazables, sin mapear ni interpretar nada. Usar SIEMPRE que el usuario entregue un PDF con canvas 7Cs, mencione "procesar los canvas", "leer la entrega", "generar el COM", "iniciar el pipeline 7Cs" o quiera producir especificaciones Spec Kit desde canvas — este skill se ejecuta antes que cualquier skill de mapeo 7cs-*.
---

# 7cs-canvas-ingest — Etapa A · Ingesta

**Entrada:** PDF de una entrega de canvas 7Cs.
**Salida:** un COM (JSON) por cada canvas + un índice de páginas fuera de alcance.
**Este skill NO mapea nada.** No produce requisitos, no clasifica post-it en destinos,
no interpreta. Su único trabajo es formalizar la imagen en datos.

Leer `references/com-schema.md` antes de emitir cualquier COM.

## Contrato

```yaml
name: 7cs-canvas-ingest
when_to_use: >
  El usuario entrega un PDF de canvas 7Cs y quiere iniciar el pipeline.
  Se ejecuta antes que cualquier skill de mapeo.
inputs:
  pdf: ruta del PDF de la entrega
  delivery_id: string          # p.ej. "E1"; si no se declara, derivarlo del nombre del archivo
outputs:
  coms: [CanvasObjectModel]    # un JSON por canvas, en com/{delivery_id}-{canvas}-p{n}.json
  page_index: json             # clasificación de TODAS las páginas, incluidas out_of_scope
  ingest_report: markdown      # conteos por canvas, secciones vacías, dudas de lectura
```

## Vocabulario cerrado de tipos de canvas

El título en la esquina superior izquierda de cada página se compara con exactamente
seis tipos:

| Título literal | `canvas` |
|---|---|
| Business Context Canvas | `business_context` |
| Architectural Context Canvas | `architectural_context` |
| System Context Canvas | `system_context` |
| Structural Canvas | `structural` |
| Functional Canvas | `functional` |
| Deployment Canvas | `deployment` |

Cualquier página cuyo título no coincida (nómina de equipo, diagrama C4, hoja vacía,
portada) se registra en `page_index` como `out_of_scope` con su motivo y **no se procesa**.
El Functional Canvas puede repetirse: hay una instancia por bundle. Emitir **un COM por
página**, nunca fusionar ni promediar instancias.

## Procedimiento

1. **Separar páginas.** Cada página del PDF contiene típicamente una sola imagen JPEG de
   gran formato sin capa de texto. Extraer cada página como imagen **sin recomprimir**
   (p.ej. `pdfimages -all` o PyMuPDF con extracción del stream original): la imagen es
   la evidencia citable. Guardar en `evidence/{delivery_id}-p{n}.jpg`.
2. **Clasificar el canvas.** Leer el título superior izquierdo de cada imagen (etapa de
   visión) y compararlo con el vocabulario cerrado. Registrar toda página en `page_index`.
3. **Leer la cabecera.** System, Organization, Canvas, Version, Date. Copiar literal;
   campos vacíos → `null`. La cabecera vacía es un dato: se reporta, no se completa.
4. **Segmentar secciones.** Las secciones son rectángulos blancos sobre fondo gris con
   rótulo propio. Detectarlas por contorno y etiquetarlas con el **rótulo leído, no por
   posición fija** (la posición varía entre entregas). Si un rótulo no coincide con el
   vocabulario de secciones del tipo de canvas (ver skills de mapeo), aplicar coincidencia
   aproximada y registrar la decisión en `notes` para confirmación humana.
5. **Leer post-it.** Cada rectángulo amarillo produce un registro `{id, text, bbox, parent}`.
   Texto literal, incluidos errores. El tamaño de fuente varía: **no** inferir importancia
   del tamaño. Numerar ids de forma estable (orden de lectura: izquierda→derecha,
   arriba→abajo dentro de cada sección) para garantizar idempotencia.
6. **Resolver agrupadores.** Un rectángulo con borde que contiene post-it y un rótulo
   suelto ("Público general") se traduce en jerarquía `parent`. Un rótulo huérfano
   (jerarquía dibujada solo por proximidad, sin rectángulo) se reporta en `notes`.
7. **Registrar secciones vacías.** Toda sección del vocabulario sin post-it entra en
   `empty_sections`. Agrupar dudas por causa (tres celdas vacías del mismo bloque = 1
   duda, no 3).
8. **Emitir el reporte de ingesta:** páginas procesadas y fuera de alcance, post-it
   contados por canvas, secciones vacías, y dudas de lectura visual (texto ilegible por
   tamaño 12–14 px → citar el bbox para que el auditor recorte y verifique).

## Guardrails

- Prohibido interpretar, resumir, corregir o traducir el texto de un post-it.
- Prohibido omitir páginas: toda página del PDF aparece en `page_index`.
- Prohibido asumir un solo Functional Canvas: iterar por instancia.
- Prohibido rellenar campos de cabecera vacíos.

## Aceptación

- Todo COM valida contra el esquema de `references/com-schema.md` sin secciones desconocidas.
- `page_index` cubre el 100% de las páginas del PDF.
- El recuento de post-it por canvas queda en el reporte para verificación manual
  (criterio del método: verificar a mano 2 canvas por entrega).
- Reejecutar la ingesta sobre el mismo PDF produce los mismos ids y el mismo COM
  carácter a carácter (idempotencia).
