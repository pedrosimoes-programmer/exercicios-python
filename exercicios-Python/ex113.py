def leiaInt(msg):
    while True:
        try:
            n = str(input(msg))
            if n.isnumeric():
                break
        except ValueError:
            print('\33[31mERRO: por favor, digite um número inteiro válido.\33[m')
    return int(n)


def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg))
        except ValueError:
            print('\33[31mERRO: por favor, digite um número real válido.\33[m')
        else:
            if n.find('0123456789.,'):
                valorTrocado = n.replace(',', '.')
                break
    return float(valorTrocado)


# Programa Principal
int = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {int} e o real foi {real}')