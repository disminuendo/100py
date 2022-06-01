# Problema 1
# Escribe un programa que encuentre todos esos números que son divisibles por 7 pero no son múltiplos de 5,
# entre 2000 y 3200 (ambos incluidos). Los números obtenidos deben imprimirse en una secuencia separada
# por comas en una sola línea.


from ntpath import join


def encontrar_numeros (rango_inf, rango_sup):
    """
    int, int -> list
    DEF: Retornar con valores comprendidos entre rango_inf y rango_sup que sean divisibles por 7 pero no multiplos de 5
    """
    numeros = []
    for i in  range(rango_inf, rango_sup):
        if (i%7== 0 and i%5!=0):
            numeros.append(i)
    return numeros

print(encontrar_numeros(2000,3201))


##### SOLUCION #####

### Usar el metodo JOIN para para convertir
### una lista en un string
### join(',', numeros)

def encontrar_numeros_solucion():
    l = []
    for i in range (2000, 3201):
        if (i % 7 == 0) and (i%5 != 0):
            l.append(str(i))
    return(','.join(l))

print(encontrar_numeros_solucion())
