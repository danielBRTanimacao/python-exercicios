'''help(input.__doc__)
help(input)
def contador(i, m, f):
    """
    -> Faz uma contagem e mostra na tela
    :parametro i: iniciu da minha contagem
    :parametro m: fim da minha contagem
    :parametro f: em quantos numeros ele ira pular
    :return : sem retorno
    """
    c = i
    while c <= m:
        print(f"{c}...", end='')
        c += f
    print("FIM!")


contador(2, 10, 2) #DOCsTRING 

def somar(a, b, c=0): #Parametro opcinal
    """
    -> Essa fução irar somar 3 valores
    :parametro a > ira receber um valor
    :parametro b > ira receber um valor
    :parametro c > ira receber um valor
    :return: nao retorna
    """
    soma = a + b + c
    print(f'A soma vale {soma}')


somar(2, 6, 3)

#ESCOPO DE VARIAVEIS
def teste():
    x = 8 #Escopo local
    print(f"O valor n vale {n}")
    print("")


n = 2 #escopo global
print(f"O valor n vale {n}")
teste()
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')

def funcao(b):
    global a
    a = 8
    b += 2
    c = 2
    print(f"a dentro recebe {a}")
    print(f"b dentro recebe {b}")
    print(f"c dentro recebe {c}")
a = 2
print(f"a fora recebe {a}")
funcao(a)
'''
#RETORNANDO VALORES
