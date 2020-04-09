n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
# Maior
if n1 > n2 and n1 > n3:
    print('O maior número é: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior número é: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número é: {}'.format(n3))

# Menor
if n1 < n2 and n1 < n3:
    print('O menor número é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor número é: {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número é: {}'.format(n3))

