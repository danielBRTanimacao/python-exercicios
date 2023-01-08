from random import randint
v = 0
while True:
    jogador = int(input("Digite o valor: "))
    computador = randint(1, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou impar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total {total}")
    print("DEU PAR" if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print("Você venceu!")
            v += 1
        else:
            print("Você perdeu!")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("Você venceu!!")
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente")
