valores = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        print('Valor adicionado ao final da lista')
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista')
                break
            pos += 1


print(f'Os valores digitados em ordem são{valores}')