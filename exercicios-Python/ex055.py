pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        pesomenor = peso
        pesomaior = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        elif peso < pesomenor:
            pesomenor = peso
print('O maior peso lido foi {}KG e o menor {}KG'.format(pesomaior, pesomenor))