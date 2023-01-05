'''n = int(input("Digite um número: "))
cont = 0
while True:
    if cont != n:
        cont += 1
        print(cont, '-> ', end="")
    if cont == n:
        break
print("Acabou")'''
s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"Acabou e a soma vale {s}")
