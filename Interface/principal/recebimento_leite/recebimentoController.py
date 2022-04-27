from Interface.models.Recebimento import Recebimento
from .recebimentoModel import RecebimentoModel
from .recebimentoView import RecebimentolView

from ...functions.funcoes import verificar_vazios_dict

class RecebimentoController:

    def __init__(self, ui):
        self.ui = ui
        self.view = RecebimentolView()
        self.model = RecebimentoModel(self.ui)

        self.view.btnSalvar.clicked.connect(lambda: self.recebimento())

    def recebimento(self):
        dados = self.view.receber_dados()
        if not verificar_vazios_dict(dados):
            recebimento = Recebimento(dados['data'], dados['fornecedor'], dados['quantidade'])
            status = recebimento.validar()
            if not status:
                self.view.aviso.exibir_aviso('danger', recebimento.get_erro) 
            else:
                post = self.ui.api.post('recebimento-leite/', recebimento.post)
                if post.status_code == 201:
                    self.view.aviso.exibir_aviso('success', 'Recebimento adicionado com sucesso')
                    self.view.limpar()
                else:
                    self.view.aviso.exibir_aviso('warning', 'Recebimento não adicionado, erro na conexão com o servidor.')
        else:
            self.view.aviso.exibir_aviso('danger', 'Preencha os campos vazios')

    def preencher_campo_data(self):
        self.view.preencher_input_data()

    def preencher_campo_fornecedor(self):
        self.model.definir_fornecedores()
        self.view.preencher_input_fornecedor(self.model.fornecedores)