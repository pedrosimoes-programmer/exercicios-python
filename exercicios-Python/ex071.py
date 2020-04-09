#  Programa Simulador de Caixa Eletrônico
#  O caixa possui cédulas de 50, 20, 10 e 1
# Forma 1 = MINHA FORMA, COMPLICADA, MEIO NO CHUTE
print('=' * 50)
print('{:^50}'.format(' BANCO SIMÕES '))
print('=' * 50)
valor = int(input('Qual valor você quer sacar: R$'))
while True:
    if valor % 50 != 1:
        if valor // 50 > 0:
            print(f'Total de {valor//50} cédulas de R$50,00')
        valor = valor - (valor // 50) * 50
        if (valor // 50) * 50 - valor == 0:
            break
    if valor % 20 != 1:
        if valor // 20 > 0:
            print(f'Total de {valor//20} cédulas de R$20,00')
        valor = valor - (valor // 20) * 20
        if (valor // 20) * 20 - valor == 0:
            break
    if valor % 10 != 1:
        if valor // 10 > 0:
            print(f'Total de {valor//10} cédulas de R$10,00')
        valor = valor - (valor//10) * 10
        if (valor // 10) * 10 - valor == 0:
            break
    if valor % 1 == 0:
        if valor // 1 > 0:
            print(f'Total de {valor//1} cédulas de R$1,00')
        valor = (valor // 1) * 1 - valor == 0
        if (valor // 1) * 1 - valor == 0:
            break
print('=' * 50)
print('Obrigado, volte sempre ao BANCO SIMÕES!')

#FORMA 2: Curso em Vídeo, SIMPLES
print('=' * 50)
print('{:^50}'.format(' BANCO SIMÕES '))
print('=' * 50)
valor = int(input('Qual valor você quer sacar: R$'))
total = valor  # Total do montante a ser sacado, que começa valendo o valor digitado pelo usuário
cedula = 50  # A primeira cédula a ser verificada é 50
totalCedulas = 0  # Contagem de cédulas
while True:
    if total >= cedula:  # Se o total for maior que o valor da cédula, retiro do total uma cédula e o totalCédulas é +1
        total -= cedula
        totalCedulas += 1
    else:  # Se não conseguir retirar o do total uma cédula
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R${cedula},00')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:  # Tem que ser elif, se não, o programa entra em conflito com os valores e vai a R$1 direto
            cedula = 10
        elif cedula == 10:  # Tem que ser elif, se não, o programa entra em conflito com os valores e vai a R$1 direto
            cedula = 1
        totalCedulas = 0  # Sempre que o valor da cédula for trocado, o total de cédulas volta a 0
        if total == 0:
            break
print('=' * 50)
print('Obrigado, volte sempre ao BANCO SIMÕES!')
