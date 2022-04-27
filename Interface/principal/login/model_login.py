import requests
from ...api.Api import Api

class LoginModel:

    def __init__(self):
        self.usuario = None
        self.senha = None
        self.api = Api('http://127.0.0.1:8000/')

    def definir_credenciais(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.api.definir_auth(self.usuario, self.senha)

    def autenticar(self):
        request = self.api.autenticar_usuario()
        if request['status'] == 200:
            return True, request['dict']
        else:
            return False, request['dict']