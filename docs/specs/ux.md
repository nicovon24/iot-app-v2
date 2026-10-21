# Recorridos y aceptación de la primera etapa

Alcance: refinamiento del prototipo de portfolio. Identidad de referencia: [DESIGN.md](../../DESIGN.md). Los criterios siguientes son propuestas de aceptación para implementación; no certifican cumplimiento actual.

## Recorrido prioritario

1. Abrir Vista global y reconocer el carácter simulado.
2. Identificar una condición que requiere atención.
3. Seleccionar Porta o Argentina y abrir Córdoba.
4. Entrar en Inaudi, Máquina 01 y Sensor 1.
5. Interpretar lectura, unidad, umbral, estado y tiempo.
6. Abrir la alarma correspondiente, investigarla y reconocerla.
7. Volver a la vista anterior conservando el contexto.

Ruta directa de investigación: Alarmas → dispositivo → contexto del activo/ubicación.

## Entradas y contexto

Cliente y país son filtros combinables. La selección de una solución conserva ambos. La búsqueda global puede cambiar el alcance para mostrar la entidad elegida y debe hacer visible el nuevo contexto.

La diferencia entre alcance y jerarquía debe ser comprensible: país aparece como filtro; cliente, ubicación, área, activo y dispositivo describen pertenencia. La ubicación y su única área hoy comparten renderer; el modelo multiarea requiere evolución posterior.

## Requisitos

| ID | Aceptación observable |
| --- | --- |
| UX-001 | La pantalla inicial identifica IoTArg como demo e informa dónde hay condiciones activas, con acceso a ubicación o alarma. |
| UX-002 | Desde Vista global se completa el recorrido Porta → Córdoba → Inaudi → Máquina 01 → Sensor 1; cada detalle permite reconocer su pertenencia. |
| UX-003 | Cliente, país y solución activos son visibles y removibles. Una combinación sin datos muestra explicación y acción para recuperar resultados. |
| UX-004 | Búsqueda abre clientes, ubicaciones, activos y dispositivos en contexto; Atrás/Adelante restaura la vista y los filtros asociados. |
| UX-005 | Sensor muestra lectura válida o ausencia de señal, unidad, instante/último reporte, ventana de gráfica, umbral y estado; no confunde mínimo/máximo de escenario con ventana visible. |
| UX-006 | Reconocer una alarma cambia su reconocimiento y conserva la condición activa mientras la simulación la mantenga. La interacción produce feedback accesible. |
| UX-007 | El recorrido prioritario se completa por teclado mediante controles HTML y listados, aunque el canvas no permita seleccionar países por teclado. El foco es visible y no queda oculto por paneles. |
| UX-008 | Búsqueda coloca el foco al abrir, lo contiene en el diálogo, cierra con Escape y lo devuelve al disparador. El menú móvil dispone de apertura/cierre accesible. |
| UX-009 | A 390×844 y 1440×900, en ambos temas, los controles del recorrido son utilizables sin solapamientos ni scroll horizontal de página. Tablas pueden usar scroll localizado y anunciado. |
| UX-010 | Con WebGL no disponible se puede localizar una instalación y abrir su sensor mediante SVG/listado; no se bloquea la demo. |
| UX-011 | Severidad y conectividad se expresan también en texto; revisar contraste con objetivo de 4,5:1 para texto normal y 3:1 para texto grande y elementos esenciales. Objetivo de área táctil: 44×44 px para controles principales. |
| UX-012 | Movimiento reducido evita transiciones prescindibles. El instante simulado conserva enlaces directos y etiquetas temporales sin requerir la franja de reproducción, retirada por OPA-006. |
| UX-013 | Todas las secciones vigentes tienen una entrada comprensible; Metodología y Administración conservan acceso visible. Escenarios se retiró con la instantánea fija de Spec 02. |
| UX-014 | Las siete soluciones explican su cobertura simulada y muestran vacío cuando no hay datos pertinentes; etiquetas y nombres siguen una política de idioma consistente. |
| UX-015 | Un único botón del sidebar alterna entre Solo íconos y Completo en todas las vistas de escritorio. Solo íconos conserva la navegación y oculta los nombres; Completo muestra íconos y texto. El mapa inicia en Solo íconos; las demás vistas inician en Completo cuando hay ancho suficiente y en Solo íconos entre 761 y 980 px. La elección se conserva al navegar. En móvil, el menú se abre desde la cabecera y se cierra desde el sidebar. |

Los objetivos de accesibilidad anteriores son criterios internos de aceptación; esta entrega no certifica cumplimiento de una norma.

## Estados a revisar

Normal, advertencia, crítico, sin señal, sin datos, alarma reconocida, búsqueda sin coincidencias, almacenamiento local no disponible, clipboard no disponible, URL inválida y fallback del mapa.

En el HTML no se agregan estados de autenticación o red ficticios. Loading, errores de proveedor y permisos se especificarán al implementar una aplicación conectada.

## Verificación por recorrido

| Caso | Preparación | Resultado esperado |
| --- | --- | --- |
| V-01 | Sobretemperatura, minuto 28, Porta/Argentina | Abrir `p1s1`, interpretar condición crítica y reconocer alarma sin resolverla |
| V-02 | Porta + Chile | Vacío útil; quitar país recupera Córdoba |
| V-03 | Abrir enlaces heredados con `scenario=offline&time=11`, `12` y `28` | Se normalizan a la instantánea simulada fija; el dispositivo sin señal conserva su última lectura válida de las 10:11 y no recibe una muestra nueva |
| V-04 | Abrir enlace de sensor y navegar Atrás/Adelante | Contexto restaurado; entrada inválida se normaliza según DATA-006 |
| V-05 | Solo teclado, escritorio y menú móvil | Completar selección, búsqueda, sensor y alarma con foco gestionado |
| V-06 | Forzar falta de WebGL | Recorrido por SVG/listado completo |
| V-07 | Claro/oscuro y movimiento reducido | Información de estado legible y navegación usable |

Guardar resultados y capturas de la validación cuando se implemente; no marcar pruebas como realizadas al redactar esta tabla.
