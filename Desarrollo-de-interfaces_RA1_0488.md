# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-09-21 20:22:19 +0200
- **Usuario:** dlc
- **UID:** 1000
- **Equipo:** kali
- **Sistema operativo:** Linux
- **Versión del kernel:** 6.19.11+kali-amd64
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `/home/dlc/RA1-IU-Mejorado`
- **Proyecto documentado:** `/tmp/iu-final-i5o1s_fb/RA1-IU-Mejorado`
- **HMAC-SHA-256 de autenticidad:** `0bed47f0a315df0db9f167d3eed4be7cd3206993b598308993a8a689cfdf4489`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
/tmp/iu-final-i5o1s_fb/RA1-IU-Mejorado
├── README.md
├── diseno
│   ├── formulario-editor.json
│   ├── formulario-generado.css
│   └── formulario-generado.html
├── docs
│   ├── MEMORIA.md
│   ├── OPERACIONES.md
│   ├── PROCEDENCIA.md
│   ├── VERIFICACION.md
│   └── capturas
│       ├── aplicacion.png
│       └── editor.png
├── editor
│   ├── editor.js
│   └── index.html
├── public
│   ├── css
│   │   └── estilo.css
│   ├── data
│   │   ├── clientes.json
│   │   ├── datos.json
│   │   ├── entidades.json
│   │   └── menu.json
│   ├── index.html
│   ├── js
│   │   ├── componentes.js
│   │   └── solicitudes.js
│   └── templates
│       └── formulario-solicitud.html
├── requirements-dev.txt
└── scripts
    ├── adaptar_formulario.py
    ├── disenar_formulario.py
    ├── preparar_editor.py
    └── probar_aplicacion.py
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# RA1-IU-Mejorado
**README.md**
```markdown
# jocarsa | iu mejorado — RA1

**0488 · Desarrollo de interfaces · Generación de interfaces de usuario.**

Mejora de la interfaz integrada de jocarsa mediante un formulario de solicitudes
creado en un editor visual, exportado y adaptado al código de la aplicación.
Caso ficticio: solicitudes internas de Integra Tech Consulting.

## Ejecutar la aplicación

Requiere Python 3 para servir los archivos y navegador moderno con JavaScript:

```bash
python3 -m http.server 8047 --bind 127.0.0.1 --directory public
```

Abrir `http://127.0.0.1:8047`. La aplicación final no necesita GrapesJS ni conexión
a Internet. Pulsar **+ Nuevo**, completar nombre, correo y asunto, seleccionar
prioridad y guardar. La nueva fila aparece en el listado. La búsqueda filtra las
solicitudes; Limpiar reinicia el formulario y Escape vuelve al listado.

Los datos se guardan en `localStorage` de ese navegador y origen (incluido el
puerto). No existe servidor de datos, autenticación ni sincronización entre
equipos. El registro inicial es ficticio. No se debe interpretar la interfaz
como un sistema empresarial desplegado.

## Abrir el editor visual

La herramienta utilizada es **GrapesJS 0.23.6**, con una paleta configurada para
los componentes de la práctica. Los botones de la paleta insertan bloques en su
lienzo; se selecciona cada campo y se editan sus propiedades en el panel derecho.

```bash
python3 scripts/preparar_editor.py
python3 -m http.server 8046 --bind 127.0.0.1
```

Abrir `http://127.0.0.1:8046/editor/`. La descarga inicial de la dependencia
requiere red. Se guarda en `.runtime/`, excluida de Git y del informe.

Para reproducir el diseño manualmente:

1. Añadir Contenedor formulario y Título.
2. Añadir Nombre, Correo, Asunto, Prioridad y Detalle.
3. Añadir Limpiar y después Guardar; pulsar **Subir seleccionado** para situar
   Guardar delante de Limpiar.
4. Seleccionar cada uno de los campos Nombre, Correo y Asunto en el lienzo.
   Editar la propiedad Ayuda y marcar Obligatorio.
5. Pulsar **Exportar proyecto** para descargar JSON con HTML, CSS y modelo editable.

**Abrir diseño guardado** recupera el proyecto conservado en `diseno/`.
La configuración utiliza la API de bloques/componentes y el panel nativo de
propiedades de GrapesJS; no es un editor diseñado desde cero.

## Exportación y adaptación

- `diseno/formulario-editor.json`: proyecto editable y exportación obtenida.
- `diseno/formulario-generado.html` y `.css`: salida original conservada.
- `public/templates/formulario-solicitud.html`: plantilla adaptada.
- `scripts/adaptar_formulario.py`: transformación reproducible de la exportación.
- `docs/capturas/editor.png`: evidencia del uso del editor.
- `docs/capturas/aplicacion.png`: formulario integrado y cumplimentado.

La adaptación elimina el contenedor `body` del fragmento y los IDs automáticos,
añade límites, autocompletado, clases de jocarsa-iu y un mensaje de estado. Se
emplea el estilo de la aplicación en lugar de importar reglas globales del editor.
La exportación de `diseno/` se conserva para comparar el antes y el después.

## Preparar y ejecutar las pruebas

Con Python 3, Chromium y Node disponibles:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
python3 scripts/preparar_editor.py
.venv/bin/python scripts/disenar_formulario.py
python3 scripts/adaptar_formulario.py
.venv/bin/python scripts/probar_aplicacion.py
```

El diseño automatizado usa clics sobre la paleta, selección en el lienzo,
edición en el panel de propiedades y descarga desde el botón del editor.
La exportación usa los métodos `getHtml`, `getCss` y `getProjectData` del editor.
La ejecución de este script vuelve a generar los archivos de `diseno/`; los IDs
internos pueden variar. No regenera el informe oficial automáticamente.

Las pruebas de aplicación usan un navegador aislado y un servidor local temporal.
Comprueban validación, alta, recarga, búsqueda, limpieza y error de almacenamiento.
Las dependencias de pruebas no son necesarias para utilizar la aplicación final.

## Documentación e informe

- [Memoria y criterios a–h](docs/MEMORIA.md).
- [Procedencia del código](docs/PROCEDENCIA.md).
- [Operaciones e incidencias](docs/OPERACIONES.md).
- [Resultados de las pruebas](docs/VERIFICACION.md).

Informe de `jocarsa/generador`: `Desarrollo-de-interfaces_RA1_0488.md`.
Se incluye en el repositorio junto con la aplicación. La entrada del generador
excluye `.git`, `.venv`, `.runtime`, cachés y el propio informe. Sí incluye los
archivos de diseño porque son evidencia necesaria de los criterios b–f.

## Relación con Integra Tech Consulting y uso de IA

El caso de uso es una propuesta académica de recepción de solicitudes, con datos
ficticios. No se ha integrado en sistemas reales de la empresa.

Codex ha ayudado a adaptar el código del profesor, operar el editor mediante
automatización del navegador, documentar y probar la aplicación. El alumno debe
revisar y comprender el trabajo antes de entregarlo; esa revisión personal no
queda acreditada por las pruebas automáticas.
```
## diseno
**formulario-editor.json**
```json
{
  "versionEditor": "0.23.6",
  "html": "<body><form id=\"solicitud\"><h2 id=\"idcc\">Nueva solicitud</h2><label id=\"io7s\">Nombre<input id=\"nombre\" name=\"nombre\" type=\"text\" placeholder=\"Nombre del solicitante\" required/></label><label id=\"inet\">Correo<input id=\"email\" name=\"email\" type=\"email\" placeholder=\"persona@example.com\" required/></label><label id=\"i4dpl\">Asunto<input id=\"asunto\" name=\"asunto\" type=\"text\" placeholder=\"Describe brevemente la solicitud\" required/></label><label id=\"iz20b\">Prioridad<select name=\"prioridad\"><option>Normal</option><option>Alta</option><option>Baja</option></select></label><label id=\"isl7v\">Detalle<textarea name=\"detalle\" rows=\"3\"></textarea></label><button type=\"submit\" id=\"i6jx5\">Guardar solicitud</button><button type=\"reset\" id=\"i0lab\">Limpiar</button></form></body>",
  "css": "* { box-sizing: border-box; } body {margin: 0;}body{font-family:Arial;color:rgb(36, 50, 70);}form{display:grid;row-gap:16px;column-gap:16px;padding-top:24px;padding-right:24px;padding-bottom:24px;padding-left:24px;background-image:initial;background-position-x:initial;background-position-y:initial;background-size:initial;background-repeat:initial;background-attachment:initial;background-origin:initial;background-clip:initial;background-color:rgb(255, 255, 255);}label{display:grid;row-gap:6px;column-gap:6px;}input, select, textarea, button{font-style:inherit;font-variant-ligatures:inherit;font-variant-caps:inherit;font-variant-numeric:inherit;font-variant-east-asian:inherit;font-variant-alternates:inherit;font-variant-position:inherit;font-variant-emoji:inherit;font-weight:inherit;font-stretch:inherit;font-size:inherit;line-height:inherit;font-family:inherit;font-optical-sizing:inherit;font-size-adjust:inherit;font-kerning:inherit;font-feature-settings:inherit;font-variation-settings:inherit;font-language-override:inherit;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;border-top-width:1px;border-right-width:1px;border-bottom-width:1px;border-left-width:1px;border-top-style:solid;border-right-style:solid;border-bottom-style:solid;border-left-style:solid;border-top-color:rgb(116, 132, 153);border-right-color:rgb(116, 132, 153);border-bottom-color:rgb(116, 132, 153);border-left-color:rgb(116, 132, 153);border-image-source:initial;border-image-slice:initial;border-image-width:initial;border-image-outset:initial;border-image-repeat:initial;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;}button{background-image:initial;background-position-x:initial;background-position-y:initial;background-size:initial;background-repeat:initial;background-attachment:initial;background-origin:initial;background-clip:initial;background-color:rgb(41, 76, 119);color:white;}",
  "proyecto": {
    "dataSources": [],
    "assets": [],
    "styles": [
      {
        "selectors": [],
        "selectorsAdd": "body",
        "style": {
          "font-family": "Arial",
          "color": "rgb(36, 50, 70)"
        }
      },
      {
        "selectors": [],
        "selectorsAdd": "form",
        "style": {
          "display": "grid",
          "row-gap": "16px",
          "column-gap": "16px",
          "padding-top": "24px",
          "padding-right": "24px",
          "padding-bottom": "24px",
          "padding-left": "24px",
          "background-image": "initial",
          "background-position-x": "initial",
          "background-position-y": "initial",
          "background-size": "initial",
          "background-repeat": "initial",
          "background-attachment": "initial",
          "background-origin": "initial",
          "background-clip": "initial",
          "background-color": "rgb(255, 255, 255)"
        }
      },
      {
        "selectors": [],
        "selectorsAdd": "label",
        "style": {
          "display": "grid",
          "row-gap": "6px",
          "column-gap": "6px"
        }
      },
      {
        "selectors": [],
        "selectorsAdd": "input, select, textarea, button",
        "style": {
          "font-style": "inherit",
          "font-variant-ligatures": "inherit",
          "font-variant-caps": "inherit",
          "font-variant-numeric": "inherit",
          "font-variant-east-asian": "inherit",
          "font-variant-alternates": "inherit",
          "font-variant-position": "inherit",
          "font-variant-emoji": "inherit",
          "font-weight": "inherit",
          "font-stretch": "inherit",
          "font-size": "inherit",
          "line-height": "inherit",
          "font-family": "inherit",
          "font-optical-sizing": "inherit",
          "font-size-adjust": "inherit",
          "font-kerning": "inherit",
          "font-feature-settings": "inherit",
          "font-variation-settings": "inherit",
          "font-language-override": "inherit",
          "padding-top": "10px",
          "padding-right": "10px",
          "padding-bottom": "10px",
          "padding-left": "10px",
          "border-top-width": "1px",
          "border-right-width": "1px",
          "border-bottom-width": "1px",
          "border-left-width": "1px",
          "border-top-style": "solid",
          "border-right-style": "solid",
          "border-bottom-style": "solid",
          "border-left-style": "solid",
          "border-top-color": "rgb(116, 132, 153)",
          "border-right-color": "rgb(116, 132, 153)",
          "border-bottom-color": "rgb(116, 132, 153)",
          "border-left-color": "rgb(116, 132, 153)",
          "border-image-source": "initial",
          "border-image-slice": "initial",
          "border-image-width": "initial",
          "border-image-outset": "initial",
          "border-image-repeat": "initial",
          "border-top-left-radius": "5px",
          "border-top-right-radius": "5px",
          "border-bottom-right-radius": "5px",
          "border-bottom-left-radius": "5px"
        }
      },
      {
        "selectors": [],
        "selectorsAdd": "button",
        "style": {
          "background-image": "initial",
          "background-position-x": "initial",
          "background-position-y": "initial",
          "background-size": "initial",
          "background-repeat": "initial",
          "background-attachment": "initial",
          "background-origin": "initial",
          "background-clip": "initial",
          "background-color": "rgb(41, 76, 119)",
          "color": "white"
        }
      }
    ],
    "pages": [
      {
        "frames": [
          {
            "component": {
              "type": "wrapper",
              "stylable": [
                "background",
                "background-color",
                "background-image",
                "background-repeat",
                "background-attachment",
                "background-position",
                "background-size"
              ],
              "components": [
                {
                  "tagName": "form",
                  "attributes": {
                    "id": "solicitud"
                  },
                  "components": [
                    {
                      "tagName": "h2",
                      "type": "text",
                      "attributes": {
                        "id": "idcc"
                      },
                      "components": [
                        {
                          "type": "textnode",
                          "content": "Nueva solicitud"
                        }
                      ]
                    },
                    {
                      "type": "label",
                      "attributes": {
                        "id": "io7s"
                      },
                      "components": [
                        {
                          "type": "textnode",
                          "content": "Nombre"
                        },
                        {
                          "tagName": "input",
                          "type": "campo-solicitud",
                          "void": true,
                          "attributes": {
                            "id": "nombre",
                            "name": "nombre",
                            "type": "text",
                            "placeholder": "Nombre del solicitante",
                            "required": true
                          }
                        }
                      ]
                    },
                    {
                      "type": "label",
                      "attributes": {
                        "id": "inet"
                      },
                      "components": [
                        {
                          "type": "textnode",
                          "content": "Correo"
                        },
                        {
                          "tagName": "input",
                          "type": "campo-solicitud",
                          "void": true,
                          "attributes": {
                            "id": "email",
                            "name": "email",
                            "type": "email",
                            "placeholder": "persona@example.com",
                            "required": true
                          }
                        }
                      ]
                    },
                    {
                      "type": "label",
                      "attributes": {
                        "id": "i4dpl"
                      },
                      "components": [
                        {
                          "type": "textnode",
                          "content": "Asunto"
                        },
                        {
                          "tagName": "input",
                          "type": "campo-solicitud",
                          "void": true,
                          "attributes": {
                            "id": "asunto",
                            "name": "asunto",
                            "type": "text",
                            "placeholder": "Describe brevemente la solicitud",
                            "required": true
                          }
                        }
                      ]
                    },
                    {
                      "type": "label",
                      "attributes": {
                        "id": "iz20b"
                      },
                      "components": [
                        {
                          "type": "textnode",
                          "content": "Prioridad"
                        },
                        {
                          "tagName": "select",
                          "attributes": {
                            "name": "prioridad"
                          },
                          "components": [
                            {
                              "tagName": "option",
                              "type": "text",
                              "components": [
                                {
                                  "type": "textnode",
                                  "content": "Normal"
                                }
                              ]
                            },
                            {
                              "tagName": "option",
                              "type": "text",
                              "components": [
                                {
                                  "type": "textnode",
                                  "content": "Alta"
                                }
                              ]
                            },
                            {
                              "tagName": "option",
                              "type": "text",
                              "components": [
                                {
                                  "type": "textnode",
                                  "content": "Baja"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "label",
                      "attributes": {
                        "id": "isl7v"
                      },
                      "components": [
                        {
                          "type": "textnode",
                          "content": "Detalle"
                        },
                        {
                          "tagName": "textarea",
                          "attributes": {
                            "name": "detalle",
                            "rows": "3"
                          }
                        }
                      ]
                    },
                    {
                      "tagName": "button",
                      "type": "text",
                      "attributes": {
                        "type": "submit",
                        "id": "i6jx5"
                      },
                      "components": [
                        {
                          "type": "textnode",
                          "content": "Guardar solicitud"
                        }
                      ]
                    },
                    {
                      "tagName": "button",
                      "type": "text",
                      "attributes": {
                        "type": "reset",
                        "id": "i0lab"
                      },
                      "components": [
                        {
                          "type": "textnode",
                          "content": "Limpiar"
                        }
                      ]
                    }
                  ]
                }
              ],
              "head": {
                "type": "head"
              },
              "docEl": {
                "tagName": "html"
              }
            },
            "id": "SCTnAID9yEqsndvh"
          }
        ],
        "type": "main",
        "id": "fSDlaR5oGulxqw5x"
      }
    ],
    "symbols": []
  }
}
```
**formulario-generado.css**
```css
* { box-sizing: border-box; } body {margin: 0;}body{font-family:Arial;color:rgb(36, 50, 70);}form{display:grid;row-gap:16px;column-gap:16px;padding-top:24px;padding-right:24px;padding-bottom:24px;padding-left:24px;background-image:initial;background-position-x:initial;background-position-y:initial;background-size:initial;background-repeat:initial;background-attachment:initial;background-origin:initial;background-clip:initial;background-color:rgb(255, 255, 255);}label{display:grid;row-gap:6px;column-gap:6px;}input, select, textarea, button{font-style:inherit;font-variant-ligatures:inherit;font-variant-caps:inherit;font-variant-numeric:inherit;font-variant-east-asian:inherit;font-variant-alternates:inherit;font-variant-position:inherit;font-variant-emoji:inherit;font-weight:inherit;font-stretch:inherit;font-size:inherit;line-height:inherit;font-family:inherit;font-optical-sizing:inherit;font-size-adjust:inherit;font-kerning:inherit;font-feature-settings:inherit;font-variation-settings:inherit;font-language-override:inherit;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;border-top-width:1px;border-right-width:1px;border-bottom-width:1px;border-left-width:1px;border-top-style:solid;border-right-style:solid;border-bottom-style:solid;border-left-style:solid;border-top-color:rgb(116, 132, 153);border-right-color:rgb(116, 132, 153);border-bottom-color:rgb(116, 132, 153);border-left-color:rgb(116, 132, 153);border-image-source:initial;border-image-slice:initial;border-image-width:initial;border-image-outset:initial;border-image-repeat:initial;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;}button{background-image:initial;background-position-x:initial;background-position-y:initial;background-size:initial;background-repeat:initial;background-attachment:initial;background-origin:initial;background-clip:initial;background-color:rgb(41, 76, 119);color:white;}
```
**formulario-generado.html**
```html
<body><form id="solicitud"><h2 id="idcc">Nueva solicitud</h2><label id="io7s">Nombre<input id="nombre" name="nombre" type="text" placeholder="Nombre del solicitante" required/></label><label id="inet">Correo<input id="email" name="email" type="email" placeholder="persona@example.com" required/></label><label id="i4dpl">Asunto<input id="asunto" name="asunto" type="text" placeholder="Describe brevemente la solicitud" required/></label><label id="iz20b">Prioridad<select name="prioridad"><option>Normal</option><option>Alta</option><option>Baja</option></select></label><label id="isl7v">Detalle<textarea name="detalle" rows="3"></textarea></label><button type="submit" id="i6jx5">Guardar solicitud</button><button type="reset" id="i0lab">Limpiar</button></form></body>
```
## docs
**MEMORIA.md**
```markdown
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

La operación la ejecuta una automatización de navegador; no se presenta como una
sesión manual del alumno. `scripts/disenar_formulario.py` deja trazabilidad de
las acciones, y `docs/capturas/editor.png` muestra el resultado en el editor.

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
La publicación remota y la revisión personal del alumno no quedan acreditadas
por la existencia del repositorio local o del informe generado.
```
**OPERACIONES.md**
```markdown
# Operaciones e incidencias — 21/09/2026

1. Revisión de controles, plantillas, eventos y clases de la unidad 1 de clase.
2. Creación de repositorio independiente a partir de la interfaz con objetos;
   sustitución de identidad y datos por una demostración ficticia de solicitudes.
3. Descarga de GrapesJS 0.23.6 en `.runtime/` y configuración de su paleta visual.
4. Creación del formulario mediante los controles del editor, modificación de
   propiedades y exportación de HTML, CSS y modelo JSON.
5. Conservación de la exportación y captura del editor; adaptación de la plantilla
   mediante un script independiente.
6. Integración con la aplicación y asociación de eventos de envío, limpieza,
   búsqueda y navegación. Incorporación de persistencia local y aviso de error.
7. Pruebas en Chromium con Playwright y revisión de captura de la aplicación.
8. Preparación del informe oficial con código, diseño y documentación, excluyendo
   dependencias, entorno virtual y metadatos Git.

## Incidencias reales resueltas

- El primer selector de automatización de propiedades suponía que el editor
  asignaba `name=placeholder` a su entrada. Se inspeccionó el DOM real y se usó el
  contenedor de la propiedad. La operación final sigue siendo una edición visual.
- La casilla nativa del editor estaba oculta bajo un control visual. Se accionó
  la etiqueta visible de la casilla para activar Obligatorio.
- La primera simulación de falta de espacio devolvía una función que Playwright
  ejecutaba inmediatamente. Se envolvió la preparación en una función sin retorno;
  así el error se produce al guardar, como requiere la prueba.
- En la revisión visual, Guardar ocupaba la altura de la fila Detalle. Se asignó
  una fila completa a Detalle en la adaptación y se repitió la prueba.

## Pendiente externo

La credencial GitHub comprobada durante esta sesión es inválida. El proyecto y
su informe quedan en un repositorio local; no se afirma que se hayan publicado.
```
**PROCEDENCIA.md**
```markdown
# Procedencia

Referencia: `jocarsa/tame2627dam2`, unidad 1 de Desarrollo de interfaces,
`009-Clases, propiedades, métodos/005-jocarsa iu con objetos`.

Se conserva su interfaz integrada y las clases de `js/componentes.js` como base.
El primer commit sustituye los datos por una demostración ficticia de solicitudes
y elimina del índice la identidad personal y los recursos gráficos remotos.
Los cambios posteriores añaden el formulario generado visualmente y su lógica.

Caso académico: recepción de solicitudes ficticias para Integra Tech Consulting.
No se conecta con sus sistemas ni se presenta como una versión oficial de jocarsa.
```
**VERIFICACION.md**
```markdown
# Verificación ejecutada — 21/09/2026

La exportación se obtuvo utilizando `scripts/disenar_formulario.py`, con
GrapesJS 0.23.6 y Chromium; se conservaron HTML, CSS, JSON y captura.

## `node --check editor/editor.js`

```text
Código de salida: 0
```

## `node --check public/js/componentes.js`

```text
Código de salida: 0
```

## `node --check public/js/solicitudes.js`

```text
Código de salida: 0
```

## `.venv/bin/python scripts/probar_aplicacion.py`

```text
OK: formulario generado integrado; campos obligatorios bloquean un envío vacío
OK: alta, aviso de éxito y persistencia tras recargar
OK: filtro de búsqueda y resultado vacío
OK: limpiar formulario y volver al listado con Escape
OK: fallo simulado de almacenamiento conserva el formulario y no anuncia éxito
Código de salida: 0
```
```
### capturas
## editor
**editor.js**
```js
// Configuración del editor y paleta de bloques sencillos; no contiene el formulario terminado.
const editor = grapesjs.init({
    container: '#lienzo', height: '100%', storageManager: false,
    panels: {defaults: []}, traitManager: {appendTo: '#traits'},
    canvas: {styles: []},
    plugins: [editor => {
        editor.DomComponents.addType('campo-solicitud', {
            isComponent: elemento => elemento.tagName === 'INPUT',
            model: {defaults: {traits: [
                {type: 'text', name: 'name', label: 'Nombre'},
                {type: 'text', name: 'placeholder', label: 'Ayuda'},
                {type: 'checkbox', name: 'required', label: 'Obligatorio'},
                {type: 'select', name: 'type', label: 'Tipo', options: ['text', 'email']}
            ]}}
        });
    }]
});
editor.setStyle('body{font-family:Arial;color:#243246}form{display:grid;gap:16px;padding:24px;background:#ffffff}label{display:grid;gap:6px}input,select,textarea,button{font:inherit;padding:10px;border:1px solid #748499;border-radius:5px}button{background:#294c77;color:white}');
const bloques = [
    ['formulario', 'Contenedor formulario', '<form id="solicitud"></form>'],
    ['titulo', 'Título', '<h2>Nueva solicitud</h2>'],
    ['nombre', 'Nombre', '<label>Nombre<input id="nombre" name="nombre" type="text"></label>'],
    ['email', 'Correo', '<label>Correo<input id="email" name="email" type="email"></label>'],
    ['asunto', 'Asunto', '<label>Asunto<input id="asunto" name="asunto" type="text"></label>'],
    ['prioridad', 'Prioridad', '<label>Prioridad<select name="prioridad"><option>Normal</option><option>Alta</option><option>Baja</option></select></label>'],
    ['detalle', 'Detalle', '<label>Detalle<textarea name="detalle" rows="3"></textarea></label>'],
    ['guardar', 'Guardar', '<button type="submit">Guardar solicitud</button>'],
    ['limpiar', 'Limpiar', '<button type="reset">Limpiar</button>']
];
for (const [id, etiqueta, contenido] of bloques) {
    editor.BlockManager.add(id, {label: etiqueta, content: contenido});
    const boton = document.createElement('button');
    boton.textContent = etiqueta;
    boton.dataset.bloque = id;
    boton.addEventListener('click', () => {
        const formulario = editor.getWrapper().find('#solicitud')[0];
        if (id === 'formulario' && formulario) return;
        if (id !== 'formulario' && !formulario) {
            document.querySelector('#aviso').textContent = 'Añade primero el contenedor.';
            return;
        }
        const destino = id === 'formulario' ? editor.getWrapper() : formulario;
        const [componente] = destino.append(editor.BlockManager.get(id).get('content'));
        editor.select(componente);
    });
    document.querySelector('#paleta').appendChild(boton);
}
document.querySelector('#subir').addEventListener('click', () => {
    const seleccionado = editor.getSelected();
    if (seleccionado && seleccionado.parent() && seleccionado.index() > 0) {
        seleccionado.move(seleccionado.parent(), {at: seleccionado.index() - 1});
    }
});
document.querySelector('#exportar').addEventListener('click', () => {
    const datos = {versionEditor: '0.23.6', html: editor.getHtml(), css: editor.getCss(), proyecto: editor.getProjectData()};
    const url = URL.createObjectURL(new Blob([JSON.stringify(datos, null, 2)], {type: 'application/json'}));
    const enlace = document.createElement('a');
    enlace.href = url; enlace.download = 'formulario-editor.json'; enlace.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
});
const abrir = document.createElement('button');
abrir.textContent = 'Abrir diseño guardado';
abrir.addEventListener('click', async () => {
    try {
        const respuesta = await fetch('../diseno/formulario-editor.json');
        if (!respuesta.ok) throw new Error('Exportación no disponible');
        const datos = await respuesta.json();
        editor.loadProjectData(datos.proyecto);
        document.querySelector('#aviso').textContent = 'Diseño cargado.';
    } catch (error) {
        document.querySelector('#aviso').textContent = 'No se pudo abrir el diseño guardado.';
    }
});
document.querySelector('aside').appendChild(abrir);
```
**index.html**
```html
<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Diseño visual · jocarsa iu</title>
<link rel="stylesheet" href="../.runtime/grapes.min.css">
<style>body{margin:0;font:14px Arial}header{padding:12px;background:#eef2f6}#zona{display:grid;grid-template-columns:210px 1fr 250px;height:85vh}aside{padding:12px;background:#f5f5f5}button{display:block;margin:7px 0;padding:9px;width:100%}#exportar{display:inline-block;width:auto}#propiedades{background:#444;color:white;padding:10px}#lienzo{min-width:0}</style>
</head><body>
<header><strong>Editor visual GrapesJS · Formulario de solicitudes</strong> <button id="exportar">Exportar proyecto</button><span id="aviso"></span></header>
<div id="zona"><aside><h2>Componentes</h2><div id="paleta"></div><button id="subir">Subir seleccionado</button><p>Selecciona un campo en el lienzo para editar sus propiedades.</p></aside><div id="lienzo"></div><div id="propiedades"><h2>Propiedades</h2><div id="traits"></div></div></div>
<script src="../.runtime/grapes.min.js"></script><script src="editor.js"></script>
</body></html>
```
## public
**index.html**
```html
<!DOCTYPE html>
<html lang="es">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width,initial-scale=1" name="viewport"/>
  <title>
   jocarsa | iu mejorado
  </title>

  <link href="css/estilo.css" rel="stylesheet"/>
 </head>
 <body class="jocarsa-iu">
  <header>
   <div class="corporativo">

    <h1>
     jocarsa | iu mejorado
    </h1>
   </div>
   <div id="herramientas">
    <input aria-label="Buscar solicitudes" id="buscador" placeholder="Buscar solicitudes…" type="search"/>
    <button id="nuevo">
     + Nuevo
    </button>
   </div>
   <div id="usuario">
    <div class="imagen">
    </div>
    <div>
     <p>
      Usuario de demostración
     </p>
     <a href="#formulario" id="abrirFormulario">
      Formulario
     </a>
    </div>
   </div>
  </header>
  <main>
   <nav id="navegacion">
    <div class="titulo-columna">
     Módulos
    </div>
    <div class="contenido-columna">
    </div>
    <button class="minimizar" title="Minimizar">
     ◀
    </button>
   </nav>
   <div class="separador" data-left="navegacion">
   </div>
   <section id="entidades">
    <div class="titulo-columna">
     Vistas
    </div>
    <div class="contenido-columna">
    </div>
    <button class="minimizar" title="Minimizar">
     ◀
    </button>
   </section>
   <div class="separador" data-left="entidades">
   </div>
   <div class="escenario" id="escenario">
   </div>
  </main>
  <template id="tpl-nav">
   <a href="#">
    <span class="ficha">
    </span>
    <span class="etiqueta">
    </span>
   </a>
  </template>
  <template id="tpl-card">
   <article draggable="true">
    <span class="ficha">
    </span>
    <span class="etiqueta">
    </span>
   </article>
  </template>
  <template id="tpl-fila">
   <tr>
   </tr>
  </template>
  <script src="js/solicitudes.js"></script>
  <script src="js/componentes.js">
  </script>
 </body>
</html>

```
### css
**estilo.css**
```css
:root {
  --tono:200;
  --saturacion:50%;
  --brillo:30%;
  --escalon:20%;
  --relleno:12px;
  --texto:12px;
  --chaflan:12px;
  --color0:hsl(var(--tono),var(--saturacion),calc(var(--brillo) - var(--escalon)));
  --color:hsl(var(--tono),var(--saturacion),var(--brillo));
  --color2:hsl(var(--tono),var(--saturacion),calc(var(--brillo) + var(--escalon)));
  --color3:hsl(var(--tono),var(--saturacion),calc(var(--brillo) + var(--escalon)*2));
  --color4:hsl(var(--tono),var(--saturacion),calc(var(--brillo) + var(--escalon)*3));
  --texto-nav:white;
  --ancho-nav:210px;
  --ancho-section:260px
}
* {
  box-sizing:border-box
}
html,body {
  width:100%;
  height:100%;
  margin:0
}
.jocarsa-iu {
  font-family:Ubuntu,Arial,sans-serif;
  font-size:var(--texto);
  display:flex;
  flex-direction:column;
  overflow:hidden;
  background:var(--color3)
}
header {
  height:54px;
  flex:none;
  background:var(--color);
  display:flex;
  align-items:center;
  gap:12px;
  padding:12px;
  color:var(--texto-nav)
}
.corporativo {
  display:flex;
  align-items:center;
  gap:10px;
  flex:1
}
.corporativo img {
  width:28px;
  height:28px
}
.corporativo h1 {
  font-size:20px;
  font-weight:bold;
  margin:0
}
header input,header button {
  border:0;
  padding:8px 10px;
  background:var(--color2);
  color:inherit;
  outline:none
}
header input {
  min-width:260px;
  background:var(--color0)
}
main {
  display:flex;
  flex:1;
  min-height:0
}
nav,section {
  position:relative;
  display:flex;
  flex-direction:column;
  gap:10px;
  padding:12px;
  background:var(--color);
  color:white;
  overflow:hidden;
  flex:none;
  transition:width .25s
}
nav {
  width:var(--ancho-nav)
}
section {
  width:var(--ancho-section);
  background:var(--color2);
  color:#111
}
.titulo-columna {
  font-weight:bold;
  opacity:.75
}
.contenido-columna {
  display:flex;
  flex-direction:column;
  gap:10px;
  overflow:auto;
  min-height:0
}
.contenido-columna a,.contenido-columna article {
  display:flex;
  align-items:center;
  gap:9px;
  padding:9px;
  background:var(--color2);
  color:inherit;
  text-decoration:none;
  cursor:pointer;
  clip-path:polygon(0 0,calc(100% - var(--chaflan)) 0,100% var(--chaflan),100% 100%,0 100%);
  transition:.2s
}
.contenido-columna article {
  background:var(--color3)
}
.contenido-columna .activo {
  transform:translateX(8px);
}
.ficha {
  width:28px;
  height:28px;
  display:grid;
  place-items:center;
  border-radius:50%;
  color:white;
  font-weight:bold;
  flex:none
}
.minimizar {
  position:absolute;
  right:5px;
  bottom:5px;
  border:0;
  width:28px;
  height:28px;
  cursor:pointer
}
.compacto {
  width:58px!important
}
.compacto .titulo-columna,.compacto .etiqueta {
  display:none
}
.compacto .contenido-columna {
  overflow:hidden
}
.separador {
  width:5px;
  cursor:col-resize;
  background:var(--color0);
  flex:none
}
.escenario {
  flex:1;
  min-width:0;
  padding:14px;
  overflow:auto;
  background:var(--color3)
}
table {
  width:100%;
  border-collapse:collapse;
  background:white
}
caption {
  text-align:left;
  padding:12px;
  background:var(--color2);
  font-weight:bold
}
th,td {
  padding:10px;
  border-bottom:1px solid #ddd;
  text-align:left
}
thead {
  background:var(--color)
}
tbody tr:hover {
  background:#f1f1f1
}
.panel {
  background:white;
  padding:16px;
  max-width:1000px
}
.campos {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:12px
}
.campo {
  display:flex;
  flex-direction:column;
  gap:5px
}
.campo input,.campo textarea,.campo select {
  padding:9px;
  border:1px solid #bbb
}
.campo textarea {
  min-height:90px
}
.acciones {
  display:flex;
  gap:8px;
  margin-top:14px
}
.acciones button {
  padding:9px 14px;
  border:0;
  background:var(--color);
  color:white
}
.drag-over {
  outline:3px dashed var(--color0)
}
.estado {
  margin:0 0 10px;
  padding:8px;
  background:rgba(255,255,255,.55)
}
/* =========================================================
   REGLAS 010: SEPARADORES + MENUS CONTRAIDOS
   ========================================================= */
nav,section {
  transition:width .3s ease,flex-basis .3s ease,padding .3s ease
}
.separador {
  flex:0 0 7px;
  width:7px;
  min-width:7px;
  padding:0;
  cursor:col-resize;
  position:relative;
  z-index:4;
  transition:background .3s ease
}
nav + .separador {
  background:var(--color2)
}
section + .separador {
  background:var(--color3)
}
.separador:hover {
  background:var(--color4)
}
body.redimensionando {
  cursor:col-resize;
  user-select:none
}
body.redimensionando * {
  cursor:col-resize!important
}
.minimizar {
  position:absolute;
  bottom:var(--relleno);
  left:var(--relleno);
  right:var(--relleno);
  width:auto;
  height:28px;
  border:0;
  background:var(--color2);
  color:inherit;
  cursor:pointer;
  font:inherit;
  z-index:20;
  transition:left .3s,right .3s,width .3s,background .3s
}
section .minimizar {
  background:var(--color3)
}
.minimizar:hover {
  background:var(--color4)
}
nav.compacto,section.compacto {
  flex-basis:52px!important;
  width:52px!important;
  padding-left:6px;
  padding-right:6px;
  align-items:center
}
nav.compacto .contenido-columna,section.compacto .contenido-columna {
  width:40px;
  overflow:hidden;
  align-items:center
}
nav.compacto .contenido-columna a,section.compacto .contenido-columna article {
  width:40px!important;
  min-width:40px;
  max-width:40px;
  height:40px;
  min-height:40px;
  max-height:40px;
  padding:6px;
  justify-content:center;
  overflow:hidden;
  flex:none;
  transform:none!important
}
nav.compacto .titulo-columna,section.compacto .titulo-columna,nav.compacto .etiqueta,section.compacto .etiqueta {
  display:none
}
nav.compacto .minimizar,section.compacto .minimizar {
  left:6px;
  right:6px;
  width:40px
}
/* =========================================================
   LIBRERIA: FORMULARIOS
   ========================================================= */
.ju-card {
  background:white;
  padding:18px;
  clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,0 100%)
}
.ju-form-grid {
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:16px;
  margin-top:16px
}
.ju-form-full {
  grid-column:1/-1
}
.ju-form-grid label {
  display:flex;
  flex-direction:column;
  gap:8px;
  font-size:14px;
  font-weight:500
}
.ju-form-grid input,.ju-form-grid select,.ju-form-grid textarea {
  width:100%;
  border:1px solid #d8dfeb;
  background:#f8fafc;
  color:#172033;
  padding:12px 14px;
  font:inherit;
  outline:none;
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,0 100%)
}
.ju-form-grid textarea {
  min-height:110px;
  resize:vertical
}
.ju-form-grid input:focus,.ju-form-grid select:focus,.ju-form-grid textarea:focus {
  border-color:var(--color);
  box-shadow:0 0 0 4px color-mix(in srgb,var(--color) 18%,transparent);
  background:white
}
.ju-check {
  display:inline-flex!important;
  flex-direction:row!important;
  align-items:center;
  gap:10px!important
}
.ju-check input {
  width:18px!important;
  height:18px;
  clip-path:none!important
}
.ju-btn {
  border:0;
  padding:11px 16px;
  background:var(--color);
  color:white;
  cursor:pointer;
  font:inherit;
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,0 100%)
}
.ju-btn.secondary {
  background:var(--color2);
  color:#111
}
.ju-button-row {
  display:flex;
  gap:10px;
  flex-wrap:wrap;
  margin-top:16px
}
/* LOGIN jocarsa-iu */
.ju-login-page {
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  background:radial-gradient(circle at top left,var(--color4),transparent 35%),linear-gradient(180deg,var(--color3),var(--color4));
  padding:30px
}
.ju-login-layout {
  width:min(920px,100%);
  display:grid;
  grid-template-columns:minmax(280px,400px) minmax(320px,520px);
  gap:24px
}
.ju-login-side,.ju-login-card {
  padding:28px;
  clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,0 100%)
}
.ju-login-side {
  background:linear-gradient(180deg,var(--color0),var(--color));
  color:white;
  display:flex;
  flex-direction:column;
  justify-content:center
}
.ju-login-card {
  background:white
}
.ju-login-brand {
  text-align:center
}
.ju-login-brand img {
  width:72px;
  height:72px
}
.ju-login-product-title {
  font-size:28px;
  margin:12px 0 6px
}
.ju-login-card h2 {
  margin-top:0
}
.ju-login-actions {
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:14px
}
.ju-text-link {
  color:var(--color);
  font-weight:bold;
  text-decoration:none
}
/* TOASTS jocarsa-iu */
.ju-toast-stack {
  position:fixed;
  right:22px;
  bottom:22px;
  z-index:1000;
  width:min(420px,calc(100vw - 44px));
  display:flex;
  flex-direction:column;
  gap:12px;
  pointer-events:none
}
.ju-toast {
  pointer-events:auto;
  position:relative;
  display:grid;
  grid-template-columns:42px 1fr auto;
  gap:12px;
  align-items:start;
  padding:14px;
  background:rgba(255,255,255,.97);
  box-shadow:0 18px 38px rgba(0,0,0,.14);
  clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,0 100%);
  transform:translateX(22px);
  opacity:0;
  animation:juToastIn .28s ease forwards
}
.ju-toast:before {
  content:"";
  position:absolute;
  left:0;
  top:0;
  bottom:0;
  width:7px;
  background:#3b82f6
}
.ju-toast.is-success:before {
  background:#22c55e
}
.ju-toast.is-warning:before {
  background:#f59e0b
}
.ju-toast.is-danger:before {
  background:#ef4444
}
.ju-toast-icon {
  width:42px;
  height:42px;
  display:grid;
  place-items:center;
  background:var(--color3);
  font-weight:800
}
.ju-toast-title {
  margin:0 0 3px;
  font-weight:800
}
.ju-toast-text {
  margin:0;
  color:#667085;
  font-size:13px
}
.ju-toast-close {
  border:0;
  background:transparent;
  font-size:20px;
  cursor:pointer
}
.ju-toast.is-leaving {
  animation:juToastOut .22s ease forwards
}
@keyframes juToastIn {
  to {
    transform:translateX(0);
    opacity:1
  }
}
@keyframes juToastOut {
  to {
    transform:translateX(24px);
    opacity:0
  }
}
@media(max-width:800px) {
  .ju-form-grid,.ju-login-layout {
    grid-template-columns:1fr
  }
}
/* =========================================================
   V3 · AJUSTES DE COHERENCIA JOCARSA-IU
   ========================================================= */
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400;500;700&display=swap');
html,body,button,input,select,textarea {
  font-family:Ubuntu,Arial,sans-serif
}
/* Las cajas de ambas columnas quedan centradas dentro de su menú. */
nav .contenido-columna,section .contenido-columna {
  align-items:center;
  width:100%
}
nav .contenido-columna>a,section .contenido-columna>article {
  width:100%;
  margin-left:auto;
  margin-right:auto
}
nav.compacto .contenido-columna,section.compacto .contenido-columna {
  margin-left:auto;
  margin-right:auto
}
/* Login: composición centrada y fondo de proyecto. jocarsa.png vive en la raíz. */
.ju-login-page {
  position:relative;
  isolation:isolate;
  min-height:100vh;
  margin:0;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:40px 20px;
  background-image:linear-gradient(rgba(215,230,227,.72),rgba(215,230,227,.72)),url('../jocarsa.png');
  background-size:cover;
  background-position:center;
  background-repeat:no-repeat;
}
.ju-login-layout {
  width:min(980px,100%);
  margin:auto;
  align-items:stretch
}
.ju-login-side,.ju-login-card {
  min-height:450px
}
.ju-login-card {
  display:flex;
  flex-direction:column;
  justify-content:center
}
.ju-login-brand {
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  text-align:center
}
/* Páginas de demostración de la librería */
.ju-demo-page {
  min-height:100vh;
  overflow:auto;
  background:var(--color3);
  color:#172033
}
.ju-demo-header {
  min-height:64px;
  background:var(--color);
  color:white;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:16px;
  padding:12px 20px
}
.ju-demo-header h1 {
  margin:0;
  font-size:20px;
  font-weight:500
}
.ju-demo-header p {
  margin:3px 0 0;
  opacity:.75
}
.ju-demo-header nav {
  width:auto!important;
  background:transparent;
  padding:0;
  display:flex;
  flex-direction:row;
  gap:8px;
  overflow:visible
}
.ju-demo-header a {
  color:white;
  text-decoration:none;
  padding:10px 14px;
  background:var(--color2);
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,0 100%)
}
.ju-demo-main {
  width:min(1100px,calc(100% - 40px));
  margin:32px auto;
  display:grid;
  gap:20px
}
.ju-demo-grid {
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:20px
}
.ju-demo-page .ju-card h2,.ju-demo-page .ju-card h3 {
  margin-top:0
}
.ju-fieldset {
  border:1px solid #e2e8f0;
  background:#f8fafc;
  padding:16px;
  display:flex;
  flex-direction:column;
  gap:12px
}
.ju-check-group {
  display:flex;
  gap:18px;
  flex-wrap:wrap
}
@media(max-width:800px) {
  .ju-demo-grid {
    grid-template-columns:1fr
  }
  .ju-demo-header {
    align-items:flex-start;
    flex-direction:column
  }
  .ju-demo-header nav {
    flex-wrap:wrap
  }
}
/* =========================================================
   V4 · fidelidad jocarsa-iu 010
   ========================================================= */
/* Header completo: corporativo / herramientas / usuario */
header .corporativo {
  flex:1
}
header #herramientas {
  display:flex;
  gap:var(--relleno);
  align-items:center;
  justify-content:center;
  flex:2;
  height:100%
}
header #usuario {
  display:flex;
  align-items:center;
  justify-content:flex-end;
  gap:var(--relleno);
  flex:1;
  height:100%
}
header #usuario .imagen {
  width:28px;
  height:28px;
  background:var(--color2);
  border-radius:100px;
  flex:none
}
header #usuario>div:last-child {
  display:flex;
  align-items:center;
  gap:var(--relleno);
  flex:none
}
header #usuario p {
  margin:0;
  white-space:nowrap
}
header #usuario a {
  background:var(--color2);
  border:0;
  padding:calc(var(--relleno)/2);
  height:28px;
  display:flex;
  align-items:center;
  color:var(--texto-nav);
  text-decoration:none;
  font:inherit
}
/* Las fichas de letra son cuadrados achaflanados, nunca círculos */
.ficha {
  border-radius:0!important;
  clip-path:polygon(0 0,calc(100% - 7px) 0,100% 7px,100% 100%,0 100%)
}
/* El destacado atraviesa visualmente el separador, sin provocar scroll horizontal. */
nav {
  overflow:visible!important;
  z-index:3
}
nav .contenido-columna {
  overflow-y:auto;
  overflow-x:visible;
  padding-right:0
}
section {
  overflow:visible!important;
  z-index:2
}
section .contenido-columna {
  overflow-y:auto;
  overflow-x:visible;
  padding-right:0
}
.contenido-columna .activo {
  transform:none
}
#navegacion .contenido-columna a,#entidades .contenido-columna article {
  width:100%;
  height:40px;
  flex:none;
  transition:width .3s ease,background .3s ease
}
#navegacion .contenido-columna a:hover,#entidades .contenido-columna article:hover {
  width:calc(100% + var(--relleno)*.9)
}
#navegacion .contenido-columna a.activo,#entidades .contenido-columna article.activo {
  width:calc(100% + var(--relleno)*2);
  position:relative;
  z-index:10
}
nav.compacto .contenido-columna a:hover,nav.compacto .contenido-columna a.activo,section.compacto .contenido-columna article:hover,section.compacto .contenido-columna article.activo {
  width:40px!important
}
/* Login realmente centrado + fondo jocarsa.png de la raíz */
body.ju-login-page {
  width:100%;
  height:100vh;
  min-height:100vh;
  margin:0;
  display:grid!important;
  place-items:center;
  overflow:auto;
  padding:30px;
  background:linear-gradient(rgba(235,244,243,.72),rgba(235,244,243,.72)),url('../jocarsa.png') center center/cover no-repeat fixed
}
body.ju-login-page main.ju-login-layout {
  flex:none!important;
  min-height:0!important;
  margin:0!important;
  width:min(920px,calc(100vw - 60px));
  align-self:center;
  justify-self:center
}
/* Páginas de demostración: mismo esqueleto de dos menús + escenario */
body.ju-library-page {
  font-family:Ubuntu,Arial,sans-serif;
  font-size:var(--texto);
  display:flex;
  flex-direction:column;
  overflow:hidden;
  background:var(--color3)
}
body.ju-library-page main {
  display:flex;
  flex:1;
  min-height:0;
  overflow:hidden
}
body.ju-library-page .library-nav {
  width:var(--ancho-nav);
  flex:0 0 var(--ancho-nav);
  background:var(--color);
  color:white;
  padding:12px;
  position:relative;
  overflow:visible;
  display:flex;
  flex-direction:column;
  gap:10px
}
body.ju-library-page .library-section {
  width:var(--ancho-section);
  flex:0 0 var(--ancho-section);
  background:var(--color2);
  color:#111;
  padding:12px 12px 12px 3px;
  position:relative;
  overflow:visible;
  display:flex;
  flex-direction:column;
  gap:10px
}
body.ju-library-page .library-nav .contenido-columna,body.ju-library-page .library-section .contenido-columna {
  overflow-y:auto;
  overflow-x:visible
}
body.ju-library-page .library-nav a,body.ju-library-page .library-section a {
  height:40px;
  flex:none;
  display:flex;
  align-items:center;
  gap:9px;
  padding:6px;
  background:var(--color2);
  color:inherit;
  text-decoration:none;
  clip-path:polygon(0 0,calc(100% - var(--chaflan)) 0,100% var(--chaflan),100% 100%,0 100%)
}
body.ju-library-page .library-section a {
  background:var(--color3)
}
body.ju-library-page .library-nav a.activo,body.ju-library-page .library-section a.activo {
  width:calc(100% + var(--relleno)*2);
  position:relative;
  z-index:10
}
body.ju-library-page .library-stage {
  flex:1;
  min-width:0;
  padding:14px;
  overflow:auto;
  background:var(--color3)
}
body.ju-library-page .library-stage>.ju-card {
  max-width:1100px
}
/* =========================================================
   V5 · continuidad entre columnas sin scroll horizontal
   ========================================================= */
/*
  No usamos un contenedor scrollable alrededor de las fichas: cuando un
  elemento activo es más ancho que su columna, overflow:auto convierte el
  desbordamiento horizontal en una barra de scroll. En jocarsa-iu el
  destacado debe poder atravesar el límite de la columna y cubrir el
  separador visualmente.
*/
.jocarsa-iu nav .contenido-columna, .jocarsa-iu section .contenido-columna, body.ju-library-page .library-nav .contenido-columna, body.ju-library-page .library-section .contenido-columna {
  overflow:visible !important;
  width:100%;
  min-width:0;
  align-items:stretch;
}
/* Las fichas normales ocupan siempre todo el ancho útil de su columna. */
.jocarsa-iu nav .contenido-columna > a, .jocarsa-iu section .contenido-columna > article, body.ju-library-page .library-nav .contenido-columna > a, body.ju-library-page .library-section .contenido-columna > a {
  width:100%;
  max-width:none;
  margin:0;
  flex:0 0 40px;
}
/* Hover y selección continúan físicamente hacia la columna siguiente. */
.jocarsa-iu nav .contenido-columna > a:hover, .jocarsa-iu section .contenido-columna > article:hover, body.ju-library-page .library-nav .contenido-columna > a:hover, body.ju-library-page .library-section .contenido-columna > a:hover {
  width:calc(100% + (var(--relleno) * .9));
  position:relative;
  z-index:9;
}
.jocarsa-iu nav .contenido-columna > a.activo, .jocarsa-iu section .contenido-columna > article.activo, body.ju-library-page .library-nav .contenido-columna > a.activo, body.ju-library-page .library-section .contenido-columna > a.activo {
  width:calc(100% + (var(--relleno) * 2));
  position:relative;
  z-index:10;
}
/* El separador queda por debajo del destacado, como en 010. */
.jocarsa-iu main .separador, body.ju-library-page main .separador {
  z-index:4
}
.jocarsa-iu nav, body.ju-library-page .library-nav {
  z-index:6
}
.jocarsa-iu section, body.ju-library-page .library-section {
  z-index:5
}
/* La columna central de las demos conserva exactamente la misma geometría
   que la columna central de index.html. */
body.ju-library-page .library-section {
  padding:var(--relleno);
  padding-left:3px;
}
body.ju-library-page .library-section .contenido-columna > a {
  padding:calc(var(--relleno) / 2);
  height:40px;
  min-height:40px;
  display:flex;
  align-items:center;
  justify-content:flex-start;
  gap:calc(var(--relleno) / 2);
  background:var(--color3);
}
/* Contraído: anula expresamente cualquier crecimiento por hover/activo. */
.jocarsa-iu nav.compacto .contenido-columna, .jocarsa-iu section.compacto .contenido-columna {
  width:40px;
  align-items:center;
}
.jocarsa-iu nav.compacto .contenido-columna > a, .jocarsa-iu nav.compacto .contenido-columna > a:hover, .jocarsa-iu nav.compacto .contenido-columna > a.activo, .jocarsa-iu section.compacto .contenido-columna > article, .jocarsa-iu section.compacto .contenido-columna > article:hover, .jocarsa-iu section.compacto .contenido-columna > article.activo {
  width:40px !important;
  min-width:40px;
  max-width:40px;
}

/* Adaptación del formulario exportado: alcance limitado a esta vista. */
#solicitud { width: min(100%, 850px); margin: 0 auto; padding: 24px; background: white; border-radius: 10px; align-content: start; }
#solicitud label { display: grid; gap: 6px; }
#solicitud input, #solicitud select, #solicitud textarea { width: 100%; min-width: 0; padding: 10px; font: inherit; }
#solicitud h2 { margin: 0; }
#solicitud button { min-height: 44px; }
#estadoFormulario { min-height: 1.5em; }
:focus-visible { outline: 3px solid #d58218; outline-offset: 2px; }
@media (max-width: 700px) {
  body.jocarsa-iu > header { height: auto; flex-wrap: wrap; gap: 10px; }
  #usuario, #entidades, .separador { display: none; }
  #navegacion { width: 110px; flex-basis: 110px; }
  #solicitud { display: grid; grid-template-columns: 1fr; padding: 12px; }
}
```
### data
**clientes.json**
```json
{
  "titulo": "Solicitudes de demostración",
  "columnas": [
    {
      "campo": "nombre",
      "etiqueta": "Nombre"
    },
    {
      "campo": "email",
      "etiqueta": "Correo"
    },
    {
      "campo": "asunto",
      "etiqueta": "Asunto"
    },
    {
      "campo": "prioridad",
      "etiqueta": "Prioridad"
    }
  ],
  "registros": [
    {
      "nombre": "Equipo Demo",
      "email": "demo@example.com",
      "asunto": "Preparar equipo de prueba",
      "prioridad": "Normal"
    }
  ]
}
```
**datos.json**
```json
{
  "campos": [
    {
      "nombre": "id",
      "etiqueta": "ID",
      "tipo": "number"
    },
    {
      "nombre": "nombre",
      "etiqueta": "Nombre",
      "tipo": "text"
    },
    {
      "nombre": "apellidos",
      "etiqueta": "Apellidos",
      "tipo": "text"
    },
    {
      "nombre": "email",
      "etiqueta": "Correo electrónico",
      "tipo": "email"
    },
    {
      "nombre": "telefono",
      "etiqueta": "Teléfono",
      "tipo": "tel"
    },
    {
      "nombre": "fecha_nacimiento",
      "etiqueta": "Fecha de nacimiento",
      "tipo": "date"
    },
    {
      "nombre": "numero_empleados",
      "etiqueta": "Número de empleados",
      "tipo": "number"
    },
    {
      "nombre": "facturacion",
      "etiqueta": "Facturación anual",
      "tipo": "number"
    },
    {
      "nombre": "web",
      "etiqueta": "Página web",
      "tipo": "url"
    },
    {
      "nombre": "tipo_cliente",
      "etiqueta": "Tipo de cliente",
      "tipo": "select",
      "opciones": [
        "Particular",
        "Autónomo",
        "Empresa",
        "Administración"
      ]
    },
    {
      "nombre": "activo",
      "etiqueta": "Cliente activo",
      "tipo": "checkbox"
    },
    {
      "nombre": "observaciones",
      "etiqueta": "Observaciones",
      "tipo": "textarea"
    }
  ],
  "datos": [
    {
      "id": 1,
      "nombre": "Laura",
      "apellidos": "Martínez García",
      "email": "laura.martinez@example.com",
      "telefono": "612345678",
      "fecha_nacimiento": "1987-04-12",
      "numero_empleados": 1,
      "facturacion": 42000,
      "web": "https://example.com/laura",
      "tipo_cliente": "Autónomo",
      "activo": true,
      "observaciones": "Cliente desde 2023."
    },
    {
      "id": 2,
      "nombre": "Carlos",
      "apellidos": "Sánchez López",
      "email": "carlos.sanchez@example.com",
      "telefono": "623456789",
      "fecha_nacimiento": "1979-11-03",
      "numero_empleados": 18,
      "facturacion": 380000,
      "web": "https://example.com/carlos",
      "tipo_cliente": "Empresa",
      "activo": true,
      "observaciones": "Interesado en servicios de desarrollo."
    },
    {
      "id": 3,
      "nombre": "Marta",
      "apellidos": "Ruiz Navarro",
      "email": "marta.ruiz@example.com",
      "telefono": "634567890",
      "fecha_nacimiento": "1992-07-21",
      "numero_empleados": 1,
      "facturacion": 31500,
      "web": "https://example.com/marta",
      "tipo_cliente": "Particular",
      "activo": false,
      "observaciones": "Actualmente sin proyectos activos."
    },
    {
      "id": 4,
      "nombre": "Javier",
      "apellidos": "Torres Romero",
      "email": "javier.torres@example.com",
      "telefono": "645678901",
      "fecha_nacimiento": "1984-02-15",
      "numero_empleados": 42,
      "facturacion": 920000,
      "web": "https://example.com/javier",
      "tipo_cliente": "Empresa",
      "activo": true,
      "observaciones": "Solicita mantenimiento periódico."
    },
    {
      "id": 5,
      "nombre": "Ana",
      "apellidos": "Gómez Pérez",
      "email": "ana.gomez@example.com",
      "telefono": "656789012",
      "fecha_nacimiento": "1990-09-28",
      "numero_empleados": 6,
      "facturacion": 125000,
      "web": "https://example.com/ana",
      "tipo_cliente": "Autónomo",
      "activo": true,
      "observaciones": "Contacto preferente por correo electrónico."
    }
  ]
}
```
**entidades.json**
```json
[
  {
    "texto": "Listado"
  },
  {
    "texto": "Formulario"
  },
  {
    "texto": "Toasts"
  }
]
```
**menu.json**
```json
[
  {
    "texto": "Solicitudes",
    "activo": true
  }
]
```
### js
**componentes.js**
```js
/**
 * jocarsa | iu
 * Control principal de la interfaz mediante programación orientada a objetos.
 *
 * Nota sobre el namespace:
 * JavaScript no admite "|" dentro de un identificador. Por ello el namespace
 * técnico equivalente es `jocarsa.iu`.
 */
window.jocarsa = window.jocarsa || {};
window.jocarsa.iu = window.jocarsa.iu || {};

(() => {
  "use strict";

  class DOM {
    static uno(selector, contexto = document) {
      return contexto.querySelector(selector);
    }

    static todos(selector, contexto = document) {
      return [...contexto.querySelectorAll(selector)];
    }
  }

  class Utilidades {
    static hashTexto(texto) {
      let hash = 0;

      for (const caracter of texto) {
        hash = caracter.charCodeAt(0) + ((hash << 5) - hash);
      }

      return Math.abs(hash);
    }

    static colorTexto(texto) {
      return `hsl(${Utilidades.hashTexto(texto) % 360},55%,45%)`;
    }
  }

  class OrigenDatos {
    static async cargarJSON(url) {
      const respuesta = await fetch(url);

      if (!respuesta.ok) {
        throw new Error(url);
      }

      return respuesta.json();
    }
  }

  class EstadoIU {
    constructor() {
      this.menu = [];
      this.entidades = [];
      this.clientes = null;
      this.formulario = null;
      this.seleccion = "Listado";
    }
  }

  class FichaIU {
    static completar(elemento, texto) {
      const ficha = DOM.uno(".ficha", elemento);
      const etiqueta = DOM.uno(".etiqueta", elemento);

      ficha.textContent = texto.charAt(0).toUpperCase();
      ficha.style.background = Utilidades.colorTexto(texto);
      etiqueta.textContent = texto;
    }
  }

  class ToastIU {
    constructor(selectorPila = "#toastStack") {
      this.selectorPila = selectorPila;
      this.iconos = {
        success: "✓",
        info: "i",
        warning: "!",
        danger: "×"
      };
    }

    obtenerPila() {
      let pila = DOM.uno(this.selectorPila);

      if (!pila) {
        pila = document.createElement("div");
        pila.id = this.selectorPila.replace(/^#/, "");
        pila.className = "ju-toast-stack";
        document.body.appendChild(pila);
      }

      return pila;
    }

    mostrar(tipo = "info", titulo = "Información", texto = "Operación realizada") {
      const pila = this.obtenerPila();
      const toast = document.createElement("article");

      toast.className = `ju-toast is-${tipo}`;
      toast.setAttribute("role", "status");
      toast.innerHTML = `
        <div class="ju-toast-icon">${this.iconos[tipo] || "i"}</div>
        <div>
          <p class="ju-toast-title"></p>
          <p class="ju-toast-text"></p>
        </div>
        <button class="ju-toast-close" type="button" aria-label="Cerrar aviso">×</button>
      `;

      DOM.uno(".ju-toast-title", toast).textContent = titulo;
      DOM.uno(".ju-toast-text", toast).textContent = texto;
      const cerrar = () => {
        toast.classList.add("is-leaving");
        setTimeout(() => toast.remove(), 240);
      };

      DOM.uno("button", toast).addEventListener("click", cerrar);
      pila.appendChild(toast);
      setTimeout(cerrar, 5000);
    }
  }

  class GestorColumnas {
    constructor() {
      this.anchoMinimo = 100;
      this.anchoMaximo = 600;
    }

    activar() {
      this.activarMinimizacion();
      this.activarSeparadores();
    }

    activarMinimizacion() {
      DOM.todos(".minimizar").forEach((boton) => {
        const columna = boton.closest("nav,section");
        columna.dataset.ancho = columna.getBoundingClientRect().width;

        boton.addEventListener("click", () => {
          this.alternarColumna(columna, boton);
        });
      });
    }

    alternarColumna(columna, boton) {
      if (columna.classList.contains("compacto")) {
        const ancho = parseFloat(columna.dataset.ancho) || 250;

        columna.classList.remove("compacto");
        columna.style.flexBasis = `${ancho}px`;
        columna.style.width = `${ancho}px`;
        boton.textContent = "◀";
        return;
      }

      columna.dataset.ancho = columna.getBoundingClientRect().width;
      columna.style.flexBasis = `${columna.dataset.ancho}px`;
      columna.style.width = `${columna.dataset.ancho}px`;

      void columna.offsetWidth;

      columna.classList.add("compacto");
      boton.textContent = "▶";
    }

    activarSeparadores() {
      DOM.todos(".separador").forEach((separador) => {
        separador.addEventListener("pointerdown", (evento) => {
          this.iniciarRedimension(separador, evento);
        });
      });
    }

    iniciarRedimension(separador, evento) {
      evento.preventDefault();

      const columna = separador.previousElementSibling;

      if (!columna || columna.classList.contains("compacto")) {
        return;
      }

      const inicio = evento.clientX;
      const anchoInicial = columna.getBoundingClientRect().width;

      columna.style.transition = "none";
      document.body.classList.add("redimensionando");
      separador.setPointerCapture(evento.pointerId);

      const mover = (eventoMovimiento) => {
        const ancho = Math.min(
          this.anchoMaximo,
          Math.max(this.anchoMinimo, anchoInicial + eventoMovimiento.clientX - inicio)
        );

        columna.style.width = `${ancho}px`;
        columna.style.flexBasis = `${ancho}px`;
        columna.dataset.ancho = ancho;
      };

      const terminar = () => {
        separador.removeEventListener("pointermove", mover);
        columna.style.transition = "";
        document.body.classList.remove("redimensionando");
      };

      separador.addEventListener("pointermove", mover);
      separador.addEventListener("pointerup", terminar, { once: true });
      separador.addEventListener("pointercancel", terminar, { once: true });
    }
  }

  class AplicacionIU {
    constructor() {
      this.estado = new EstadoIU();
      this.toast = new ToastIU();
      this.columnas = new GestorColumnas();
      this.almacen = new window.jocarsa.iu.AlmacenSolicitudes();
      this.cambioVista = 0;
    }

    async iniciar() {
      try {
        [
          this.estado.menu,
          this.estado.entidades,
          this.estado.clientes,
          this.estado.formulario
        ] = await Promise.all([
          OrigenDatos.cargarJSON("data/menu.json"),
          OrigenDatos.cargarJSON("data/entidades.json"),
          OrigenDatos.cargarJSON("data/clientes.json"),
          OrigenDatos.cargarJSON("data/datos.json")
        ]);

        try {
          this.estado.clientes.registros = this.almacen.cargar(this.estado.clientes.registros);
        } catch (error) {
          this.toast.mostrar("warning", "Almacenamiento local", "No se pudo leer el almacenamiento. Se muestran datos de demostración.");
        }
        this.renderMenu();
        this.renderEntidades();
        this.mostrarTabla();
        this.columnas.activar();
        this.activarEventos();
      } catch (error) {
        DOM.uno("#escenario").innerHTML = `
          <div class="panel">
            <h2>No se pudieron cargar los orígenes de datos</h2>
            <p>Sirve esta carpeta mediante HTTP, por ejemplo: <code>python3 -m http.server 8000</code></p>
            <pre>${error}</pre>
          </div>
        `;
      }
    }

    renderMenu() {
      const contenedor = DOM.uno("#navegacion .contenido-columna");
      contenedor.innerHTML = "";

      this.estado.menu.forEach((elemento, indice) => {
        const nodo = DOM.uno("#tpl-nav").content.cloneNode(true);
        const enlace = DOM.uno("a", nodo);

        FichaIU.completar(enlace, elemento.texto);
        enlace.classList.toggle("activo", Boolean(elemento.activo));
        enlace.dataset.indice = indice;

        enlace.addEventListener("click", (evento) => {
          evento.preventDefault();
          DOM.todos("#navegacion a").forEach((item) => item.classList.remove("activo"));
          enlace.classList.add("activo");
          this.mostrarTabla();
        });

        contenedor.appendChild(nodo);
      });
    }

    renderEntidades() {
      const contenedor = DOM.uno("#entidades .contenido-columna");
      contenedor.innerHTML = "";

      this.estado.entidades.forEach((elemento, indice) => {
        const nodo = DOM.uno("#tpl-card").content.cloneNode(true);
        const articulo = DOM.uno("article", nodo);

        FichaIU.completar(articulo, elemento.texto);
        articulo.classList.toggle("activo", elemento.texto === this.estado.seleccion);
        articulo.dataset.indice = indice;

        articulo.addEventListener("click", () => {
          this.estado.seleccion = elemento.texto;
          this.renderEntidades();
          this.mostrarVista(elemento.texto);
        });

        articulo.addEventListener("dragstart", (evento) => {
          evento.dataTransfer.setData("text/plain", elemento.texto);
        });

        contenedor.appendChild(nodo);
      });
    }

    mostrarVista(vista) {
      if (vista === "Elemento" || vista === "Formulario") {
        this.mostrarFormularioUI();
      } else if (vista === "Login") {
        this.mostrarLoginDemo();
      } else if (vista === "Toasts") {
        this.mostrarToastsDemo();
      } else {
        this.mostrarTabla();
      }
    }

    mostrarTabla(filtro = "") {
      this.cambioVista++;
      const datos = this.estado.clientes;
      const registros = datos.registros.filter((registro) =>
        Object.values(registro)
          .join(" ")
          .toLowerCase()
          .includes(filtro.toLowerCase())
      );
      const escenario = DOM.uno("#escenario");
      const tabla = document.createElement("table");

      escenario.innerHTML = "";
      tabla.innerHTML = `
        <caption>${datos.titulo}</caption>
        <thead>
          <tr>${datos.columnas.map((columna) => `<th>${columna.etiqueta}</th>`).join("")}</tr>
        </thead>
        <tbody></tbody>
        <tfoot>
          <tr>
            <th colspan="${Math.max(1, datos.columnas.length - 1)}">Total</th>
            <td>${registros.length}</td>
          </tr>
        </tfoot>
      `;

      const cuerpo = DOM.uno("tbody", tabla);

      registros.forEach((registro) => {
        const fila = DOM.uno("#tpl-fila").content.cloneNode(true).querySelector("tr");

        datos.columnas.forEach((columna) => {
          const celda = document.createElement("td");
          celda.textContent = registro[columna.campo] ?? "";
          fila.appendChild(celda);
        });

        cuerpo.appendChild(fila);
      });

      escenario.appendChild(tabla);
    }

    async mostrarFormularioUI() {
      const turno = ++this.cambioVista;
      const escenario = DOM.uno("#escenario");
      escenario.textContent = "Cargando formulario…";
      try {
        const respuesta = await fetch("templates/formulario-solicitud.html");
        if (!respuesta.ok) throw new Error("No se pudo cargar la plantilla");
        const html = await respuesta.text();
        if (turno !== this.cambioVista) return;
        escenario.innerHTML = html;
        const formulario = DOM.uno("#solicitud");
        const mensaje = DOM.uno("#estadoFormulario");
        formulario.addEventListener("submit", (evento) => {
          evento.preventDefault();
          if (!formulario.reportValidity()) return;
          const registro = Object.fromEntries(new FormData(formulario));
          for (const campo of Object.keys(registro)) registro[campo] = registro[campo].trim();
          if (!registro.nombre || !registro.email || !registro.asunto) {
            mensaje.textContent = "Nombre, correo y asunto no pueden estar vacíos.";
            return;
          }
          const nuevos = [...this.estado.clientes.registros, registro];
          try {
            this.almacen.guardar(nuevos);
          } catch (error) {
            mensaje.textContent = "No se pudo guardar en este navegador. Los datos siguen en el formulario.";
            this.toast.mostrar("danger", "No guardado", "Comprueba el almacenamiento del navegador.");
            return;
          }
          this.estado.clientes.registros = nuevos;
          this.estado.seleccion = "Listado";
          DOM.uno("#buscador").value = "";
          this.renderEntidades();
          this.mostrarTabla();
          this.toast.mostrar("success", "Solicitud guardada", "La solicitud se ha guardado en este navegador.");
        });
        formulario.addEventListener("reset", () => { mensaje.textContent = "Formulario limpiado."; });
        DOM.uno("#nombre").focus();
      } catch (error) {
        if (turno === this.cambioVista) escenario.textContent = "No se pudo cargar el formulario. Inténtalo de nuevo.";
      }
    }

    mostrarLoginDemo() {
      this.cambioVista++;
      const escenario = DOM.uno("#escenario");

      escenario.innerHTML = `
        <div class="ju-login-layout" style="margin:auto">
          <article class="ju-login-side">
            <div class="ju-login-brand">
              <img src="https://static.jocarsa.com/logos/white.svg" alt="">
              <h1 class="ju-login-product-title">jocarsa | interfaz integrada</h1>
              <p>Pantalla de acceso basada en jocarsa-iu.</p>
            </div>
          </article>
          <article class="ju-login-card">
            <h2>Iniciar sesión</h2>
            <form id="loginDemo" class="ju-form-grid">
              <label class="ju-form-full">
                <span>Email</span>
                <input type="email" required>
              </label>
              <label class="ju-form-full">
                <span>Contraseña</span>
                <input type="password" required>
              </label>
              <label class="ju-check ju-form-full">
                <input type="checkbox">
                <span>Mantener sesión</span>
              </label>
              <div class="ju-form-full ju-login-actions">
                <button class="ju-btn">Entrar</button>
                <a class="ju-text-link" href="login.html">Abrir pantalla completa</a>
              </div>
            </form>
          </article>
        </div>
      `;

      DOM.uno("#loginDemo").addEventListener("submit", (evento) => {
        evento.preventDefault();
        this.toast.mostrar(
          "success",
          "Acceso simulado",
          "Login capturado como componente reutilizable."
        );
      });
    }

    mostrarToastsDemo() {
      this.cambioVista++;
      const escenario = DOM.uno("#escenario");

      escenario.innerHTML = `
        <article class="ju-card">
          <h2>Librería · Toasts</h2>
          <p>Mensajes emergentes reutilizables con autocierre y cierre manual.</p>
          <div class="ju-button-row">
            <button class="ju-btn" data-t="success">Éxito</button>
            <button class="ju-btn secondary" data-t="info">Información</button>
            <button class="ju-btn secondary" data-t="warning">Aviso</button>
            <button class="ju-btn secondary" data-t="danger">Error</button>
          </div>
        </article>
      `;

      const titulos = {
        success: "Correcto",
        info: "Información",
        warning: "Revisar",
        danger: "Error"
      };

      DOM.todos("[data-t]", escenario).forEach((boton) => {
        boton.addEventListener("click", () => {
          this.toast.mostrar(
            boton.dataset.t,
            titulos[boton.dataset.t],
            "Ejemplo de mensaje emergente de la librería."
          );
        });
      });
    }

    activarEventos() {
      DOM.uno("#abrirFormulario").addEventListener("click", evento => {
        evento.preventDefault();
        this.mostrarFormularioUI();
      });
      DOM.uno("#buscador").addEventListener("input", (evento) => {
        this.mostrarTabla(evento.target.value);
      });

      DOM.uno("#nuevo").addEventListener("click", () => {
        this.estado.seleccion = "Formulario";
        this.renderEntidades();
        this.mostrarFormularioUI();
      });

      const escenario = DOM.uno("#escenario");

      escenario.addEventListener("dragover", (evento) => {
        evento.preventDefault();
        escenario.classList.add("drag-over");
      });

      escenario.addEventListener("dragleave", () => {
        escenario.classList.remove("drag-over");
      });

      escenario.addEventListener("drop", (evento) => {
        evento.preventDefault();
        escenario.classList.remove("drag-over");

        const vista = evento.dataTransfer.getData("text/plain");
        this.estado.seleccion = vista;
        this.renderEntidades();
        this.mostrarVista(vista);
      });

      document.addEventListener("keydown", (evento) => {
        if (evento.key === "Escape") {
          this.mostrarTabla();
        }
      });
    }
  }

  window.jocarsa.iu.DOM = DOM;
  window.jocarsa.iu.Utilidades = Utilidades;
  window.jocarsa.iu.OrigenDatos = OrigenDatos;
  window.jocarsa.iu.EstadoIU = EstadoIU;
  window.jocarsa.iu.FichaIU = FichaIU;
  window.jocarsa.iu.ToastIU = ToastIU;
  window.jocarsa.iu.GestorColumnas = GestorColumnas;
  window.jocarsa.iu.AplicacionIU = AplicacionIU;

  document.addEventListener("DOMContentLoaded", () => {
    window.jocarsa.iu.aplicacion = new AplicacionIU();
    window.jocarsa.iu.aplicacion.iniciar();
  });
})();
```
**solicitudes.js**
```js
window.jocarsa = window.jocarsa || {};
window.jocarsa.iu = window.jocarsa.iu || {};

class AlmacenSolicitudes {
    constructor() { this.clave = 'jocarsa-iu-ra1-solicitudes'; }
    cargar(iniciales) {
        const texto = localStorage.getItem(this.clave);
        if (texto === null) return iniciales;
        const registros = JSON.parse(texto);
        if (!Array.isArray(registros) || !registros.every(r => r &&
            ['nombre', 'email', 'asunto', 'prioridad'].every(campo => typeof r[campo] === 'string'))) {
            throw new Error('Los datos locales no tienen el formato esperado.');
        }
        return registros;
    }
    guardar(registros) { localStorage.setItem(this.clave, JSON.stringify(registros)); }
}
window.jocarsa.iu.AlmacenSolicitudes = AlmacenSolicitudes;
```
### templates
**formulario-solicitud.html**
```html
<form id="solicitud" class="ju-form-grid">
<h2 class="ju-form-full">Nueva solicitud</h2>
<label>Nombre<input id="nombre" name="nombre" maxlength="80" autocomplete="name" type="text" placeholder="Nombre del solicitante" required/>
</label>
<label>Correo<input id="email" name="email" maxlength="120" autocomplete="email" type="email" placeholder="persona@example.com" required/>
</label>
<label>Asunto<input id="asunto" name="asunto" maxlength="120" type="text" placeholder="Describe brevemente la solicitud" required/>
</label>
<label>Prioridad<select name="prioridad">
<option>Normal</option>
<option>Alta</option>
<option>Baja</option>
</select>
</label>
<label class="ju-form-full">Detalle<textarea name="detalle" maxlength="1000" rows="3">
</textarea>
</label>
<button class="ju-btn" type="submit">Guardar solicitud</button>
<button class="ju-btn secondary" type="reset">Limpiar</button>
<p id="estadoFormulario" class="ju-form-full" role="status">
</p>
</form>
```
## scripts
**adaptar_formulario.py**
```python
"""Adapta la exportación del editor sin sobrescribirla."""
from pathlib import Path
import re

raiz = Path(__file__).resolve().parent.parent
s = (raiz / 'diseno/formulario-generado.html').read_text()
s = s.removeprefix('<body>').replace('</body>', '')
s = re.sub(r' id="i[a-z0-9]+"', '', s)
s = s.replace('<form id="solicitud">', '<form id="solicitud" class="ju-form-grid">')
s = s.replace('<h2>', '<h2 class="ju-form-full">')
s = s.replace('name="nombre"', 'name="nombre" maxlength="80" autocomplete="name"')
s = s.replace('name="email"', 'name="email" maxlength="120" autocomplete="email"')
s = s.replace('name="asunto"', 'name="asunto" maxlength="120"')
s = s.replace('<textarea name="detalle"', '<textarea name="detalle" maxlength="1000"')
s = s.replace('<label>Detalle', '<label class="ju-form-full">Detalle')
s = s.replace('<button type="submit"', '<button class="ju-btn" type="submit"')
s = s.replace('<button type="reset"', '<button class="ju-btn secondary" type="reset"')
s = s.replace('</form>', '<p id="estadoFormulario" class="ju-form-full" role="status"></p></form>')
s = s.replace('><', '>\n<')
destino = raiz / 'public/templates/formulario-solicitud.html'
destino.parent.mkdir(exist_ok=True)
destino.write_text(s.rstrip() + '\n')
print('OK: plantilla adaptada; exportación original conservada.')
```
**disenar_formulario.py**
```python
"""Usa los controles visibles del editor y conserva su exportación original."""
from pathlib import Path
import json
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.request
from playwright.sync_api import sync_playwright

raiz = Path(__file__).resolve().parent.parent
with socket.socket() as conexion:
    conexion.bind(('127.0.0.1', 0))
    puerto = conexion.getsockname()[1]
with tempfile.TemporaryFile() as registro:
    servidor = subprocess.Popen(['python3', '-m', 'http.server', str(puerto), '--bind', '127.0.0.1', '--directory', str(raiz)], stdout=registro, stderr=registro)
    try:
        url = f'http://127.0.0.1:{puerto}/editor/'
        for _ in range(50):
            try:
                urllib.request.urlopen(url, timeout=1).close()
                break
            except OSError:
                time.sleep(.1)
        with sync_playwright() as p:
            navegador = p.chromium.launch(executable_path=shutil.which('chromium'), headless=True)
            pagina = navegador.new_page(viewport={'width': 1440, 'height': 1000})
            pagina.goto(url)
            pagina.wait_for_selector('.gjs-frame')
            for bloque in ['formulario', 'titulo', 'nombre', 'email', 'asunto', 'prioridad', 'detalle', 'limpiar', 'guardar']:
                pagina.locator(f'[data-bloque="{bloque}"]').click()
            # Reubicar Guardar antes de Limpiar mediante el control del editor.
            pagina.locator('#subir').click()
            marco = pagina.frame_locator('.gjs-frame')
            for campo, ayuda in [('nombre', 'Nombre del solicitante'), ('email', 'persona@example.com'), ('asunto', 'Describe brevemente la solicitud')]:
                marco.locator('#' + campo).click(force=True)
                pagina.locator('#traits .gjs-trt-trait__wrp-placeholder input').fill(ayuda, timeout=3000)
                pagina.locator('#traits .gjs-trt-trait__wrp-placeholder input').press('Tab')
                pagina.locator('#traits .gjs-field-checkbox').click()
            (raiz / 'docs/capturas').mkdir(parents=True, exist_ok=True)
            pagina.screenshot(path=str(raiz / 'docs/capturas/editor.png'), full_page=True)
            with pagina.expect_download() as descarga:
                pagina.locator('#exportar').click()
            destino = raiz / 'diseno/formulario-editor.json'
            descarga.value.save_as(destino)
            exportado = json.loads(destino.read_text())
            assert 'required' in exportado['html']
            assert exportado['html'].index('Guardar solicitud') < exportado['html'].index('Limpiar')
            (raiz / 'diseno/formulario-generado.html').write_text(exportado['html'] + '\n')
            (raiz / 'diseno/formulario-generado.css').write_text(exportado['css'] + '\n')
            print('OK: componentes colocados, Guardar reubicado, tres campos modificados y exportación guardada.')
            navegador.close()
    finally:
        servidor.terminate()
        servidor.wait(timeout=5)
```
**preparar_editor.py**
```python
from pathlib import Path
import urllib.request

raiz = Path(__file__).resolve().parent.parent
runtime = raiz / '.runtime'
runtime.mkdir(exist_ok=True)
for remoto, nombre in [('dist/grapes.min.js', 'grapes.min.js'), ('dist/css/grapes.min.css', 'grapes.min.css')]:
    url = 'https://unpkg.com/grapesjs@0.23.6/' + remoto
    urllib.request.urlretrieve(url, runtime / nombre)
    print('Descargado:', nombre, '(GrapesJS 0.23.6)')
```
**probar_aplicacion.py**
```python
from pathlib import Path
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.request
from playwright.sync_api import sync_playwright

raiz = Path(__file__).resolve().parent.parent
with socket.socket() as conexion:
    conexion.bind(('127.0.0.1', 0))
    puerto = conexion.getsockname()[1]
url = f'http://127.0.0.1:{puerto}'
with tempfile.TemporaryFile() as log:
    servidor = subprocess.Popen(['python3', '-m', 'http.server', str(puerto), '--bind', '127.0.0.1', '--directory', str(raiz / 'public')], stdout=log, stderr=log)
    try:
        for _ in range(50):
            try:
                urllib.request.urlopen(url, timeout=1).close()
                break
            except OSError:
                time.sleep(.1)
        with sync_playwright() as p:
            navegador = p.chromium.launch(executable_path=shutil.which('chromium'), headless=True)
            pagina = navegador.new_page(viewport={'width': 1440, 'height': 1000})
            errores = []
            pagina.on('pageerror', lambda error: errores.append(str(error)))
            pagina.goto(url)
            pagina.wait_for_selector('tbody tr')
            assert pagina.locator('tbody tr').count() == 1
            pagina.locator('#nuevo').click()
            pagina.wait_for_selector('#solicitud')
            assert pagina.locator('#nombre').evaluate('(el) => el.required')
            pagina.locator('#solicitud button[type=submit]').click()
            assert pagina.locator('#solicitud').count() == 1
            assert pagina.evaluate('localStorage.length') == 0
            print('OK: formulario generado integrado; campos obligatorios bloquean un envío vacío')
            pagina.locator('#nombre').fill('Equipo Prueba')
            pagina.locator('#email').fill('correo-no-valido')
            pagina.locator('#asunto').fill('Preparar portátil')
            pagina.locator('#solicitud button[type=submit]').click()
            assert pagina.locator('#email').evaluate('(el) => !el.validity.valid')
            pagina.locator('#email').fill('equipo@example.com')
            pagina.locator('[name=prioridad]').select_option(label='Alta')
            pagina.locator('[name=detalle]').fill('Solicitud ficticia de prueba.')
            pagina.screenshot(path=str(raiz / 'docs/capturas/aplicacion.png'), full_page=True)
            pagina.locator('#solicitud button[type=submit]').click()
            pagina.wait_for_selector('tbody tr')
            assert pagina.locator('tbody tr').count() == 2
            assert pagina.get_by_text('Solicitud guardada', exact=True).count() == 1
            pagina.reload()
            pagina.wait_for_selector('tbody tr')
            assert pagina.locator('tbody tr').count() == 2
            print('OK: alta, aviso de éxito y persistencia tras recargar')
            pagina.locator('#buscador').fill('Equipo Prueba')
            assert pagina.locator('tbody tr').count() == 1
            assert 'Preparar portátil' in pagina.locator('tbody').inner_text()
            pagina.locator('#buscador').fill('ninguna-coincidencia-xyz')
            assert pagina.locator('tbody tr').count() == 0
            print('OK: filtro de búsqueda y resultado vacío')
            pagina.locator('#nuevo').click()
            pagina.wait_for_selector('#solicitud')
            pagina.locator('#nombre').fill('Borrar este texto')
            pagina.locator('button[type=reset]').click()
            assert pagina.locator('#nombre').input_value() == ''
            assert pagina.locator('#estadoFormulario').inner_text() == 'Formulario limpiado.'
            pagina.keyboard.press('Escape')
            pagina.wait_for_selector('tbody tr')
            print('OK: limpiar formulario y volver al listado con Escape')
            pagina.locator('#nuevo').click()
            pagina.wait_for_selector('#solicitud')
            pagina.locator('#nombre').fill('No guardado')
            pagina.locator('#email').fill('prueba@example.com')
            pagina.locator('#asunto').fill('Prueba sin espacio')
            pagina.evaluate("() => { Storage.prototype.setItem = () => { throw new DOMException('Prueba controlada', 'QuotaExceededError'); }; }")
            pagina.locator('button[type=submit]').click()
            assert 'No se pudo guardar' in pagina.locator('#estadoFormulario').inner_text()
            assert pagina.locator('#nombre').input_value() == 'No guardado'
            print('OK: fallo simulado de almacenamiento conserva el formulario y no anuncia éxito')
            assert not errores, errores
            navegador.close()
    finally:
        servidor.terminate()
        servidor.wait(timeout=5)
```
