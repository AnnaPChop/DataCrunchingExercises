'''Una empresa envía a sus clientes un boletín electrónico mensual con novedades y ofertas de los socios. Sabemos que el 40% de los clientes abre el boletín.

Uno de los socios está planeando una campaña publicitaria y espera llegar a unos 9000 clientes. Calcula la probabilidad de que se cumplan las expectativas del socio si el boletín se envía a 23 000 personas.

En el ejemplo anterior, hemos creado una variable llamada clicks. Aquí, crea otra llamada threshold y guarda el valor 9000 en ella. Que el tamaño de la población sea binom_n y que la probabilidad de que se abra el boletín sea binom_p.

Guarda la probabilidad de que se cumplan las expectativas del socio como p_threshold y muéstrala.'''
#Código
from scipy import stats as st
import math as mt

binom_n = 23000
binom_p = 0.4

threshold = 9000

mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

p_threshold = 1 - st.norm(mu, sigma).cdf(threshold)
print(p_threshold)
