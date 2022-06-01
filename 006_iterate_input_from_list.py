# √(Q = (2 ∗ C ∗ D)/H) | C = 50 ; H = 50 | D = variable separada por comas 

import math


def calcula_formula(d_list):
    c = 50
    h = 30
    
    resultado = []
    for numero in d_list:
        resultado.append(round(math.sqrt((2*c*float(numero))/h)))
    return resultado


#prueba
print(calcula_formula([100,150,180]))
    