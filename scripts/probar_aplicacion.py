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
