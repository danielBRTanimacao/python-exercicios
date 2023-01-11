times = ('Palmeiras', 'Internacional', "Fluminense",
"Corinthians", "Flamengo", "Athletico-PR", "Atlético-MG",
"Fortaleza", "São Paulo", "América-MG", "Botafogo", "Santos", "Goiás",
"Bragantino", "Coritiba", "Cuiabá", "Ceará", "Atlético-GO",
"Avaí",	"Juventude")
print(">>>>>"*15)
print(f"Lista de times brasileiros {times}")
print(">>>>>"*15)
print(f"Os Primeiros são {times[:5]}")
print(">>>>>"*15)
print(f"Os cinco ultimos são {times[-5:]}")
print(">>>>>"*15)
print(f"Times em ordem alfabetica {sorted(times)}")
print(">>>>>"*15)
print(f"O Botafogo esta {times.index('Botafogo')+1}° posição")
