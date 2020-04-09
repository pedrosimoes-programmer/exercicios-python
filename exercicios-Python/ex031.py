distancia = float(input('Digite a distância da sua viagem, em KM: '))
# forma 1
if distancia > 200:
    preço = 0.45 * distancia
else:
    preço = 0.50 * distancia

# forma 2
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua viagem é: R${:.2f}'.format(preço))
