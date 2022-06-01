# Problema 14

# Escribe un programa que acepte una oración y calcule el número de letras mayúsculas y minúsculas.
# Suponga que se proporciona la siguiente entrada al programa: ¡Hola Mundo!

# Entonces, la salida debería ser:
# MAYÚSCULAS 2
# MINÚSCULAS 7

# Sugerencias:
# En caso de que se suministren datos de entrada, se debe suponer que es una entrada de consola.



oracion = input().replace(" ", "")
dict = {"Low":0, "High":0}
for c in oracion:
    if c.islower():
        dict["Low"] += 1
    elif c.isupper():
        dict["High"] += 1
    else: pass
    
print (f'MINÚSCULAS {dict["Low"]}\nMAYÚSCULAS {dict["High"]}')

