#Arrays pregenerados
"""
Crear arrays a partir de listas puede ser tedioso, para eso numpy integra
varias funciones muy útiles para generar arrays de us común en el álgebra de
matrices
"""
#Array de ceros
"""
Un array de ceros es cuando todos sus elementos son ceros 
se genera por el método zeros:
"""
import numpy as np

array_0s_2d = np.zeros(3)
print(array_0s_2d)

arrau_0s_2d = np.zeros((2, 4))
print(arrau_0s_2d)

array_0s_3d = np.zeros([2, 2, 3])
print(array_0s_3d)
print('dimension de arrau 0s_3d', array_0s_3d.ndim)

#Array de unos
print('\nmatriz de puros unos')
#lo mismo podemos pero utilizando el método ones:
array_1s = np.ones(6)
print(array_1s)

array_1s_2d = np.ones([3, 6])
print(array_1s_2d)

#Array de identidad
print('\nmatriz de ceros con diagonal de unos')
"""
Los arrays de identidad son matrices cuadradas (con el mismo numero de filas
que de columnas) donde todos los valores son ceros a excepción de la 
diagonal donde son unos. Podemos generarlas con el método eye:
"""

array_id = np.eye(4)
print(array_id)

#Método arange
print('\nmétodo arange')

rango_range = np.arange(5)
print(rango_range)

print('\nmatriz con arange tipo: inicio, final, step')
rango_range = np.arange(-10, 50, 2) #formato: inicio, final, separacion
print(rango_range)

