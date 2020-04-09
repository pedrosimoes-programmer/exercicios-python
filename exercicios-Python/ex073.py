times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Botafogo', 'Fluminense', 'Ceará', 'Cruzeiro', 'CSA',
         'Chapecoense', 'Avaí')
print('=' * 20)
print('Lista de Times do Brasileirão 2019')
print('=' * 20)
print(f'Os 5 primeiros colocados são {times[:5]}')
print(f'Os 4 últimos colocados são {times[-4:]}')
print('Times em ordem alfabética: ', sorted(times))
print(f'A Chapecoense está em {times.index("Chapecoense")+1}º lugar')

# Outra FORMA:
#for posição, time in enumerate(times):
#    print(f'{posição+1}º {time}')
#print('\nOs 5 primeiros colocados são: ')
#for c in range(0, 5):
#    print(f'{c+1}º {times[c]}')
#print('\nOs 4 últimos colocados são: ')
#for c in range(16, 20):
#    print(f'{c+1}º {times[c]}')
#for posição, time in enumerate(times):
#    if time in 'Chapecoense':
#        print(f'A Chapecoense está em {posição+1}º lugar')
