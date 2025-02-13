import re

def somador_on_off(texto):
    ligado = True  # Inicialmente, o somador está ligado
    soma = 0

    # Percorre o texto palavra por palavra
    for item in re.findall(r'\d+|=|on|off', texto, re.IGNORECASE):
        if item.lower() == "off":
            ligado = False
        elif item.lower() == "on":
            ligado = True
        elif item == "=":
            print(soma)
        elif ligado and item.isdigit():
            soma += int(item)

# Exemplo de uso
entrada = input('Enter digits: ')  # Correção feita aqui
somador_on_off(entrada)