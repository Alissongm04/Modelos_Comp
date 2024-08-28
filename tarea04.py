#TAREA 4

# Considerando las siguientes calificaciones
calif_1 = 10
calif_2 = 7
calif_3 = 4
#Calcula el promedio considerando que:
    #La primera vale un 15% del total
    #La segunda vale un 35% del total
    #La tercera vale un 50% del total

porcentaje_1 = 0.15
porcentaje_2 = 0.35
porcentaje_3 = 0.50

#calculamos el promedio considerando los porcentajes
Promedio_p1 = (calif_1 * 0.15) + (calif_2 * 0.35) + (calif_3 * 0.5)
Promedio_p2 = Promedio_p1/3
print(Promedio_p2)

# La siguiente matriz debe cumplit que el 4to valor de cada fila debe ser igual a la suma de los primeros 3 valores. Crea un código para hacer las correcciones necesarias

matriz = [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]
for fila in matriz:
    suma = sum(fila[:3])  # Sumamos los tres primeros valores de la fila
    fila[3] = suma  # Asignamos la suma al 4to valor

print(matriz)