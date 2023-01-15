'''num = [1, 2, 4, 8, 5]
num[2] = 6 #LISTA
num.append(9)
num.insert(3, 2)
if 20 in num:
    num.remove(20)
else:
    print('Número não foi encontrado')
num.sort(reverse=True)
#num.pop(3) #Remove o parametro final
print(num)
print(f'Essa lista tem {len(num)} elementos')
valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite o valor: ")))
valores.sort() #so para testar
for c, v in enumerate(valores):
    print(f"O valor {v}... Foi encontrado na posição {c}")
print("Fim")'''
