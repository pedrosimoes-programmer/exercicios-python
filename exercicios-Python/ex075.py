números = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
pares = 0
cont = 0
print(f'Você digitou os valores {números}')
if números.count(9) == 1:
    print(f'O número 9 apareceu {números.count(9)} vez.')
elif números.count(9) >= 1:
    print(f'O número 9 apareceu {números.count(9)} vezes.')
else:
    print(f'O número 9 não apareceu nenhuma vez.')
if números.count(3) == 0:
    print(f'O número 3 não foi digitado em nenhuma posição.')
else:
    if números.index(3) > 0:
        print(f'O primeiro número 3 foi digitado na {números.index(3)+1}ª posição.')
for n in números:
    if cont == 0:
        if n % 2 == 0:
            print(f'Os números pares digitados foram {n}', end=' ')
            pares += 1
            cont += 1
    else:
        if cont > 0:
            if n % 2 == 0:
                print(f'{n}', end=' ')
if pares == 0:
    print('Não foi digitado nenhum valor par.')



