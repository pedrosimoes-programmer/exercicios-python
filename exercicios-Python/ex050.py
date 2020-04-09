soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print('Você informou {} valores pares e a soma deles foi: {}'.format(cont, soma))