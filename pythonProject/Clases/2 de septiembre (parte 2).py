"""
Las funciones
Son fragmentos de código que se pueden ejecutar múltiples veces.
Pueden recibir y devolver información para comunicarse con el proceso principal.
"""
#Definición y llamada
def saludar():
    print("Hola! Este print se llama desde la función saludar()")

saludar() #Este es como instrucción el script para que salude
saludar()
saludar()

def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i, i * 5))

dibujar_tabla_del_5()

"""
otra forma es solo poniendo 
for i in range(10): 
    print('5 * ', i, ' = ', 5*i) 
las veces que queramos que se imprima, pero es más practico declararlo
con 'def' para que al poner "dibujar_tabla_del_5" cuantas veces queramos 
se imprima esa cantidad de veces sin tener que copiar y pegar. 
"""
# Formas de usar el print
print("Formas de usar el print")
val = 10
print('5 *', val, '=', 5*val)
print('5 * {} = {}'.format(10, 50))
print('5 * {0} = {1}'.format(10, 50))
print('5 * {1} = {0}'.format(10, 50))
print(f'5 * {val} = {5*val}')

#Ámbito de las variables
"""
Una variable declarada en una función no existe en la función principal:
def test():
    n = 10
"""
print("Ámbito de las variables")
"""
def test():
    n = 10
    print(n)
def test1():
    n = 20
    print(n)

print('antes de las funciones')
test()
print('después de la función test pero antes del test1')
test1()
print('después de test1')
"""

# Variables globales vs variables
def test_con_return():
    n = 10
    print('localmente n =', n)
    return n*5

# m = test_con_return ()
# print('globalmente m =', m)

print("test_con_multiple_return")

def test_con_multiple_return():
    n = 10
    print('localmente n =', n)
    return n, n*5, 6**2, [5, 'lobo']

vals = test_con_multiple_return()
print(vals, type(vals))

val1, val2, val3, val4 = test_con_multiple_return()
print('vals:', val1, val2, val3, val4)

print(vals)