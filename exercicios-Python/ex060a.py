from math import factorial
n = int(input('Digite um  número para calcular seu Fatorial: '))
print('Fatorial de {}! = '.format(n))
for c in range(n, 0, -1):
    if c == 1:
        print('{}'.format(c), end=' ')
    else:
        print('{}'.format(c), end=' x ')
print('= {}'.format(factorial(n)))
