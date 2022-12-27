'''for c in range(1, 10):
    print(c)
print("Acabou")'''
'''r = 's'
while n != 0:
    n = int(input("Digite um número: "))
print("Fim")'''

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"A quantidade de números pares digitados foram de {par} e de impares {impar}")