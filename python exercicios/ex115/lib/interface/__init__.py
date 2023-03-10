def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mPor favor digite um número inteiro!\033[m")
            continue
        except (KeyboardInterrupt):
            print("O usuario preferio não digitar")
            return 0
        else:
            return n
        

def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[36m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua opção:\033[m ')
    return opc