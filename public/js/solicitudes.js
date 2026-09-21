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
