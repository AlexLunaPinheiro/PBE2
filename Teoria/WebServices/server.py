import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

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
        
#Função principal do programa
def main():
    port = 8001#Define a porta em que estará rodando o servidor
    server_addres = ('', port)
    httpd = HTTPServer(server_addres, MyHandle)#Variavel que armazena o nosso servidor
    print(f"Servidor rodando em http://127.0.0.1:{port}")
    httpd.serve_forever()#Deixa o servidor rodando eternamente


#chama a função principal do programa
main()