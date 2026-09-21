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

## Acceso a GitHub

El acceso inicial falló. Se completó una nueva autenticación como MTNRS y se
creó el repositorio público de la tarea.

Destino del proyecto y del informe: [MTNRS/RA1-IU-Mejorado](https://github.com/MTNRS/RA1-IU-Mejorado).
