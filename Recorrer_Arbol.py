class Recorrer_Arbol:

    def __init__(self,arbol,ruta):
        self.arbol = arbol
        #self.cadena = cadena
        self.ruta = ruta
        self.resultado = []


    def hacer_recorrido(self):
        #ruta = []
        ubicacion = self.arbol[0][0]
        print(ubicacion)
        print(len(self.arbol))
        print("busqueda en el arbol")
        j = 1
        for i in self.ruta:
            if i ==0:
                print("cero")
                pivote = ubicacion[1]
                print(pivote)
                ubicacion = self.arbol[j][pivote]
            else:
                print("uno")
                pivote = ubicacion[2]
                ubicacion = self.arbol[j][pivote]

            j = j +1
        #print(ubicacion)
        self.resultado = ubicacion



    def imprimir_arbol(self):
        print("Resultado: ")
        print(self.resultado)



#Ejecucion del programa
#lista_ruta  = [0, 0, 0, 1, 1, 0]
#lista_ruta2 = [1, 1, 1, 1, 1, 1]
#lista_ruta3 = [0, 0, 0, 0, 0, 0]
#lista_ruta4 = [0, 1, 0, 0, 0, 1]
#lista_ruta5 = [1, 1, 1, 0, 0, 0]
#lista_arbol = [[[1, 1, 2]], [[1, 1, 2], [2, 2, 3]], [[1, 1, 2], [2, 2, 3], [3, 3, 4]], [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5]], [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6]], [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6], [6, 6, 7]], [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6], [6, 6, 7], [7, 7, 8]]]
#arbol_2 = [[[1, 0, 1]], [[1, 0, 1], [2, 1, 2]], [[1, 0, 1], [2, 1, 2], [3, 2, 3]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5], [6, 5, 6]], [[1, 0, 1], [2, 1, 2], [3, 2, 3], [4, 3, 4], [5, 4, 5], [6, 5, 6], [7, 6, 7]]]
#prueba4 = Recorrer_Arbol(arbol_2,lista_ruta3)
#prueba4.hacer_recorrido()
#prueba4.imprimir_arbol()