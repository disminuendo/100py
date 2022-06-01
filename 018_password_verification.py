# Problema 18

# Un sitio web requiere que los usuarios ingresen el nombre de usuario y la contraseña para registrarse.
# Escriba un programa para verificar la validez de la contraseña ingresada por los usuarios. 

# Los siguientes son los criterios para verificar la contraseña:
#     1 Al menos 1 letra entre [a-z]
#     2 Al menos 1 número entre [0-9]
#     3 Al menos 1 letra entre [A-Z]
#     4 Al menos 1 carácter de [$#@]
#     5 Longitud mínima de la contraseña: 6
#     6 Longitud máxima de la contraseñad: 12

# Su programa debe aceptar una secuencia de contraseñas separadas por comas y las verificará de acuerdo
# con los criterios anteriores. Las contraseñas que coincidan con los criterios deben imprimirse, cada una
# separada por una coma.

# Ejemplo
# Si se proporcionan las siguientes contraseñas como entrada al programa:
# ABd1234@1,a F1#,2w3E*,2We3345
# Entonces, la salida del programa debería ser:
# ABd1234@1

import re
salida = []

passwords = [x for x in input().split(',')]

for p in passwords:
    if (len(p) < 6 or len(p)>12):
        continue
    else:
        pass
    if  not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif not re.search("[a-z]",p):
        
        continue
    else:
        salida.append(p)

print(salida)
