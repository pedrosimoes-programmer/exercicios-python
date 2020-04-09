#Faça um programa que calcule a soma entre todos os números ímpares, entre 1 e 500, que são múltiplos de 3
soma = 0
somavalores = 0
for c in range(1, 501): # outra forma: for c in range (1, 501, 2)
    if c % 3 == 0:  # múltiplo de 3
        if c % 2 != 0:  # ímpar
            soma += c
            somavalores += 1
print('\33[34mA soma de todos os {} valores foi: {}\33[m'.format(somavalores, soma))
