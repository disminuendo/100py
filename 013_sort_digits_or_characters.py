# Problema 13

# Escribe un programa que acepte una oración y calcule el número de letras y dígitos. 
# Suponga que se proporciona la siguiente entrada al programa: 
# ¡Hola Mundo! 123 Entonces, la salida debe ser: LETRAS 10 DIGITOS 3

def calculo_letras_numeros():
    """
    none -> none
    DEF: Cuenta el numero de letras y numeros de un input
    """
    oracion = input().replace(" ", "")
    letras=[]
    digitos=[]
    for letra in oracion:
        try:
            int(letra)
            digitos.append(letra)
        except:
            letras.append(letra)

    print(f'LETRAS {len(letras)} DIGITOS {len(digitos)}')


#TEST
calculo_letras_numeros()

#SOLUCION (SE RECOMIENDA USAR => isdigit() y isalpha()) ; TAMBIEN USO DE DICCIONARIO

# s = input('Oración : ')
# d = {"DIGITOS":0, "LETRAS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITOS"]+ = 1
#     elif c.isalpha():
#         d["LETRAS"]+ = 1
#     else:
#         pass
# print("LETRAS", d["LETRAS"])
# print("DIGITOS", d["DIGITOS"])