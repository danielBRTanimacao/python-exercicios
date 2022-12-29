from time import sleep
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
print("Calculando...")
sleep(1.5)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima \033[1;32mPODEM\033[m formar um triangulo ", end='')
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISOCELES")
else:
    print("Os segmentos acima \033[1;31mNÃO\033[m podem formar um triangulo!")