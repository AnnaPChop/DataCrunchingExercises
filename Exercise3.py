'''Escribe el código para encontrar el número de formas en las que 90 de cada 100 usuarios hacen clic en el banner. Guarda el resultado en la variable c.'''
from math import factorial

c = factorial(100)/(factorial(90)*factorial(10))

print(c)
