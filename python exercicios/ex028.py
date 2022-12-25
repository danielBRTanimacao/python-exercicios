from random import randint
from time import sleep
num = randint(0, 5)
print("-=-" * 30)
print("VAMOS JOGAR UM JOGO DE ADVINHAÇÃO, TENTE ADIVINHAR O NÚMERO QUE IREI PENSAR ENTRE 0 E 5!!")
print("-=-" * 30)
sleep(2)
n = int(input("DIGITE O NÚMERO QUE VOCÊ ACHA QUE EU PENSEI! "))
print("--" * 10, "PROCESSANDO", "--" * 10)
sleep(1.5)
if n == num:
    print(f"PARRABENS VOCÊ ACERTOU O NÚMERO ESCOLHIDO QUE ERA {num}")
else:
    print(f"VOCÊ ERROU!! o número escolhido foi {num} ja o que você escolheu era {n}")
sleep(2)
print("=" * 10 ,"OBRIGADO POR JOGAR!!", "=" * 10)
