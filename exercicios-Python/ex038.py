#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
n1 = float(input('\33[34mDigite o primero valor: \33[m'))
n2 = float(input('\33[36mDigite o segundo valor: \33[m'))

if n1 > n2:
    print('\33[31;4mO primeiro valor é maior: {} > {}\33[m'.format(n1, n2))
elif n2 > n1:
    print('\33[32;1mO segundo valor é maior: {} > {}\33[m'.format(n2, n1))
else:
    print('\33[35;4mNão existe valor maior, os dois são iguais: {} = {}\33[m'.format(n1, n2))
