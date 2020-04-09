# Sequência de Fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print('Sequência de Fibonacci')
print('-=' * 20)
termos = int(input('Quantos termos você quer ver: '))
c = 3
n1 = 0
n2 = 1
print('{} -> {}'.format(n1, n2), end=' -> ')
while c <= termos:
    n3 = n1 + n2
    print(n3, end=' -> ')
    n1 = n2
    n2 = n3
    c += 1
print('FIM')
