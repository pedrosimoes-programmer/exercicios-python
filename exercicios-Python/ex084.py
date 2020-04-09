dadosPessoas = []
dadoTemporario = []
c = maiorPeso = menorPeso = 0
while True:
    dadoTemporario.append(str(input('Nome: ')))
    dadoTemporario.append(float(input('Peso(KG): ')))
    dadosPessoas.append(dadoTemporario[:])
    if c == 0:  # Posso usar len(dadoTemporario) para fazer o contador
        maiorPeso = dadoTemporario[1]
        menorPeso = dadoTemporario[1]
    if dadoTemporario[1] > maiorPeso:
        maiorPeso = dadoTemporario[1]
    if dadoTemporario[1] < menorPeso:
        menorPeso = dadoTemporario[1]
    dadoTemporario.clear()
    c += 1
    r = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break
print('=' * 50)
print(f'Foram cadastradas {c} pessoas.')   # len(dadosPessoas) pode ser usado no lugar de Contador
print(f'O maior peso foi {maiorPeso} KG. Peso de', end=' ')
for c, p in enumerate(dadosPessoas):
    if p[1] == maiorPeso:
        print(f'{p[0]}...', end=' ')
print()
print(f'O menor peso foi {menorPeso} KG. Peso de', end=' ')
for c, p in enumerate(dadosPessoas):
    if p[1] == menorPeso:
        print(f'{p[0]}...', end=' ')
print()
