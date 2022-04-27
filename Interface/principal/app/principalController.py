from Interface.api.Api import Api
from Interface.principal.home.homeController import HomeController
from .principalView import PrincipalView
from .principalModel import PrincipalModel

from ..recebimento_leite.recebimentoController import RecebimentoController

from ...animacoes.efeitos import toggle_width

from...models.User import User

class PrincipalController:
    
    def __init__(self):
        self.view = PrincipalView()
        self.model = PrincipalModel()

        self.api = Api('https://rancho-alere.herokuapp.com/api/')

        #CONTROLLERS
        self.homeController = HomeController(self)  
        self.recebimentoController = RecebimentoController(self)

        self.toogleMenuLeft()
        self.definirTelas()

        #Buttons
        self.view.btn_home.clicked.connect(lambda: self.navegar(0))
        self.view.btn_recebimento.clicked.connect( lambda: self.navegar(1))

        self.view.btn_toogle.clicked.connect(self.toogleMenuLeft)

    def definir_user(self, user):
        self.user = User(user['id'], user['username'], user['password'], user['first_name'], user['last_name'], user['groups'])
        self.configurar_api()
        self.atualizar_user()

    def configurar_api(self):
        self.api.definir_auth(usuario=self.user.get_usuario, senha=self.user.get_senha)

    def atualizar_user(self):
        self.view.label_3.setText(self.user.get_name)
        self.view.label_4.setText(self.user.get_group)

    def definirTelas(self):
        self.view.navWidget.insertWidget(0, self.homeController.view)
        self.view.navWidget.insertWidget(1, self.recebimentoController.view)

    def navegar(self, index):
        nav = {
            0 : {'titulo': 'Home',  'funcao' : self.home},
            1 : {'titulo': 'Recebimento Leite',  'funcao' : self.recebimento}
        }

        self.view.navWidget.setCurrentIndex(index)
        self.view.editar_titulo(nav[index]['titulo'])
        func = nav[index]['funcao']
        func()

    def toogleMenuLeft(self):
        toggle_width(self, self.view.menu_lateral, 200, True)

    def recebimento(self):
        self.recebimentoController.preencher_campo_fornecedor()
        self.recebimentoController.preencher_campo_data()
        self.recebimentoController.view.aviso.exibicao(False)

    def home(self):
        pass