# Palíndromo = frase que pode ser lida de trás pra frente = Ex: O lobo ama o bolo
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()  # Fatiar as palavras / espaços da frase
semespaços = ''.join(palavras)  # Juntar as palavras da frase fatiada anteriormente
inverso = ''

# Forma 1
for letra in range(len(semespaços) - 1, -1, -1):  # len(semespaços) = última letra/ -1 = até a primeira, -1 = -1 em -1
    inverso += semespaços[letra]

# Forma 2
# inverso = semespaços[::-1]
if inverso == semespaços:
    print('Temos um palíndromo!')
    print(semespaços)
    print(inverso)
else:
    print('A frase digitada não é um palíndromo!')
    print(semespaços)
    print(inverso)
