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

## Relación con Integra Tech Consulting

El caso de uso es una propuesta académica de recepción de solicitudes, con datos
ficticios. No se ha integrado en sistemas reales de la empresa.

## Uso de IA

Se utilizó Codex para adaptar el código, automatizar el uso del editor visual,
documentar y probar la aplicación. Pendiente de revisión personal antes de
la entrega.
