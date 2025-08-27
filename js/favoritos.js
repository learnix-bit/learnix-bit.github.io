const lista = document.getElementById("listaFavoritos");
let favoritos = JSON.parse(localStorage.getItem("favoritos")) || [];

if(favoritos.length === 0) {
    lista.innerHTML = "<p>No tienes cursos favoritos aún.</p>";
} else {
    lista.innerHTML = "";
    favoritos.forEach(curso => {
        const div = document.createElement("div");
        div.classList.add("curso-fav");
        div.textContent = curso;
        lista.appendChild(div);
    });
}
