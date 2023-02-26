from time import sleep #-----------------modulos-----------------#

c = ('\033[m',      # 0 - Sem cor
     '\033[31m',    # 1 - cor vermelha
     '\033[32m',    # 2 - cor verde
     '\033[33m',    # 3 - amarelo
     '\033[34m',    # 4 - Azul
     '\033[35m',    # 5 - Roxo
     '\033[7;30m'   # 6 - Branco
    )


def ajuda(com):
    titulo(f'acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print(f"~"* tam)
    print(f'  {msg}')
    print(f"~"* tam)
    print(c[0])
    sleep(1)


#-----------------programa principal-----------------#
comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else: 
        ajuda(comando)
titulo('Obrigado, até logo!', 1)