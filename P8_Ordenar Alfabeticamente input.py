# Problema 8
# Escriba un programa que acepte una secuencia de palabras separadas por comas como entrada e imprima
# las palabras en una secuencia separada por comas después de ordenarlas alfabéticamente.
# Suponga que se proporciona la siguiente entrada al programa: sin, hola, bolsa, mundo
# La salida del programa debe ser: bolsa, hola, mundo, sin


def ordenar_input ():
    """
    None -> list
    OBJ: Ordenar alfabeticamente una lista de palabras
    PRE: Las palabras han de estar separadas por comas
    """    
    palabras = input("Esciba las palabras a ordenar separadas por comas: ").split(',')
    palabras_sin_espacios= []
    for palabra in palabras:
        palabras_sin_espacios.append(palabra.strip())        
    return(sorted(palabras_sin_espacios))

#TEST
#print(ordenar_input())

#### SOLUCION ####

elementos = [x for x in input().split(',')]
elementos.sort()
print(','.join(elementos))
