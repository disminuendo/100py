# Problema 20

# Escriba un programa para eliminar una(s) tupla(s) vacía(s) de una lista de tuplas.

# Ejemplo:
# Si se proporcionan las siguientes tuplas como entrada al programa : 
# [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Entonces, la salida del programa debería ser : [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# Sugerencias:
# Defina la tupla por comprensión

li = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
li = [x for x in li if x]
print(li)
