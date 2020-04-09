teste = list()
teste.append('Pedro')
teste.append(15)
galera = list()
galera.append(teste[:])
teste[0] = 'Ronaldo'
teste[1] = '22'
galera.append(teste[:])
print(galera)
