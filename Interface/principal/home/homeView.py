from Interface.principal.home.ui_home import Ui_Form
from PyQt5.QtWidgets import QWidget


class HomeView(Ui_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def msg(self, status, msg='Usuario ou senha Incorretos'):
        if status:
            self.label_msg.setText(msg)
            self.label_msg.setMaximumHeight(40)
        else:
            self.label_msg.setMaximumHeight(0)
