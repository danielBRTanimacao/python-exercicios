n = int(input("Quantos termos você que mostrar? ")) #numero de termos
t1 = 0 #
t2 = 1 # termos iniciais
print("~"*10)
print(f"{t1} -> {t2}", end='') #iniciu 0 -> 1
cont = 3 #contador do ultimo ponto
while cont <= n: #enquanto cont for menor ou igual a n
    t3 = t1 + t2 # termo 3 sera a soma dos termos anteriores
    print(f" -> {t3}", end='')
    t1 = t2 #para p proximos termos os termos anteriores passam a ser os termos novos por iso
    # t1 recebe t2 assim como t2 recebera t3
    t2 = t3
    cont += 1 #apenas contara
print(" -> Acabou")
