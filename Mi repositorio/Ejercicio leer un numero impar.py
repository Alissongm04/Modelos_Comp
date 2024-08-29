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
