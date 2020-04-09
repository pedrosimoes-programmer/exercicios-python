# As TUPLAS são imutáveis, dentro do programa
times = ('Palmeiras', 'Flamengo', 'São Paulo', 'Santos', 'Corinthians', 'Fluminense', 'Cruzeiro', 'Grêmio')
a = (1, 2, 3, 4, 8)
b = (5, 6, 7, 8)
c = a + b
print(c)  # A ordem altera os fatores em tuplas
c = b + a
print(c)  # A ordem altera os fatorem em tuplas

pessoa = ('Pedro', 15, 'M', 85.5)  # Tuplas podem receber vários tipos de dados, como: String, Integer, etc
print(pessoa)
#del pessoa  # A função Del serve para apagar algo da memória do Python, NÃO POSSO APAGAR APENAS UM ITEM DA TUPLA
print(pessoa)


# Propriedas internas:

print(c.count(8))  # Conta quantos elementos há na minha tupla = Count
print(c.index(8))  # Mostra a posição em que o elemento está = Index, mostra a posição do PRIMEIRO ELEMENTO
print(c.index(8, 4))  # Index que mostra a posição  do segundo elemento, começa a contar a partir da 4ª posição



print(times)
print(times[0])
print(times[:5])
print(times[0:7])
print(times[2:])
print(times[-2])
print(times[-4:])
c = 1
print('Times:', len(times))
for time in times:  # Forma 1, com posição
    print(f'{c}º lugar {time}')
    c += 1
for c in range(0, len(times)):  # Forma 2, sem posição
    print(times[c])
for c, time in enumerate(times):  # Forma 3, com posição (enumerate)
    print(f'{c}º lugar {time}')


print(sorted(times))  # Organizar em ordem alfabética = Sorted