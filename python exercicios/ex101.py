def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos voto NEGADO!"
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos voto opcional!'
    else:
        return f'Com {idade} anos Voto OBRIGATORIO'


#programa principal
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
