class User:

    def __init__(self, cod, username, password, f_name, l_name, group ):
        self._id = cod
        self._username = username
        self._password = password
        self._first_name = f_name
        self._last_name = l_name
        self._groups = self.definir_group(group)

    def definir_group(self, group):
        groups = {
            1: 'Adiministrador',
            2: 'Funcionario',
            3: 'Desenvolvedor'
        }

        for g in groups.keys():
            if g == group[0]:
                return groups[group[0]]
  
        return 'Indefinido'

    @property
    def get_group(self):
        return self._groups

    @property
    def get_name(self):
        return f"{self._first_name} {self._last_name}"