from random import randint
lista = []
jogos = []
quant = int(input("Quantos jogos você quer que eu sorteie: "))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1,61)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
