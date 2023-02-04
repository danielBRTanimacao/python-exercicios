'''def soma(a, b):
    print(f"O valor de A = {a} e o valor de B = {b}")
    s = a + b
    print(f'A soma de A + B = {s}')


#programa principal
soma(b=9, a=4)
def contador(*num):
    print(num)
contador(4, 5 , 7, 3, 6, 0)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 4, 6, 8, 5, 2]
dobra(valores)
print(valores)
'''
def soma(* num):
    s = 0
    for valores in num:
        s += valores
    print(f'Somando os valores {num} e igual a {s}')


soma(2, 4)
soma(3, 2, 1)
