valores = list()
valores.append(2)
valores.append(5)
valores.append(0)
valores.append(1)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei {v}!')
print('Cheguei ao final da lista!')