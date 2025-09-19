import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

filmes = {}

#Classe para manipular os métodos e requisições feitas em nosso servidor
class MyHandle (SimpleHTTPRequestHandler):

    #Método para carregar os arquivos, recebendo como parametro o nome do arquivo
    def carregarArquivo(self, caminho):
        with open(os.path.join(os.getcwd(), caminho), 'r') as arquivo:#Abre o nosso arquivo através do caminho, lê o conteúdo e guarada na variável "arquivo"
            content = arquivo.read()#Armazena o conteudo da variavel arquivo em "content"
            self.send_response(200)#Retorna o status positivo para o cliente
            self.send_header("content-type", "text/html")#Retorna o tipo do conteúdo
            self.end_headers()#Determina que os headers foram finalizados
            self.wfile.write(content.encode("utf-8"))#Escreve através da função wfile o conteúdo na tela com a encodificação "utf-8"

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
    
    #Método GET que retorna o conteúdo da página login
    def do_GET(self):
        #Executa a abertura do arquivvo caso o caminho aponte para login
        if self.path == '/login':
            try:
                self.carregarArquivo("login.html")#Chama a função para carregar arquivo
            
             #Lançamento de exceção caso o arquivo não exista ou não for encontrado
            except FileNotFoundError:
                self.send_error(404, "File not Found")

        #Executa a abertura do arquivvo caso o caminho aponte para cadastro
        elif self.path == "/cadastro":
            try:
                self.carregarArquivo("cadastro.html")

            #Lançamento de exceção caso o arquivo não exista ou não for encontrado
            except FileNotFoundError:
                self.send_error(404, "File not Found")
        
        #Executa a abertura do arquivvo caso o caminho aponte para listarFilmes
        elif self.path == "/listarFilmes":
            try:
                self.carregarArquivo("listarFilmes.html")

            #Lançamento de exceção caso o arquivo não exista ou não for encontrado
            except FileNotFoundError:
                self.send_error(404, "File not Found")

        else:
            #Mostra a mensagem de error response no html
            super().do_GET()

    def accont_user(self, user, password):
        usuario = "alex@gmail.com"
        senha = "123456"
 
        if user == usuario and senha == password:
            print("Usuário Logado")
            self.carregarArquivo("listarFilmes.html")
        
    def do_POST(self):
            if self.path == '/send_login':
                content_length = int(self.headers['Content-length'])
                body = self.rfile.read(content_length).decode('utf-8')
                form_data = parse_qs(body)
    
                login = form_data.get('usuario', [""])[0]
                password = form_data.get('senha', [""])[0]
    
                self.accont_user(login, password)
                print("Data Form:")
                print("Usuario: ", login)        
                print("Password: ", password)    



            elif self.path == '/send_movies':
                content_length= int(self.headers['Content-length'])
                body = self.rfile.read(content_length).decode('utf-8')
                form_data = parse_qs(body)

                nome = form_data.get('nome', [""])[0]
                ano = form_data.get('ano', [""])[0]
                atores = form_data.get('atores',[""])[0]
                genero = form_data.get('genero',[""])[0]
                diretor = form_data.get('diretor',[""])[0]
                produtora = form_data.get('produtora',[""])[0]
                sinopse = form_data.get('sinpose',[""])[0]

                filme = {
                    "nome": nome,
                    "ano":ano,
                    "atores":atores,
                    "genero":genero,
                    "diretor":diretor,
                    "produtora":produtora,
                    "sinopse":sinopse
                }

                filmes[len(filmes)+1] = filme
                print(filmes)


            else:
                super(MyHandle, self).do_POST()
        
#Função principal do programa
def main():
    port = 8001#Define a porta em que estará rodando o servidor
    server_addres = ('', port)
    httpd = HTTPServer(server_addres, MyHandle)#Variavel que armazena o nosso servidor
    print(f"Servidor rodando em http://127.0.0.2:{port}")
    httpd.serve_forever()#Deixa o servidor rodando eternamente


#chama a função principal do programa
main()