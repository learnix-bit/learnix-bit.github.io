// Buscador básico
const inputBuscar = document.getElementById("buscarCurso");
const cursos = document.querySelectorAll(".curso");

inputBuscar.addEventListener("input", () => {
    const texto = inputBuscar.value.toLowerCase();
    cursos.forEach(curso => {
        const nombre = curso.querySelector("h3").textContent.toLowerCase();
        if(nombre.includes(texto)) {
            curso.style.display = "block";
        } else {
            curso.style.display = "none";
        }
    });
});

// Favoritos desde cursos.html
const botonesFav = document.querySelectorAll(".btn-fav");

botonesFav.forEach(btn => {
    btn.addEventListener("click", () => {
        const cursoNombre = btn.parentElement.querySelector("h3").textContent;
        let favoritos = JSON.parse(localStorage.getItem("favoritos")) || [];
        if(!favoritos.includes(cursoNombre)) {
            favoritos.push(cursoNombre);
            localStorage.setItem("favoritos", JSON.stringify(favoritos));
            alert(`${cursoNombre} agregado a favoritos`);
        } else {
            alert(`${cursoNombre} ya está en favoritos`);
        }
    });
});
