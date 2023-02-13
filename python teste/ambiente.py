'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c #pega o numero e faz vezes ele
    return f


n = int(input("Digite um número; "))
print(f"O fatorial de {n} é igual a {fatorial(n)}")
'''
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um valor: "))
if par(num):
    print('É PAR')
else:
    print("NÃO e par")
