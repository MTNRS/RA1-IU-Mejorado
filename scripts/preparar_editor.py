from pathlib import Path
import urllib.request

raiz = Path(__file__).resolve().parent.parent
runtime = raiz / '.runtime'
runtime.mkdir(exist_ok=True)
for remoto, nombre in [('dist/grapes.min.js', 'grapes.min.js'), ('dist/css/grapes.min.css', 'grapes.min.css')]:
    url = 'https://unpkg.com/grapesjs@0.23.6/' + remoto
    urllib.request.urlretrieve(url, runtime / nombre)
    print('Descargado:', nombre, '(GrapesJS 0.23.6)')
