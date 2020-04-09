r = 's'
c = media = menor = maior = soma = 0
while r in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n  # Faz o maior e o menor valerem N
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / c
print('''Foram digitados {} números, a média entre eles foi {:.2f}, o MENOR valor lido foi {} e o MAIOR valor lido 
foi {}'''.format(c, media, menor, maior))
