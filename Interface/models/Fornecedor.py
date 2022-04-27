class Fornecedor:

    def __init__(self, cod, nome):
        self._id = cod
        self._nome = nome

    @property
    def get_nome(self):
        return self._nome

    def __str__(self):
        return self._nome