# IoTArg: especificación del proyecto

Estado: entrega documental completada y revisión independiente aprobada. Modalidad: SDD / especificación. Fecha: 2026-10-20.

## Objetivo

Documentar IoTArg como demo de portfolio, usando el prototipo existente como evidencia y definiendo el trabajo pendiente con aceptación observable. La ubicación canónica es `docs/specs/`, elegida por el usuario en lugar de `docs/features/`.

## Alcance de esta entrega

Especificaciones de producto, interacción, datos y evolución técnica; documentación raíz `PRODUCT.md` y `DESIGN.md`; inventario verificable de la maqueta; tareas y orquestación contrastada con la configuración local y el repositorio `nicovon24/harness-nicovon24` indicado por el usuario.

La entrega especifica la evolución del HTML y su futura ubicación en `designs/IoTArg.html`. No implementa la aplicación Next.js, integra servicios, publica la demo ni cambia el comportamiento del prototipo.

## Aceptación de la documentación

| ID | Criterio observable |
| --- | --- |
| REQ-001 | Existe un índice en `docs/specs/README.md` con enlaces válidos a las especificaciones y documentación raíz. |
| REQ-002 | El inventario identifica capacidades observadas en código, límites y pendientes; no presenta inspección estática como prueba de navegador. |
| REQ-003 | Producto y UX documentan el objetivo de portfolio, la jerarquía, el alcance cliente/país/solución y el recorrido de una alarma hasta el sensor. |
| REQ-004 | La especificación de datos registra simulación, severidades, URL y persistencia; la arquitectura futura distingue decisiones propuestas de implementación existente. |
| REQ-005 | Las tareas incluyen ID, requisito relacionado, dependencias, rutas, comprobación y estado; separan la entrega documental de la implementación futura. |
| REQ-006 | La orquestación identifica el commit del harness indicado por el usuario, distingue soporte Claude/Codex, documenta su adaptación a `docs/specs/` y separa configuración propuesta de ejecución real, sin afirmar instalación ni modelos no reportados. |
| REQ-007 | `PRODUCT.md` y `DESIGN.md` contienen contexto durable consistente con la maqueta y decisiones confirmadas, sin promesas funcionales inventadas. |
| REQ-008 | La documentación recibe revisión independiente y registra evidencia, limitaciones y siguiente paso; el HTML conserva su contenido. |

## Contratos de trabajo

El coordinador es el único editor de documentación compartida. Los investigadores trabajan en lectura y entregan hallazgos con referencias. Hasta dos subagentes activos. El reviewer recibe contexto nuevo y no modifica archivos.

## Fuentes y estado inicial

- Usuario: demo de portfolio confirmada; prototipo HTML primero; Next.js después.
- Fuentes presentes: `README.md`, `IoTArg.html`.
- No se encontraron `AGENTS.md` en el proyecto ni en los ancestros inspeccionados.
- `git status --short --branch`: falla porque esta carpeta no es un repositorio Git. No se dispone de rama, commit o diff.
- Fuente de orquestación aportada por el usuario: `https://github.com/nicovon24/harness-nicovon24`, commit `da43b1f00426606088de2b8afff59671a9c6f639`, inspeccionado mediante clon temporal. No fue instalado en IoTArg.

## Evidencia y próximo paso

Registro detallado en `tasks.md` y `review.md`. Revisión independiente aprobada tras una ronda de correcciones documentales. Próximo paso: organizar y validar visualmente el HTML según IMP-01 a IMP-03; la integración del harness sigue OPS-00/OPS-01.
