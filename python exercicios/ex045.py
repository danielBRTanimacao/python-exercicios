import random
from time import sleep
print("""Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jog = int(input("Qual a sua jogada? "))
itens = ['PEDRA', 'PAPEL', 'TESOURA']
comp = random.randint(0, 2)
sleep(1.2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(0.5)
print("-=-" * 9)
print(f"O computador jogou {itens[comp]}")
print(f"E você escolheu {itens[comp]}")
print("-=-" * 9)
if comp == 0: # pedra
    if jog == 0: # pedra
        print("Empate")
    elif jog == 1: #papel
        print("Jogador ganhou")
    elif jog == 2: #tesoura
        print("computador ganhou")
    else:
        print("Jogada invalida")
elif comp == 1: #papel
    if jog == 0: # pedra
        print("computador ganhou")
    elif jog == 1: #papel
        print("Empate")
    elif jog == 2: #tesoura
        print("Jogador ganhou")
    else:
        print("Jogada invalida")
elif comp == 2: #tesoura
    if jog == 0: # pedra
        print("Jogador ganhou")
    elif jog == 1: #papel
        print("computador ganhou")
    elif jog == 2: #tesoura
        print("Empate")
    else:
        print("Jogada invalida")