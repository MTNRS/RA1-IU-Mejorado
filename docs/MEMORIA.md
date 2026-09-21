# Memoria — jocarsa | iu mejorado

## Identificación y alcance

0488 · Desarrollo de interfaces · Unidad 1 · RA1. Actividad: jocarsa | iu mejorado.
Se parte de la aplicación con objetos del profesor y se integra un formulario
creado visualmente para registrar solicitudes ficticias. El enunciado contiene
los criterios a–h, sin otras funciones obligatorias especificadas.

## a) Herramientas y librerías de interfaces

| Herramienta | Tecnología y salida | Uso y limitaciones para la práctica |
| --- | --- | --- |
| Qt Widgets Designer | Componentes Qt; descripción `.ui` | Adecuado para escritorio Qt y distribución de widgets; no produce directamente la interfaz web de clase |
| JavaFX Scene Builder | Componentes JavaFX; FXML | Permite diseñar visualmente y enlazar controladores Java; introduciría otra plataforma |
| GrapesJS | Componentes web; modelo editable, HTML y CSS | Compatible con la aplicación HTML/CSS/JS del profesor; la exportación visual necesita lógica de aplicación adicional |
| Librería `jocarsa.iu` de clase | Clases JS, plantillas HTML, CSS y JSON | Proporciona navegación, fichas, tablas, formularios y avisos; en la versión revisada no es un editor visual completo |

Se elige GrapesJS para construir el formulario y se conserva jocarsa.iu para la
aplicación. Un editor de texto permite modificar código, pero por sí solo no
acredita haber colocado componentes mediante un editor visual.

Fuentes oficiales consultadas el 21/09/2026:
[Qt Designer](https://doc.qt.io/qt-6.5/qtdesigner-manual.html),
[JavaFX y Scene Builder](https://openjfx.io/),
[GrapesJS: introducción](https://grapesjs.com/docs/getting-started.html),
[bloques](https://grapesjs.com/docs/modules/Blocks) y
[propiedades](https://grapesjs.com/docs/modules/Traits.html).

## b) Creación de la interfaz con editor visual

Se configura GrapesJS con bloques básicos: contenedor de formulario, título,
etiquetas con entrada, selector, área de texto y botones. La paleta no contiene
un formulario completo preconstruido. El diseño se crea incorporando esos bloques
por medio de los controles visibles del editor y se conserva su exportación.

`scripts/disenar_formulario.py` permite reproducir las acciones realizadas en
el editor. `docs/capturas/editor.png` muestra el diseño y las propiedades
de los componentes.

## c) Ubicación de los componentes

Los componentes se insertan en el formulario, que utiliza una disposición Grid.
Se añaden los campos en secuencia: Nombre, Correo, Asunto, Prioridad y Detalle.
Se insertan Limpiar y Guardar y se utiliza **Subir seleccionado** para cambiar la
posición de Guardar. El editor actualiza la jerarquía y el orden del HTML.

No se afirma que se haya usado arrastre para esta colocación: se utilizan los
controles de inserción y reordenación de la configuración del editor. La aplicación
base conserva además las funciones de arrastre de vistas y columnas de clase.

## d) Propiedades modificadas

En el panel de propiedades se seleccionan tres entradas:

| Campo | Nombre técnico | Ayuda (`placeholder`) | Obligatorio | Tipo |
| --- | --- | --- | --- | --- |
| Nombre | nombre | Nombre del solicitante | Sí | text |
| Correo | email | persona@example.com | Sí | email |
| Asunto | asunto | Describe brevemente la solicitud | Sí | text |

Ayuda y obligatoriedad se cambian mediante la interfaz del editor. Nombre y tipo
proceden de los bloques configurados. Prioridad ofrece Normal, Alta y Baja;
Detalle utiliza un área de texto. Se distingue la configuración de un bloque de
las propiedades efectivamente modificadas durante la sesión.

## e) Análisis del código generado

`formulario-generado.html` contiene un `body`, un `form` y la jerarquía colocada
visualmente. Cada etiqueta envuelve su control. Los atributos `name` permiten
extraer los datos con `FormData`; `required` y `type=email` activan validación
nativa. Los botones tienen tipos `submit` y `reset`, con acciones diferentes.

El editor añade IDs a algunos nodos. El CSS exportado contiene reglas globales
para `body`, `form`, `label` y controles, con propiedades normalizadas. El modelo
JSON conserva componentes y estilos para poder reabrir el diseño.

La exportación no guarda solicitudes, no contiene una base de datos ni implementa
los avisos de la aplicación. Son responsabilidades añadidas en la adaptación.

## f) Modificación del código generado

Se conserva la salida original en `diseno/`. La transformación reproducible está
en `scripts/adaptar_formulario.py` y escribe una plantilla independiente:

- Elimina `body` porque la plantilla se inserta dentro de `#escenario`.
- Retira IDs automáticos y mantiene `solicitud`, `nombre`, `email` y `asunto`.
- Añade clases de la librería, límites de longitud y autocompletado.
- Sitúa el detalle en una fila completa y añade una zona de mensajes con `role=status`.
- Reutiliza el CSS de la aplicación y añade reglas limitadas a `#solicitud`.

Esto evita que el CSS global exportado cambie de forma involuntaria las tablas,
la navegación u otros controles. La aplicación no depende del editor en ejecución.

## g) Eventos y acciones

| Evento | Acción |
| --- | --- |
| `click` en + Nuevo, Formulario o vista Formulario | Cargar la plantilla generada y enfocar Nombre |
| `submit` | Validar, normalizar espacios, persistir y actualizar tabla |
| `reset` | Limpiar campos y actualizar mensaje |
| `input` del buscador | Filtrar filas del listado |
| `keydown` Escape | Volver al listado |
| `click` en el cierre de un aviso | Retirar el aviso |
| `pointerdown` y `pointermove` de separadores | Redimensionar columnas, función conservada del ejemplo |

El guardado se anuncia solo después de escribir en `localStorage`. Si falla, se
mantienen los datos del formulario y se muestra un error. Las cargas asíncronas
usan un contador de cambios de vista para evitar que una respuesta tardía
reemplace el listado cuando el usuario ya ha salido del formulario.

## h) Aplicación integrada y pruebas

`AplicacionIU` conserva la estructura de clase: `EstadoIU`, `OrigenDatos`,
`FichaIU`, `ToastIU` y `GestorColumnas`. Se añade `AlmacenSolicitudes` como una
clase sencilla para leer y guardar registros en el navegador. No se añade servidor
ni framework de ejecución a la aplicación.

Las pruebas verifican la plantilla integrada, rechazo del envío vacío y correo
inválido, alta, aviso, persistencia tras recargar, filtro con y sin resultados,
limpieza, Escape y fallo simulado del almacenamiento. La captura muestra el
formulario funcionando dentro de la interfaz de jocarsa.

## Correspondencia con los criterios

| Criterio | Evidencia conservada |
| --- | --- |
| a | Comparación de herramientas y justificación |
| b | Editor configurado, automatización y captura del diseño |
| c | Inserción por bloques y cambio de posición de Guardar |
| d | Propiedades de ayuda y obligatoriedad en la exportación |
| e | Análisis y HTML/CSS/JSON originales |
| f | Script de adaptación y plantilla final |
| g | Eventos en componentes.js y resultados de pruebas |
| h | Aplicación ejecutable, persistencia local y captura |

## Límites

La persistencia es local a un navegador/origen; no ofrece colaboración,
autenticación ni control de permisos. Se usan datos ficticios y la aplicación
permanece como prototipo académico independiente de Integra Tech Consulting.
