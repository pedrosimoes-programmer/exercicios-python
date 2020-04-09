valorM = float(input('\33[1;31mDigite o valor desejado, em metros: \33[m'))
#print('O valor desejado em centímetros ficaria: {} e em milímetros: {}'.format(valorM*100, valorM*1000))
print('\33[4;33m{}Km \n {}Hm \n {}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm\33[m'.format(valorM/1000, valorM/100, valorM/10, valorM*10, valorM*100, valorM*1000))
