n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))
s = n1 + n2
sub = n1 - n2
d = n1 / n2
pot = n1 ** n2
multi = n1 * n2
di = n1 // n2
res = n1 % n2
print('A soma dos valores é: {}, a subtração dos valores é: {}, a multiplicação dos valores é: {}, a divisão dos valores é {:.3f}, \nA potenciação dos valores é: {:.3f}, a divisão inteira é: {} e o resto da divisão é: {}'.format(s, sub, multi, d, pot, di, res), end=' >>> ')
print('A divisão dos valores é: {:.3f},a potenciação dos valores é: {:.3f}, \na divisão inteira é: {} e o resto da divisão é: {} '.format(d, pot, di, res))
