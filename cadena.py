import random

class Cadena:

    def __init__(self,longitud):
        self.longitud = longitud
        self.cadena = []


    def numero_aleatorio(self):
        numero = random.randint(0,100)
        #print(numero)
        if numero < 50:
            return 0
        else:
            return 1



    def construir(self):
        i = 0
        while i < self.longitud:
            bit = self.numero_aleatorio()
            self.cadena.append(bit)
            i = i + 1



    def imprimir_cadena(self):
        print(self.cadena)




#prueba = Cadena(6)
#print(prueba.numero_aleatorio())
#prueba.construir()
#prueba.imprimir_cadena()