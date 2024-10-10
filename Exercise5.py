'''Supongamos que, al lado de una tienda de hardware Pineapple, hay un gran centro comercial con otra tienda que vende computadoras Banana. 160 clientes visitan esa tienda durante el día. ¿Cuál es la probabilidad de que 50 de esos visitantes se compren una computadora portátil?

Recuerda que solo el 20% de los usuarios están dispuestos a comprar un portátil de la marca Banana.

Guarda el resultado en la variable probability y muéstralo.'''
#Código
from math import factorial

p = 0.2
q = 0.8
n = 160
k = 50

probability = factorial(n) / (factorial(k) * factorial(n-k)) * (p ** k) * (q ** (n-k))

print(probability)
