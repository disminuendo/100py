# Problema 17

# Escriba un programa que calcule el monto neto de una cuenta bancaria basándose en un registro de
# transacciones de la entrada de la consola.

# El formato del registro de transacciones se muestra a continuación:
# D 100 .- D significa depósito
# R 200 .- R significa retiro

# Suponga que se proporciona la siguiente entrada al programa:
# D 300
# D 300
# R 200
# D 100
# Entonces, la salida debe ser: 500

def calcula_neto():
    fin = False
    cuenta = 0
    print('Escriba D para deposito o R para retiro y la cantidad\nEjemplo: D 100')

    while not fin:
        transaccion = input('Operacion: ')
        operacion = transaccion.split(" ")
        if operacion[0] == 'D':
            cuenta += int(operacion[1])
        elif operacion[0] == 'R':
            cuenta -= int(operacion[1])
        else: fin = True
    return cuenta

#TEST
print(calcula_neto())
