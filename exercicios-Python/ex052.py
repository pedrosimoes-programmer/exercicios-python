# Número Primo = número ser divisível APENAS por 1 e por ele mesmo
divisivel = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
     divisivel += 1
     print('\33[33m', c, end='\33[m')
    else:
     print('\33[31m', c, end='\33[m')
if divisivel == 2:
    print('\nO número {} foi divisível {} vezes, e por isso \33[35mé um NÚMERO PRIMO\33[m'.format(n, divisivel)) # \n é uma quebra de linha
else:
    print('\nO número {} foi divisível {} vezes, e por isso \33[32mnão é um NÚMERO PRIMO\33[m'.format(n, divisivel))
