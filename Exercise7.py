'''Otra tienda online, Fancy Pants, vende productos de regalo a un público muy limitado de clientes corporativos. 
Las ventas semanales en la tienda de conjuntos de ajedrez de lujo fabricados con colmillo de mamut tienen una distribución normal con una media de 420 
y una desviación estándar de 65. El equipo de inventario está decidiendo cuántos conjuntos pedir. 
Quieren que la posibilidad de venderlos todos la próxima semana sea del 90%. ¿Cuántos deben pedir?'''
#Código
from scipy import stats as st

mu = 420
sigma = 65
prob = 0.9

n_shipment = st.norm(mu, sigma).ppf(1 - prob)

print('Cantidad de artículos a pedir:', int(n_shipment))
