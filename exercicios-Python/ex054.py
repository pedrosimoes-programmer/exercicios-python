# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
contadormaior = 0
contadormenor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - ano >= 21:
        contadormaior += 1
    else:
        contadormenor += 1
print('{} pessoas atingiram a maioridade e {} ainda não atingiram!'.format(contadormaior, contadormenor))
