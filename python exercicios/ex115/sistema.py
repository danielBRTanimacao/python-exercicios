from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        print('opc 1')
    elif resposta == 2:
        print('opc 2')
    elif resposta == 3:
        cabecalho('\033[35mSaindo do sistema... até logo!\033[m')
        break
    else:
        print("\033[31mPor favor digite uma opção valida!\033[m")
    sleep(2)
