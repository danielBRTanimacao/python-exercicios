'''from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(n)
print(f"o fatorial de {n}! é {f}")
OU ESSE >>>>>>
n = int(input("Digite um número para calcular seu fatorial: "))
c = n #fatorial de c começa com n
f = 1
print(f"Calculando {n}! =", end=' ')
while c > 0:
    print(c, end=' ')
    if c > 1:
        print("x", end=' ')
    else:
        print("=", end=' ')
    f *= c
    c -= 1
print(f"{f}")
Agora esse>>>>>'''
n = int(input("Digite um número para calcular seu fatorial: "))
f = 1
for c in range(n, 0, -1):
    print(c, end=' ')
    if c > 1:
        print("x", end=' ')
    else:
        print("=", end=' ')
    f *= c
    c -= 1
print(f"{f}")