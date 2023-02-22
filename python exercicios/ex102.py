def fatorial(n, show=False):
    """
    -> Fatorial uma função que recebe valores para serem fatorados
    : parametro n >>> recebe o número a ser fatorado
    : parametro show >>> e um valor opcional que pode ser verdadeiro ou falso
    : return >>> retorna um valor de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#programa principal
print(fatorial(5, True))
help(fatorial)