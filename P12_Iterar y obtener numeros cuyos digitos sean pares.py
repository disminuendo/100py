# Problema 12
#
# Escriba un programa que encuentre todos los números entre 1000 y 3000 (ambos incluidos) de modo que
# cada dígito del número sea un número par. Los números obtenidos deben imprimirse en una secuencia
# separada por comas en una sola línea.

def obtener_valores_digitos_pares(valor_inf, valor_sup):
    """
    int, int -> str
    DEF: Obtener todos los valores en un rango cuyas cifras sean todas pares
    PRE: (valor_inf) < (valor_sup); ambos han de tener 4 cifras
    """
    valores = []
    for i in range (valor_inf, valor_sup):
        s = str(i)
        if ((int(s[0])%2 ==0)  and (int(s[1])%2 ==0) and (int(s[2])%2 ==0) and (int(s[3])%2 ==0)):
            valores.append(s)
    return (",".join(valores))

# TEST
print (obtener_valores_digitos_pares(1000,3000))
