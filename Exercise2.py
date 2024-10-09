'''Vamos a seguir con los resultados del examen. Ahora tenemos que contar no solo a los estudiantes que reprobaron, 
sino también a los que obtuvieron otros resultados: excelente (90 puntos o más), notable (70-89 puntos), 
satisfactorio (50-69) y aprobado (20-49).

Crea un diccionario summarized_data y escribe código para rellenarlo con los datos necesarios.'''
#Código
import numpy as np

exam_results = np.array(
    [
        42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
        66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
        34,  47,  64,  58,  61,  12,  30,  63,  20,  68
    ]
)
summarized_data = {'excellent': 0, 'good': 0, 'average': 0, 'passable': 0, 'failed': 0}

for score in exam_results:
    if score >= 90:
        summarized_data['excellent'] += 1
    elif score >= 70:
        summarized_data['good'] += 1
    elif score >= 50:
        summarized_data['average'] += 1
    elif score >= 20:
        summarized_data['passable'] += 1
    else:
        summarized_data['failed'] += 1

for result in summarized_data:
    print(result, '-', summarized_data[result])
