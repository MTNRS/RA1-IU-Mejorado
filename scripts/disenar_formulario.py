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
