import requests


def urlOk(url):
    try:
        r = requests.head(url)
    except Exception as ConnectionError:
        return False
    else:
        if r.status_code == 200:
            return True



# Programa Principal

urlPudim = 'http://pudim.com.br'
resposta = urlOk(urlPudim)
if resposta is True:
    print(f'\33[33mO site do Pudim está acessível\33[m')
elif resposta is False:
    print('\33[31mO site do Pudim não está acessível no momento\33[m')


# OUTRA SOLUÇÃO

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site do Pudim não está acessível no momento')
else:
    print('O site do Pudim foi acessado com sucesso')
    site.read()  # Função para pegar o conteúdo HTML do site que foi acessado
