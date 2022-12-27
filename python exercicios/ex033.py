n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))
menor = n1 #menor numero
if n2 < n1 and n3 < n2:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# maior numero agora
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f"O MAIOR número é {maior}")
print(f"O MENOR número é {menor}")