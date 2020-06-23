from time import sleep
def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

def PyHELP():
    while True:
        titulo('SISTEMA DE AJUDA PyHELP')
        msg = str(input('Função ou Biblioteca: ')).strip()
        if msg.upper() == 'FIM':
            sleep(0.5)
            titulo('ATÉ LOGO')
            sleep(0.5)
            break
        sleep(0.5)
        titulo(f'ACESSANDO O MANUAL DO COMANDO {msg}')
        sleep(1)
        help(msg)
        sleep(2)


# Programa Principal
PyHELP()