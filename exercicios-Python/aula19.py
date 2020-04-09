estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Digite o nome do estado: '))
    estado['sigla'] = str(input('Digite a sigla do estado: '))
    brasil.append(estado.copy())
# Forma 1: for state in brasil:
    # Forma 1: print(f'O nome do estado é {state["uf"]} e sua sigla é {state["sigla"]}.')
#Forma 2:
for state in brasil:
    for v in state.values():
        print(v, end=' ')
    print()
