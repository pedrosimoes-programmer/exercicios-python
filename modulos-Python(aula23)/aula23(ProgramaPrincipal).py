import funcoes

#Programa Principal
num = int(input('Digite um número: '))
fat = funcoes.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {funcoes.dobro(num)}')
