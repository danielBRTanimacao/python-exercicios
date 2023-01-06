cont = c = soma = 0
c = int(input("Digite um numero, digite[999] para parar: "))
while c != 999:
    soma += c
    cont += 1
    c = int(input("Digite um numero, digite[999] para parar: "))
print(f"Você digitou {cont} números")
print(soma)
