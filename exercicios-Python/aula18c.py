galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 5):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])  # Se não tiver [:], criará listas vazias, pq ele faz uma interligação, invés de uma cópia
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print('=' * 50)
if totmaior > 1 and totmenor > 1:
    print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
elif totmaior > 1 and totmenor <= 1:
    print(f'Temos {totmaior} maiores e {totmenor} menor de idade.')
elif totmaior <= 1 and totmenor > 1:
    print(f'Temos {totmaior} maior e {totmenor} menores de idade.')
elif totmaior <= 1 and totmenor <= 1:
    print(f'Temos {totmaior} maior e {totmenor} menor de idade.')
