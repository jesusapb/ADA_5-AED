class Recorrer_Arbol:

    def __init__(self,arbol,cadena):
        self.arbol = arbol
        self.cadena = cadena
        self.resultado = 0
        pass




    def hacer_recorrido(self):
        ruta = []
        ubicacion = self.arbol[0][0]
        print(ubicacion)
        #print(ubicacion[1+ self.cadena[0]])
        #self.cadena.pop(0)
        pivote = ubicacion[self.cadena[0]+1]
        print(pivote)

        print("busqueda en el arbol")
        for i,j in zip(self.cadena,range(len(self.cadena))):
            print(self.arbol[j + 1])
            if i == 0:
                 print("cero")
                 print(j,":",i)
                 print(self.arbol[j + 1][0][ i + 1])
                 #ubicacion = self.arbol[j][pivote - 1]
                 #pivote = ubicacion[1]
            else:
                print("uno")
                print(j,":",i)
                print(self.arbol[j + 1][i][i + 1])
                #ubicacion = self.arbol[j][pivote - 1]
                #pivote = ubicacion[2]

        #print(ubicacion)


    def imprimir_arbol(self):
        print("prueba")



#Ejecucion del programa
lista_ruta  = [0, 0, 0, 1, 1, 0]
lista_ruta2 = [1, 1, 1, 1, 1, 1]
lista_arbol = [[[1, 1, 2]], [[1, 1, 2], [2, 2, 3]], [[1, 1, 2], [2, 2, 3], [3, 3, 4]], [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5]], [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6]], [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6], [6, 6, 7]], [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6], [6, 6, 7], [7, 7, 8]]]
prueba4 = Recorrer_Arbol(lista_arbol,lista_ruta2)
prueba4.hacer_recorrido()