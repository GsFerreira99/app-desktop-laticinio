from Interface.principal.login.ui_login import Ui_Form
from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QIcon


class LoginView(Ui_Form, QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QIcon('logo.ico'))
        self.setWindowTitle('Login')

        self.label_msg.setMaximumHeight(0)
        
    def definir_campos(self, usuario, senha):
        self.input_senha.setText(senha)
        self.input_usuario.setText(usuario)

    def msg_erro(self, status, msg='Usuario ou senha Incorretos'):
        if status:
            self.label_msg.setText(msg)
            self.label_msg.setMaximumHeight(40)
        else:
            self.label_msg.setMaximumHeight(0)

    def receber_dados(self):
        usuario = self.input_usuario.text()
        senha = self.input_senha.text()

        return {'usuario': usuario, 'senha': senha}







        