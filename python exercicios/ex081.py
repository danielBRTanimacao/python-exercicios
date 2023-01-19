valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    per = str(input("Deseja continuar?[S/N] ")).lower().strip()[0]
    if per in 'n':
        break
print("-="*25)
print(f"Você digitou os valores {valores}")
if 5 in valores:
    print("O número 5 esta presente na lista")
else:
    print("O número 5 NÃO esta na lista")
valores.sort(reverse=True)
print(f"Os valores em ordem descrecentes são {valores}")