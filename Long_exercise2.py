'''
Tenemos dos datasets: el tiempo que un grupo de usuarios pasó en sus páginas personales en un sitio web, registrado antes y después de que se rediseñó la página personal. 
Prueba la hipótesis de que el tiempo que pasan allí cambió (aumentó o disminuyó) después del rediseño.
Piensa en la frase "el tiempo que pasan allí cambió" de la hipótesis anterior. ¿Sugiere la necesidad de una prueba unilateral o bilateral?'''
#Código
from scipy import stats as st
import numpy as np

time_before = [1732, 1301, 1540, 2247, 1632, 1550, 754, 1946, 1889, 
          2748, 1349, 1648, 1665, 2416, 1470, 1681, 1868, 1629, 
          1271, 1633, 2131, 942, 1599, 1127, 2200, 661, 1207, 
          1737, 2410, 1486]

time_after = [955, 2577, 360, 139, 1618, 990, 644, 1796, 1487, 949, 472, 
         1906, 1758, 1258, 2554, 612, 309, 1864, 1294, 1487, 1164, 1559, 
         491, 2286, 1270, 2069, 1553, 1629, 1704, 1623]

alpha = 0.05  # el nivel de significancia estadística crítica

results = st.ttest_rel(time_before, time_after)

print('valor p:', results.pvalue)

if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

#Resultado
valor p: 0.0751397944405015
No podemos rechazar la hipótesis nula
-----------------------
'''Tenemos dos datasets: la cantidad de balas compradas por jugadores apasionados de un juego online, antes y después de introducir una mecánica que proporcionó incentivos 
para disparar en ráfagas. Prueba la hipótesis de que los jugadores empezaron a usar más balas después de que se introdujo la nueva característica.
Piensa en la palabra "más" de la hipótesis anterior. ¿Sugiere la necesidad de una prueba unilateral o bilateral?'''
#Código
from scipy import stats as st
import numpy as np
import pandas as pd

bullets_before = [821, 1164, 598, 854, 455, 1220, 161, 1400, 479, 215, 
          564, 159, 920, 173, 276, 444, 273, 711, 291, 880, 
          892, 712, 16, 476, 498, 9, 1251, 938, 389, 513]

bullets_after = [904, 220, 676, 459, 299, 659, 1698, 1120, 514, 1086, 1499, 
         1262, 829, 476, 1149, 996, 1247, 1117, 1324, 532, 1458, 898, 
         1837, 455, 1667, 898, 474, 558, 639, 1012]

print('media anterior:', pd.Series(bullets_before).mean())
print('media posterior:', pd.Series(bullets_after).mean())

alpha = 0.05 # significación estadística crítica

results = st.ttest_rel(
    bullets_before, 
    bullets_after)

print('valor-p:', results.pvalue / 2)

if (results.pvalue < alpha):
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")
#Resultado
media anterior: 591.7333333333333
media posterior: 932.0666666666667
valor-p: 0.005394751910405561
Rechazamos la hipótesis nula
# Comentario: ¡Funcionó! Ahora los jugadores disparan en ráfagas y emplean más balas. 
#Seleccionamos una prueba unilateral debido a la palabra "más". Si no sabemos la dirección del cambio, entonces utilizaremos la prueba bilateral.
