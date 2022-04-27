from ...models.Fornecedor import Fornecedor

class RecebimentoModel:

    def __init__(self, ui):
        self.ui = ui
        self.fornecedores = []

    
    def definir_fornecedores(self):
        dados = self.get_fornecedores()
        self.fornecedores = []
        for fornecedor in dados:
            self.fornecedores.append(Fornecedor(fornecedor['id'], fornecedor['nome']))

    def get_fornecedores(self):
        request = self.ui.api.get_fornecedores()
        if request['status'] == 200:
            return request['dict']
        else:
            return request['status'], request['dict']

    