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


