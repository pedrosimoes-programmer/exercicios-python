from time import sleep
resposta = 0
n1 = int(input('Digite o valor do 1º número: '))
n2 = int(input('Digite o valor do 2º número: '))
while resposta != 5:
    resposta = int(input('''MENU:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa

    Digite o que quer fazer: '''))
    if resposta == 1:
        soma = n1 + n2
        print('A soma de {} + {} foi: {}'.format(n1, n2, soma))
    elif resposta == 2:
        multi = n1 * n2
        print('A multiplicação de {} x {} foi: {}'.format(n1, n2, multi))
    elif resposta == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
    elif resposta == 4:
        n1 = int(input('Digite o valor do 1º número novamente: '))
        n2 = int(input('Digite o valor do 2º número novamente: '))
    elif resposta == 5:
        print('FINALIZANDO...')
        sleep(2)
        print('Adeus! Volte sempre!')
    else:
        print('Opção Inválida! Tente novamente!')