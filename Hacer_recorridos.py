from Recorrer_Arbol import *


class Hacer_recorridos:

    def __init__(self,lista_cadenas,arbol):
        self.lista_cadenas = lista_cadenas
        self.arbol = arbol
        self.resultados = []



    def proceso(self):
        for i in self.lista_cadenas:
            print(i)
            recorrido = Recorrer_Arbol(self.arbol,i)
            recorrido.hacer_recorrido()
            self.resultados.append(recorrido.resultado)



    def imprimir_resultado(self):
        print(self.resultados)
        pass


#arbol = [[[1, 0, 1]], [[1, 0, 1], [2, 1, 2]], [[1, 0, 1], [2, 1, 2], [3, 2, 3]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5], [6, 5, 6]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5], [6, 5, 6], [7, 6, 7]]]
#tiros = [[1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1]]

#prueba_7 = Hacer_recorridos(tiros,arbol)
#prueba_7.proceso()
#prueba_7.imprimir_resultado()