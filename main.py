from PyQt5.QtWidgets import QApplication
import sys

#Controlers
from Interface.principal.login.controller_login import LoginController
from Interface.principal.app.principalController import PrincipalController

class App:
    def __init__(self):
        self.principalController = PrincipalController()
        self.loginController = LoginController(self.principalController)
        #self.loginController.view.show()

        

root = QApplication(sys.argv)
app = App()


sys.exit(root.exec_())