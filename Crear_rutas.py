#import random
from Cadena import *

'''En esta clase se crea la lista de rutas que pueden seguir las pelotitas'''
class Crear_rutas:
    #se pasa al construtor el tamaño de la lista de rutas y la longitud que tendran las rutas
    def __init__(self,tama,longitud):
        self.tama = tama
        self.longitud = longitud
        self.lista_rutas = []


    #se construye una lista de listas de las rutas que puede tomar
    def construir_rutas(self):
        for i in range(self.tama):
            individuo = Cadena(self.longitud)
            individuo.construir()
            self.lista_rutas.append(individuo.cadena)


    # Metodo para pruebas locales, No USAR en el programa global
    def imprimir_cadenas(self):
        for i in self.lista_rutas:
            print(i)
        print(self.lista_rutas)


#prueba1 = Crear_cadenas(10,6)
#prueba1.construir_cadenas()
#prueba1.imprimir_cadenas()

