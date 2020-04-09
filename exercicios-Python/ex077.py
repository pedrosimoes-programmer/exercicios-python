palavras = ('garrafa', 'caneca', 'celular', 'computador', 'teclado', 'mouse', 'gabinete', 'escova')
vogais = ('a', 'e', 'i', 'o', 'u')
c = 0
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()}, as vogais são ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')