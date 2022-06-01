# Problema 10

# Escriba un programa que acepte una secuencia de palabras separadas por espacios en blanco como
# entrada e imprima las palabras después de eliminar todas las palabras duplicadas y clasificarlas
# alfanuméricamente.

# Suponga que se proporciona la siguiente entrada al programa:
# hola mundo y la práctica hace la perfección y hola mundo de nuevo

# Sugerencias:
# Usamos set para eliminar datos duplicados automáticamente y luego usamos sorted() para
# ordenar los datos.

def eliminiar_duplicadas_ordenar():
    """
    
    """

    palabras = sorted(set(input().split(" ")))
    
    print (palabras)

eliminiar_duplicadas_ordenar()