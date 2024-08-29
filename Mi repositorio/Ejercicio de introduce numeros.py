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