from http.server import SimpleHTTPRequestHandler, HTTPServer

#definição de porta 
port = 8000

#definindo o handler da requisição
handler = SimpleHTTPRequestHandler

#criando a instancia servidor
server = HTTPServer(('localhost',port),handler)

print(f"servidor rodando na porta http://127.0.0.1:{port}")

server.serve_forever()



