nome = input("Digite seu nome: ").title()
if nome == "Daniel":
    print(f"\033[1;32mQue nome bonito\033[m {nome}")
elif nome == "Bungas" or nome == "Mamaco" or nome == "Kokushibou":
    print(f"Seu nome e um nome de \033[1;31mvagabundo\033[m {nome}")
else:
    print("Seu nome e bem comum")
print(f"Tenha um bom dia, {nome}!")