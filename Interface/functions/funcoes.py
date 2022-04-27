def verificar_vazios_dict(dados):
    for dado in dados.values():
        if dado == '':
            return True
    return False