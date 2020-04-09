#forma 1 (não é 100% funcional)
import math
#num = input('Digite um valor de 0 a 9999: ')
#if num > 9999:
    #print('Você digitou um número maior que 9999, tente novamente')

#print('Unidades: {}'.format(num[3]))
#print('Dezenas: {}'.format(num[2]))
#print('Centenas: {}'.format(num[1]))
#print('Milhares: {}'.format(num[0]))

#forma 2
num = int(input('Digite um número entre 0 a 9999: '))
if num > 9999:
    print('Você digitou um valor maior que 9999, tente novamente')
print('Unidades: {}'.format(num // 1 % 10))
print('Dezenas : {}'.format(num // 10 % 10))
print('Centenas: {}'.format(num/100 % 10))
print('Milhares: {}'.format(num/1000 % 10))
