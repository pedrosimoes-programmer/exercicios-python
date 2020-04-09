valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar digitando valores [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Foram digitados {len(valores)} elementos')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente é {valores}')
if valores.count(5) == 1:
    print(f'O valor 5 foi digitado {valores.count(5)} vez e está na lista na posição ', end='')
    for i, v in enumerate(valores):
        if v == 5:
            print(f'{i}', end=' ')
elif valores.count(5) > 1:
    print(f'O valor 5 foi digitado {valores.count(5)} vezes e está na lista nas posições ', end='')
    for i, v in enumerate(valores):
        if v == 5:
            print(f'{i}...', end=' ')
else:
    print('O valor 5 não está na lista e não foi digitado.')

