class Crear_arbol:

    #este metodo crea el arbol segun el numero de niveles que
    # se pasan como parametro por el contructor de la clase
    def __init__(self,niveles):
        self.niveles = niveles
        self.lista_arbol = []


    #se construye el arbol simuladolo en una lista
    def construir_arbol(self):
        #contador = 1
        for i in range(1,self.niveles+1):
            j = 0
            a= 0
            b = 1
            lista_temporal = []
            while j < i:
                lista_temporal.append([j + 1,a,b])
                a = a + 1
                b = b + 1
                #contador
                j = j + 1
            self.lista_arbol.append(lista_temporal)



    # Metodo para pruebas locales, NO USAR en programa global
    def imprimir_arbol(self):
        #print(self.lista_arbol)
        for i in self.lista_arbol:
            print(i)
        #    print(len(i))



#prueba2 = Crear_arbol(7)
#prueba2.construir_arbol()
#prueba2.imprimir_arbol()