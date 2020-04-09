#forma 1
cidade = input('Digite o nome da cidade: ').strip()
print('A sua cidade começa com Santo? ---> {}'.format(cidade[:5].upper() == 'SANTO'))

#forma 2
#cidade = input('Digite o nome da cidade: ')
#cidade = cidade.split()
#if cidade[0] == 'Santo' or 'SANTO' or 'santo':
#    print('A cidade escolhida começa com Santo')
#else:
#    print('A cidade escolhida não começa com Santo')
