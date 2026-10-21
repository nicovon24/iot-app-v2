# Spec 02 — Entidades operativas y Administración

Fecha: 2026-10-20. **Revisión 2: plan para revisión del usuario antes de implementar.** Sustituye la Administración como lista de pendientes y la propuesta de cinco grillas. El estado de cada corte se registra solo en [tasks.md](../tasks.md).

## Objetivo y ruta SDD

La demo de portfolio debe permitir entender, de un vistazo, qué clientes, ubicaciones, activos y dispositivos requieren atención, y pasar de cada entidad a sus descendientes en un clic. Inventario agrupa las cuatro tablas operativas. Administración ofrece dos tablas coordinadas: Estructura jerárquica y Contenido con activos/dispositivos. Ambas permiten administrar sus entidades y relaciones desde formularios laterales. La primera implementación trabaja con datos locales de demo; ThingsBoard es una etapa posterior.

**Ruta: SDD delegado para la implementación.** Hay un contrato compartido de alcance/estado, varias pantallas y una futura superficie de escritura. El coordinador fija este contrato y `tasks.md`; un único implementador modifica el HTML por corte y una revisión independiente comprueba los criterios antes de cerrar. Esta entrega modifica documentación, no certifica comportamiento en navegador.

Fuente editable: [IoTArg.html](../../../designs/IoTArg.html). La maqueta hoy muestra Clientes en tarjetas; Ubicaciones, Activos y Dispositivos ya tienen tablas de lectura con navegación al detalle. Las cuatro secciones carecen de búsqueda, orden y filtros locales. Las entidades y lecturas del prototipo son simuladas.

## Cortes de entrega y prioridad

| Corte | Prioridad | Resultado |
| --- | --- | --- |
| Base — Relaciones coherentes | Prerrequisito | Áreas con identidad, niveles por cliente, lectores compartidos, estados vacíos y persistencia de sesión. |
| A — Inventario | P0 | Clientes pasa a tabla; cuatro pestañas comparten estados, filtros, navegación contextual y accesos a descendientes. |
| B — Administración | P1 | Tabla árbol Estructura a la izquierda y tabla Contenido a la derecha; selección, búsqueda, activos expandibles y dispositivos sin asignar. |
| C — Acciones de demo | P1 | Agregar, editar, eliminar, asignar, mover y desvincular desde las tablas, con formularios laterales, confirmaciones y actualización de las demás vistas. |
| D — Aplicación conectada | Futuro | Adaptar los formularios y permisos a las entidades y API reales de `iot_app`/ThingsBoard según [integración](tbd-thingsboard-integration.md). |

La entrega propuesta incluye Base + A + B + C y el retiro del timeline. El usuario aprobó esta revisión y autorizó iniciar la implementación. Los campos y acciones adicionales de la demo no se presentan como API ya disponible en `iot_app`.

## Navegación y modelo de demo

- Sidebar: Vista global, **Inventario** y **Administración**, conservando las demás secciones existentes. Inventario contiene Clientes, Ubicaciones, Activos y Dispositivos como pestañas; se conservan los valores de `view` y enlaces de detalle actuales. El riel de íconos, el botón de expansión y el menú móvil siguen disponibles.
- Normalizar nodos con ID estable, cliente, padre y nivel; la secuencia de niveles se configura al crear el cliente y queda inmutable después. La configuración común es Ubicación → Área → Activo → Dispositivo. La secuencia válida es: Ubicación opcional al inicio, cero o más niveles de agrupación/Área, exactamente un Activo terminal y exactamente un Dispositivo final. Etiquetas obligatorias y roles explícitos permiten renombrar niveles sin alterar su comportamiento. Si falta Ubicación, el cliente sigue accesible en Inventario/Administración y no recibe geografía ficticia.
- Ubicación, Área y Activo se interpretan como niveles de Asset para la migración futura. La demo tendrá IDs propios para áreas y varios nodos por nivel. Preservar los IDs actuales de clientes, ubicaciones, activos y dispositivos. Un adaptador conservará los campos heredados que usa el mapa mientras se reemplazan lectores directos; ubicación y área de un dispositivo se derivan de sus ancestros y no se editan como relaciones independientes.
- Los enlaces antiguos `view=area&id=<ubicación>` resuelven al área de compatibilidad creada para esa ubicación; si hay varias áreas, abren su listado sin elegir una arbitrariamente. Nuevos enlaces de área usan ID de área estable.
- Resolver datos desde un único estado de demo compartido por Inventario, Administración, mapas, alarmas y detalles. Guardar cambios válidos en `sessionStorage` con versión de esquema y restaurar tras recargar la pestaña. Estado ausente/incompatible/corrupto vuelve a la fixture inicial con aviso; si el almacenamiento falla, continuar en memoria e informar que no se conservará al recargar. «Restablecer demo» requiere confirmación y restaura catálogo y relaciones, conservando tema y preferencias visuales.
- Clientes/activos vacíos y dispositivos sin asignar permanecen consultables. Sin país o solución seleccionados, el cliente cuenta también sus dispositivos sin activo. Con filtros geográficos/de solución, solo entran entidades cuya pertenencia se pueda resolver. Un sitio sin coordenadas sigue en listas y Pendientes de configuración, y no recibe un marcador ficticio. No extender cartografía para este corte.
- Mantener las lecturas deterministas de los dispositivos originales. Los dispositivos nuevos no reciben series fabricadas: muestran Sin datos hasta contar con muestras de demo explícitas. Cambiar metadatos no altera la lectura; cambiar la clave o unidad de medición invalida la serie incompatible y muestra Sin datos. Los detalles deben tolerar cero dispositivos y reemplazar los conteos fijos de equipos/sensores.
- Una mutación válida actualiza contadores, pendientes, marcadores y alarmas desde el mismo estado, conservando la cámara del mapa. Al borrar la entidad seleccionada se vuelve a su padre válido con aviso; enlaces/historial/dashboard guardado que apunten a IDs borrados muestran recuperación explícita. Limpiar referencias locales huérfanas. Renderizar nombres/etiquetas de formularios como texto o escaparlos al construir HTML; no interpolar entradas editables sin tratamiento.

## Tablas operativas

| Sección | Columnas iniciales | Acción de fila y accesos rápidos |
| --- | --- | --- |
| Clientes | Cliente, sector de demo, países, estado, ubicaciones, activos, dispositivos | Nombre abre el contexto del cliente. Botones «Ubicaciones · N», «Activos · N» y «Dispositivos · N» abren la tabla correspondiente limitada a ese cliente. |
| Ubicaciones | Ubicación, cliente, área, país, estado, activos, dispositivos | Nombre abre detalle. Botones de Activos y Dispositivos abren solo descendientes de la ubicación. |
| Activos | Activo, cliente, ubicación/área, estado, dispositivos | Nombre abre detalle. Botón Dispositivos abre solo dispositivos del activo. |
| Dispositivos | Dispositivo, activo/ubicación, última lectura válida, unidad, hora del dato, estado | Nombre o «Ver detalle» abre la ficha del dispositivo. |

La cantidad de cada botón cuenta entidades descendientes **únicas** dentro del alcance activo, no claves de telemetría. Cada botón usa etiqueta y número, un punto/borde semántico discreto y un resumen accesible de las **entidades destino** por Normal/Atención/Crítico/Sin señal/Sin datos. Para Ubicaciones y Activos se usa el estado agregado de cada entidad; para Dispositivos, su estado propio. El color del botón resume los estados de esas entidades con la misma prioridad semántica; nunca es la única señal. **Cero entidades** muestra «0», deshabilita el acceso y explica «Sin entidades disponibles». Una entidad existente sin dispositivos sí cuenta y aparece como «Sin datos».

Las cuatro tablas ofrecen búsqueda local por nombre y contexto, filtro por estado agregado de fila y orden por nombre/estado; cantidades se ordenan donde existan. El orden inicial es nombre ascendente. En móvil, conservar nombre, estado y accesos en una tabla con desplazamiento horizontal o celdas apiladas legibles, sin ocultar acciones. Encabezados anuncian orden; filtros y botones admiten teclado y foco visible.

### Alcance, estado y navegación

- Partir del alcance global existente de cliente, país y solución. Los accesos añaden filtros de ubicación y activo **separados** del ID de detalle y del foco geográfico del mapa. El país sigue siendo filtro, no padre del cliente.
- Mostrar chips removibles para el alcance operativo. Quitar un padre elimina sus filtros descendientes. Cambiar de cliente limpia ubicación y activo incompatibles. Un filtro válido sin coincidencias presenta estado vacío y acción para limpiar; nunca expone entidades fuera del alcance.
- Los accesos a descendientes llevan a la vista solicitada, conservan filtros globales compatibles y limpian búsqueda/estado/orden locales de la tabla de origen. Cambiar de sección desde el sidebar también limpia los filtros locales y los filtros de ubicación/activo; Atrás restaura el estado anterior.
- Persistir alcance operativo (`scopeLocation`, `scopeArea`, `scopeAsset`) y filtros locales (`q`, `status`, `sort`, `dir`) en el hash, separados de `id`, `geo`, `extent` y `fit`. Administración usa `view=admin`, `node` para selección y `content=all|assets|devices|unassigned`. Aceptar solo valores conocidos; un ID inexistente o fuera del alcance muestra un vacío explícito. Recarga y Atrás/Adelante restauran la selección válida.
- Un mismo conjunto de dispositivos y minuto produce el mismo estado en tabla, detalle, mapa y contador. Para clientes, ubicaciones y activos: **Crítico > Atención > Sin señal > Normal**. Sin dispositivos aplicables = **Sin datos**, visualmente distinto de Normal. El filtro «Sin señal» selecciona filas cuyo **resumen agregado** es Sin señal; el desglose del botón informa además problemas de menor prioridad ocultos por ese resumen.
- El dispositivo Sin señal conserva su última lectura válida y el timestamp de origen con indicación de antigüedad; no se crea una lectura del minuto actual. Esta regla también rige la tabla.

### Simulación temporal

Quitar la franja inferior «Reproducir el escenario» y su control de reproducción. No agregar selector de días ni timewindow en estos cortes. Conservar el minuto simulado (`time` en el hash, entero 0–60), escenarios, enlaces directos y ventana 60/15 minutos de gráficos; el instante de datos sigue visible en contexto. Al activar un escenario se usa su minuto inicial actual (0 en Normal, 28 en los demás); «Reiniciar a las 10:00» conserva su acción. Para verificar minutos 11/12/28 se usan enlaces directos con `scenario=offline&time=...`, sin exigir un control temporal nuevo. Actualizar el texto de Escenarios que remite a la barra inferior y los criterios antiguos de reproducir/pausar.

## Administración

### Corte B: dos tablas coordinadas

En escritorio, Estructura ocupa aproximadamente un tercio y Contenido el resto. A menos de 1100 px se apilan con Estructura plegable; en móvil, el botón «Estructura» abre un panel con búsqueda y árbol, y la tabla de contenido usa el ancho disponible. Encabezados y acciones deben quedar legibles; no reducir texto para hacer caber ambas tablas.

**Estructura:** tabla árbol con nombre/nivel y acciones, clientes y niveles intermedios. Expandir y seleccionar son acciones diferentes. Seleccionar cliente/ubicación/área filtra el contenido a ese subárbol; cambiar padre limpia selección inválida y conserva las ramas abiertas que sigan existiendo. La búsqueda muestra coincidencias y sus ancestros. Agregar cliente es acción de cabecera; cada fila permite agregar el siguiente nivel configurado, editar y eliminar. Cuando el próximo nivel es Activo, el alta crea el activo en Contenido.

Administración aplica el cliente del selector global al árbol, pero muestra toda su estructura: los filtros operativos de país/solución se conservan para volver a Inventario y aparecen inactivos en Administración con la explicación «Se aplican en Inventario». Seleccionar una fila no cambia ese filtro global; cambiar el filtro de cliente limpia un nodo incompatible. Crear cliente lo selecciona y fija el selector global al nuevo cliente para que el resultado quede visible.

**Contenido:** breadcrumb del nodo seleccionado; filtros Todos, Activos, Dispositivos y Sin asignar. Todos muestra activos terminales del subárbol, expandibles con sus dispositivos, y un grupo separado de dispositivos sin asignar solo al seleccionar cliente. Activos muestra filas de equipos; Dispositivos presenta lista plana única con columna «Activo asignado» y ubicación/área. Sin asignar se habilita en contexto cliente, ya que un dispositivo sin activo no pertenece a un área por inferencia. Si se selecciona una ubicación con varias áreas, cada fila incluye su ruta para distinguirla.

Columnas: nombre, tipo, contexto/activo asignado, estado, cantidad de dispositivos cuando corresponda y **Acciones**. La selección usa lavanda; salud usa indicador y texto propios. «Asignar dispositivo» y «Editar» son visibles por fila de activo; dispositivos muestran «Asignar» si no tienen activo o «Mover» si ya están vinculados, más «Editar». Agregar/Eliminar en Estructura y Desvincular/Eliminar en Contenido son botones de ícono con nombres accesibles, tooltip y área táctil suficiente; las acciones no dependen de hover y pueden envolver a otra línea en móvil.

La cabecera de Contenido siempre muestra **+ Activo**, **+ Dispositivo** y **Asignar dispositivo**. Requieren un cliente seleccionado en Estructura y explican esa condición si falta. «+ Dispositivo» funciona incluso con cliente vacío o filtro Sin asignar: abre alta con ese cliente, activo opcional y Sin datos inicial. «+ Activo» preselecciona un padre compatible si el nodo actual lo es; en otro caso permite elegirlo entre los padres válidos del cliente. Si aún no existe un padre requerido, explica qué nivel crear primero y ofrece enfocarlo en Estructura. «Asignar dispositivo» permite elegir activo del contexto antes de elegir dispositivo; desde una fila de activo lo preselecciona. Crear un dispositivo con activo opcional no crea automáticamente una ubicación o máquina.

### Corte C: formularios y acciones desde ambas tablas

El panel lateral muestra entidad y ruta completa, secciones General y Relación, y campos de configuración solo cuando apliquen. Guardar valida antes de modificar el estado compartido; Cancelar no modifica datos. Una edición con cambios sin guardar requiere confirmar su descarte al cerrar o cambiar selección. Escape, ciclo de foco y devolución del foco al botón de origen funcionan. Borrar requiere diálogo con nombre y consecuencias; nunca elimina en cascada.

| Entidad | Campos y operaciones en la demo |
| --- | --- |
| Cliente | Nombre obligatorio, sector opcional de demo y niveles ordenados/nombrados durante el alta. Editar nombre/sector; niveles inmutables tras crear. Alta de clientes raíz en este corte; jerarquía entre Customers queda para integración. Borrar solo sin nodos ni dispositivos del cliente. |
| Ubicación | Nombre, etiqueta, país, coordenadas opcionales y soluciones del catálogo existente; nivel y cliente desde contexto. Coordenadas deben venir en par y ser válidas. No inferir provincia por nombre: si se selecciona, validar pertenencia al país. Alta/edición/borrado sin dependencias. |
| Área/intermedio | Nombre, etiqueta y padre del nivel anterior en el mismo cliente. Agregar, editar, mover dentro de niveles compatibles y borrar solo sin descendientes. |
| Activo terminal | Nombre, etiqueta, tipo descriptivo y padre compatible. Agregar, editar, mover, asignar dispositivo y borrar solo sin dispositivos/hijos. Mover recalcula ubicación/área de todos los dispositivos vinculados. |
| Dispositivo | Nombre, etiqueta, tipo descriptivo, cliente y activo opcional; clave/unidad de medición y umbrales opcionales (advertencia menor que crítico cuando ambos existan). Agregar/editar/eliminar localmente, asignar/mover/desvincular. Tipo descriptivo no cambia la clave de telemetría. Cliente se elige al alta y queda fijo en esta etapa. |

**Relaciones:** en la demo un dispositivo pertenece a un cliente y tiene cero o un activo principal. Asignar desde la fila de activo abre selector de dispositivos de ese cliente; asignar desde Device permite elegir activo. Un dispositivo ya vinculado requiere «Mover» con origen/destino explícitos. La operación local valida primero y reemplaza la relación en un único cambio de estado; cancelar/fallar conserva la relación original. No permitir ciclos, duplicados, saltos de nivel o movimientos entre clientes. Desvincular mantiene el dispositivo bajo su cliente como Sin asignar. Eliminar dispositivo borra solo sus datos locales y vínculos de demo, con confirmación distinta de Desvincular.

**Pendientes de configuración:** subvista de Administración con dispositivos sin asignar, ubicaciones sin coordenadas, activos sin dispositivos y dispositivos sin clave/unidad de medición. Cada fila abre el nodo o formulario correspondiente; corregir el dato actualiza los pendientes. Este panel sustituye la antigua lista genérica de tareas futuras. Usuarios/permisos y gestión de conexiones quedan para Configuración en la etapa conectada.

**Diferencia con la referencia:** `iot_app` ya ofrece relaciones Asset → Contains → Device, edición de etiqueta y asignar/desvincular; no se confirmó unicidad de padre en backend ni alta/borrado de Device en esa UI. El CRUD amplio de esta maqueta es nuevo alcance de demo. Antes de D se deben especificar endpoints, permisos, atomicidad de mover y reglas de propiedad para esas operaciones. Sector y roles semánticos de los niveles también necesitan mapeo explícito. Reutilizar entidades ThingsBoard, sin tablas duplicadas; «reclamar» un Device desde otro alcance no se simula como autorización real.

## Aceptación observable

| ID | Criterio |
| --- | --- |
| OPA-001 | Clientes es una tabla en escritorio y móvil; cada fila muestra estado y tres botones con cantidad y destino inequívoco. |
| OPA-002 | Cliente → Ubicaciones/Activos/Dispositivos, Ubicación → Activos/Dispositivos y Activo → Dispositivos abren exactamente los descendientes contados, sin perder el contexto. |
| OPA-003 | Búsqueda, filtro y orden funcionan en las cuatro tablas; cambio de sección limpia filtros locales, y Atrás/Adelante o recarga restauran el enlace válido. |
| OPA-004 | Estados mixtos, sin señal y sin datos aplican una única regla de agregación. Color, texto y desglose coinciden; una lectura offline conserva el último timestamp válido. |
| OPA-005 | Controles y tablas son utilizables con teclado y a 390 px, con foco visible, nombres accesibles y sin ocultar accesos a descendientes. |
| OPA-006 | La franja inferior de reproducción no aparece ni deja errores; escenarios, minuto compartible y rango de gráficos siguen siendo coherentes. |
| OPA-007 | Administración se alcanza desde sidebar y muestra Estructura/Contenido coordinadas, activos expandibles, dispositivos y contexto correcto; adaptación móvil conserva acciones. |
| OPA-008 | Altas/ediciones válidas actualizan ambas tablas, Inventario y agregados; errores se anuncian, Cancelar no modifica datos y borrar exige confirmación. |
| OPA-009 | Formularios respetan campos, niveles, dependencias y límites definidos; alta/borrado de Device se identifican como operaciones de demo. |
| OPA-010 | La preparación del corte D identifica qué acciones necesitan permisos reales y mantiene los datos simulados separados de ThingsBoard. |
| OPA-011 | Inventario agrupa las cuatro pestañas sin romper enlaces anteriores, búsqueda global, sidebar compacto ni menú móvil. |
| OPA-012 | Dos áreas en una ubicación y clientes con distinta cantidad/nombre de niveles producen estructura y pertenencias correctas; IDs y lectores heredados se mantienen coherentes. |
| OPA-013 | Asignar funciona desde Asset y Device; mover reemplaza la relación sin duplicar conteos, cancelar conserva origen y desvincular deja Device accesible en Sin asignar. No hay movimientos entre clientes. |
| OPA-014 | Recargar conserva cambios válidos de sesión; almacenamiento inválido tiene recuperación explícita; restablecer demo restaura catálogo/relaciones sin alterar tema. Un enlace a entidad borrada ofrece recuperación. |
| OPA-015 | Pendientes de configuración identifica las cuatro categorías y sus acciones permiten corregirlas desde Administración. |
| OPA-016 | Entidades vacías y nuevas sin lectura/coordenadas siguen consultables sin errores ni datos inventados. La última muestra de `p1s2` desconectado sigue siendo minuto 11. |

## Verificación prevista tras implementar

1. Recorrer cliente → ubicación → activo → dispositivos desde cada botón, comprobar conteos, búsqueda/filtros y retorno por historial. Cliente sin ubicación y activo sin dispositivos deben seguir visibles con estado apropiado.
2. Crear localmente un segundo área y un cliente con niveles distintos; editar nombres, mover un activo entre áreas del mismo cliente y confirmar que Inventario, breadcrumb, marcadores y estado mantienen pertenencias correctas. Rechazar ciclos, padre incompatible y cliente distinto.
3. Crear Device sin lecturas, asignarlo desde Asset y desde Device, moverlo, cancelar un movimiento y desvincularlo. Verificar ausencia de doble conteo, Sin asignar y confirmaciones distintas de eliminar. Intentar borrar un padre con dependencias debe explicar el bloqueo.
4. Recargar y restablecer demo; revisar sesión corrupta/almacenamiento no disponible con recuperación visible. Abrir un enlace a una entidad borrada y un enlace de área anterior a la migración. Nombres con caracteres especiales deben mostrarse como texto.
5. Comprobar p1s2 en minutos 11/12/28 por enlace, retirada del timeline, cambio de escenario y rango 60/15. No presentar una muestra nueva mientras está sin señal.
6. Revisar a 1440, 900 y 390 px, claro/oscuro, teclado, panel lateral y confirmaciones. En `file://`, comprobar mapa existente, globo, encuadre de datos, fallback y cámara estable después de editar entidades. Registrar capturas y límites sin afirmar rendimiento de equipos físicos a partir de headless.

Estos casos son futuros; la revisión de documentos no equivale a ejecutarlos. No se añade infraestructura de tests ajena al HTML como requisito de esta entrega.

## Evidencia y próximo paso

- Inspección estática del prototipo: tarjetas de Clientes y tablas de Ubicaciones/Activos/Dispositivos; no equivale a QA de navegador.
- Referencia administrativa: `../iot_app/frontend/src/app/admin/page.tsx`, componentes de grillas/formularios y DTOs de `../iot_app/backend/src/`; esta especificación no afirma conexión activa.
- La aprobación documental inicial corresponde a la revisión 1. Esta revisión 2 modifica OPA-007/008/009 y añade OPA-011 a OPA-016. `/root/spec02_v2_plan_review` aprobó la revisión documental; el usuario confirmó el plan y la implementación comenzó en OPA-BASE. Evidencia en [review.md](../review.md).
- Investigación de revisión 2: `/root/inventory_admin_gap_v2` confirmó `location.area` textual, `device.loc` duplicado, `renderAsset()` dependiente de `ds[0]`, conteos fijos y ausencia de persistencia del catálogo. Se integraron como prerrequisitos del corte Base.
- Secuencia aprobada: Base → A → B → C → retiro de timeline → QA integrada. Un solo escritor Sol high modifica el HTML por corte; una revisión independiente comprueba cada corte. El registro real de modelos se mantiene en [orchestration.md](../orchestration.md).
