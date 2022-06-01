# Problema 2

# Escribe un programa que pueda calcular el factorial de un número dado. Los resultados deben imprimirse en
# una secuencia separada por comas en una sola línea.

# Suponga que se proporciona la siguiente entrada al programa: 8
# Entonces, la salida debe se: 40320


def factorial (numero):
    """
    DEF: int -> int
    OBJ: Obtener el factorial de un numero
    PRE: numero > 0 
    """
    resultado = 1
    for i in range (numero):
        resultado = resultado * (i+1)
    return resultado

x = int(input('Escribe el numero a factorizar'))
print (f'El factorial de {x} es', factorial(x))