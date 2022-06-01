# Problema 16

# Defina una lista por comprensión para cuadrar cada número impar en una lista. 
# La lista se introducirá mediante una secuencia de números separados por comas.

# Suponga que se proporciona la siguiente entrada al programa: 1,2,3,4,5,6,7,8,9
# Entonces, la salida debe ser: 1,3,5,7,9


numeros = input()
# lista = cadena.split(',')
# impares = []
# for n in lista:
#     if (int(n) % 2 != 0):
#         impares.append(n)

# print(",".join(impares))


# MEJORA #
impares = [x for x in numeros.split(",") if int(x) % 2 != 0]
print(",".join(impares))
