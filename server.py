from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from io import BytesIO

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def GET_handler(self):

        # codígo 200 implica q tudo está ok

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Resposta do servidor enviada")
    
    def POST_handler(self):

        conteudo_tam = (int)(self.headers["Content-Length"])
        conteudo = self.rfile.read(conteudo_tam)

        resp = BytesIO()
        resp.write(b'Essa e o POST request recebido: ')
        resp.write(conteudo)
        self.wfile.write(resp.getvalue())

httpServer = HTTPServer(('localhost', 4433), HTTPRequestHandler)

context = ssl._create_unverified_context(certfile="certificate.pem", keyfile="key.pem")

print(f"Servidor: localhost 127.0.0.1, port = 4433")

httpServer.socket = context.wrap_socket(httpServer.socket, server_side=True)

httpServer.serve_forever()