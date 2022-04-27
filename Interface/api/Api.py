import imp
from requests import Session, Request
import requests

class Api:

    def __init__(self, url):
        self.url = url
        self.header = {'Content-type': 'application/json'}

    def definir_auth(self, usuario, senha):
        self.auth = (usuario, senha)

    def get(self, url):
        return requests.get(f'{self.url}{url}', auth = self.auth)

    def get_status_code(self):
        return self.resposta.status_code

    def get_json(self):
        return self.resposta.json()

    def post(self, url, dados):
        return requests.post(f'{self.url}{url}', auth = self.auth, data=dados, headers=self.header)

    def get_fornecedores(self):
        try:
            self.resposta = self.get('fornecedores/')
            return {'status' : self.get_status_code(), 'dict': self.get_json()}
        except requests.exceptions.ConnectionError:
            return {'status' : 500, 'dict': {'detail': 'Não foi possivel se conectar ao servidor.'}}

    def autenticar_usuario(self):
        try:
            self.resposta = self.get('api/usuarios/')
            return {'status' : self.get_status_code(), 'dict': self.get_json()}
        except requests.exceptions.ConnectionError:
            return {'status' : 500, 'dict': {'detail': 'Não foi possivel se conectar ao servidor.'}}


