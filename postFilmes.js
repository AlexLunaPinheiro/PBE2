document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".register-form");
    if (!form) return;

    async function enviarFormulario(event) {
        event.preventDefault(); // impede o submit padrão
     
        const formData = new FormData(form);
     
        const response = await fetch("/send_movies", {
            method: 'POST',
            body: new URLSearchParams(formData)
        });
     
        if (response.status === 409) {
            alert("Filme já cadastrado, tente outro");
        } else if (response.status === 201) {
            alert("Filme cadastrado com sucesso");
            window.location.href = "/listarFilmes";
        } else {
            alert("Erro ao cadastrar o filme");
        }
    }
     
    form.addEventListener("submit", enviarFormulario);
});
