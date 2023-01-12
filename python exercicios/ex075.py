num = (int(input("Digite um valor: ")) ,int(input("Digite outro valor: ")) ,int(input("Digite mais um valor: ")) ,
int(input("Digite penultimo valor: ")) ,int(input("Digite o ultimo valor: ")) ,)
print(f"Você digitou os valores {num}")
print(f"O número 9 apareceu {num.count(9)} vezes") #count conta quantas vezes algo apareceu
if 3 in num:
    print(f"O valor 3 apareceu na posição {num.index(3)+1}° posição")
else:
    print("O valor 3 não esta na tupla")
print("Os valores pares foram", end=' ')
for n in num: #lista os números pares
    if n % 2 == 0:
        print(n, end=' ')