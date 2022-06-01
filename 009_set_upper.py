# Problema 9

# Escriba un programa que acepte la secuencia de líneas como entrada e imprima las líneas después de
# poner todos los caracteres de la oración en mayúsculas.

# Suponga que se proporciona la siguiente entrada al programa:
# Hola mundo
# La práctica hace la perfección

# La salida del programa debe ser:
# HOLA MUNDO
# LA PRÁCTICA HACE LA PERFECCIÓN

lineas = []
salir = False
while not salir:
    s = input()
    if s:
        lineas.append(s.upper())
    else:
        salir = True
for sentencia in lineas:
    print(sentencia)