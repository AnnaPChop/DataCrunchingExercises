'''Estás vendiendo sandías online. Para venderlas todas antes de que termine la temporada, contrataste a desarrolladores web para crear una página web llamada Watermelon Life. 
Observando las estadísticas, notaste que cuanto más tiempo las personas pasaban en tu sitio web (cuantos más bloques veían), más a menudo compraban sandías. 
El promedio de bloques vistos fue de 4.867.
Los diseñadores insistieron en que cambies los primeros bloques para cumplir con las nuevas pautas, lo hiciste, pero la cantidad de pedidos no cambió. 
Pero probablemente los usuarios empezaron a realizar compras más rápidamente. Comprobemos si ese es el caso: si es así, los usuarios deberían decidir realizar compras después 
de ver solo los primeros bloques de la página web, por lo que la cantidad de bloques que ven debería ser menor ahora.
Utilizaremos una muestra de 100 clientes seleccionados al azar. El dataset es el número de bloques de la página web vistos. 
Nuestra hipótesis nula es que el número de bloques de páginas de destino vistos es mayor o igual que 4.867.'''
#Código
from scipy import stats as st
import pandas as pd

screens = pd.Series([4, 2, 4, 5, 5, 4, 2, 3, 3, 5, 2, 5, 2, 2, 2, 3, 3, 4, 8, 3, 4, 3, 5, 5, 4, 2, 5, 2, 3, 7, 5, 5, 6,  5, 3, 4, 3, 6, 3, 4, 4, 3, 5, 4, 4, 8, 4, 7, 4, 5, 5, 3, 4, 6, 7, 2, 3, 6, 5, 6, 4, 4, 3, 4, 6, 4, 4, 6, 2, 6, 5, 3, 3, 3, 4, 5, 3, 5, 5, 4, 3, 3, 3, 1, 5, 4, 3, 4, 6, 3, 1, 3, 2, 7, 3, 6, 6, 6, 5, 5])

prev_screens_value = 4.867 # número promedio de bloques vistos

alpha = 0.05  # nivel de significación

results = st.ttest_1samp(screens, prev_screens_value)

# prueba unilateral: el valor p se divide en dos
print('valor-p: ', results.pvalue / 2)

# prueba unilateral a la izquierda:
# rechaza la hipótesis solo si la media muestral es significativamente menor que el valor propuesto
if (results.pvalue / 2 < alpha) and (screens.mean() < prev_screens_value):
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")
