function getFilmes() {
    const filmesContainer = document.getElementById('filmes-container');
    // Se o container de filmes não existir na página, a função para de executar.
    if (!filmesContainer) return;

    fetch('/get_filmes')
        .then(response => response.json())
        .then(data => {
            
            filmesContainer.innerHTML = ''; // Limpa a lista antes de adicionar os filmes
            console.log(data)
            data.forEach(filme => {
                const card = document.createElement('div');
                card.classList.add('movie-card');

                card.innerHTML = `
                    <h2>${filme.titulo} (${filme.ano})</h2>
                    <p><strong>Orçamento:</strong> ${filme.orcamento}</p>
                    <p><strong>Duração:</strong> ${filme.tempo_duracao}</p>
                    <p id="poster"><strong>Poster:</strong> ${filme.poster}</p>
                    <div class="botoes-crud">
                        <button class="btn-atualizar" data-id="${filme.id}">ATUALIZAR</button>
                        <button class="btn-apagar" data-id="${filme.id}">DELETAR</button>
                    </div>
                `;
                filmesContainer.appendChild(card);
            });

            // Adiciona os eventos aos botões de apagar
            document.querySelectorAll('.btn-apagar').forEach(button => {
                button.addEventListener('click', function () {
                    const filmeId = this.getAttribute('data-id');
                    fetch(`/delete_film/${filmeId}`, { method: 'DELETE' })
                        .then(res => {
                            if (res.ok) {
                                this.closest('.movie-card').remove();
                            }
                        })
                        .catch(console.error);
                });
            });

            // Adiciona os eventos aos botões de atualizar
            document.querySelectorAll('.btn-atualizar').forEach(button => {
                button.addEventListener('click', function () {
                    const filmeId = this.getAttribute('data-id');
                    window.location.href = `/atualizar?id=${filmeId}`;
                });
            });
        })
        .catch(error => console.error('Erro ao buscar filmes:', error));
}


function setupUpdatePage() {
    const updateForm = document.getElementById('update-form');
    // Se o formulário de atualização não existir, a função para de executar.
    if (!updateForm) return;

    const params = new URLSearchParams(window.location.search);
    const filmeId = params.get('id');

    // Se houver um ID na URL, busca os dados do filme para preencher o formulário
    if (filmeId) {
        fetch(`/get_filme/${filmeId}`)
            .then(response => response.json())
            .then(filme => {
                document.getElementById('filme-id').value = filme.id;
                document.getElementById('nome').value = filme.nome;
                document.getElementById('ano').value = filme.ano;
                document.getElementById('atores').value = filme.atores;
                document.getElementById('genero').value = filme.genero;
                document.getElementById('diretor').value = filme.diretor;
                document.getElementById('produtora').value = filme.produtora;
                document.getElementById('sinopse').value = filme.sinopse;
            })
            .catch(error => console.error('Erro ao buscar dados do filme:', error));
    }

    // Adiciona o evento de 'submit' ao formulário para enviar os dados atualizados
    updateForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const id = document.getElementById('filme-id').value;
        const formData = new URLSearchParams(new FormData(this)).toString();

        fetch(`/update_film/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData
        })
        .then(response => {
            if (response.ok) {
                // Redireciona para a página de listagem após o sucesso
                window.location.href = '/listarFilmes';
            }
        })
        .catch(error => console.error('Erro ao atualizar filme:', error));
    });
}



// Quando a página carregar, executa ambas as funções.
// Cada função tem uma verificação interna para só rodar na página correta.
document.addEventListener('DOMContentLoaded', function () {
    getFilmes();
    setupUpdatePage();
});