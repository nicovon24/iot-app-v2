# Especificaciones de IoTArg

IoTArg es una demo de portfolio de operaciones conectadas. Esta carpeta es la ubicación canónica elegida para SDD; no hay una copia paralela en `docs/features/`.

## Lectura

| Documento | Responsabilidad |
| --- | --- |
| [PRODUCT.md](../../PRODUCT.md) | Objetivo, usuarios, capacidades y límites durables. |
| [DESIGN.md](../../DESIGN.md) | Sistema visual observado y criterios de refinamiento. |
| [Spec 01 — Diseño espacial, mapa y recorrido](subspecs/01-initial-design.md) | Rediseño visual, demo sudamericana, navegación cartográfica, cámara y criterios de aceptación. |
| [Spec 02 — Entidades operativas y Administración](subspecs/02-operational-tables-admin.md) | Inventario con cuatro pestañas; Administración con Estructura/Contenido, formularios y relaciones de demo. Revisión 2 pendiente de revisión del usuario antes de implementar. |
| [TBD — Integración ThingsBoard](subspecs/tbd-thingsboard-integration.md) | Propuesta para portar el diseño a `iot_app`, normalizar entidades/telemetría y verificar un piloto real. |
| [requirements.md](requirements.md) | Alcance y aceptación de esta entrega documental. |
| [baseline.md](baseline.md) | Qué existe en la maqueta y qué evidencia lo respalda. |
| [ux.md](ux.md) | Recorridos y aceptación de la primera etapa visual. |
| [data.md](data.md) | Entidades, alcance, simulación, URL y persistencia. |
| [design.md](design.md) | Contratos técnicos, arquitectura propuesta y decisiones pendientes. |
| [cartography.md](cartography.md) | Origen, licencia y tratamiento de países mundiales y divisiones administrativas. |
| [orchestration.md](orchestration.md) | Orquestación observada, adaptación y ejecución verificable. |
| [tasks.md](tasks.md) | Único registro de estado de tareas y dependencias. |
| [review.md](review.md) | Revisión independiente y comprobaciones. |

## Cómo interpretar el estado

- **Observado en código:** evidencia estática del HTML, sin equivaler a una prueba de funcionamiento en navegador.
- **Objetivo confirmado:** decisión expresada por el usuario.
- **Propuesto / pendiente:** contrato para trabajo futuro, todavía sin implementación o aprobación detallada.
- **Verificado:** comprobación ejecutada con resultado registrado.

Los IDs `REQ-*` aceptan esta documentación. `UX-*`, `DATA-*` y `APP-*` definen aceptación de cambios futuros; escribirlos no certifica que el prototipo los cumpla.

Las specs de producto viven en `subspecs/` y se enlazan desde este índice. Las specs aceptadas usan numeración estable (`01-`, `02-`) y títulos/IDs de aceptación coherentes. Los documentos transversales permanecen en `docs/specs/`; `tasks.md` conserva el único registro de estados.

`subspecs/tbd-thingsboard-integration.md` conserva el nombre solicitado y usa criterios `TB-*`. Es una propuesta de etapa conectada con decisiones abiertas, basada en la aplicación existente `iot_app`. Cuando el alcance se cierre, renombrarla a `03-thingsboard-integration.md` y retirar `TBD` del título; no cambiar los IDs `TB-*`.

## Secuencia de trabajo

1. Completar y revisar especificaciones.
2. Organizar el prototipo en `designs/IoTArg.html`, ajustar README y verificar apertura.
3. Validar visualmente la base; refinar el recorrido prioritario.
4. Verificar navegación, datos, accesibilidad y adaptación.
5. Resolver el piloto de [integración con `iot_app`](subspecs/tbd-thingsboard-integration.md) y verificar su backend/conector existentes antes de portar las vistas conectadas.

El prototipo editable está en [IoTArg.html](../../designs/IoTArg.html). La revisión visual inicial se hizo antes del traslado y el hash original consta en `baseline.md`.

La revisión visual inicial se adelantó sobre ese archivo por pedido del usuario. Hay capturas en `designs/evidence/`; el primer corte cartográfico mundial de Spec 01 está implementado y revisado. Los criterios de recorrido, datos, accesibilidad y aplicación futura mantienen su estado específico en [tasks.md](tasks.md).
