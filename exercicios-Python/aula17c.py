a = [1, 2, 3, 4]
b = a  # Criar uma cópia da lista, desse jeito, o Pyhton fez uma ligação entre as listas,
# por isso se eu trocar um valor da b, ele troca da a, CUIDADO!
b[3] = 6
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b = a[:]
b[3] = 20
print(f'Lista A: (Original) {a}')
print(f'Lista B (Cópia): {b}')