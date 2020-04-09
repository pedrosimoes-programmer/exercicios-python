#forma 1
#from random import shuffle
#a1 = input('Primeiro aluno: ')
#a2 = input('Segundo aluno: ')
#a3 = input('Terceiro aluno: ')
#a4 = input('Quarto aluno: ')
#lista = [a1, a2, a3, a4]
#random.shuffle(lista)
#print('A ordem de apresentação será: {}'.format(lista))

#forma 2 (A melhor forma)
from random import sample
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = sample([a1, a2, a3, a4], k=4)
print('A ordem de apresentação será: {}'.format(lista))

#forma 3
#from random import choice
#a1 = input('Primeiro aluno: ')
#a2 = input('Segundo aluno: ')
#a3 = input('Terceiro aluno: ')
#a4 = input('Quarto aluno: ')
#lista = [a1, a2, a3, a4]
#primeiro  = choice(lista)
#print('O primeiro aluno a apresentar será: {}'.format(primeiro))
#lista.remove(primeiro)
#segundo  = choice(lista)
#print('O segundo aluno a apresentar será: {}'.format(segundo))
#lista.remove(segundo)
#terceiro = choice(lista)
#print('O terceiro aluno a apresentar será: {}'.format(terceiro))
#lista.remove(terceiro)
#quarto = choice(lista)
#print('O último aluno a apresentar será: {}'.format(quarto))
#lista.remove(quarto)


