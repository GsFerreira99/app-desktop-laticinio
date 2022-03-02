import imp
from Interface.principal.cadastros.ui_cadastro import Ui_Form
from Interface.principal.cadastros.clientes.clientes import Clientes as Cliente
from PyQt5.QtWidgets import QFrame


class Cadastro(Ui_Form, QFrame):

    def __init__(self, widget, parent=None):
        super().__init__(parent)
        super().setupUi(widget)

        self.definir_telas()
        self.navegacao.setCurrentIndex(0)

        self.clientes_2.clicked.connect(lambda: self.navegacao.setCurrentIndex(1))
        self.fornecedores.clicked.connect(lambda: self.navegacao.setCurrentIndex(2))

    def definir_telas(self):
        self.tela_clientes = Cliente(self.clientes)
        