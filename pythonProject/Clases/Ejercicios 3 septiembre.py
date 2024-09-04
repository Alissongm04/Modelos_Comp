# Ejercicios
"""
# 1) Crear una función que te de un entero y calcular el factorial
de ese numero (un entero no negativo)

2) Crear una función que reciba 3 numeros y verifica si el tercer
numero está entre los 2 primeros numeros

3) Dada una cadena, crea 2 funciones que cuenten el numero de espacios en esa cadena
(quiero papitas, espacios: 1)

4) Dada una lista, crear una función para imprimir la cantidad de numeros en la lista
"""
# Ejercicio 1
numero_str = input("Introduce un número: ")
n = int(numero_str)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print("El factorial de este número es:", factorial(n))

# Ejercicio 24
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

numero1= float(numero1)
numero2 = float(numero2)
numero3 = float(numero3)

def tres_numeros(numero1, numero2, numero3):
    menor = min(numero1, numero2)
    maximo = max(numero1, numero2)

    if menor <= numero3 <= maximo:
        return print('si está entre los dos números')
    else:
        return print('no está entre los dos números')

