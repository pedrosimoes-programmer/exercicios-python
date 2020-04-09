# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaIdades = 0
mediaIdades = 0
nomeVelho = ''
idadeHomemVelho = 0
mulheresMenores = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}ª pessoa: M = (Masculino) F = (Feminino) '.format(c)))
    somaIdades += idade
    if sexo == 'F' or 'f':
        if idade < 20:
            mulheresMenores += 1
    elif sexo == 'M' or 'm': # Sexo in 'Mm' <- outra possibilidade
        if idade > idadeHomemVelho:
            idadeHomemVelho = idade
            nomeVelho = nome
mediaIdades = somaIdades / 4
print('''A média da idade do grupo foi {}, o nome do homem mais velho é {} e ele tem {} anos
e há {} mulheres menores de 20 anos'''.format(mediaIdades, nomeVelho, idadeHomemVelho, mulheresMenores))