'''Tenemos a 30 estudiantes que realizaron un examen. Sus puntuaciones se almacenan en la variable exam_results. 
Si un estudiante obtuvo menos de 20 puntos, reprobó el examen. 
Escribe un programa que cuente cuántos estudiantes reprobaron el examen y almacena el resultado en la variable failed_students. 
Muestra el resultado'''
#Código 
import numpy as np

exam_results = np.array(
    [
        42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
        66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
        34,  47,  64,  58,  61,  12,  30,  63,  20,  68
    ]
)

failed_students = 0

for score in exam_results:
    if score < 20:
        failed_students += 1

print('Número de estudiantes reprobados:', failed_students)
