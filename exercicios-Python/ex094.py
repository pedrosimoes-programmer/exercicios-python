allPeople = []
soma = mulheresTot = 0
mulheresNomes = []
while True:
    person = dict()
    person['Nome'] = str(input('Nome: '))
    person['Idade'] = int(input('Idade: '))
    #Ideia de Implementação de verificação: se idade for número, continua, se não, looping infinito!
    #if not person['Idade'].isnumeric():
        #while True:
            #print('ERRO! Digite apenas números!')
            #person['Idade'] = int(input('Idade: '))
            #if person['Idade'].isnumeric():
                #break
    soma += person['Idade']
    person['Sexo'] = str(input('Sexo[M/F]: '))[0].upper().strip()
    if person['Sexo'] not in 'FM':
        while True:
            print('ERRO! Digite apenas M ou F!')
            person['Sexo'] = str(input('Sexo[M/F]: '))[0].upper().strip()
            if person['Sexo'] in 'MF':
                break
    if person['Sexo'] == 'F':
        mulheresTot += 1
        mulheresNomes.append(person['Nome'])
    allPeople.append(person)
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r not in 'SN':
        while True:
            print('ERRO! Digite apenas S ou N!')
            r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
            if r in 'NS':
                break
    if r == 'N':
        break
media = soma / len(allPeople)
print('=' * 50)
print(f'Foram cadastradas {len(allPeople)} pessoas.')
print(f'A média de idade do grupo é {media:.2f} anos.')
print(f'Foram cadastradas {mulheresTot} mulheres, as quais foram {mulheresNomes}.')
print(f'>- Lista das pessoas com idade acima da média: ')
for p in allPeople:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
print('<= Obrigado e Volte Sempre! >=')
print('     >>> ENCERRADO <<< ')
