from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'curso_em_video.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #opção listar conteudo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo cadastro')
        nome = str(input("Nome: "))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('\033[35mSaindo do sistema... até logo!\033[m')
        break
    else:
        print("\033[31mPor favor digite uma opção valida!\033[m")
    sleep(2)
