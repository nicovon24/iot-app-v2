# Evidencia del primer corte del mapa

Capturas realizadas el 2026-10-20 en Chrome headless. El mapa muestra geometría mundial; los estados IoT provienen solo de las cuatro ubicaciones simuladas.

| Comprobación | Captura |
| --- | --- |
| Mundo, escritorio 1440×900 | [world-1440.png](world-1440.png) |
| Argentina y provincia Córdoba, escritorio | [argentina-1440.png](argentina-1440.png) |
| Argentina, móvil 390×844 con leyenda legible | [argentina-mobile-final.png](argentina-mobile-final.png) |
| Atribución Georef visible en móvil desde `file://` | [mobile-credit-final.png](mobile-credit-final.png) |
| Argentina SVG con WebGL desactivado | [fallback-argentina-fixed.png](fallback-argentina-fixed.png) |
| Render tras redimensionar sin recargar | [resize-fixed-1440.png](resize-fixed-1440.png) |

Las demás imágenes de esta carpeta registran fallos intermedios que se corrigieron durante la implementación (canvas vacío tras redimensionar y falta de encuadre SVG); no representan el estado final. La [revisión](../../../docs/specs/review.md) indica qué verificaciones siguen pendientes.
