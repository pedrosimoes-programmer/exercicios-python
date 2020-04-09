n1 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze')
n2 = ('Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
números = n1 + n2
resposta = 's'
while True:
    if resposta in 'Ss':
        r = int(input('Digite um número entre 0 e 20: '))
        while r < 0 or r > 20:  # Forma 1
            r = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        print(f'Você digitou o número: {números[r]}')
    elif resposta in 'Nn':
        break
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

#while True:  # Forma 2
#    r = int(input('Digite  um número entre 0 e 20: '))
#    if 0 <= r <= 20:
#        break
#    print('Tente Novamente. ', end='')


