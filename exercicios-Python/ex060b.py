from math import factorial
n = int(input('Digite o valor para calcular seu fatorial: '))
c = n
print('Fatorial de {}! ='.format(n), end=' ')
while c != 0:
    if c == 1:
        print('{}'.format(c), end=' ')
    else:
        print('{}'.format(c), end=' x ')
    c -= 1
print('= {}'.format(factorial(n)))
