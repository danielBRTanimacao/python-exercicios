def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Por favor digite um número inteiro!")
            continue
        except (KeyboardInterrupt):
            print("O usuario preferio não digitar")
            return 0
        else:
            return n


#programa principal
num = leiaInt('Digite um número: ')
print(f"O valor digitado foi {num}")
