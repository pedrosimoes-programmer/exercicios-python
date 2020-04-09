dinheiro = float(input('\33[4;36mQuanto dinheiro você tem: R$\33[m'))
dolar = float(input('\33[4;31mO valor do dólar hoje: \33[m'))
print('\33[1;35mVocê poderia comprar: {:.1f} dólares!\33[m'.format(dinheiro/dolar))