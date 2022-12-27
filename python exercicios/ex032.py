from datetime import date
ano = int(input("Digite um ano qualquer ou coloque 0 para calcular o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #calculo para saber se o ano e bissesto
    print(f"O ano {ano} e bissesto SIM")
else:
    print(f"O ano {ano} NÃO e bissesto")
