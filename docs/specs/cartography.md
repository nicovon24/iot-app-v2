# Cartografía: fuentes, cobertura y licencias

La cartografía responde **dónde está un territorio**. No contiene mediciones ni cobertura IoT. Una forma visible en el mapa mundial puede no tener instalaciones en esta demo y debe aparecer como «Sin datos IoT».

## Foco de la demo sudamericana

El mapa conserva su cobertura mundial. [Spec 01](subspecs/01-initial-design.md) cambia el encuadre y las ubicaciones IoT simuladas a Argentina, Chile, Perú y Uruguay; no agrega ni regenera geometría. Lima se vincula a `PER-587` y Montevideo a `UY-MO` en la versión simplificada de `world-admin1.js`. Estados Unidos y México siguen seleccionables como territorios sin datos IoT de esta demo.

## Base mundial

Para ampliar el visor al planeta se descargaron dos capas del [repositorio de Natural Earth](https://github.com/nvkelso/natural-earth-vector/tree/master/geojson): [países 1:50m](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson) y [estados/provincias 1:10m](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_10m_admin_1_states_provinces.geojson). La capa de provincias 1:50m se descartó para alcance mundial: el archivo obtenido solo contiene nueve países. La [documentación oficial de 1:10m](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/) describe más de 4.500 divisiones de primer nivel, con algunas excepciones en territorios pequeños.

| Capa fuente | Fecha | Entidades comprobadas | Tamaño y SHA-256 del archivo descargado |
| --- | --- | --- | --- |
| Países 1:50m | 2026-10-20 | 242 entidades de países/territorios; `Polygon`/`MultiPolygon` | 3.083.490 bytes; `3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb` |
| Admin 1 mundial 1:10m | 2026-10-20 | 4.596 divisiones en 241 códigos de país; `Polygon`/`MultiPolygon` | 40.726.851 bytes; `22d0e3ad85eb3e27f17cabf8ba2d50e554fbc27a87796ff891d958185da62fb5` |

La [licencia oficial de Natural Earth](https://www.naturalearthdata.com/about/terms-of-use/) declara los datos de dominio público. Se acreditará «Made with Natural Earth» en el visor aunque no es obligatorio. La [política de límites](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-admin-0-countries-2/) usa una representación *de facto*; sus formas no son una afirmación de IoTArg sobre disputas de soberanía.

Los campos de identificación se normalizan a un código único por territorio y a `ISO 3166-2` o `adm1_code` para divisiones. Algunas formas de Natural Earth tienen `ISO_A2=-99` o códigos particulares: no se puede usar ese valor como ID único. El archivo admin 1 presenta algunas etiquetas con caracteres defectuosos y algunas divisiones sin nombre; el procesamiento debe conservar IDs, aplicar un nombre legible cuando exista y permitir un fallback explícito. Los 241 códigos de admin 1 no implican que todos los territorios de la capa de 242 países admitan desglose.

La maqueta empaqueta un contorno mundial compacto en el HTML y las divisiones admin 1 en un script local. Construye las mallas de un país cuando se entra en él; la fuente geográfica mundial se carga desde disco, sin consultar una API durante el recorrido. El conjunto `designs/IoTArg.html` + `designs/map-data/world-admin1.js` funciona también con `file://`. Un país con geometría administrativa pero sin ubicaciones IoT muestra sus límites y el estado «Sin datos IoT», sin colorearlo como saludable ni asignarle altura de medición. El primer recorrido operativo sigue en Córdoba; agregar cartografía mundial no crea clientes, sensores ni alarmas fuera de las cuatro ubicaciones simuladas.

### Geometría entregada

| Asset | Resultado del procesamiento |
| --- | --- |
| `designs/IoTArg.html` | 242 territorios de Natural Earth 1:50m embebidos para el mapa mundial. |
| `designs/map-data/world-admin1.js` | 4.556 divisiones de 239 países de Natural Earth 1:10m; Argentina se sustituye por 24 divisiones de Georef dentro del HTML. Total navegable: 240 países con admin 1. Archivo derivado: 2.033.052 bytes, SHA-256 `6a87d1fb286ad6c6964cd53a971fa47b29bdc383f06ecbf836f8560fd888556d`. |

Las 16 divisiones restantes del archivo fuente 1:10m no tienen correspondencia con un polígono país independiente en la base 1:50m usada por la maqueta. Los países sin desglose permanecen seleccionables a nivel nacional. La simplificación independiente por anillo reduce mucho el tamaño para la demo; puede producir pequeñas diferencias visuales entre fronteras compartidas al acercar demasiado. Antes de usar esta cartografía en una aplicación de precisión, procesar topología compartida y revisar las etiquetas/códigos defectuosos del origen.

Los scripts reproducibles son [`build_world.py`](../../designs/map-data/build_world.py) y [`build_admin1.py`](../../designs/map-data/build_admin1.py). Requieren pasarles como argumentos los GeoJSON fuente descargados de las rutas arriba y vuelven a generar los assets de `designs/`. Los GeoJSON originales de 40 MB no se versionan en la maqueta; sus URL y hashes permiten comprobarlos.

## Fuente incorporada para el primer corte

El mapa provincial de Argentina se prepara a partir del [GeoJSON completo de provincias de Georef](https://apis.datos.gob.ar/georef/api/provincias.geojson), servicio del Estado argentino. La [documentación de descarga de Georef](https://www.argentina.gob.ar/georef/descarga-de-la-base-completa) publica también la ruta de la API v2.0 y explica el formato GeoJSON. La descarga usada en este corte procede de la ruta anterior de la misma API; se registra exactamente para que pueda reproducirse.

| Campo | Valor comprobado |
| --- | --- |
| Fecha de obtención | 2026-10-20 |
| Ruta descargada | `https://apis.datos.gob.ar/georef/api/provincias.geojson` |
| SHA-256 del archivo fuente | `b086852064c26813d9f607c82c91b4e74e18ea83fd21993ddedd473cf8495af5` |
| Tamaño | 614706 bytes |
| Formato | GeoJSON `FeatureCollection`, 24 entidades `Polygon`/`MultiPolygon` |
| Córdoba | ID Georef `14`; `iso_id` `AR-X`; `fuente` `IGN` |
| Archivo fuente de trabajo | Directorio temporal local durante la construcción; la aplicación usa geometría incluida con su entrega |

La [licencia y condiciones oficiales](https://www.argentina.gob.ar/georef/condiciones-de-uso-y-licencia) establecen **CC BY 4.0**, atribución obligatoria y aviso de modificaciones. La UI y la documentación de entrega deben mostrar:

> Cartografía provincial: Servicio Georef – argentina.gob.ar/georef (CC BY 4.0). Geometría adaptada para visualización.

La fuente geográfica describe territorios. No aporta clientes, ubicaciones, sensores ni severidad de IoTArg. Esos valores proceden únicamente de la demo simulada y de sus filtros.

## Tratamiento para la maqueta

- Mantener IDs oficiales y relación explícita de la ubicación Córdoba con provincia `14`.
- Aplicar la proyección de la cartografía existente de América; conservar anillos, huecos y partes de `MultiPolygon`.
- Simplificar y/o redondear coordenadas solo si el resultado conserva límites legibles y no abre huecos entre provincias. Documentar el método y hash del resultado cuando el implementador cierre el archivo.
- El encuadre continental de Argentina se calcula sobre el territorio visible elegido. Si una geometría contiene porciones alejadas, su exclusión **del encuadre** se declara; no alterar silenciosamente los datos de origen.
- El HTML debe abrirse desde `file://` sin depender de una petición a Georef. Cualquier cartografía procesada usada por el visor se empaqueta con la maqueta.
- El mapa distingue territorio sin cobertura IoT («Sin datos IoT») de dispositivo operativo y alarma crítica.

Estado de fuentes: **Natural Earth global y Georef Argentina descargados, validados e integrados en el primer corte**. La verificación visual y los límites se registran por separado en [tareas](tasks.md) y [revisión](review.md).
