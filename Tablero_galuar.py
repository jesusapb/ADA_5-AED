from Crear_arbol import *
from Crear_cadena import *
from Hacer_recorridos import *
from Probabilidades import *

class Tablero_galuar:


    def __init__(self,tama,niveles = 7):
        self.tama = tama
        self.niveles = niveles
        self.arbol = []
        self.rutas = []
        self.resultados_recorridos = []
        self.resultados_probabilidades = []




    def construir_tablero_rutas(self):
        #ARBOL
        crear = Crear_arbol(self.niveles)
        crear.construir_arbol()
        self.arbol = crear.lista_arbol
        #crear.imprimir_arbol()
        #RUTAS
        crear_rutas = Crear_cadenas(self.tama,self.niveles-1)
        crear_rutas.construir_cadenas()
        self.rutas = crear_rutas.lista_cadenas



    def simular_recorridos(self):
        recorrido = Hacer_recorridos(self.rutas,self.arbol)
        recorrido.proceso()
        #recorrido.imprimir_resultado()
        self.resultados_recorridos = recorrido.resultados


    def sacar_probabilidades(self):
        proba = Probabilidades(self.resultados_recorridos,self.niveles)
        proba.sacar_probabilidades()
        self.resultados_probabilidades = proba.resultados
        pass




    def imprimir_resultados(self):
        print("Arbol: ",self.arbol)
        print("Rutas: ",self.rutas)
        print("resultados: ",self.resultados_recorridos)
        print(self.resultados_probabilidades)


#prueba_10 = Tablero_galuar(100)
#prueba_10.construir_tablero_rutas()
#prueba_10.simular_recorridos()
#prueba_10.sacar_probabilidades()
#prueba_10.imprimir_resultados()

