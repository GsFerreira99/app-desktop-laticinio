from ..functions.funcoes import converter_string_para_float
import json

class Recebimento:

    def __init__(self, data, fornecedor, quantidade):
        self._data = data
        self._fornecedor = fornecedor
        self._quantidade = quantidade
        self._erro = ''

    @property
    def get_erro(self):
        return self._erro

    def validar(self):
        self.tratar_data()
        if not self._validar_quantidade():
            return False
        else: 
            return True

    @property
    def post(self):
        return json.dumps({"data": self._data, "fornecedor": self._fornecedor, "quantidade": self._quantidade})

    def tratar_data(self):
        self._data = self._data.toString('yyyy-MM-dd hh:mm')

    def _validar_quantidade(self):
        string = converter_string_para_float(self._quantidade)
        if not string:
            self._erro = 'Preencha o campo quantidade apenas com numeros ex.: 132.56'
            return False
        else:
            self._quantidade = string
            return True        
