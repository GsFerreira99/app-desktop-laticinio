from Interface.principal import ui_menu_principal
from Interface.principal.cadastros.cadastros import Cadastro

nav = {
        0 : "Home",
        1 : "Vendas",
        2 : "Cadastro",
        3 : "Financeiro",
        4 : "Configuracoes",
    }

class Navegacao(ui_menu_principal.Ui_MainWindow):

    def navegar(self, index):
        if index in nav.keys():
            self.stackedWidget.setCurrentIndex(index)
            self.titulo.setText(nav[index])

    def definir_telas(self):
        self.frame_cadastro = Cadastro(self.Cadastros)