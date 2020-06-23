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


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
