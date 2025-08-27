function sumarPuntos() {
    let puntos = parseInt(localStorage.getItem("puntos")) || 0;
    puntos += 10;
    localStorage.setItem("puntos", puntos);
    alert(`¡Has ganado 10 puntos! Total: ${puntos}`);
}
