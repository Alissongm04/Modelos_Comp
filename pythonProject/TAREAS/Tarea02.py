# TAREA 2
##
"""Determina si los tipos de datos range cumplen:
    # Mutabilidad
    # Suma
    # Producto por un entero
    # Slicing
    # Convertir a lista o tupla
    # Función len
"""
#establecemos nuestro rango
rango = range(10)

#MUTABILIDAD
print("Mutabilidad")

try:
    rango[0] = 5
except TypeError:
    print("El objeto 'range' es inmutable.")
else:
    print("El objeto 'range' es mutable.")
#Debe lanzar que inmutable ya que 'range' en python es inmutable

#SUMA
print("\nSuma:")

rango2 = range(1,11) #rango del 1 al 10

suma_esperada = 55

suma_calculada = sum(rango2)
#establecemos si la suma calculada coincide con la suma esperada
if suma_calculada == suma_esperada:
    print("La suma del rango cumple con el valor esperado")
else:
    print("La suma del rango no cumple con el valor esperado")

# Producto por un entero
print("\nProducto por un entero")

rango3 = range(1,22)
n = 2 #El entero que vamos a trabajar como múltiplo de todos

#Para verificar si todos los elementos son múltiplos de n
todos_multiples = all(x % n == 0 for x in rango3)

print("¿Todos los numeros del rango son múltiplos de 'n'?", todos_multiples)

#Si n es diferente (múltiplo de todos = 1)
rango31 = range(1,11)
n = 1
todos_multiples2 = all(x % n == 0 for x in rango31)
print("¿Todos los números del rango son múltiples de 'n'?", todos_multiples2)

#Slicing
print("\nSlicing")
rango4 = range(0,10)
subrango = rango[3:7]

if subrango == rango[3:7]:
    print("El objeto 'range' soporta slicing")
    print(list(subrango))
else:
    print("El objeto 'range' no soporta slicing")

# Convertir a lista o tupla
print("\nConvertir a lista o tupla")

rango5 = range(0,15)
print(rango5)

#Verificamos que el objeto es de tipo range
if isinstance(rango5, range):
    lista = list(rango5) # Para convertir a lista
    print("Convertido a lista:", lista)

    tupla = tuple(rango5)  #Para convertir a tupla
    print("Convertido a tupla:", tupla)
else:
    print("El dato no es de tipo range")

# Funcion len
print("\nFunción len")

rango6 = range(8)
print("Mi rango:",list(rango6))

longuitud = len(rango6)
print("Longuitud:", longuitud)