# Tarea 1

## Instrucciones

# Crear un script donde impriman un ejemplo de cada uno de los métodos listados

print ("Ejemplo de la función list.append")
#Mi lista
mi_lista = ["Tengo", "muchas", "ganas", "de", "un"]
print("Esta es la lista original:", mi_lista)
# Función list.append(x)
mi_lista.append("helado")

print("Al agregar 'helado':", mi_lista)

print ("\nEjemplo de la funcion list.extend(iterable)")
#Se usa para extender una lista ya existente en vez de modificarla por otra

#Creamos la otra lista
segunda_lista = ["y", "chocokrispis"]

#Usamos la función
mi_lista.extend(segunda_lista)

#imprimimos el resultado
print(mi_lista)

print ("\nEjemplo de la funcion list.insert(i, x)")
#Se usa para insertar un elemento 'x' en una lista en una posición específica 'i', no reemplaza el valor en la posición 'i', sino que desplaza los ya existentes
mi_lista.insert(5, "waffle")

print(mi_lista)

#Función list.remove(x)
print ("\nEjemplo de la función list.remove(x)")
mi_lista.remove("waffle")
print(mi_lista)

#Función list.pop(x)
print ("\nEjemplo de la funcion list.pop")

#Eliminamos y obtenemos el elemento en la posición 2 (el tercer elemento)
elemento_eliminado = mi_lista.pop(1)

#Impresión del elementos eliminado
print("Elemento elimiando:", elemento_eliminado)

#Impresión de la lista con el elemento ya eliminado
print("Lista actualizada:", mi_lista)

print ("\nEjemplo de la funcion list.clear()")
print('Lista antes de usar clear:', mi_lista)

#Función list.clear
mi_lista.clear()

#Imprimimos la lista después de usar
print("Lista después de usar clear:", mi_lista)

print("\nEjemplo de la Función list.index(x[, start[, end]]")
#Función index(x[, start[, end]])
Lista_de_nombres = ["Anette", "Karime", "Dafne", "Estela", "Carolina", "Vladimir"]
print("Usamos esta nueva lista:", Lista_de_nombres)
#Quiero saber donde está Anette
indice_Anette = Lista_de_nombres.index("Anette")
print("\nAnette se encuentra en esta posición en el índice:", indice_Anette)

#Ahora quiero saber donde está Estela pero solo buscando después del índice 1
indice_Estela_despues_3 = Lista_de_nombres.index("Estela", 1)
print ("Estela está en esta posición después del índice 1:", indice_Estela_despues_3)

#O para identificar en qué posición está Dafne en un rango más específico
indice_Karime_entre_Vladimir = Lista_de_nombres.index("Dafne",1,5)
print ("Dafne está en esta posición desde los índice 1,3 en:", indice_Karime_entre_Vladimir)

#Función list.count(x)
print("\nEjemplo de la función list.count")
#Esta función se usa para contar cuantas veces aparece el elemento 'x' en una lista
lista_count = [2,4,6,4,3,1,2,2,2,4,6,45,2,2]
print("\nEn mi siguiente lista:", lista_count)
#Si quiero contar cuantas veces está el 2
cantidad_2 = lista_count[2]
print("En esta lista, el 2 se repite ",(cantidad_2), "veces")
#Si quiero contar cuantas veces está el 6
cantidad_6 = lista_count[6]
print("En esta lista el 6 está", cantidad_6, "veces")

#Función list.sort(*, key=None, reverse=False)
print("\nEjemplo de la funcion list.sort y list.reverse()")
#Esta función se usa para ordenar los elementos de una lista

#Lista de personas
Personas = [
    {"\nNombre": "Carla", "edad": 21},
    {"Nombre": "Fernando", "edad": 24},
    {"Nombre": "Yael", "edad": 50},
    {"Nombre": "Elizabeth", "edad": 36},
    {"Nombre": "David", "edad": 51},
    {"Nombre": "Gerardo", "edad": 70},
]

#Para ordenar esta lista por edades en orden asceedente
Personas.sort(key=lambda x: x["edad"])
# Aquí se especifica que la lista se ordena en base al valor "edad"
#Mostrar la lista ordenada
print("\nLista de edades en orden ascendente:", Personas)

#Para ordenarlos en orden descedente
print("\nEjemplo de la función list.reverse en esta misma lista")
Personas.sort(key=lambda x: x["edad"], reverse=True)
#Aquí añadimos 'reverse=True' para que cambie el orden a descendente
print("Lista de edades en orden descendente:", Personas)

#Función list.copy
print("\nEjemplo de la función list.copy")
#Esta función se usa para hacer una copia superficial de una lista, aunque es una nueva lista con los mismos elementos, ambas son objetos distintos en la memoria

lista_original = ["azul", "dorado", "rosa", "morado", "violeta"]

#Para hacer una copia
lista_copiada = lista_original.copy()

print("Lista copiada:", lista_copiada)
print("Lista original:", lista_original)

#si quisiera modificar la lista copiada, uso append
lista_copiada.append("amarillo")
print("Lista copiada (modificada):", lista_copiada)








