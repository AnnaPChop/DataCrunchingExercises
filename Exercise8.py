'''Los precios de los pedidos realizados en una tienda virtual tienen una distribución normal 
con una media de 24 dólares y una desviación estándar de 3.20 dólares.Algunos clientes eligen la entrega rápida por mensajería, 
que tiene un precio fijo independientemente del valor del pedido.
Los clientes tienden a molestarse cuando el costo de la entrega es igual al costo del pedido.
¿Cuánto debería costar el envío por mensajería para que no supere el precio del pedido en el 75% de los casos?'''
#Código
from scipy import stats as st

mu = 24
sigma = 3.2
threshold = .75

max_delivery_price = st.norm(mu, sigma).ppf(1 - threshold)

print('Costo máximo de envío por mensajería:', max_delivery_price)
