import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

filmes = []

def carregar_max_id():
    global contagemId
    arquivo = "dados.json"
    if os.path.exists(arquivo):
        try:
            with open(arquivo, encoding="utf-8") as f:
                filmes = json.load(f)

                if filmes:
                    max_id = max(filme.get("id", 0) for filme in filmes)
                    contagemId = max_id
            

        except Exception as e:
            print("Erro ao carregar dados.json para contagemId:", e)

#Classe para manipular os métodos e requisições feitas em nosso servidor
class MyHandle (SimpleHTTPRequestHandler):
    #Método para carregar os arquivos, recebendo como parametro o nome do arquivo
    def carregarArquivo(self, caminho):
        # Utilizo um try-except para garantir que o servidor não quebre se um arquivo não for encontrado
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
        try:
            f = open(os.path.join(path, 'index.html'), 'r')#Diferentemente da função, nesta maneira o processo de abrir e fechar o arquivo não são automáticos

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()#Fecha o arquivo após a leitura
            return None#Define para a classe pai que tudo que deveria ser feito no método já foi executado

        #Lançamento de exceção caso o arquivo não exista ou não for encontrado
        except FileNotFoundError:
            self.send_error(404, "File not Found")#Envia o código do erro com uma mensagem

        #Retorna os diretórios disponpiveis
        return super().list_directory(path)
    
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
        elif self.path == "/atualizar":
            self.carregarArquivo("atualizar.html")

        # Rota para a API que envia os dados dos filmes
        elif self.path == '/get_filmes':
            if os.path.exists("dados.json"):
                try:
                    with open("dados.json", encoding="utf-8") as f:
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        data = json.load(f)
                        
                except ( json.JSONDecodeError):
                        data = []
                        self.send_response(404)         

                self.wfile.write(json.dumps(data).encode('utf-8'))           
            else:
                return {FileNotFoundError: "Caminho não encontrado!"}
        
        #  handler para servir arquivos CSS
        elif self.path.endswith(".css"):
            try:
                with open(os.path.join(os.getcwd(), self.path[1:]), 'r') as css_file:
                    content = css_file.read()
                    self.send_response(200)
                    # Define o tipo de conteúdo correto para arquivos CSS
                    self.send_header("Content-type", "text/css")
                    self.end_headers()
                    self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "CSS não encontrado")
        
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
                
                global filmes
                global contagemId
                contagemId+=1
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length).decode('utf-8')
                form_data = parse_qs(body)


            
                arquivo = "./dados.json"

                if os.path.exists(arquivo):
                    with open (arquivo, encoding="utf-8") as lista:
                        try:
                            filmes = json.load(lista)
                        except json.JSONDecodeError:
                            filmes = []
                    
                    print(len(filmes))
                    if len(filmes) == 0:
                        contagemId = 0 
                    # Extrai os dados do formulário
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
                else:
                    filmes = [filme]

                with open(arquivo, "w", encoding="utf-8") as lista:
                    json.dump(filmes,lista,indent=4,ensure_ascii=False)


                # Redireciona o usuário para a página de listagem de filmes
                self.send_response(302) # 302 é o código para redirecionamento
                self.send_header('Location', '/listarFilmes')
                self.end_headers()


            else:
                super().do_POST()

    def do_DELETE(self):
        path = self.path.split("/")
        print(path[1])
        if path[1] == 'delete_film':

            id = path[2]
            id_filme = int(id)

            if os.path.exists("dados.json"):
                try:
                    with open("dados.json", encoding="utf-8") as f:
                        data = json.load(f)  

                        novo_data = [filme for filme in data if filme.get("id") != id_filme]
                        
                        
                    with open("dados.json", "w", encoding="utf-8") as lista:
                            json.dump(novo_data,lista,indent=4,ensure_ascii=False)

                except (json.JSONDecodeError):
                        data = []
                        print("errado")
        
#Função principal do programa
def main():
    carregar_max_id()
    port = 8001#Define a porta em que estará rodando o servidor
    server_addres = ('', port)
    httpd = HTTPServer(server_addres, MyHandle)#Variavel que armazena o nosso servidor
    print(f"Servidor rodando em http://127.0.0.1:{port}") 
    httpd.serve_forever()#Deixa o servidor rodando eternamente


#chama a função principal do programa
main()