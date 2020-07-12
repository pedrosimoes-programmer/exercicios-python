def leiaDinheiro(msg):
    valorMonetario = 0
    validacao = False
    while True:
        entrada = str(input(msg)).strip()
        if entrada.isalpha() or entrada.isupper() or entrada.islower() or entrada == '':
            print(f'\33[31mERRO!!! \"{entrada}\" não é um valor monetário válido!\33[m')
        elif entrada.find('0123456789.,'):
            validacao = True
            valorTrocado = entrada.replace(',', '.')
            valorMonetario = float(valorTrocado)
        if validacao:
            break
    return valorMonetario


def leiaInt(msg):
    validacao = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            validacao = True
            valor = int(n)
        else:
            print('ERRO! Digite um número inteiro válido!')
        if validacao:
            break
    return valor
