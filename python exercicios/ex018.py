from math import cos, sin, tan, radians
'''import math
ang = float(input("Digite o angulo: "))
cos = math.cos(math.radians(ang))
seno = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f"O resultado do COSENO é {cos:.2f} \nO resultado do SENO é {seno:.2f} \nO resultado da TANGENTE é {tan:.2f}")'''
ângulo = float(input("Digite o angulo: "))
coseno = cos(radians(ângulo))
seno = sin(radians(ângulo))
tangente = tan(radians(ângulo))
print(f"O valor do angulo {ângulo} vale em coseno {coseno:.2f}")
print(f"O valor do angulo {ângulo} vale o seno {seno:.2f}")
print(f"O valor do angulo {ângulo} vale a tangente {tangente:.2f}")
