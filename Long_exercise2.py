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
