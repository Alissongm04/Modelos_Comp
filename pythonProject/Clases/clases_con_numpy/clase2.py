# día: 17 de septiembre
import numpy as np

arr_2d = np.array(([0,5,10], [15,20,25], [30,35,40]))

print(arr_2d)
print("Forma:", arr_2d.shape)
print("Dimensiones:",arr_2d.ndim)

# Si tenemos dos dimensiones, necesitamos dos índices, uno para las filas
# y otro para las columnas

#primera fila
primerafila = arr_2d[2]
print(primerafila)
# primera fila y primera columna
primerafilaycolumna = arr_2d[2][1]
print(primerafilaycolumna)
# última fila y última columna
ultimafilaycolumna = arr_2d[-1][-1]
print(ultimafilaycolumna)
# edición de la primera columna en la última fila
arr_2d[-1][0] = 99 #aquí cambiamos un valor

#usando slicing
x = arr_2d[:, :]
print(x)

#subarray de las dos primeras filas
a = arr_2d[:2,:]
print("\ndos primeras filas\n", a)

#subarray de la primera columna
b = arr_2d[:,:1]
print("\nprimera columna\n", b)

#subarray de la primera fila, primera columna
c = arr_2d[1:,:1]
print("primera columna desde 1\n", c)

#Edición masiva de la segunda columna
arr_2d[:,1:2] = 99
print(arr_2d)

#edición masiva de la última fila
arr_2d[-1,:] = [88,200,203]
print(arr_2d)

#Fancy index
#se basa en pasarle una lista al array haciendo referencia a las filas
#donde queremos acceder

#Creamos un array 2d de ceros
arr_2d = np.zeros((5,10))
print(arr_2d)

#modificacion masiva de la primera, tercer y última fila
arr_2d[[0,2,-1]] = 5
print(arr_2d)

#usando bucles for
#podemos recorrer las filas de un array con un bucle for como si se tratase de una lista

for fila in arr_2d:
    print("usando for", fila)

for i, fila in enumerate(arr_2d):
    for j, columna in enumerate(fila):
        arr_2d[i][j] = len(fila) * i + j

print(arr_2d)

#EJERCICIOS
arr_2d = np.zeros((5,10))

for i, fila in enumerate(arr_2d):
    for j, columna in enumerate(fila):
        arr_2d[i][j] = len(fila) * i + j

#Ejercicio 1: Determine la dimensión y forma de la matriz arr_2d
print("forma:", arr_2d.shape)
print("Dimensión:",arr_2d.ndim)
#Ejercicio 2: Transponga la matriz
print('la transpuesta de la matriz es:\n', arr_2d.T)
#Ejercicio 3: Modifique los valores de la 5 columna por 999
arr_2d[:,5] = 999
print(arr_2d)
#Ejercicio 4: Modifique los valores de las filas 3 y 4 por -5
arr_2d[2:4, :] = -5
print(arr_2d)

#igual que
arr_1 = ([1,2,3,4,5])
arr_2 = ([4,5,3,4,5])
igualque = np.equal(arr_1, arr_2)
print(igualque)

#Funciones aleatorias

#numero decimal entre 0 y 1
np.random.rand()
print(np.random.rand())

#array 1D de decimales entre 0 y 1
d1 = np.random.rand(4)
print(d1)