from random import randint
pc = (randint(1, 10) ,randint(1, 10) ,randint(1, 10) ,randint(1, 10) ,randint(1, 10))
print(f"Eu sortiei os valores:", end=' ') #Outra maneira de fazer
for n in pc:
    print(f" {n} ", end='')
print(f"\nO maior numero sorteado foi {max(pc)}") #max pode ser usado em tuplas
print(f"O menor valor foi {min(pc)}")