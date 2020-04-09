valores = [[], []]
for v in range(0, 7):
    v = int(input('Digite um valor: '))
    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)
valores[0].sort()
valores[1].sort()
print('=' * 50)
print(f'Os valores pares digitados foram {valores[0]}')
print(f'Os valores ímpares digitados foram {valores[1]}')
