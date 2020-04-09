#Para ordenar um dicionário, é necessário aplicar os seguintes comandos:
#1= importar a função itemgetter, da biblioteca operator
#2= criar um novo dicionário para guardar os valores ordenados
#3= usar a função Sorted, da váriavel.items que quero ordenar
#4= identificar qual chave quero ordenar, 0, 1
#5= OPCIONAL: caso queira do maior pro menor, usar o reverse=True
#5= COMANDO = váriavelOrdenada = sorted(váriavelPadrão.items(), key=itemgetter(1))
from operator import itemgetter
from random import randint
num = {'jogador1': randint(1, 6),
       'jogador2': randint(1, 6),
       'jogador3': randint(1, 6),
       'jogador4': randint(1, 6)}
numOrdenado = sorted(num.items(), key=itemgetter(1), reverse=True)
print(numOrdenado)
