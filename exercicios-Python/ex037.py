#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('1 para Binário')
print('2 para Octal')
print('3 para Hexadecimal')
opcao = int(input('Qual será a base de conversão? '))
if opcao == 1:
    print('{} convertido para binário é: {}'.format(num, bin(num)[2:])) # [2:] <--- Significa q começará do segúndo dígito para frente
elif opcao == 2:
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))
elif opcao != 1 or 2 or 3:
    print('Você digitou um número fora dos valores para a base de conversão!')
    print('TENTE NOVAMENTE')
