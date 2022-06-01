# Problema 15

# Escriba un programa que calcule el valor de a+aa+aaa+aaaa con un dígito dado como valor de a.
# Suponga que se proporciona la siguiente entrada al programa: 9
# Entonces, la salida debería ser: 11106

from dataclasses import replace


def replace_values(val):
    operacion = 'a+aa+aaa+aaaa'
    valores = operacion.split('+')
    resultado = []

    for v in valores: 
        resultado.append(int(v.replace('a',val)))
        
    return sum(resultado)

#print(replace_values('9'))

# SOLUCION #

a = input()
n1 = int( "%s"%a )
n2 = int( "%s%s"%(a,a) )
n3 = int( "%s%s%s"%(a,a,a) )
n4 = int( "%s%s%s%s"%(a,a,a,a) )
print(n1+n2+n3+n4)