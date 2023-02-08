from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 números da lista...')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(.3)
    print("PRONTO!")

def somaPar(lista): #recebe uma lista tambem
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Sorteando os valores pares de {lista} temos {soma}")

numeros = list()
sorteia(numeros) #recebi os numeros da lista
somaPar(numeros)