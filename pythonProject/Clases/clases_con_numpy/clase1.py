# Clase array de NumPy

lista1 = [2, 3, 4, 5, 6]
lista2 = [2,3,4,5,6]

print(lista1)

# ARREGLOS
import numpy as np

#diferencia de imprimir con array es que no imprime con comas

array = np.array(lista1)
print(array)
print(type(array))

print(len(lista1))
print(len(array))
print(array.ndim) #dimension del arreglo
print(array.shape) #forma del arreglo

# Arreglos bi dimensionales
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7,8, 9, 10]
])
print(array)
print(array.shape) #dos filas x cinco columnas
