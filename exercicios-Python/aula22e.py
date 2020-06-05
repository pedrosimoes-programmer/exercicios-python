def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


n = int(input('Valor fatorial: '))
print(f'O fatorial de {n} é {fatorial(n)}')