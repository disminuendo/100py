# Problema 19

# Debe escribir un programa para ordenar las tuplas (nombre, edad, altura) en orden ascendente donde el
# nombre es una cadena, la edad y la altura son números.
# Los criterios de clasificación son:
#     1. Ordenar según el nombre;
#     2. Luego ordene según la edad;
#     3. Luego ordene por puntaje.
# La prioridad es ese nombre > edad > puntuación.
# Si se proporcionan las siguientes tuplas como entrada al programa:
#     Tom,19,80
#     John,20,90
#     Jony,17,91
#     Jony,17,93
#     Json,21,85

# Entonces, la salida del programa debería ser:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


from operator import itemgetter


l = []
salir = False 
while not salir:
    s = input()
    if not s:
        salir = True
    else:
        l.append(tuple(s.split(",")))

print(sorted(l, key = itemgetter(0,1,2)))

# The itemgetter() function returns the item based on the index passed onto it.
