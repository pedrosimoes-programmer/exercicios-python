from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que deseja: '))
angulo2 = radians(angulo)

print('O ângulo de {} tem o seno {:.2f}'.format(angulo, sin(angulo2)))
print('O ângulo de {} tem o cosseno {:.2f}'.format(angulo, cos(angulo2)))
print('O ângulo de {} tem a tangente {:.2f}'.format(angulo, tan(angulo2)))

