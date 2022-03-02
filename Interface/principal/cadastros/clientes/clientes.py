from Interface.principal.cadastros.clientes.ui_clientes import Ui_Form
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QFrame

class Clientes(Ui_Form, QFrame):

    def __init__(self, widget, parent=None):
        super().__init__(parent)
        super().setupUi(widget)

        self.btn_busca_avancada.clicked.connect(self.aba_pesquisa_avancada)

    def aba_pesquisa_avancada(self):
        self.efeito(150, True)

    
    def efeito(self, maxWidth, enable):

        if enable:
            width = self.busca_avancada.height()
            maxExtend = maxWidth
            standard = 0
            
            if width == 0:
                widthExtend = maxExtend
                self.toggle = True
            else:
                self.toggle = False
                widthExtend = standard

            self.animation = QPropertyAnimation(self.busca_avancada, b'maximumHeight')
            self.animation.setDuration(200)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.start()