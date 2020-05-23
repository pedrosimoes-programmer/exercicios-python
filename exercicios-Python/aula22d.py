def par(n=1):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))

if par(num) == True:
    print('É par!')
else:   
    print('Não é par!')