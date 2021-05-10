class Probabilidades:

    '''A esta clase se le pasa atraves del constructor la lista de resultados y el tamaño de los las rutas'''
    def __init__(self,lista_listas,tama):
        self.listas_listas = lista_listas
        self.lista_probabilidades = []
        self.tama = tama
        self.resultados = []


    # este metodo saca las probabiliddes y regresa los resultados
    def sacar_probabilidades(self):
        for i in self.listas_listas:
            self.lista_probabilidades.append(i[0])

        for i in range(1,self.tama+1):
            self.resultados.append(self.lista_probabilidades.count(i))


# Este metodo es especial ya que calcula las probabilidades
    def sacar_probabilidades_2(self):

        for i in self.listas_listas:
            self.lista_probabilidades.append(i[0])

        for i in range(1,self.tama+1):
            self.resultados.append(self.lista_probabilidades.count(i))
        #
        #print("resultados:", self.resultados)
        divisor = len(self.listas_listas) # se divide entre el numero de elementos que tiene la lista
        #my_list = list(map(lambda x: x / divisor, my_list))
        self.resultados = list(map(lambda x: x / divisor, self.resultados))
        #https: // es.stackoverflow.com / questions / 374572 / c % C3 % B3mo - puedo - dividir - una - lista - con - un - numero - en - python


    # Metodo para pruebas locales, NO USAR en el programa global
    def imprimir_resultados(self):
        print(self.lista_probabilidades)
        print(self.resultados)



#lista_lis = [[4, 3, 4], [3, 2, 3], [5, 4, 5], [4, 3, 4], [4, 3, 4], [5, 4, 5], [4, 3, 4], [3, 2, 3], [4, 3, 4], [6, 5, 6]]
#prueba_8 = Probabilidades(lista_lis,7)
#prueba_8.sacar_probabilidades()
#prueba_8.imprimir_resultados()




