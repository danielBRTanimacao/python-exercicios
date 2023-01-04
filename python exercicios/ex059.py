v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite um segundo valor: "))
print("-=-"*12)
c = 1
while c != 5:
    print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa")
    c = int(input(">>>>>> Qual sua escolha? "))
    if c == 1:
        print(f"A soma de {v1} + {v2} = {v1+v2}")
    if c == 2:
        print(f"A multiplicação de {v1} x {v2} = {v1*v2}")
    if c == 3:
        if v1 < v2:
            maior = v2
            print(f"O maior número e {maior}")
        else:
            maior = v1
            print(f"O maior e {maior}")
    if c == 4:
        print("Informe os números novamente...")
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite um segundo valor: "))
    if c < 1 and c > 5:
        print("Por favor tente de novo")
print("Acabou")
    