# Problema 11

# Escriba un programa que acepte una secuencia de números binarios de 4 dígitos separados por comas
# como entrada y luego verifique si son divisibles por 5 o no. Los números divisibles por 5 deben imprimirse en
# una secuencia separada por comas.

# Ejemplo: 0100,0011,1010,1001
# Entonces la salida debería ser: 1010

valores = []
elementos = [x for x in input().split(',')]
for p in elementos:
    intp = int(p, 2)
    if not intp % 5:
        valores.append(p)
print((valores))