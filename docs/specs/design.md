# Contratos técnicos y evolución

La propuesta de etapa conectada se detalla en [TBD — Integración ThingsBoard](subspecs/tbd-thingsboard-integration.md). La investigación encontró Next.js, NestJS y un conector ThingsBoard implementados en el repositorio hermano `iot_app`; aquí, en `iol-new`, continúa la maqueta sin backend. La nueva ruta propone reutilizar esa aplicación y sustituye el scaffold desde cero para esa integración. La disponibilidad actual de la cuenta sigue pendiente de verificación.

## Decisiones y autoridad

| Decisión | Estado / fundamento |
| --- | --- |
| Demo de portfolio | Confirmada por el usuario |
| Primera etapa sobre HTML | Confirmada; la maqueta es la referencia de interacción |
| `docs/specs/` como ubicación SDD | Solicitada por el usuario; evita duplicar `docs/features/` |
| `PRODUCT.md` y `DESIGN.md` en raíz | Solicitados; documentados en esta entrega |
| `designs/IoTArg.html` | Ubicación actual de la única maqueta editable; traslado con hash idéntico comprobado |
| Next.js App Router + TypeScript | Dirección indicada por README para etapa siguiente; no hay scaffold |
| Base de datos, autenticación, hosting, versión de framework | Pendientes |
| ThingsBoard detrás de un modelo normalizado | Intención del README; no hay conector implementado |

## Contrato de la etapa HTML

El archivo debe seguir abriendo como demo autocontenida. Mantener datos, navegación, escenarios y fallback salvo correcciones especificadas. El traslado de ruta se hace como una tarea separada para poder distinguirlo de cambios funcionales.

Estructura objetivo después de esa tarea:

```text
README.md
PRODUCT.md
DESIGN.md
designs/
  IoTArg.html
docs/
  specs/
    README.md
    requirements.md
    baseline.md
    ux.md
    data.md
    design.md
    orchestration.md
    tasks.md
    review.md
```

No mantener dos HTML editables con igual propósito. El traslado a `designs/IoTArg.html` conservó el SHA previo en la evidencia y los enlaces principales se actualizaron. Git local está inicializado, todavía sin commit.

## Arquitectura futura propuesta

```text
Vistas Next.js / componentes
              ↓
Estado de navegación y consultas normalizadas
              ↓
Casos de uso: alcance, telemetría, alarmas
              ↓
Contrato de proveedor
       ↙                 ↘
Simulación local     Adaptador ThingsBoard futuro
```

Separar el cálculo de dominio de componentes y representación. El proveedor simulado conserva escenarios deterministas para pruebas y demostración. Un proveedor real deberá declarar capacidades y errores; no fingir equivalencia cuando no soporte historial o reconocimiento.

La elección de Server Actions, route handlers, estrategia de caché y renderizado se resolverá para operaciones concretas. El README previo no demuestra su implementación.

## Requisitos de aplicación futura

| ID | Aceptación observable |
| --- | --- |
| APP-001 | Scaffold Next.js + TypeScript con instrucciones reproducibles; build y chequeo de tipos pasan con versiones fijadas. |
| APP-002 | Dominio y proveedor simulado funcionan independientemente del render; pruebas verifican DATA-001 a DATA-005. |
| APP-003 | El recorrido UX-002 se conserva en componentes y rutas, con soporte de enlaces y recuperación de URL inválida. |
| APP-004 | El contrato de proveedor devuelve entidades y telemetría normalizadas; una implementación simulada puede sustituirse sin reescribir vistas. |
| APP-005 | Antes de conectar ThingsBoard se define contrato con muestras autorizadas, errores, unidades, timestamps, paginación y credenciales del lado servidor; se verifica en entorno de prueba. |
| APP-006 | Antes de persistir datos o incorporar usuarios se especifican autenticación, permisos y aislamiento entre clientes, con pruebas y revisión independiente. |
| APP-007 | Un despliegue de portfolio dispone de URL y recorrido de demo verificado; proveedor, acceso y configuración se seleccionan antes de publicar. |

APP-005 y APP-006 son gates para una etapa posterior. No autorizan acceso a una cuenta o a dispositivos reales ni establecen que esas integraciones sean necesarias para terminar la demo.

## Dependencias y riesgos

- La revisión de la maqueta precede al refinamiento para fijar evidencia visual.
- La normalización de último reporte precede a cambios de telemetría sin señal.
- Múltiples áreas requieren ampliar el modelo, no solo agregar pantallas.
- El bundle Three.js embebido dificulta revisar diffs; evitar reformatearlo accidentalmente con cambios de UI.
- Git se inicializó al comenzar la implementación visual; los hashes iniciales siguen en `baseline.md`. No hay commit ni publicación por ese hecho.
- Referencias visuales ausentes no deben decidir la implementación.

## Decisiones pendientes

1. Orden y agrupación definitivos de navegación tras inspección visual.
2. Regla exacta del último reporte sin señal.
3. Política de nombres en español para soluciones y términos técnicos.
4. Alcance del MVP posterior al prototipo.
5. Activación del harness tras resolver su ruta fija de aceptación y verificar soporte del runtime elegido; fuente ya confirmada por el usuario en `nicovon24/harness-nicovon24`.

El estado de las tareas se mantiene en [tasks.md](tasks.md).
