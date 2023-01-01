pares = 0 #par e zero pois o resto do número par e == 0 ex: num % 2 == 0
for c in range(1, 7):
    num = int(input(f"Digite o {c}° numero: "))
if c % 2 == 0: #se o resto da divisão c for igual a 0
    pares += c #não entendi
print(f"A soma dos numeros pares são {pares}")