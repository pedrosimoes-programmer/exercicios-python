n = soma = c = 0  # Faz todos os valores receberem 0
while n != 999:
    n = int(input('Digite um número [PARA PARAR: 999]: '))
    if n != 999:
        soma += n
        c += 1
print('Foram digitados {} números e a soma entre eles foi {}'.format(c, soma))
