valores = []
pares = []
ímpares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar a digitar valores? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Os valores digitados foram {valores}')
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores ímpares digitados foram {ímpares}')
