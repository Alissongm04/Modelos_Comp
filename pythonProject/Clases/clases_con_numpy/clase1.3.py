# Operaciones básicas
"""
La c

"""
import numpy as np

lista1 = list(range(5))
lista2 = [11, 12, 13, 14, 15]

array1 = np.array(lista1)
array2 = np.array(lista2)
print(array1.shape, array2.shape)

print('suma de listas:', lista1 + lista2)
print('suma de arrays:', array1 + array2)

print('la suma de array TIENE QUE tener la misma forma')
print('resta de arrays:')
print('resta', np.array([1, 2, 3])-np.array([5,6,1]))

# Producto

arr_1 = np.array([12, 14, 16, 18, 30])
arr_2 = np.array([3, 7, 12, 2, 10])

print('division por array', arr_1/arr_2)

print('division por constante', arr_1/2)

print('divsion constante sobre array', 10/arr_1)

print('potencia de array', arr_2**2)

print('raiz de array', arr_2**(0.5))

print('potencia de array con "numeros negativos"', 1/arr_2**2)

#potencia entre arreglos
#un arreglo elevado a otra potencia
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([2,3,4,5])
print('potencia entre arreglos', arr_1**arr_2)