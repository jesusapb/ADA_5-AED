from Recorrer_Arbol import *

'''Esta clase toma la lista de rutas y el ambol para sacar los resultados '''
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
        pass


#arbol = [[[1, 0, 1]], [[1, 0, 1], [2, 1, 2]], [[1, 0, 1], [2, 1, 2], [3, 2, 3]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5], [6, 5, 6]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5], [6, 5, 6], [7, 6, 7]]]
#tiros = [[1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1]]

#prueba_7 = Hacer_recorridos(tiros,arbol)
#prueba_7.proceso()
#prueba_7.imprimir_resultado()