from PyQt5.QtWidgets import QMainWindow, QApplication
from GUI.ui_menu_principal import Ui_MainWindow
from Interface.principal.navegacao import Navegacao
import sys

class MenuPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)

        self.btn_home.clicked.connect(lambda: Navegacao.navegar(self, 0))
        self.btn_vendas.clicked.connect(lambda: Navegacao.navegar(self, 1))
        self.btn_clientes.clicked.connect(lambda: Navegacao.navegar(self, 2))
        self.btn_financeiro.clicked.connect(lambda: Navegacao.navegar(self, 3))
        self.configuracoes.clicked.connect(lambda: Navegacao.navegar(self, 4))



root = QApplication(sys.argv)
app = MenuPrincipal()
app.showMaximized()

sys.exit(root.exec_())