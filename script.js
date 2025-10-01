 function getFilmes(){
     //requisição para o endpoint /get_filmes
            fetch('/get_filmes')
                // Quando a resposta chegar, passa ela para o formato JSON
                .then(response => response.json()) 
                // chamo a função para criar os cards
                .then(data => {
                    console.log(data)
                    // elemento container onde os cards serão inseridos
                    const filmesContainer = document.getElementById('filmes-container');
                    
                    // Percorro cada filme retornado pela API
                    for (const id in data) {
                        const filme = data[id];
                        
                        
                        const card = document.createElement('div');
                        card.classList.add('movie-card'); // classe de estilo ao card
                        
                        // conteúdo HTML do card, preenchendo com os dados do filme
                        card.innerHTML = `
                            <h2>${filme.nome} (${filme.ano})</h2>
                            <p><strong>Gênero:</strong> ${filme.genero}</p>
                            <p><strong>Diretor:</strong> ${filme.diretor}</p>
                            <p><strong>Atores:</strong> ${filme.atores}</p>
                            <p><strong>Produtora:</strong> ${filme.produtora}</p>
                            <div class="sinopse">
                                <strong>Sinopse:</strong>
                                <p>${filme.sinopse}</p>
                            </div>
                            <div class="botoes-crud">
                                <button class="btn-atualizar" id="atualizar-${filme.id}">atualizar</button>
                                <button class="btn-apagar" id="apagar-${filme.id}">deletar</button>
                            </div>
                        `;
                        
                        // adiciona o card recém-criado dentro do container
                        filmesContainer.appendChild(card);
                        if (filme.id) {
                            const botaoAtualizar = document.getElementById(`atualizar-${filme.id}`);
                            const botaoApagar = document.getElementById(`apagar-${filme.id}`);

                            botaoApagar.addEventListener('click', (e)=> {
                                fetch(`/delete_film/${filme.id}`, { method : 'DELETE'})
                                    .then(res => res.text())
                                    .then(msg => {
                                        card.remove()
                                    })
                                    .catch(console.error)
                                    
                            })

}
                    }
                })
                // Se der algum erro na requisição, exibe no console
                .catch(error => console.error('Erro ao buscar filmes:', error));
 }

 
 

 // evento quando a página terminar de carregar
        document.addEventListener('DOMContentLoaded', function() {
           getFilmes();
        });