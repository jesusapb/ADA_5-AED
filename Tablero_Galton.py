from Crear_arbol import *
from Crear_rutas import *
from Hacer_recorridos import *
from Probabilidades import *

class Tablero_Galton:

    #se pasa al constructor atraves de "tama" el numero de pelotas
    # que caeran y el numero de niveles que tiene el tablero
    def __init__(self,tama,niveles = 7):
        self.tama = tama
        self.niveles = niveles
        self.arbol = []
        self.rutas = []
        self.resultados_recorridos = []
        self.resultados_probabilidades = []


    # En este metodo se crea el arbol y se construyen las rutas
    def construir_tablero_rutas(self):
        #ARBOL
        crear = Crear_arbol(self.niveles)
        crear.construir_arbol()
        self.arbol = crear.lista_arbol
        #RUTAS
        construir_rutas = Crear_rutas(self.tama,self.niveles-1)
        construir_rutas.construir_rutas()
        self.rutas = construir_rutas.lista_rutas


    def simular_recorridos(self):
        recorrido = Hacer_recorridos(self.rutas,self.arbol)
        recorrido.proceso()
        #recorrido.imprimir_resultado()
        self.resultados_recorridos = recorrido.resultados


    def sacar_probabilidades(self,tipo =0):
        proba = Probabilidades(self.resultados_recorridos,self.niveles)
        #Aqui se hace el ajusta para sacar las probabilidades en decimales o acululados
        if tipo ==0:
            proba.sacar_probabilidades_2()
            self.resultados_probabilidades = proba.resultados
        else:
            proba.sacar_probabilidades()
            self.resultados_probabilidades = proba.resultados



    def imprimir_resultados(self):
        print("Tablero de Galton")
        print("Arbol: ",self.arbol)
        print("Rutas: ",self.rutas)
        print("Resultados de las rutas: ",self.resultados_recorridos)
        print("Probabilidades: ",self.resultados_probabilidades)


