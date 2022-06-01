# Problema 5

# Defina una clase que tenga al menos dos métodos:
# getString : para obtener una cadena desde la consola
# printString : para imprimir la cadena en mayúsculas.
# También incluya una función de prueba simple para probar los métodos de la clase.
#
# Sugerencias:
# Use el metodo __init__ method para crear algunos parámetros

class InputOutString():

    def __init__(self):
        self.string = ""

    def getString (self):  
        self.string = input()

    def printString(self):
        print(self.string.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
