'''El 1 de junio de 2019 tomaste un curso del famoso coach y empresario llamado Robby Tobbinson. Si aplicas sus exclusivas técnicas conscientes de negocio se garantiza que 
tu proyecto online generará al menos $800 por día, quizás más, en solo un mes. Él te lo promete. Las promesas están bien pero las pruebas estadísticas son mejores.
Vamos a ver qué nos dicen los números.
Utiliza un dataset con los ingresos diarios del último mes para probar tu hipótesis. La hipótesis es que tus ingresos diarios promedio igualaron o superaron los $800.
Recuerda: la hipótesis que contiene el signo de igualdad suele ser la hipótesis nula. Por lo tanto,
"Todo saldrá como lo predijo el coach" es tu hipótesis nula y "Los ingresos serán menores de lo que se predijo" es la hipótesis alternativa. 
Las desviaciones aleatorias siempre son posibles. Solo puedes decir "¡La metodología de Tobbinson no funcionó!" si tus ingresos son significativamente inferiores a la 
cantidad propuesta.'''
#Codigo
from scipy import stats as st
import numpy as np
import pandas as pd

revenue = pd.Series([727, 678, 685, 669, 661, 705, 701, 717, 
                     655,643, 660, 709, 701, 681, 716, 655, 
                     716, 695, 684, 687, 669,647, 721, 681, 
                     674, 641, 704, 717, 656, 725, 684, 665])

interested_value = 800

alpha = 0.05  # el nivel de significancia estadística crítica

results = st.ttest_1samp(revenue, interested_value)

print('valor p:', results.pvalue / 2)

if (results.pvalue / 2 < alpha) and (revenue.mean() < interested_value):
    print(
        "Rechazamos la hipótesis nula: los ingresos fueron significativamente inferiores a 800 dólares"
    )
else:
    print(
        "No podemos rechazar la hipótesis nula: los ingresos no fueron significativamente inferiores"
    )
