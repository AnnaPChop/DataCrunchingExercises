'''Hay dos conjuntos de datos: el tiempo promedio que pasan en un sitio web 1) los usuarios que inician sesión con nombre de usuario y contraseña, y
2) los usuarios que inician sesión a través de las redes sociales. Prueba la hipótesis de que ambos grupos de usuarios pasan la misma cantidad de tiempo en el sitio web.'''
#Código
from scipy import stats as st
import numpy as np

# tiempo pasado en el sitio web por usuarios con un nombre de usuario y contraseña
time_on_site_logpass = [368, 113, 328, 447, 1, 156, 335, 233, 
                       308, 181, 271, 239, 411, 293, 303, 
                       206, 196, 203, 311, 205, 297, 529, 
                       373, 217, 416, 206, 1, 128, 16, 214]

# tiempo pasado en el sitio web por los usuarios que inician sesión a través de las redes sociales
time_on_site_social  = [451, 182, 469, 546, 396, 630, 206, 
                        130, 45, 569, 434, 321, 374, 149, 
                        721, 350, 347, 446, 406, 365, 203, 
                        405, 631, 545, 584, 248, 171, 309, 
                        338, 505]


alpha = 0.05  # significación estadística crítica

results = st.ttest_ind(time_on_site_logpass, time_on_site_social)

print('valor p:', results.pvalue)

if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")
---------------------
#Result
valor p: 0.0010501061456827461
Rechazamos la hipótesis nula
--------------------
'''Tenemos dos datasets: la profundidad de la visita al sitio web de diferentes grupos de usuarios para los meses de verano y otoño. 
Prueba la hipótesis de que las profundidades de visita de los sitios web son iguales. Por ejemplo, puede ser que en verano los visitantes no se sumerjan tanto en el 
contenido, lo que sería algo a tener en cuenta al planificar una campaña publicitaria para los meses de verano. Vamos a establecer el nivel de significación en 0.05.
No esperamos que las varianzas sean las mismas así que establece el parámetro equal_var en False.  Puedes ejecutar np.var(pages_per_session_autumn) 
etcétera para verificar la varianza del conjunto.'''
#Código
from scipy import stats as st
import numpy as np

pages_per_session_autumn = [7.1, 7.3, 9.8, 7.3, 6.4, 10.5, 8.7, 
                            17.5, 3.3, 15.5, 16.2, 0.4, 8.3, 
                            8.1, 3.0, 6.1, 4.4, 18.8, 14.7, 16.4, 
                            13.6, 4.4, 7.4, 12.4, 3.9, 13.6, 
                            8.8, 8.1, 13.6, 12.2]
pages_per_session_summer = [12.1, 24.3, 6.4, 19.9, 19.7, 12.5, 17.6, 
                            5.0, 22.4, 13.5, 10.8, 23.4, 9.4, 3.7, 
                            2.5, 19.8, 4.8, 29.0, 1.7, 28.6, 16.7, 
                            14.2, 10.6, 18.2, 14.7, 23.8, 15.9, 16.2, 
                            12.1, 14.5]

# tu código va debajo

alpha = 0.05  # el nivel de significancia estadística crítica

results = st.ttest_ind(
    pages_per_session_autumn, pages_per_session_summer, equal_var=False
)

print('valor p:', results.pvalue)

if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")
  -------------------------
#Result
valor p: 0.002200163165401993
Rechazamos la hipótesis nula
-------------------------------



