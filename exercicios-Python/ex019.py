from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
print('O aluno(a) sorteado(a) foi {}!'.format(choice([a1, a2, a3, a4])))