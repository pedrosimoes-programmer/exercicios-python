#  Tratamento de Erros e Exceções

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Houve um problema com os tipos de dados que foi informado')
except ZeroDivisionError:
    print('Não é possível realizar a divisão por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar o restante dos dados')
except Exception as erro:
    print(f'O erro encotrado foi: {erro}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Agradecemos muito!')




# try: tente fazer alguma coisa
# expect: caso ocorra uma falha (exceção), o que vai ocorrer
# else: (cláusula opcional) caso o erro não ocorra, o que vai ocorrer
# finally: (cláusula opcional) ocorre, independente se der falha ou se ocorrer corretamente

#