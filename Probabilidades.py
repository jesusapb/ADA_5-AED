class Probabilidades:

    def __init__(self,lista_listas,tama):
        self.listas_listas = lista_listas
        self.lista_probabilidades = []
        self.tama = tama
        self.resultados = []



    def sacar_probabilidades(self):
        for i in self.listas_listas:
            self.lista_probabilidades.append(i[0])

        for i in range(1,self.tama+1):
            self.resultados.append(self.lista_probabilidades.count(i))




    def imprimir_resultados(self):
        print(self.lista_probabilidades)
        print(self.resultados)



#lista_lis = [[4, 3, 4], [3, 2, 3], [5, 4, 5], [4, 3, 4], [4, 3, 4], [5, 4, 5], [4, 3, 4], [3, 2, 3], [4, 3, 4], [6, 5, 6]]
#prueba_8 = Probabilidades(lista_lis,7)
#prueba_8.sacar_probabilidades()
#prueba_8.imprimir_resultados()




