#Funções (sem parâmetros)

def multiplicar():
    n1 = n2 = multi = 0
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    multi = n1 * n2
    print(f'A multiplicação é {multi}!')


def somar():
    n1 = n2 = soma = 0
    n1 = int(input('1º Número: '))
    n2 = int(input('2º Número: '))
    soma = n1 + n2
    print(f'A soma é {soma}!')


#Programa Principal
while True:
    print('''*****************************
                 (1) para SOMAR
                 (2) para MULTIPLICAR
                 (3) para sair''')
    userAnswer = int(input('O que deseja realizar: '))
    if userAnswer == 1:
        somar()
    elif userAnswer == 2:
        multiplicar()
    if userAnswer == 3:
        print('Obrigado e volte sempre!!!')
        break
