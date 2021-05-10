
''' Esta clase recorre el arbol para ver donde esta el resultado'''

class Recorrer_Arbol:
    #Al constructor se le pasa el arbol que va a recorrer y la ruta que seguira,
    # se regresa la hoja resultante de la ruta
    def __init__(self,arbol,ruta):
        self.arbol = arbol
        self.ruta = ruta
        self.resultado = []


    def hacer_recorrido(self):
        ubicacion = self.arbol[0][0]
        j = 1
        for i in self.ruta:
            if i ==0:
                pivote = ubicacion[1]
                ubicacion = self.arbol[j][pivote]
            else:
                pivote = ubicacion[2]
                ubicacion = self.arbol[j][pivote]

            j = j +1

        self.resultado = ubicacion


    # Metodo para pruebas locales, No USAR en programa global
    def imprimir_arbol(self):
        print("Resultado: ")
        print(self.resultado)
