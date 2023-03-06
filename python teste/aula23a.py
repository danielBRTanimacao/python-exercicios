'''cor = [
    '\033[31m',
    '\033[m',
    '\033[32m'
]'''
while True:
    try:
        a = int(input("Numerador: "))
        b = int(input("Denominador: "))
        r = a / b
    except (ValueError, TypeError):
        print("Tivemos um erro com os tipos de dados que você digitou")
    #   print(f"{cor[0]}Deu erro meu nobre :( foi esse {cor[1]}{cor[2]}<{erro.__class__}>{cor[1]}")
    except ZeroDivisionError:
        print("Não e possivel dividir um número por zero")
    except KeyboardInterrupt:
        print("O usuario não digitou")
    else:
        print(f'{r:.2f}')
        break
print("Muito obg volte sempre")