# Problema 4

# Escriba un programa que acepte una secuencia de números separados por comas desde la consola y
# genere una lista y una tupla que contenga cada número.
# Suponga que se proporciona la siguiente entrada al programa: 34,67,55,33,12,98
# La salida debe se:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Sugerencias:
# Se debe suponer que es una entrada por consola.
# El método tuple() puede convertir la lista en tupla


def obtener_lista_tupla ():
    """
    None -> list, tuple
    OBJ: Obtener cadena por sonsola y devolver una lista y una tupla
    PRE: Los elementos de la cadena deberan de estar separados por comas
    """

    cadena = input()
    lista = cadena.split(',')
    tupla = tuple(lista)

    return(lista, tupla)

#test
print(obtener_lista_tupla())