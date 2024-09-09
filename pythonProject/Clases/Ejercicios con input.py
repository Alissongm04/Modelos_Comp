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

print(list(range(1, n+1)))

#
"""
1) Realiza un programa que lea un número impar por teclaro.
si el usuario no introduce un número impar,
debe repetirse el proceso hasta que lo introduzca correctamente
"""
numero_str = input('introduce un numero impar: ')

numero = int(numero_str)
if numero % 2 != 0:
    print('el número si es impar')
if numero % 2 == 0:
    print('el numero es par')