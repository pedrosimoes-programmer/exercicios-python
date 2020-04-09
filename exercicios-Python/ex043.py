#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
print('-' * 20, 'Programa de IMC', '-' * 20)
peso = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura (METROS): '))
imc = peso / (altura * altura) #Altura = (RAIZ QUADRADA de ALTURA) altura ** 2
if imc < 18.5:
    print('Seu IMC é: {:.1f}'.format(imc))
    print('CUIDE-SE URGENTEMENTE!')
    print('\33[31mVocê está ABAIXO DO PESO!\33[m')
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é: {:.1f}'.format(imc))
    print('PARABÉNS!')
    print('\33[34mVocê está com o PESO IDEAL!\33[m')
elif imc > 25 and imc < 30:
    print('Seu IMC é: {:.1f}'.format(imc))
    print('CUIDADO!')
    print('\33[33mVocê está com SOBREPESO!\33[m')
elif imc > 30 and imc < 40:
    print('Seu IMC é: {:.1f}'.format(imc))
    print('CUIDE-SE!')
    print('\33[35mVocê está com OBESIDADE!\33[m')
elif imc > 40:
    print('Seu IMC é: {:.1f}'.format(imc))
    print('CUIDE-SE URGENTEMENTE!')
    print('\33[30mVocê está com OBESIDADE MÓRBIDA!\33[m')