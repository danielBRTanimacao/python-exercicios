def leiaInt(msg):
    """
    -> leiaInt função recebe mensagem(msg) para ler números inteiros
    : parametro msg: recebe a mensagem escrita no leiaInt, leiaInt(msg)
    : return: retorna um valor True
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[31mErro, Tente de novo!\033[m")
        if ok:
            break
    return valor


#programa principal
n = leiaInt("Digite um valor: ")
print(f"Você acabou de digitar o valor {n}")
help(leiaInt)