import random

'''Esta clase construye las rutas que seguiran las pelotas cuando caigan por el arbol(tablero)'''
class Ruta:
    #Al constructor se le pasa el la longitud de la cadena
    def __init__(self,longitud):
        self.longitud = longitud
        self.ruta = []


    # se genera un numero aleatorio y si esta en un rango adecuado es 0 o es 1 segun corresponda
    def numero_aleatorio(self):
        numero = random.randint(0,100)
        #print(numero)
        if numero < 50:
            return 0
        else:
            return 1


    #se construye el la ruta con la logitud establecida
    def construir(self):
        i = 0
        while i < self.longitud:
            bit = self.numero_aleatorio()
            self.ruta.append(bit)
            i = i + 1


    #Metodo para pruebas locales, No USAR en el programa global
    def imprimir_cadena(self):
        print(self.ruta)




#prueba = Cadena(6)
#print(prueba.numero_aleatorio())
#prueba.construir()
#prueba.imprimir_cadena()