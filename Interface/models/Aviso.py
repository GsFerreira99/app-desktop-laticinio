class Aviso:

    def __init__(self, campo) -> None:
        self._mensagem = ''
        self._campo = campo

        self._tipo = {
            "danger" : "color: #721c24; border-radius:10px;    background-color: #f8d7da;    border-color: #f5c6cb;",
            "warning" : "color: #856404; border-radius:10px;    background-color: #fff3cd;    border-color: #ffeeba;",
            "info" : "color: #0c5460; border-radius:10px;    background-color: #d1ecf1;    border-color: #bee5eb;",
            "success" : "color: #155724; border-radius:10px;    background-color: #d4edda;    border-color: #c3e6cb;",
        }
        self.exibicao(False)

    def exibicao(self, status):
        if status:
            self._campo.setMaximumHeight(40)
        else:
            self._campo.setMaximumHeight(0)

    def exibir_aviso(self, tipo, msg):
        self.exibicao(True)
        self._campo.setStyleSheet(self._tipo[tipo])
        self._campo.setText(msg)

