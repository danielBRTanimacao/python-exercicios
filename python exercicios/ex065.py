resp = 'S'
media = soma = total = maior = menor = 0
while resp in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    total += 1
    if total == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    resp = str(input("Deseja continuar? [s/n]: ")).upper().strip()[0]
media = soma / total
print(f"Você digitou {total} números e a media foi {media:.0f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")