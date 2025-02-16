import ssl
from http.client import HTTPSConnection

class ClientMsgHandler:

    def __init__(self):
        self.context = ssl.create_default_context(cafile="certificate.pem")
        self.context.check_hostname = False
        self.connection = None

    def connect(self):
        self.connection = HTTPSConnection('localhost', 8000, context=self.context)
        self.connection.connect()
    
    def get_request(self):
        self.connection.request("GET", "/")
        response = self.connection.getresponse()
        print(f"Stat: {response.status}")
        print(f"Conteudo: {response.read().decode()}")
    
    def post_request(self, text_to_send):
        self.connection.request("POST", "/", text_to_send)
        response = self.connection.getresponse()
        print(f"Stat: {response.status}")
        print(f"Conteudo: {response.read().decode()}")

client = ClientMsgHandler()
client.connect()
client.get_request()
msg = input("Insira uma mensagem para ser enviada no POST request: ")
client.post_request(msg)
client.connection.close()