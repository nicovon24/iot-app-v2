# Tareas

## Entrega documental

| ID | Requisitos | Dependencias | Responsable / rutas | Comprobación | Estado |
| --- | --- | --- | --- | --- | --- |
| DOC-01 | REQ-002, REQ-003, REQ-004 | Ninguna | Investigador maqueta; lectura de `IoTArg.html` y `README.md` | Inventario con funciones y límites observables; integración corrige hipótesis de Metodología | Completada |
| DOC-02 | REQ-006 | Ninguna | Investigador orquestación; lectura dirigida de configuración y harness fuente | Roles, modelos y diferencias con fuentes | Completada |
| DOC-03 | REQ-001 a REQ-007 | DOC-01, DOC-02 | Coordinador; `docs/specs/**`, `PRODUCT.md`, `DESIGN.md`, enlace desde `README.md` | Consistencia, cobertura y enlaces locales | Completada |
| DOC-04 | REQ-008 | DOC-03 | Reviewer independiente; solo lectura de entrega y fuentes | Hallazgos por requisito y severidad; aprobada tras ronda 1 | Completada |
| DOC-05 | REQ-001, REQ-005, REQ-008 | DOC-04 | Coordinador; documentos compartidos | R-01/R-02 resueltos, checker repetido sin errores, evidencia y siguiente paso registrados | Completada |

## Implementación de la maqueta

Ninguna tarea se considera realizada por la mera existencia de esta documentación. El archivo editable ya está en `designs/IoTArg.html`; el primer corte del visor se implementa y revisa por separado de los criterios completos de UX y datos.

| ID | Requisitos | Dependencias | Responsable / rutas asignadas | Comprobación esperada | Estado |
| --- | --- | --- | --- | --- | --- |
| IMP-01 | REQ-002, REQ-008 | DOC-05 | Coordinador; `.git/`, `.gitignore` | Inicializar versionado local, revisar exclusiones y registrar estado sin publicar | Completada: Git local inicializado, sin commit |
| IMP-02 | UX-002, UX-010 | IMP-01 | Coordinador; `IoTArg.html` → `designs/IoTArg.html`, enlaces en Markdown | Hash idéntico tras traslado; apertura y recursos integrados; enlaces válidos | Completada: SHA idéntico al traslado, HTML abierto en `file://`, 92 enlaces locales válidos |
| IMP-03 | UX-001 a UX-014 | DOC-05; revisión anticipada sobre raíz autorizada | Revisiones A/B; lectura del HTML y capturas en `designs/evidence/` | Hallazgos, escritorio/móvil y muestras de ambos temas; no equivale a validar todos los UX | Completada para diagnóstico inicial; matriz funcional pendiente en IMP-07 |
| IMP-04 | UX-001, UX-002, UX-003, UX-013, UX-014; VIS-001, VIS-005, VIS-006, VIS-011 | IMP-05 | Un implementador Sol high; `designs/IoTArg.html` | Composición compacta, mapa protagonista, panel/alarma contextual, gráfica, alcance, entradas e idioma | Pendiente |
| IMP-05 | UX-005, UX-006, DATA-001 a DATA-007; VIS-004, VIS-007 | IMP-02, IMP-03 | Mismo implementador Sol high; `designs/IoTArg.html` | Último reporte, estado por activo, URL, severidad, reconocimiento y persistencia | Pendiente |
| IMP-10 | VIS-012, VIS-015 | IMP-04 | Mismo implementador Sol high; cartografía versionada y `designs/IoTArg.html` | Fuente/licencia/atribución verificadas, límites provinciales simplificados, IDs, vínculo Córdoba y foco URL explícito | Pendiente |
| MAP-01 | VIS-016 | IMP-02 | Coordinador obtiene/verifica fuentes; implementador Sol high procesa `designs/map-data/**` | Países 1:50m y admin 1 mundial 1:10m con hashes, licencia y cobertura registrados; assets compactos en el proyecto | Completada: 242 países y 4.580 divisiones navegables; fuente, exclusiones y procesamiento documentados; sin commit |
| MAP-02 | VIS-016 | MAP-01 y geometría Georef de IMP-10 | Implementador Sol high; `designs/IoTArg.html`, `designs/map-data/**` | Mundo encuadrable, país seleccionable, divisiones disponibles, fallback para ausencia, sin datos IoT fuera de cuatro ubicaciones y apertura en `file://` | Completada para el primer corte: Mundo, AR, JP, `file://`, resize, móvil y SVG probados |
| MAP-03 | VIS-011 a VIS-016 | MAP-02 | Revisor Sol high en lectura; correcciones por implementador | Capturas y recorrido de escritorio/móvil, WebGL cenital y fallback SVG, teclado y navegación; resultados en `review.md` | Revisión estática aprobada tras corregir P1/P2; QA dinámica acotada registrada, matriz completa sigue en IMP-07 |
| SA-01 | SA-01 a SA-11 de Spec 01 | MAP-03 | Planificador Astra xhigh; implementador Sol high en `designs/IoTArg.html`; coordinador en docs y QA | AR/CL/PE/UY, mapa protagonista, cuatro marcadores pulsables, primer fotograma cenital sin salto, acercamiento suave, selector de cuatro países, movimiento reducido, deep links y SVG; ver `review.md` | Completada para este corte: nueva animación verificada y revisión independiente aprobada |
| SA-02 | SA-12 a SA-15 de Spec 01 | SA-01 | Implementador Sol high en `designs/IoTArg.html`; coordinador en docs y QA | Controles geográficos separados, encuadre calculado desde ubicaciones del alcance y tooltip contextual por capa y nivel; ratón, teclado, móvil y SVG | Completada para este corte: QA de escritorio/móvil y revisión independiente aprobada |
| SA-03 | SA-16 de Spec 01 | SA-02 | Implementador Sol high en `designs/IoTArg.html`; coordinador en docs y QA | Relieve 3D permanente con cámara cenital; sin control 2D/3D; Mundo/país/fit/deep link y SVG siguen operativos | Completada: QA WebGL/SVG y revisión independiente aprobada |
| SA-04 | SA-17 de Spec 01 | SA-03 | Implementador Sol high en `designs/IoTArg.html`; coordinador en docs y QA | Globo Ver mundo entre controles inferiores derechos, sin Mundo/Sudamérica junto al filtro; restablecer vuelve a Sudamérica; escritorio/móvil | Completada: QA móvil 390 px y escritorio; interacción/hash comprobados |
| MAP-04 | UX-015, VIS-017 | SA-04 | Implementación local; `designs/IoTArg.html`, `docs/specs/ux.md`, Spec 01 | Botón único Solo íconos / Completo dentro del sidebar; estado accesible y conservación entre vistas; menú móvil | Completada: alternancia 68 ↔ 215 px a 1440 y 900 px, Clientes conserva la elección y móvil 500×844 abre/cierra el menú; revisión posterior inicia completo en escritorio |
| IMP-09 | VIS-002, VIS-003, VIS-008, VIS-010, VIS-013, VIS-014 | IMP-10 | Mismo implementador Sol high; `designs/IoTArg.html` | Visor Three.js por niveles, relieve/leyenda semánticos, marcadores, capas, cámara, selección y fallback | Pendiente |
| IMP-06 | UX-007 a UX-012; VIS-006, VIS-009 | IMP-09 | Mismo implementador Sol high; `designs/IoTArg.html` | Teclado, foco modal, tamaños, contraste, responsive, movimiento reducido, fallback | Pendiente |
| IMP-07 | UX-001 a UX-015, DATA-001 a DATA-007; VIS-001 a VIS-017 | IMP-06 | Reviewer Sol high en lectura; correcciones del HTML por el mismo implementador Sol high, secuencialmente; coordinador registra evidencia | V-01 a V-07 y revisión visual final; devolver hallazgos al implementador y revisar otra vez lo afectado antes de aprobar | Pendiente |
| IMP-08 | REQ-001, REQ-007 | IMP-07 | Coordinador; `README.md`, `DESIGN.md`, `docs/specs/**` | README breve, rutas correctas, capturas reales, alcance implementado actualizado | Pendiente |
| APP-T01 | APP-001, APP-006 | IMP-08 | Coordinador; nueva especificación de MVP en `docs/specs/` | Confirmar alcance, stack concreto, rutas y criterios antes de scaffold | Pendiente / etapa 2 |
| APP-T02 | APP-001, APP-002, DATA-008 | APP-T01 | Implementador; rutas a asignar en APP-T01 | Build, tipos, dominio desacoplado y fixtures multinacional/multiarea | Pendiente / etapa 2 |
| APP-T03 | APP-003, APP-004 | APP-T02 | Implementador; rutas a asignar en APP-T01 | Paridad del recorrido y proveedor simulado bajo contrato | Pendiente / etapa 2 |
| APP-T04 | APP-005, APP-006 | APP-T03 y decisión explícita de integración | Roles separados según alcance; rutas por definir antes de delegar | Contratos, permisos, pruebas en entorno autorizado y revisión independiente | Diferida |
| APP-T05 | APP-007 | APP-T03 y definición de destino | Coordinador; configuración de despliegue por definir | URL desplegada y demo comprobada | Pendiente / etapa 2 |
| OPS-00 | REQ-006 | DOC-05 y alcance acordado en repositorio del harness | Coordinador del harness; schema/config/snapshot y tests a asignar allí | Soporte de aceptación en `docs/specs/`; invalidación de revisión comprobada; sin copias de requisitos | Pendiente / repositorio externo |
| OPS-01 | REQ-006 | IMP-01, OPS-00 y revisión de configuración de proyecto | Coordinador; `harness/project.json`, `.agents/`, `.gitignore`, instrucciones de proyecto | Preview, instalación Codex, validate/config/doctor y run real según harness | Pendiente |

APP-T01 debe asignar archivos concretos antes de delegar las tareas de etapa 2. Hoy esas filas son planificación, no encargos ejecutables. Las tareas que modifican el mismo HTML son secuenciales.

## Spec 02 — Entidades operativas y Administración

[Spec 02](subspecs/02-operational-tables-admin.md), revisión 3, reúne Inventario, Administración y Soluciones de demo. Base/A1/B/A2 están implementados. El usuario antepuso refinamiento visual de Administración y tres Soluciones a los formularios; C, QA de mutaciones e integración real quedan pendientes. Cada corte del HTML tiene un solo escritor y revisión independiente antes de marcarse completo.

| ID | Requisitos | Dependencia | Responsable / rutas asignadas | Comprobación esperada | Estado |
| --- | --- | --- | --- | --- | --- |
| OPA-DOC | OPA-001 a OPA-016 | Investigación de revisión 2 | Coordinador; Spec 02, índice, tareas y referencias transversales | Plan coherente y revisión independiente; presentación al usuario | Revisión documental 2 completada y aprobada por el usuario |
| OPA-BASE | OPA-004, OPA-012, OPA-014, OPA-016; DATA-001/003/004 | OPA-DOC y aprobación del usuario | Implementador Sol high; `designs/IoTArg.html` | Áreas con ID, niveles/lectores, relaciones únicas, vacíos, lectura offline y sessionStorage | Implementado; revisión estática independiente aprobada; comprobaciones dinámicas reservadas para OPA-QA |
| OPA-A1 | OPA-001 a OPA-005, OPA-011 | OPA-BASE | Mismo implementador Sol high; `designs/IoTArg.html` | Inventario con cuatro tablas/pestañas, accesos, filtros/hash y QA 1440/390 px | Implementado; revisión estática independiente aprobada; QA dinámica reservada para OPA-QA |
| OPA-B | OPA-007, OPA-012 | OPA-A1 | Mismo implementador Sol high; `designs/IoTArg.html` | Estructura + Contenido, selección, niveles, activos expandibles y devices | Implementado; revisión estática independiente aprobada; QA dinámica reservada para OPA-QA |
| OPA-A2 | OPA-006 | OPA-B | Mismo implementador Sol high; `designs/IoTArg.html` | Reproducción y Escenarios retirados; instantánea simulada fija, hash heredado normalizado y gráfico 60/15 consistente | Implementado; revisión estática aprobada tras actualizar el contrato; comprobación inicial en navegador, QA integrada pendiente |
| OPA-DOC3 | OPA-017 a OPA-026 | Decisión del usuario y plan Astra medium | Coordinador; Spec 02, tareas, revisión y orquestación | Contrato B2/S0–S3 antes de C, datos simulados honestos y aceptación verificable | Documentado; revisión independiente aprobada |
| OPA-B2 | OPA-017 a OPA-019 | OPA-A2, OPA-DOC3 | Implementador Sol high; `designs/IoTArg.html` | Paneles 50/50, árbol completo, barra/tooltip de estado y primera selección | Pendiente / siguiente |
| OPA-S0 | OPA-020, OPA-021 | OPA-B2 | Mismo implementador Sol high; `designs/IoTArg.html` | Soluciones segundo ítem, tres disponibles y cuatro En preparación; enlaces directos honestos | Pendiente |
| OPA-S1 | OPA-022, OPA-025 | OPA-S0 | Mismo implementador Sol high; `designs/IoTArg.html` | Airport Management con señales reales de la fixture de Lima/Terminal A | Pendiente |
| OPA-S2 | OPA-023, OPA-025 | OPA-S1 | Mismo implementador Sol high; `designs/IoTArg.html` | Predictive Maintenance con reglas, temperatura y vibración de Máquina 01/02 | Pendiente |
| OPA-S3 | OPA-024, OPA-025 | OPA-S2 | Mismo implementador Sol high; `designs/IoTArg.html` | Temperatura compara sensores, umbrales, unidades y hora propios | Pendiente |
| OPA-QA-READ | OPA-001 a OPA-007, OPA-011, OPA-012, OPA-017 a OPA-026 | OPA-S3 | Reviewer independiente Sol high; coordinador registra evidencia en `docs/specs/review.md` y `designs/evidence/spec02/` | QA integrada de lectura: navegación, estado, hash, teclado, claro/oscuro, 1440/900/390 y mapa | Pendiente |
| OPA-C | OPA-008, OPA-009, OPA-013 a OPA-016 | OPA-QA-READ | Mismo implementador Sol high; `designs/IoTArg.html` | Formularios, asignar/mover/desvincular, confirmaciones, dependencias, pendientes y sincronización con Inventario/mapa | Pendiente por decisión del usuario |
| OPA-QA | OPA-008, OPA-009, OPA-013 a OPA-016 | OPA-C | Reviewer independiente Sol high sin editar código; coordinador registra evidencia en `docs/specs/review.md` | QA dinámica de mutaciones: CRUD, asignar/mover/cancelar, recarga, teclado y mapa | Pendiente por decisión del usuario |
| OPA-D | OPA-010, TB-002, TB-003 | OPA-QA, TB-T01/T02; ampliación de contratos CRUD | Rutas de `iot_app` a asignar tras contrato y permisos | Acciones autorizadas por rol, relación principal, movimientos seguros, sin entidades duplicadas | Diferida / integración |

`OPA-BASE` concreta la semántica DATA-001/003/004 que necesita; su entrega se refleja después en `IMP-05` sin exigir que esa tarea entera esté terminada. `OPA-C` ampliará la demo con alta/borrado de Device y edición de campos aún no soportados por la referencia conectada. OPA-QA-READ puede cerrarse sin formularios; la revisión documental no cierra tareas de implementación.

## Propuesta de integración ThingsBoard

[TBD — Integración ThingsBoard](subspecs/tbd-thingsboard-integration.md) propone reutilizar `iot_app`. Las filas APP-T01 a APP-T05 conservan el plan previo como referencia; antes de ejecutarlas se deben reconciliar con los cortes TB-T01 a TB-T04 para evitar un segundo scaffold o implementación duplicada.

| ID | Requisitos | Dependencia | Responsable / alcance | Estado |
| --- | --- | --- | --- | --- |
| TB-DOC | Propuesta TB-001 a TB-012 | Investigación de `iot_app` | Coordinador; spec, índice y referencias técnicas | Completada: documento creado; integración pendiente |
| TB-T01 | TB-001 | TB-DOC | Inventario de `iot_app` y piloto autorizado; solo lectura; resolver instancia y datos | Pendiente |
| TB-T02 | TB-002 a TB-006, TB-009 | TB-T01 | Contrato y fixtures; asignar rutas backend/frontend antes de delegar | Pendiente |
| TB-T03 | TB-007 a TB-010 | TB-T02 | Implementación Sol high; normalización y vistas en `iot_app`, rutas por fijar | Pendiente |
| TB-T04 | TB-003, TB-010 a TB-012 | TB-T03 | Revisión independiente, prueba conectada y evidencia sanitizada | Pendiente |

## Evidencia de investigación

- DOC-01: entrega de `/root/inventory`; observaciones integradas en `baseline.md`.
- DOC-02: `/root/orchestration` inspecciona configuración local y luego el repositorio proporcionado por el usuario.
- SHA inicial del HTML registrado en `baseline.md`; Git se inicializó después de esa línea de base.
- Modelos solicitados y datos reportados se registran en `orchestration.md`; checks y revisión en `review.md`.

## Próximo paso

Revisión inicial, capturas de referencia y [Spec 01](subspecs/01-initial-design.md) disponibles. IMP-01/02 y MAP-01/02/03 se completaron para el primer corte cartográfico. Los cortes sudamericanos implementados cubren parte de IMP-04/09/10 sin cerrar esas tareas completas; su evidencia permanece en `review.md`. Secuencia vigente de Spec 02: OPA-BASE → OPA-A1 → OPA-B → OPA-A2 → OPA-B2 → OPA-S0 → OPA-S1 → OPA-S2 → OPA-S3 → OPA-QA-READ. Formularios OPA-C, QA de mutaciones e integración quedan pendientes. Un solo escritor Sol high modifica el HTML por corte; el coordinador mantiene documentos y commits separados.

Activar el harness requiere resolver OPS-00 y OPS-01; su clon temporal no equivale a instalación.
