#O quadrado da hipotenusa é igual a soma dos quadrados dos catetos

#forma 1
#from math import sqrt
#catOpos = float(input('Comprimento do cateto oposto: '))
#catAdja = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = (catOpos**2) + (catAdja**2)
#print('A hipotenusa vai medir: {:.2f}'.format(sqrt(hipotenusa)))

#forma 2

from math import hypot
catOpos = float(input('Comprimento do cateto oposto: '))
catAdja = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa medirá: {:.2f}'.format(hypot(catOpos, catAdja)))
