all = []
grades = []
provisoryName = list()
while True:
    provisoryName.append(str(input('Nome: ')))
    grades.append(float(input('Nota 1: ')))
    grades.append(float(input('Nota 2: ')))
    provisoryName.append(grades[:])
    all.append(provisoryName[:])
    provisoryName.clear()
    grades.clear()
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break
print('=' * 50)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for i, a in enumerate(all):
    print(f'{i:<4}{a[0]:<10}{(a[1][0] + a[1][1]) / 2:>8}')
print('=' * 30)
while True:
    answer = int(input('Digite o número do aluno que você quer ver as notas (999 para parar): '))
    if answer == 999:
        break
    print(f'As notas de {all[answer][0]} foram {all[answer][1]}')
    print('-' * 20)
print('Obrigado, volte sempre!')
print('     FINALIZANDO')
