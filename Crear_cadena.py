#import random
from Cadena import *


class Crear_cadenas:

    def __init__(self,tama,longitud):
        self.tama = tama
        self.longitud = longitud
        self.lista_cadenas = []




    def construir_cadenas(self):
        for i in range(self.tama):
            individuo = Cadena(self.longitud)
            individuo.construir()
            self.lista_cadenas.append(individuo.cadena)



    def imprimir_cadenas(self):
        for i in self.lista_cadenas:
            print(i)


prueba1 = Crear_cadenas(4,7)
prueba1.construir_cadenas()
prueba1.imprimir_cadenas()

