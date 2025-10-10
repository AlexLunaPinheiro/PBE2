import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import json
from repo.filmesSerializer import FilmeSerializer

filmes = []
contagemId = 0

def carregar_dados():
    global filmes
    global contagemId
    filmes = FilmeSerializer.loadFilminhos() or []

    if filmes:
        contagemId = max(filme.get("id", 0) for filme in filmes)
    else:
        contagemId = 0


#Classe para manipular os métodos e requisições feitas em nosso servidor
class MyHandle (SimpleHTTPRequestHandler):
    #Método para carregar os arquivos, recebendo como parametro o nome do arquivo
    def carregarArquivo(self, caminho):
        try:
            with open(os.path.join(os.getcwd(), caminho), 'r', encoding='utf-8') as arquivo:#Abre o nosso arquivo através do caminho, lê o conteúdo e guarada na variável "arquivo"
                content = arquivo.read()#Armazena o conteudo da variavel arquivo em "content"
                self.send_response(200)#Retorna o status positivo para o cliente
                self.send_header("content-type", "text/html; charset=utf-8")#Retorna o tipo do conteúdo, especificando utf-8
                self.end_headers()#Determina que os headers foram finalizados
                self.wfile.write(content.encode("utf-8"))#Escreve através da função wfile o conteúdo na tela com a encodificação "utf-8"
        except FileNotFoundError:
            self.send_error(404, "Arquivo não encontrado")

    #Método padrão que retorna o conteúdo do index
    def list_directory(self, path):
        self.carregarArquivo("index.html")

    

    #Método GET que retorna o conteúdo das páginas
    def do_GET(self):
        # Rota para a página de login
        if self.path == '/login':
            self.carregarArquivo("login.html")

        # Rota para a página de cadastro
        elif self.path == "/cadastro":
            self.carregarArquivo("cadastro.html")
        
        # Rota para a página de listagem de filmes
        elif self.path == "/listarFilmes":
            self.carregarArquivo("listarFilmes.html")
        
        #Rota para a pagina de atualizar filme
        elif self.path.startswith("/atualizar"):
            self.carregarArquivo("atualizar.html")

        # Rota para a API que envia os dados dos filmes
        elif self.path == '/get_filmes':
            carregar_dados()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(filmes, ensure_ascii=False).encode('utf-8'))
        
        elif self.path.startswith('/get_filme/'):
            id_filme = int(self.path.split('/')[-1])
            carregar_dados()
            filme = next((f for f in filmes if f['id'] == id_filme), None)
            if filme:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(filme).encode('utf-8'))
            else:
                self.send_error(404, "Filme não encontrado")

        # handler para servir arquivos CSS 
        elif self.path.endswith(".css"):
            try:
                with open(os.path.join(os.getcwd(), self.path[1:]), 'r', encoding='utf-8') as css_file:
                    content = css_file.read()
                    self.send_response(200)
                    # Define o tipo de conteúdo para arquivos CSS
                    self.send_header("Content-type", "text/css; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "Arquivo CSS não encontrado")
        
        else:
            #Mostra a mensagem de error response no html
            super().do_GET()

    def accont_user(self, user, password):
        usuario = "alex@gmail.com"
        senha = "123456"
 
        if user == usuario and senha == password:
            print("Usuário Logado")
            # Redireciona para a página de listagem de filmes após o login
            self.send_response(302)
            self.send_header('Location', '/listarFilmes')
            self.end_headers()
        
    def do_POST(self):
        if self.path == '/send_login':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            login = form_data.get('usuario', [""])[0]
            password = form_data.get('senha', [""])[0]
            self.accont_user(login, password)

        elif self.path == '/send_movies':
            global contagemId
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            carregar_dados()
            contagemId += 1
            
            filme = {
                "id": contagemId,
                "nome": form_data.get('nome', [""])[0],
                "ano": form_data.get('ano', [""])[0],
                "atores": form_data.get('atores', [""])[0],
                "genero": form_data.get('genero', [""])[0],
                "diretor": form_data.get('diretor', [""])[0],
                "produtora": form_data.get('produtora', [""])[0],
                "sinopse": form_data.get('sinopse', [""])[0]
            }

            filmes.append(filme)

            with open("dados.json", "w", encoding="utf-8") as f:
                json.dump(filmes, f, indent=4, ensure_ascii=False)

            self.send_response(302)
            self.send_header('Location', '/listarFilmes')
            self.end_headers()

        else:
            super().do_POST()
    
    def do_PUT(self):
        if self.path.startswith('/update_film/'):
            id_filme = int(self.path.split('/')[-1])
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            carregar_dados()
            
            filme_index = -1
            for i, f in enumerate(filmes):
                if f['id'] == id_filme:
                    filme_index = i
                    break

            if filme_index != -1:
                filmes[filme_index] = {
                    "id": id_filme,
                    "nome": form_data.get('nome', [""])[0],
                    "ano": form_data.get('ano', [""])[0],
                    "atores": form_data.get('atores', [""])[0],
                    "genero": form_data.get('genero', [""])[0],
                    "diretor": form_data.get('diretor', [""])[0],
                    "produtora": form_data.get('produtora', [""])[0],
                    "sinopse": form_data.get('sinopse', [""])[0]
                }
                
                with open("dados.json", "w", encoding="utf-8") as f:
                    json.dump(filmes, f, indent=4, ensure_ascii=False)
                
                self.send_response(200)
                self.end_headers()
            else:
                self.send_error(404, "Filme não encontrado para atualização")


    def do_DELETE(self):
        if self.path.startswith('/delete_film/'):
            id_filme = int(self.path.split('/')[-1])
            carregar_dados()
            
            filmes_filtrados = [filme for filme in filmes if filme.get("id") != id_filme]

            if len(filmes_filtrados) < len(filmes):
                with open("dados.json", "w", encoding="utf-8") as f:
                    json.dump(filmes_filtrados, f, indent=4, ensure_ascii=False)
                
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Filme deletado com sucesso.")
            else:
                self.send_error(404, "Filme nao encontrado para deletar")

#Função principal do programa
def main():
    carregar_dados()
    port = 8001#Define a porta em que estará rodando o servidor
    server_addres = ('', port)
    httpd = HTTPServer(server_addres, MyHandle)#Variavel que armazena o nosso servidor
    print(f"Servidor rodando em http://127.0.0.1:{port}") 
    httpd.serve_forever()#Deixa o servidor rodando eternamente

#chama a função principal do programa
main()