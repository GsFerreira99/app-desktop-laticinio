from .view_login import LoginView
from .model_login import LoginModel

class LoginController:
    def __init__(self, tela):
        self.view = LoginView()
        self.model = LoginModel()

        self.redirecionar = tela
        
        self.direto()

        self.view.btn_entrar.clicked.connect(self.efetuar_login)
        self.view.btn_entrar.setAutoDefault(True)

        self.dados = {
                "usuario" : '',
                "senha" : ''
            }

        self.atualizar_campos()

    def direto(self):
        self.view.close()
        self.redirecionar.view.show()

    def redirecionar_view(self):
        self.view.close()
        self.redirecionar.definir_user(self.auth[1][0])
        self.redirecionar.view.show()


    def efetuar_login(self):
        self.dados_login()
        self.model.definir_credenciais(self.dados['usuario'], self.dados['senha'])
        self.auth = self.model.autenticar()
        if self.auth[0]:
            self.auth[1][0]['username'] = self.dados['usuario']
            self.auth[1][0]['password'] = self.dados['senha']
            self.atualizar_campos()
            self.view.msg_erro(False)
            self.redirecionar_view()
        else:
            self.dados['senha'] = ''
            self.view.msg_erro(True, msg=self.auth[1]['detail'])
            self.atualizar_campos()

    def atualizar_campos(self):
        self.view.definir_campos(self.dados['usuario'], self.dados['senha'])


    def dados_login(self):
        dados = self.view.receber_dados()
        if self.validar_vazios([dados['usuario'], [dados['senha']]]):
            self.dados['usuario'] = dados['usuario']
            self.dados['senha'] = dados['senha']
        else:
            self.view.msg_erro(True)

    
    def validar_vazios(self, dados):
        for dado in dados:
            if dado == '':
                return False
        return True