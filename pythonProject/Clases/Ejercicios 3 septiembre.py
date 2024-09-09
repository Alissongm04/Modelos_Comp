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

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1))
print("El factorial de este número es:", (factorial(n)))

# Ejercicio 2
# valores_str = input ('Introduce 3 valores:')
# numero1_str, numero2_str, numero3_str = valores_str.split()
# numero1, numero2, numero3 = float(numero1_str), float(numero2_str), float(numero3_str)
# tres_numeros = (numero1, numero2, numero3)

numero1, numero2, numero3 = list(map(float, input('Introduce 3 valores').split()))

def tres_numeros(numero1, numero2, numero3):
        return numero1 <= numero2 <= numero3

print(tres_numeros(numero1, numero2, numero3))

#Ejercicio 3
def metodo1(string: str) -> int:
    numero_espacios = 0
    for letra in string:
        if letra == ' ':
            numero_espacios += 1
        return numero_espacios

print(metodo1('jaidrnvv '))

def metodo2(palabra: str) -> int:
    numero_espacios = palabra.count(' ')
    print(f'La frase tiene {numero_espacios} espacios')

cadena = input('Introduce una frase: ')
print(metodo2(cadena))

#Ejercicio 4
def imprimir_impares(lista:list):
    for numero in lista:
        if numero % 2 == 1:
            print(numero, end=' ')

listado = [2, 4, 6, 23, 7, 3, 67, 23, 6]
imprimir_impares(listado)

