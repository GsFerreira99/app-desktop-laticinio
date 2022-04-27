from Interface.principal.recebimento_leite.ui_recebimento import Ui_Form
from PyQt5.QtWidgets import QWidget
from ...functions.funcoes import datetimeNow
from ...models.Aviso import Aviso

class RecebimentolView(Ui_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        self.aviso = Aviso(self.label_msg)
    
    def preencher_input_fornecedor(self, dados):
        self.inputFornecedor.clear()
        self.inputFornecedor.addItem("")
        for fornecedor in dados:
            self.inputFornecedor.addItem(fornecedor.get_nome)

    def preencher_input_data(self):
        self.inputData.setDateTime(datetimeNow())

    def receber_dados(self):
        dados = {
            'data' : self.inputData.dateTime(),
            'fornecedor' : self.inputFornecedor.currentText(),
            'quantidade' : self.inputQuantidade.text()
        }
        return dados
        
    def limpar(self):
        self.inputQuantidade.setText('')
        
        