'''El número de visitantes mensuales de una tienda virtual tiene una distribución normal con una media de 100 500 y una desviación estándar de 3 500.

Encuentra la probabilidad de que en el próximo mes el sitio web del outlet tenga:

menos de 92 000 visitantes;
más de 111 000 visitantes.
Completa el código siguiendo los comentarios y utiliza las sentencias print() del precódigo para mostrar tus resultados.'''
#Código
from scipy import stats as st

mu = 100500
sigma = 3500

more_threshold = 111000
fewer_threshold = 92000

p_more_visitors = 1 - st.norm(mu, sigma).cdf(more_threshold)
p_fewer_visitors = st.norm(mu, sigma).cdf(fewer_threshold)

print(f'Probabilidad de que el número de visitantes sea superior a {more_threshold}: {p_more_visitors}')
print(f'Probabilidad de que el número de visitantes sea inferior a {fewer_threshold}: {p_fewer_visitors}')
