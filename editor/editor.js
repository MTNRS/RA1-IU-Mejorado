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
