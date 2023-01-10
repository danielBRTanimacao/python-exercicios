'''() TUPLA [] LISTA {} DICIONARIO
lanche = ('Hamburguer', 'Suco','Pizza', 'Pudim', 'Danonão grosso')
lanche[1] = 'Suco' >>>>> imutavel
            >>>>> TUPLAS SÃO IMUTAVEIS
print(lanche[1])

for comida in lanche:
    print(lanche) >>>>> MAIS SIMPLES

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} e a posicão {pos}")

for cont in range(0, len(lanche)): >>>>>>>> MESMO COISA DO DE CIMA
    print(f"lanche[cont] e na posição {cont}")
print("Fim do programa")

lanche = ('Hamburguer', 'Suco','Pizza', 'Pudim', 'Danonão grosso')
#sorted organizar
print(sorted(lanche))'''

#Tuplas com números
a = (1, 2, 3, 4)
b = (5, 2, 7, 2)
c = a + b
#print(c.count(2)) conta quantas vexes apareceu o número
print(c)
print(c.index(5)) #virgula para ver a posição de outro número , 1
