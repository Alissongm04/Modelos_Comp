# Retornar
def test():
    return [1,2,3,4,5]

variable = test()
print(variable)

print('usando slicing', variable[-2:])
print('usando slicing', test()[-2:])

# Parámetros y argumentos
"""
En la definición de una función, los valores que se reciben se denomina parámetros, 
y en la llamada se denominan argumentos
"""
def test_funcion(parametro1: int, parametro2: float) -> float: #en la definición se le llama parametro
    #especificar el tipo de dato no es obligatorio (:float, :int, etc.)
    print(parametro1, parametro2)

argumento1, argumento2 = 5, ['casa'] #si no tuviera corchete, es string, con corchete es una lista
test_funcion(argumento1, argumento2) #en la llamada (test) se le llama argumento

#Argumento por posición
#Trabjaando con argumentos y parámetros

def funcion1(a, b):
    print(a-b)

funcion1(25, 7) #aunque te los marca automático, también puedes especificar el orden que tu quieras
#los argumentos por posición son automáticos, los a. por nombre es cuando tu los especificas

def funcion2_resta(a = 25, b = 7):
    print(a-b)

funcion2_resta(b = -10) #si lo cambias aquí, toma este valor, no el primero

#Paso por valor y paso por referencia
"""
Paso por valor: se crea una copia local de la variable dentro de la función.
Paso por referencia: se maneja directamente la variable, los cambios realizados dentro
Las variables ocupan cierto espacio, donde sea si no especificamos su dirección.
Cada vez que creamos una variable, estas ocupan un lugar en nuestro almacenamiento
Las personas que ocupan una gran cantidad de datos en otros lenguajes, es útil esto para tener
un control del almacenamiento
"""
variable = 10
var2= variable #cuando queremos almacenar otras variables en el mismo lugar que 'variable' en este caso, sin tener que crear copias
var3 = variable

def duplicar_numero(numero):
    print(numero+2)

val = 10
duplicar_numero(val) #el paso por valor es cuando se almacena el valor (10 en este caso) pero también reserva otro con el mismo valor, aunque no lo usará
#en este paso por valor no se modifica la original, porque se hacen copias

"""
ns = [10, 50, 100]
print('antes de la función:', ns]
duplicar_valores_lista(ns[:]) <- en esta parte le indicamos la copia con ns[:], ya no se modifica la original
print('después de la funcion:', ns)
"""

#Paso por referencia
def duplicar_valores_lista(lista):
    for i, n in enumerate(lista):
        lista[i] *= 2
        print('dentro de la función', lista)
ns = [10, 50, 100]
print('antes de la función:', ns)
duplicar_valores_lista(ns)
print('después de la función', ns)
#el pase por referencia, va a alterar a la original porque mandas toda la info (valor y dirección)

