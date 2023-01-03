'''from random import randint
from time import sleep
print("Oi seu seu computador...")
sleep(1)
print("Acabei de pensar em um número de 0 a 10")
sleep(1)
print("Sera que você consegui advinhar qual foi?")
sleep(1)
jn = int(input("qual e seu palpite? "))
num = randint(0, 10)
tent = 0
while jn != num:
    if jn < num:
        print("Mais... Tente mais uma vez!")
        tent += 1
    if jn > num:
        print("Menor... Tente mais uma vez!")
        tent += 1
    jn = int(input("qual e seu palpite? "))
print(f"Parabens você acertou apos {tent} tentativas")
print("Acabou")'''

#ou
from random import randint
pc = randint(0, 10)
acertou = False
palpites = 0
while not acertou: #enquanto não acertou
    jg = int(input("Qual seu palpite: "))
    palpites += 1
    if jg == pc:
        acertou = True
print("Acertou")
print(f"O numeros de tentativas foi de {palpites}")