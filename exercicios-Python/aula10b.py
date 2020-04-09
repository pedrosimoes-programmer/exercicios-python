n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi: {:.1f}'.format(m))

#forma 1
#if m >= 7:
#    print('Parabéns, continue assim!')
#else:
#    print('ESTUDA MAIS CARALHO!')

#forma 2
print('Parabéns, continue assim!' if m >= 7 else 'ESTUDA MAIS CARALHO!')
