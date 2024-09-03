# Función while
"""
Iteraciones
# Iterar significa realizar una acción varias veces.
# Cada vez que se repite se denomina iteración

Controlado o sentencia While (mientras)
Se basa en repetir un bloque a partir de evaluar una condición lógica,
siempre que ésta sea True

Queda en las manos del programador decidir el momento en que la
condición cambie a False para hacer que el While finalice.
"""
val = 3
while val < 5:
    print(val) #Aquí va a correr a lo loco hasta que le demos stop
    val += 1

"""
Sentencia Else en bucle While 
Se encadena al While para ejecutar un bloque de código una vez que la condición 
ya no devuelve True (normalmente al final). 
"""
lista = ['chocolate', 'tristeza', 'cualquiera','naranjas', 'azul','parque']
indice = -3
while lista[indice] != 'cualquiera':
    print(indice, lista[indice])
    indice += 1
else:
    print("se cumplió la condición, ya me quiero mimir")

# Ejemplo donde no se cumple la condición de paro (sigue a lo loco)
"""
idx = 0
while True:
    idx *= 2
    print(idx)
else:
    print('salió')
"""

#Ejemplo con break
c = 0
while c <= 5:
    c += 1 #este es importante para que el código no corra en bucle, sino que se completen las iteraciones y termine
    if c == 4:
        print("Rompemos el bucle cuando c vale", c)
        continue #prueba las diferencias con, sin break y con continue
    print("c vale", c)
else:
    print("Se ha completado toda la iteración y c vale", c)

