from GUI import ui_menu_principal

nav = {
        0 : "Home",
        1 : "Vendas",
        2 : "Clientes",
        3 : "Financeiro",
        4 : "Configuracoes",
    }

class Navegacao(ui_menu_principal.Ui_MainWindow):

    def navegar(self, index):
        if index in nav.keys():
            self.stackedWidget.setCurrentIndex(index)
            self.titulo.setText(nav[index])