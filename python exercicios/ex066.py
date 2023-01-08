soma = count = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    count += 1
    soma += n
print(f"Você digitou {count} números e a soma entre eles foi {soma}")