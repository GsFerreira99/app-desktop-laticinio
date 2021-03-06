from Interface.principal.app.ui_principal import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon


class PrincipalView(Ui_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QIcon('logo.ico'))
        self.setWindowTitle('Sistema')

    def editar_titulo(self, titulo='Home'):
        self.label_titulo.setText(titulo)

