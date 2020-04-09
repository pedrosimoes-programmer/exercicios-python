frase = input('Digite a sua frase: ').strip()
print('Letra A: {}'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição: {}'.format((frase.upper().find('A')+1)))
print('A letra A aparece pela última vez na posição: {}'.format(frase.upper().rfind('A')+1))
