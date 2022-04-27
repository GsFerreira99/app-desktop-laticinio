from Interface.principal.recebimento_leite.ui_recebimento import Ui_Form
from PyQt5.QtWidgets import QWidget


class RecebimentolView(Ui_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        self.label_msg.setMaximumHeight(0)

    def receber_dados(self):
        dados = {
            'data' : self.inputData.text(),
            'fornecedor' : self.inputFornecedor.currentText(),
            'quantidade' : self.inputQuantidade.text()
        }
        return dados
        
        
        