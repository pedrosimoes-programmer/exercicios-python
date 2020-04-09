cores = {'azul': '\33[34m',
         'amarelo': '\33[33m',
         'roxo': '\33[35m',
         'vermelho': '\33[31m',
         'verde': '\33[32m',
         'ciano': '\33[36m',
         'branco': '\33[30m',
         'limpador': '\33[m'}

valor = input('Digite algo: ')
print('O tipo primitivo do que você digitou é: {} '.format(type(valor)))

# Sem o .format
# print('O que vcoê digitou é alfa-numérico? ', valor.isalnum())
# print('O que você digitou é numérico? ', valor.isnumeric())
# print('O que você digitou é alfabético? ', valor.isalpha())
# print('O que você digitou é somente espaços? ', valor.isspace())
# print('O que você digitou está somente em maiúsculo? ', valor.isupper())
# print('O que você digitou está somente em minúsculo? ', valor.islower())
# print('O que você digitou está em maiúsculo e minúsculo? ', valor.istitle())

# Com o .format
print('É alfa-numérico? {}{}{} '.format(cores['azul'], valor.isalnum(), cores['limpador']))
print('É numérico? {}{}{} '.format(cores['amarelo'], valor.isnumeric(), cores['limpador']))
print('É alfabético? {}{}{} '.format(cores['roxo'], valor.isalpha(), cores['limpador']))
print('É somente espaços? {}{}{} '.format(cores['vermelho'], valor.isspace(), cores['limpador']))
print('Está somente em maiúsculo? {}{}{} '.format(cores['verde'], valor.isupper(), cores['limpador']))
print('Está somente em minúsculo? {}{}{} '.format(cores['ciano'], valor.islower(), cores['limpador']))
print('Está em maiúsculo e minúsculo? {}{}{} '.format(cores['branco'], valor.istitle(), cores['limpador']))


