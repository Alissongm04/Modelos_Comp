# ejemplo 2
promedio = 0 #sirve para indicar el valor inicial
numeros = [0, 2, 4, 5, 6, 8]
for idx in numeros:
    promedio += idx # += es para poner promedio = promedio + idx
    print(str(idx))
promedio /= len(numeros)
print('el promedio es:', promedio)

#Ejemplo 3
numeros = [0, 2, 4, 5, 6, 8]
longuitud = 0
for idx in numeros: #idx para que vaya tomando valores en orden, en cada iteración, los que están dentro de for
    longuitud += 1
    print('se está ejecutando el for')
print('la longuitud de la lista es:', longuitud)
#lanzó 6 elementos porque es como usar la función len, aunque el rango es de 0 a 8, son 6 elementos dentro, entonces su longuitud será de 6

#Ejemplo
lista = ['azul', 'verde', 56, ['2da lista']]
print(list(enumerate(lista))) #enumerate nos agrega un contador para decirnos en que numero de la lista está el objeto

for idx, elemento in enumerate(lista):
    print('indice', idx, 'elemento:', elemento)

# o también
for idx, elemento in enumerate(lista):
    print(lista[idx])
#la ventaja de enumerate es saber en qué posición estamos

for elemento in lista:
    print(elemento)

#USO DE continue y break
for idx in range(2,18):
    print(idx)
    if idx % 2 == 0:
        print('es par')
        break #esto hace que en cuanto se ejecute el primer par (en este caso), va a parar
    else :
        print('es impar')
        continue #es para que ignore todito el código que haya debajo?

for letra in 'palabra':
    print(letra)
#función de entrada de datos: input()
string = input('Introduce un numero:\n')

print('se recibió la cadena:', string)
print('con tipo de dato:', type(string))

numero = float(string)
print('el numero es:', numero, 'con tipo de dato:', type(numero))

#Ejercicio
"""
2) Recibe por teclado un número entero e imprime 123 ,,, n

Ejemplo: 
devuelve '12345'

restricciones: 

1<n<150 

"""
numero_str = input("Introduce un número del 1 al 150: ")
n = int(numero_str)

print(list(range(1, n+1)))v