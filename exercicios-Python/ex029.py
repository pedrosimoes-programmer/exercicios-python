# Multa = 7,00 por KM acima de 80km/h
import math
velocidade = float(input('Em que velocidade você está com o seu carro: '))
if velocidade > 80:
# não é necessário  ---->   valorexc = velocidade - 80  # Calcula o quanto o motorista passou do limite
    multa = (velocidade - 80) * 7  # Valor da multa
    print('Você foi multado, a multa custará: R${:.2f}'.format(multa))
else:
    print('Siga normalmente!')
