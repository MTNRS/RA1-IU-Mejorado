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
