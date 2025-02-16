from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from io import BytesIO

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Resposta do servidor enviada")
    
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        content = self.rfile.read(content_length)

        response = BytesIO()
        response.write(b'Essa e o POST request recebido: ')
        response.write(content)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.getvalue())

httpServer = HTTPServer(('localhost', 8000), HTTPRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile = 'certificate.pem', keyfile = 'key.pem')
context.check_hostname = False
print(f"Servidor: localhost =  127.0.0.1, port = 8000")

httpServer.socket = context.wrap_socket(httpServer.socket, server_side=True)

httpServer.serve_forever()