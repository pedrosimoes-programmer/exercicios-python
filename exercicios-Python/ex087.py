matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maiorSegunda = somaTerceira = 0
for coluna in range(0, 3):
    for linha in range(0, 3):
        matriz[coluna][linha] = int(input(f'Digite um valor para a posição [{coluna}, {linha}]: '))
        if matriz[coluna][linha] % 2 == 0:
            pares += matriz[coluna][linha]
        if linha == 2:
            somaTerceira += matriz[coluna][linha]
        if coluna == 1:
            if matriz[coluna][linha] > maiorSegunda:
                maiorSegunda = matriz[coluna][linha]
print('=' * 50)
for coluna in range(0, 3):
    for linha in range(0, 3):
        print(f'[{matriz[coluna][linha]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares foi {pares}.')
print(f'A soma dos valores da terceira coluna foi {somaTerceira}.')
print(f'O maior valor da segunda linha foi {maiorSegunda}.')
