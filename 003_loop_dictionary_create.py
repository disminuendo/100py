# Problema 3
#
# Con un número entero n dado, escriba un programa para generar 
# un diccionario que contenga (i, i*i) tal que sea un número entero 
# entre 1 y n (ambos incluidos). y luego el programa debería imprimir el diccionario.
# Suponga que se proporciona la siguiente entrada al programa: 
# 8 La salida debe se: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Sugerencias:
# Considere usar dict()

diccionario = {}
for i in range (1, 8+1) :
    diccionario[i] = i*i

print (diccionario)
