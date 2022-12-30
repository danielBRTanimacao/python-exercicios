from time import sleep
print("-="*12)
print("\033[1;32mContagem regressiva para o papoco\033[m")
print("-="*12)
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("\033[1;31mOLHA O ESTOURO!!\033[m")