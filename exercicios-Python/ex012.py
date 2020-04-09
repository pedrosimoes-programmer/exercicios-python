preço = float(input('Preço do produto: '))
desc = preço - (preço*(5/100))
print('O preço do produto era: R${}, com 5% de desconto é: R${:.2f}'. format(preço, desc))
