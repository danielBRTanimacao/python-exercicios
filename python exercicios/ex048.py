s = 0 #SOMA VALE 0
for c in range(1, 501, 2):
    if c % 3 == 0: #
        s += c      # SE C RESTO DA DIVISÃO FOR IGUAL A 0
print(s)           # s = C + S