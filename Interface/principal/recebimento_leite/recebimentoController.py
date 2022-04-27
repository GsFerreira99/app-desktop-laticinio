from .recebimentoModel import RecebimentoModel
from .recebimentoView import RecebimentolView

from ...functions.funcoes import verificar_vazios_dict

class RecebimentoController:

    def __init__(self, ui):
        self.ui = ui
        self.view = RecebimentolView()
        self.model = RecebimentoModel()

        self.view.btnSalvar.clicked.connect(self.recebimento)

    def recebimento(self):
        if not verificar_vazios_dict(self.view.receber_dados()):
            print('ok')

    
