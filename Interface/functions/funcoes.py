from datetime import datetime

def verificar_vazios_dict(dados):
    for dado in dados.values():
        if dado == '':
            return True
    return False

def preencher_cb(campo, dados):
    campo.clear()
    campo.addItem("")
    for dado in dados:
        campo.addItem(dado)

def datetimeNow():
    return datetime.now()

def converter_string_para_float(num):
    try:
        numero = num.replace(',', '.')
        return float(numero)
    except:
        return False
    