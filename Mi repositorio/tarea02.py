# TAREA 2
##
"""Determina si los tipos de datos range complen:
    # Mutabilidad
    #Suma
    # Producto por un entero
    # Slicing
    # Convertir a lista o tupla
    # Función len
"""

#Para establecer un rango
x = range(1,5,1)
print(list(x)) #ponemos list para que los enumere

#Mutabilidad
#Un objeto es mutable si se puede modificar, sino es inmutable
#NOTA: range es inmutable, para verificarlo:
mi_rango = range(0,20,1)
mi_rango.pop[5] = 4
print(mi_rango)