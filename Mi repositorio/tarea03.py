#TAREA03

#Instrucciones
## Crea un archivo donde muestre un ejemplo de cado uno de los soguientes métodos de diccionarios

#pop
#Lo usamos cuando queremos eliminar un elemento de nuestra matriz
print ("**Método pop**")
frutas = {
    "manzana": "roja",
    "naranja": "naranja",
    "plátano": "amarillo",
    "uva": "verde"
}
print ("Diccionario:", frutas)
#Eliminamos la palabra "naranja" del diccionario
fruta_eliminada = frutas.pop("naranja")

print("\nAl aplicar la función 'pop' tenemos:", frutas)
print("Palabra eliminada:", fruta_eliminada)

#get
#Se usa para acceder a algún valor del diccionario
print ("\n**Método get**")
frutas_precios = {
    "manzana": 45,
    "naranja": 40,
    "platano": 20,
    "uva": 55
}
print ("Tenemos la lista de precios, de la siguiente lista de frutas:", frutas_precios)
x = frutas_precios.get("uva")
print("Al obtener el precio de la uva es:", x)

#copy
#Se usa hace una copia de nuestro diccionario especificado (tiene la excepción de que las listas o diccionarios anidados no se copian, solo hace referencia a ellos).
print ("\n**Método copy**")
#Aquí usaremos la lista ya creada de frutas
a = frutas.copy()
print("Diccionario original:", frutas)
print("Copia del diccionario:", a)

#keys
print("\n**Método keys**")
print("Del diccionario:", frutas)
#Se usa para reflejar los cambios realizados en el diccionario original y para observar las claves del diccionario, como una lista
#Las claves son en este caso las frutas, los colores son su valor
#también sirve para agregar otro nuevo par clave-valor
c = frutas.keys()
frutas["guayaba"] = "amarilla"

print(c)

#items
print("\n**Método items**")
print("Del diccionario:", frutas)
#Devuelve una lista que contiene una tupla para cada par de valores clave en forma dde (clave, valor)
i = frutas.items()

frutas["uva"] = "morado"
#También sirve para cambiar el valor de una clave (el cual se reflejará)
print(i)

#clear
print("\n**Método clear**")
#Sirve para eliminar los elementos del diccionario
print("Del diccionario:", frutas)
frutas.clear()

print("Resultante:",frutas)

#fromkeys
print("\n**Método fromkeys**")
#Devuelve un diccionario con las claves y el valor que les asignas (dos variables)
k = ('Tamborcitos', 'Picafresas', 'Chicles')
y = "un pesito"

thisdict = dict.fromkeys(k, y)

print(thisdict)

#popitem
print("\n**Método popitem**")
#Se usa para eliminar y devolver un par clave-valor aleatorio de un diccionario
Participantes = {
    'Alisson': 9,
    'Carla': 8,
    'Emmanuel': 5,
    'Roberto': 7,
    'Samantha':10
}
print("En nuestra lista de participantes:", Participantes)
par = Participantes.popitem()

#Imprimimos y específicamos que 'par' aleatorio fue el que se eliminó
print("Par clave-valor eliminado:", par)
#Nota: no cambia cada vez que corremos el script
print("Calificaciones actualizadas:", Participantes)

#setdefault
print("\n**Método setdefault**")
#Sirve para establecer un valor predeterminado para una clave en caso de que la clave no exista en el diccionario. Si existe, solo lo devuelve
#Por ejemplo, en nuestra lista de Participantes
print("Lista de participantes:", Participantes)
Participantes = {
    'Alisson': 9,
    'Carla': 8,
    'Emmanuel': 5,
    'Roberto': 7,
    'Samantha':10
}
#Si queremos obtener el puntaje de Emmanuel:
Emmanuel_puntaje = Participantes.setdefault('Emmanuel', 0)
print("Puntaje de Emmanuel:", Emmanuel_puntaje)
Alisson_puntaje = Participantes.setdefault('Alisson', 0)
print("Puntaje de Alisson:", Alisson_puntaje)

#update
print("\n**Método update**")
#Se usa para actualizar o modificar un diccionario con otro diccionario o con una secuencia de pares clave-valor
print("Lista de participantes:", Participantes)
Participantes = {
    'Alisson': 9,
    'Carla': 8,
    'Emmanuel': 5,
    'Roberto': 7,
    'Samantha':10
}
#coloco qué cosas quiero agregar para actualizarla
Participantes.update({'David': 9, 'Mónica': 10})

print("Actualización:",Participantes)

#values
print("\n**Método values**")
print("Lista de participantes:", Participantes)
#Nos devuelve los valores de nuestro diccionario

#Usando nuestra lista de participantes...
valores = Participantes.values()

print("Puntajes obtenidos:", valores)