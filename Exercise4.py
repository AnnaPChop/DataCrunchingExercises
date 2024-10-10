'''Los portátiles de Pineapple son caros, pero siguen siendo populares entre los geeks de la informática: el 60% de los clientes están dispuestos a comprarse una computadora 
portátil de esta marca si acuden a la tienda. Los portátiles de Banana son más baratos, pero no tan populares: solo el 20% de los visitantes de la tienda están dispuestos 
a comprarlos. Supongamos que la tienda solo tiene a la venta equipos de Pineapple. ¿Cuál es la probabilidad de que 50 de cada 80 clientes realicen una compra en un día?

Guarda el resultado en la variable probability y muéstralo.

No olvides que en Python se utiliza el signo ** para la exponenciación.'''
#Código
from math import factorial

p = 0.6
q = 0.4
n = 80
k = 50

probability = factorial(n) / (factorial(k) * factorial(n-k)) * (p ** k) * (q ** (n-k))

print(probability)
