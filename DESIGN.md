# Sistema visual de IoTArg

Estado: sistema visual existente y **primer corte del mapa mundial implementado y revisado en navegador**. La [Spec 01 de diseño espacial, mapa y recorrido](docs/specs/subspecs/01-initial-design.md) reúne el foco sudamericano, la entrada de cámara y el resto del rediseño, que sigue por etapas.

Fuente visual implementada: [IoTArg.html](designs/IoTArg.html), bloque `<style>`. Contexto de producto: [PRODUCT.md](PRODUCT.md). Aceptación de mejoras: [UX](docs/specs/ux.md).

## Overview

Interfaz operativa con mapa como entrada geográfica, navegación lateral y paneles de detalle. La identidad actual usa grafito en tema oscuro, superficies claras en tema claro y lavanda para interacción.

El corte sudamericano conserva esa identidad y lleva el mapa a la superficie principal: riel de navegación compacto en la Vista global, mapa amplio desde el primer viewport y controles/condición superpuestos sin bloquear los sitios. La cobertura y las ubicaciones viven en un panel flotante plegable. Las demás vistas conservan la estructura de navegación completa; su validación de rediseño sigue por etapas.

## Mapa mundial del primer corte

- Inicio en Sudamérica para mostrar Córdoba, Santiago, Lima y Montevideo; el control **Mundo** encuadra todos los territorios. Seleccionar un país abre sus divisiones administrativas si hay geometría; Argentina usa Georef y los demás países disponibles usan Natural Earth.
- Cada territorio sin instalaciones aparece en grafito y se identifica como **Sin datos IoT**. Los colores de estado corresponden a dispositivos de demostración, no a un índice geográfico. Las mallas 3D mantienen el relieve correspondiente a la capa seleccionada y la cámara permanece perpendicular al mapa. No hay control para inclinar o aplanar el visor; si falla WebGL se muestra el mapa SVG plano.
- El foco territorial y el alcance de datos se muestran por separado. «Córdoba · provincia» explora cartografía; «Córdoba · ubicación» abre el sitio. El encuadre mundial no multiplica clientes ni crea datos fuera de los cuatro países de la demo.
- El selector País contiene siempre solo Vista general y los cuatro países con sensores: Argentina, Chile, Perú y Uruguay. El mapa ofrece acceso a todos los demás territorios; si se elige uno, su nombre aparece en el alcance y el selector permanece en Vista general. Un botón de globo entre los controles inferiores derechos abre Mundo; el control de restablecer de ese grupo vuelve a Sudamérica. Centrar en mis datos y Quitar filtros permanecen junto a País/Provincia. Centrar en mis datos calcula el encuadre desde las sedes del cliente y solución activos, incluso si están en otros continentes. Hay lista equivalente y fallback SVG. En móvil la leyenda se coloca debajo del visor para conservar el territorio visible.
- El tooltip identifica país, provincia o ubicación. En Salud separa sensores normales, en atención, críticos y sin señal; Dispositivos muestra cantidad y conectividad; Cobertura muestra ubicaciones con datos. Un territorio vacío se marca Sin datos IoT. Los marcadores admiten foco y vista previa táctil antes de abrir el sitio.
- El primer fotograma WebGL visible muestra Sudamérica centrada y derecha. La preparación ocupa el mismo panel hasta ese render; luego el mapa se acerca un 5–8 % durante unos 900 ms, los marcadores aparecen con un fundido breve y Córdoba pulsa una vez. La cámara conserva la orientación cenital al terminar. Un deep link a país/provincia abre encuadrado sin esta entrada; con movimiento reducido se muestra el estado final de inmediato. El fallback SVG se revela ya encuadrado. Su verificación visual se registra en [review.md](docs/specs/review.md).
- Los límites administrativos se simplificaron para la demo. [Fuentes y tratamiento](docs/specs/cartography.md). [Captura de mundo](designs/evidence/implementation-map/world-1440.png), [Argentina](designs/evidence/implementation-map/argentina-1440.png) y [móvil](designs/evidence/implementation-map/argentina-mobile-final.png).

## Colors

Valores observados en las variables CSS raíz:

| Rol / variable | Oscuro | Claro |
| --- | --- | --- |
| Fondo `--bg` | `#0c1117` | `#f1f4f6` |
| Panel `--panel` | `#131a22` | `#ffffff` |
| Superficie secundaria `--panel2` | `#19222c` | `#f4f6f9` |
| Superficie terciaria `--panel3` | `#202d38` | `#e9eef2` |
| Borde `--line` | `#26333e` | `#dce3e9` |
| Texto `--text` | `#eff3f5` | `#172b3c` |
| Texto secundario `--muted` | `#8e9ca9` | `#667a8c` |
| Acento `--accent` | `#b4b5ff` | `#5d58bc` |
| Fondo de acento `--accentbg` | `#272947` | `#eeecff` |
| Normal `--green` | `#67c5a1` | `#218468` |
| Advertencia `--yellow` | `#e3b86c` | `#a36a16` |
| Crítico `--red` | `#ee8588` | `#bd4e59` |
| Mapa `--map` | `#101922` | `#e6eef1` |
| Navegación `--nav` | `#0e151c` | `#f9fbfc` |

Sin señal y sin datos tienen representaciones propias en las funciones de estado. Su incorporación a tokens semánticos comunes queda pendiente. Medir contraste antes de aprobar cambios; los valores actuales no implican conformidad.

## Typography

La pila declarada es `Inter, "Segoe UI", Arial, sans-serif`; declarar Inter no garantiza que esté instalada o cargada. El cuerpo actual usa 14 px y altura de línea 1,5; el título principal usa 29 px en la regla base y cambia con breakpoints. Existen textos secundarios de 10–12 px.

Criterio propuesto: fijar una escala reutilizable y verificar legibilidad de unidades, ejes, filtros y etiquetas antes de cambiar tamaños globales. Las tablas operativas deben seguir siendo escaneables.

## Layout

- Sidebar fija de 215 px en la regla base; en la Vista global de escritorio se reduce a un riel de 68 px con etiquetas accesibles.
- Cabecera superior de 70 px en la regla base y 56 px en la Vista global de escritorio; el contenido base tiene ancho máximo de 1900 px, mientras el visor global usa todo el ancho disponible.
- Vista global con mapa casi a la altura útil del navegador, controles superpuestos y panel flotante de cobertura/ubicaciones plegable; vistas internas con tablas, fichas y gráficas.
- Breakpoints observados: 1650, 1200, 980 y 760 px.
- La adaptación existente incluye apilamiento de paneles y menú desplegable en pantallas pequeñas.

Criterios propuestos: conservar filtros y breadcrumbs visibles, evitar scroll horizontal de página y permitir scroll localizado en tablas cuando sea necesario. Revisar la jerarquía del estado operativo frente a los controles de simulación.

## Elevation & Depth

Los paneles se separan mediante bordes y fondos. Las sombras se usan en elementos flotantes. La extrusión del mapa comunica la magnitud declarada por cada capa: porcentaje de dispositivos con condición, cantidad de dispositivos o altura fija de cobertura. La leyenda explica la unidad; ninguna extrusión representa altitud física. La ilustración isométrica de instalación es esquemática.

La profundidad debe ayudar a localizar y seleccionar. El flujo debe seguir siendo usable mediante listados y mapa SVG. Existe manejo de `prefers-reduced-motion`; su comportamiento completo se validará en navegador.

## Shapes

El CSS usa esquinas redondeadas, con ejemplos de 7 px para botones base, 11 px para paneles y 13 px para el modal. No existe todavía una escala única de radios documentada en el código.

Los botones de icono tienen 34 px en la regla general y variantes contextuales menores. Revisar áreas de interacción táctil, sin asumir que agrandar el dibujo del icono equivale a ampliar el área pulsable.

## Components

Patrones existentes: sidebar, selector de cliente, breadcrumbs, chips de alcance, botones, KPI, panel de mapa, listado de ubicaciones, tablas, tarjetas de entidades, badges de estado, series temporales, control de simulación, búsqueda modal y toast.

En la implementación futura cada patrón documentará estados relevantes: normal, hover, foco, selección, vacío, error y deshabilitado cuando corresponda. La especificación no obliga a inventar estados de red en el HTML sin backend.

## Do's and Don'ts

- Usar el acento para interacción y los colores de severidad para estado operativo.
- Acompañar estado y conectividad con texto comprensible.
- Mantener unidades, instante y ventana temporal identificables.
- Conservar contexto al entrar y salir de detalles.
- Diferenciar datos observados de explicaciones ilustrativas.
- No presentar extrusión, isometría o mantenimiento predictivo como información física o inferencia real.
- No cambiar paleta, tipografía o composición global por una recomendación aislada de una skill.
