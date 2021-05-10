from Recorrer_Arbol import *

'''Esta clase toma la lista de rutas y el arbol para sacar los resultados '''
class Hacer_recorridos:

    def __init__(self,lista_rutas,arbol):
        self.lista_rutas = lista_rutas
        self.arbol = arbol
        self.resultados = []


    def proceso(self):
        for i in self.lista_rutas:
            #print(i)
            recorrido = Recorrer_Arbol(self.arbol,i)
            recorrido.hacer_recorrido()
            self.resultados.append(recorrido.resultado)


    # Metodo para pruebas locales, NO USAR en el programa global
    def imprimir_resultado(self):
        print(self.resultados)
